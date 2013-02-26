"""Texture classes.

@todo: Check OpenGL memory layout; do shaders use the same coordinates as C{numpy} does?
@todo: Implement C{__getitem__} and C{__setitem__} for subimages (C{glTexSubImage3D}, C{glGetTexImage} with C{format=GL_RED} etc.).
@todo: Implement stencil textures.
@todo: Implement image textures.
@todo: Implement normalized integer types (GL_RGBA8_SNORM etc.)

@author: Stephan Wenger
@date: 2012-02-29
"""

import numpy as _np

import glitter.raw as _gl
from glitter.utils import texture_compare_funcs, texture_compare_modes, texture_min_filters, texture_mag_filters, texture_swizzles, texture_wrapmodes, dtype_to_gl_iformat, dtype_to_gl_format, gl_iformat_to_dtype, gl_iformat_to_gl_type, Datatype, coerce_array, ManagedObject, BindReleaseObject, float32, texture_formats

class Texture(ManagedObject, BindReleaseObject):
    _generate_id = _gl.glGenTextures
    _delete_id = _gl.glDeleteTextures
    _db = "textures"

    _ndim = NotImplemented
    _set = NotImplemented

    compare_funcs = texture_compare_funcs
    compare_modes = texture_compare_modes
    min_filters = texture_min_filters
    mag_filters = texture_mag_filters
    swizzles = texture_swizzles
    wrapmodes = texture_wrapmodes

    def bind(self):
        return self._context.texture_units.bind(self)

    def release(self):
        self._context.texture_units.release(self)

    def __init__(self, data=None, shape=None, dtype=None, depth=False, stencil=False, mipmap=False, context=None, **kwargs):
        if any(x is NotImplemented for x in (self._ndim, self._set)):
            raise TypeError("%s is abstract" % self.__class__.__name__)
        super(Texture, self).__init__(context=context)
        self.set_data(data, shape, dtype, depth=depth, stencil=stencil, mipmap=mipmap, set_default_interpolation=True)
        for key, value in list(kwargs.items()):
            setattr(self, key, value)

    def __getitem__(self, key):
        """Return a tuple describing a texture layer.

        This is mainly provided as a convenience notation for binding texture
        layers to L{Framebuffer}s.
        """

        return (self, key)

    def __len__(self):
        return self.shape[0]

    def set_data(self, data=None, shape=None, dtype=None, level=0, depth=False, stencil=False, mipmap=False, set_default_interpolation=False):
        if data is None:
            if shape is None:
                raise ValueError("must specify either data or shape")
            if dtype is None:
                dtype = float32
        else:
            data = coerce_array(data, dtype)
            if shape is not None:
                data = data.reshape(shape)
            shape = data.shape
            dtype = Datatype.from_numpy(data.dtype)

        if len(shape) != self._ndim:
            raise TypeError("shape must be %d-dimensional" % self._ndim)

        _iformat = dtype_to_gl_iformat[dtype, shape[-1]]
        _format = dtype_to_gl_format[dtype, shape[-1]]
        _type = dtype._as_gl()

        if depth and stencil:
            raise NotImplementedError("depth-and-stencil textures are currently not supported")
        elif depth:
            _iformat = _format = None
            for (nptype, colors), ifmt, (gltype, fmt) in texture_formats: # @UnusedVariable
                if nptype == dtype and colors == shape[-1] and fmt == _gl.GL_DEPTH_COMPONENT:
                    _iformat, _format = ifmt, fmt
            if _iformat is None or _format is None:
                raise TypeError("no matching depth texture format for %d %s colors" % (shape[-1], dtype))
        elif stencil:
            raise NotImplementedError("stencil textures are currently not supported")

        _data = data.ctypes if data is not None else _gl.POINTER(_gl.GLvoid)()
        _gl.glPixelStorei(_gl.GL_UNPACK_ALIGNMENT, 1)
        with self:
            args = [self._target, level, _iformat] + list(reversed(shape[:-1])) + [0, _format, _type, _data]
            self._set(*args)

        if not dtype.is_float(): # NEAREST is the only possible options for non-floats.
            self.min_filter = self.min_filters.NEAREST_MIPMAP_NEAREST if mipmap else self.min_filters.NEAREST # mipmap untested, use at own risk!
            self.mag_filter = self.mag_filters.NEAREST
        elif set_default_interpolation:
            self.min_filter = self.min_filters.LINEAR_MIPMAP_LINEAR if mipmap else self.min_filters.LINEAR
            self.mag_filter = self.mag_filters.LINEAR

        # No unambiguous way to determine depth component from dtype,
        # so we have to save it separately.
        self._depth = depth
        self._stencil = stencil

        if mipmap:
            self.generate_mipmap()

    def generate_mipmap(self):
        with self:
            _gl.glGenerateMipmap(self._target)

    def get_data(self, level=0):
        _shape = self.get_shape(level) # for mipmaps.
        _data = _np.empty(_shape, dtype=self.dtype.as_numpy())
        _gl.glPixelStorei(_gl.GL_PACK_ALIGNMENT, 1)
        with self:
            _gl.glGetTexImage(self._target, level, self._format, self._type, _data.ctypes)
        return _data

    @property
    def data(self):
        return self.get_data()

    @data.setter
    def data(self, data):
        self.set_data(data)

    @property
    def shape(self):
        return self.get_shape(0)

    def get_shape(self, level=0):
        """Returns the current texture data size at given mipmap level."""
        with self:
            colors = gl_iformat_to_dtype[self._iformat][1]
            _width = _gl.GLint()
            _gl.glGetTexLevelParameteriv(self._target, level, _gl.GL_TEXTURE_WIDTH, _gl.pointer(_width))
            if self._ndim == 2:
                return (_width.value, colors)
            _height = _gl.GLint()
            _gl.glGetTexLevelParameteriv(self._target, level, _gl.GL_TEXTURE_HEIGHT, _gl.pointer(_height))
            if self._ndim == 3:
                return (_height.value, _width.value, colors)
            _depth = _gl.GLint()
            _gl.glGetTexLevelParameteriv(self._target, level, _gl.GL_TEXTURE_DEPTH, _gl.pointer(_depth))
            if self._ndim == 4:
                return (_depth.value, _height.value, _width.value, colors)

    @property
    def dtype(self):
        return gl_iformat_to_dtype[self._iformat][0]

    @property
    def _iformat(self):
        _iformat = _gl.GLint()
        with self:
            _gl.glGetTexLevelParameteriv(self._target, 0, _gl.GL_TEXTURE_INTERNAL_FORMAT, _gl.pointer(_iformat))
        return _iformat.value

    @property
    def _format(self):
        if self._depth and not self._stencil:
            return _gl.GL_DEPTH_COMPONENT
        elif self._stencil and not self._depth:
            raise NotImplementedError("Stencil is not supported yet (for getting a format).")
        elif self._depth and self._stencil:
            raise NotImplementedError("Stencil AND depth is not supported yet (for getting a format).")
        else:
            return dtype_to_gl_format[self.dtype, self.shape[-1]]

    @property
    def _type(self):
        return gl_iformat_to_gl_type[self._iformat]

    @property
    def base_level(self):
        _base_level = _gl.GLint()
        with self:
            _gl.glGetTexParameterIiv(self._target, _gl.GL_TEXTURE_BASE_LEVEL, _gl.pointer(_base_level))
        return _base_level.value

    @base_level.setter
    def base_level(self, base_level):
        with self:
            _gl.glTexParameterIiv(self._target, _gl.GL_TEXTURE_BASE_LEVEL, _gl.pointer(_gl.GLint(base_level)))

    @property
    def border_color(self):
        if self.dtype.is_float():
            _border_color = (_gl.GLfloat * 4)()
            with self:
                _gl.glGetTexParameterfv(self._target, _gl.GL_TEXTURE_BORDER_COLOR, _border_color)
        elif self.dtype.is_signed():
            _border_color = (_gl.GLint * 4)()
            with self:
                _gl.glGetTexParameterIiv(self._target, _gl.GL_TEXTURE_BORDER_COLOR, _border_color)
        else:
            _border_color = (_gl.GLuint * 4)()
            with self:
                _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_BORDER_COLOR, _border_color)
        return [_border_color[i] for i in range(4)]

    @border_color.setter
    def border_color(self, border_color):
        if self.dtype.is_float():
            _border_color = (_gl.GLfloat * 4)()
            for i, v in zip(list(range(4)), border_color):
                _border_color[i] = v
            with self:
                _gl.glTexParameterfv(self._target, _gl.GL_TEXTURE_BORDER_COLOR, _border_color)
        elif self.dtype.is_signed():
            _border_color = (_gl.GLint * 4)()
            for i, v in zip(list(range(4)), border_color):
                _border_color[i] = v
            with self:
                _gl.glTexParameterIiv(self._target, _gl.GL_TEXTURE_BORDER_COLOR, _border_color)
        else:
            _border_color = (_gl.GLuint * 4)()
            for i, v in zip(list(range(4)), border_color):
                _border_color[i] = v
            with self:
                _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_BORDER_COLOR, _border_color)

    @property
    def compare_func(self):
        _compare_func = _gl.GLenum()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_COMPARE_FUNC, _gl.pointer(_compare_func))
        return self.compare_funcs[_compare_func.value]

    @compare_func.setter
    def compare_func(self, compare_func):
        _compare_func = _gl.GLenum(self.compare_funcs(compare_func)._value)
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_COMPARE_FUNC, _gl.pointer(_compare_func))

    @property
    def compare_mode(self):
        _compare_mode = _gl.GLenum()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_COMPARE_MODE, _gl.pointer(_compare_mode))
        return self.compare_modes[_compare_mode.value]

    @compare_mode.setter
    def compare_mode(self, compare_mode):
        _compare_mode = _gl.GLenum(self.compare_modes(compare_mode)._value)
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_COMPARE_MODE, _gl.pointer(_compare_mode))

    @property
    def immutable_format(self): # Textures become immutable if their storage is specified with glTexStorage1D, glTexStorage2D or glTexStorage3D
        _immutable_format = _gl.GLenum()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_COMPARE_MODE, _gl.pointer(_immutable_format))
        return bool(_immutable_format.value)

    @property
    def lod_bias(self):
        _lod_bias = _gl.GLfloat()
        with self:
            _gl.glGetTexParameterfv(self._target, _gl.GL_TEXTURE_LOD_BIAS, _gl.pointer(_lod_bias))
        return _lod_bias.value

    @lod_bias.setter
    def lod_bias(self, lod_bias):
        with self:
            _gl.glTexParameterfv(self._target, _gl.GL_TEXTURE_LOD_BIAS, _gl.pointer(_gl.GLfloat(lod_bias)))

    @property
    def min_filter(self):
        _min_filter = _gl.GLenum()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_MIN_FILTER, _gl.pointer(_min_filter))
        return self.min_filters[_min_filter.value]

    @min_filter.setter
    def min_filter(self, min_filter):
        _min_filter = _gl.GLenum(self.min_filters(min_filter)._value)
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_MIN_FILTER, _gl.pointer(_min_filter))

    @property
    def mag_filter(self):
        _mag_filter = _gl.GLenum()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_MAG_FILTER, _gl.pointer(_mag_filter))
        return self.mag_filters[_mag_filter.value]

    @mag_filter.setter
    def mag_filter(self, mag_filter):
        _mag_filter = _gl.GLenum(self.mag_filters(mag_filter)._value)
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_MAG_FILTER, _gl.pointer(_mag_filter))

    @property
    def min_lod(self):
        _min_lod = _gl.GLint()
        with self:
            _gl.glGetTexParameterIiv(self._target, _gl.GL_TEXTURE_MIN_LOD, _gl.pointer(_min_lod))
        return _min_lod.value

    @min_lod.setter
    def min_lod(self, min_lod):
        with self:
            _gl.glTexParameterIiv(self._target, _gl.GL_TEXTURE_MIN_LOD, _gl.pointer(_gl.GLint(min_lod)))

    @property
    def max_lod(self):
        _max_lod = _gl.GLint()
        with self:
            _gl.glGetTexParameterIiv(self._target, _gl.GL_TEXTURE_MAX_LOD, _gl.pointer(_max_lod))
        return _max_lod.value

    @max_lod.setter
    def max_lod(self, max_lod):
        with self:
            _gl.glTexParameterIiv(self._target, _gl.GL_TEXTURE_MAX_LOD, _gl.pointer(_gl.GLint(max_lod)))

    @property
    def max_level(self):
        _max_level = _gl.GLint()
        with self:
            _gl.glGetTexParameterIiv(self._target, _gl.GL_TEXTURE_MAX_LEVEL, _gl.pointer(_max_level))
        return _max_level.value

    @max_level.setter
    def max_level(self, max_level):
        with self:
            _gl.glTexParameterIiv(self._target, _gl.GL_TEXTURE_MAX_LEVEL, _gl.pointer(_gl.GLint(max_level)))

    @property
    def swizzle_r(self):
        _swizzle_r = _gl.GLenum()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_SWIZZLE_R, _gl.pointer(_swizzle_r))
        return self.swizzles[_swizzle_r.value]

    @swizzle_r.setter
    def swizzle_r(self, swizzle_r):
        _swizzle_r = _gl.GLenum(self.swizzles(swizzle_r)._value)
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_SWIZZLE_R, _gl.pointer(_swizzle_r))

    @property
    def swizzle_g(self):
        _swizzle_g = _gl.GLenum()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_SWIZZLE_G, _gl.pointer(_swizzle_g))
        return self.swizzles[_swizzle_g.value]

    @swizzle_g.setter
    def swizzle_g(self, swizzle_g):
        _swizzle_g = _gl.GLenum(self.swizzles(swizzle_g)._value)
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_SWIZZLE_G, _gl.pointer(_swizzle_g))

    @property
    def swizzle_b(self):
        _swizzle_b = _gl.GLenum()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_SWIZZLE_B, _gl.pointer(_swizzle_b))
        return self.swizzles[_swizzle_b.value]

    @swizzle_b.setter
    def swizzle_b(self, swizzle_b):
        _swizzle_b = _gl.GLenum(self.swizzles(swizzle_b)._value)
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_SWIZZLE_B, _gl.pointer(_swizzle_b))

    @property
    def swizzle_a(self):
        _swizzle_a = _gl.GLenum()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_SWIZZLE_A, _gl.pointer(_swizzle_a))
        return self.swizzles[_swizzle_a.value]

    @swizzle_a.setter
    def swizzle_a(self, swizzle_a):
        _swizzle_a = _gl.GLenum(self.swizzles(swizzle_a)._value)
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_SWIZZLE_A, _gl.pointer(_swizzle_a))

    @property
    def swizzle_rgba(self):
        _swizzle_rgba = (_gl.GLenum * 4)()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_SWIZZLE_RGBA, _swizzle_rgba)
        return [self.swizzles[_swizzle_rgba[i]] for i in range(4)]

    @swizzle_rgba.setter
    def swizzle_rgba(self, swizzle_rgba):
        _swizzle_rgba = (_gl.GLenum * 4)()
        for i, v in zip(list(range(4)), swizzle_rgba):
            _swizzle_rgba[i] = self.swizzles(v)._value
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_SWIZZLE_RGBA, _swizzle_rgba)

    @property
    def wrap_s(self):
        _wrap_s = _gl.GLenum()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_WRAP_S, _gl.pointer(_wrap_s))
        return self.wrapmodes[_wrap_s.value]

    @wrap_s.setter
    def wrap_s(self, wrap_s):
        _wrap_s = _gl.GLenum(self.wrapmodes(wrap_s)._value)
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_WRAP_S, _gl.pointer(_wrap_s))

    @property
    def wrap_t(self):
        _wrap_t = _gl.GLenum()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_WRAP_T, _gl.pointer(_wrap_t))
        return self.wrapmodes[_wrap_t.value]

    @wrap_t.setter
    def wrap_t(self, wrap_t):
        _wrap_t = _gl.GLenum(self.wrapmodes(wrap_t)._value)
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_WRAP_T, _gl.pointer(_wrap_t))

    @property
    def wrap_r(self):
        _wrap_r = _gl.GLenum()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_WRAP_R, _gl.pointer(_wrap_r))
        return self.wrapmodes[_wrap_r.value]

    @wrap_r.setter
    def wrap_r(self, wrap_r):
        _wrap_r = _gl.GLenum(self.wrapmodes(wrap_r)._value)
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_WRAP_R, _gl.pointer(_wrap_r))

class Texture1D(Texture):
    _target = _gl.GL_TEXTURE_1D
    _binding = "texture_binding_1d"
    _ndim = 2
    _set = _gl.glTexImage1D

class Texture2D(Texture):
    _target = _gl.GL_TEXTURE_2D
    _binding = "texture_binding_2d"
    _ndim = 3
    _set = _gl.glTexImage2D

class TextureArray1D(Texture):
    _target = _gl.GL_TEXTURE_1D_ARRAY
    _binding = "texture_binding_1d_array"
    _ndim = 3
    _set = _gl.glTexImage2D

class RectangleTexture(Texture):
    _target = _gl.GL_TEXTURE_RECTANGLE
    _binding = "texture_binding_rectangle"
    _ndim = 3
    _set = _gl.glTexImage2D

class BufferTexture(Texture):
    """Texture that stores its data in a buffer.
    
    @todo: Override constructor, C{set_data} and C{get_data}; use C{glTexBuffer}
    """

    _target = _gl.GL_TEXTURE_BUFFER
    _binding = "texture_binding_buffer"
    _ndim = 3
    _set = _gl.glTexImage2D

class CubeMapTexture(Texture):
    _target = _gl.GL_TEXTURE_CUBE_MAP
    _binding = "texture_binding_cube_map"
    _ndim = 3
    _set = _gl.glTexImage2D

class MultisampleTexture2D(Texture):
    _target = _gl.GL_TEXTURE_2D_MULTISAMPLE
    _binding = "texture_binding_2d_multisample"
    _ndim = 3
    _set = _gl.glTexImage2D

class Texture3D(Texture):
    _target = _gl.GL_TEXTURE_3D
    _binding = "texture_binding_3d"
    _ndim = 4
    _set = _gl.glTexImage3D

class TextureArray2D(Texture):
    _target = _gl.GL_TEXTURE_2D_ARRAY
    _binding = "texture_binding_2d_array"
    _ndim = 4
    _set = _gl.glTexImage3D

class MultisampleTextureArray2D(Texture):
    _target = _gl.GL_TEXTURE_2D_MULTISAMPLE_ARRAY
    _binding = "texture_binding_2d_multisample_array"
    _ndim = 4
    _set = _gl.glTexImage3D

__all__ = [
    "Texture",
    "Texture1D",
    "Texture2D",
    "TextureArray1D",
    "RectangleTexture",
    "BufferTexture",
    "CubeMapTexture",
    "MultisampleTexture2D",
    "Texture3D",
    "TextureArray2D",
    "MultisampleTextureArray2D",
]

