import numpy as _np
from rawgl import gl as _gl

import constants
from util import BindableObject

# TODO check memory layout: do shaders use the same coordinates as _np?
# TODO support depth textures
# TODO __getitem__/__setitem__ for subimages (glTexSubImage3D, glGetTexImage with format = GL_RED etc.)
# TODO mipmaps (level != 0) with glGenerateMipmap

class Texture(BindableObject):
    _generate_id = _gl.glGenTextures
    _delete_id = _gl.glDeleteTextures
    _bind = _gl.glBindTexture

    _ndim = NotImplemented
    _set = NotImplemented

    compare_funcs = constants.texture_compare_funcs
    compare_modes = constants.texture_compare_modes
    min_filters = constants.texture_min_filters
    mag_filters = constants.texture_mag_filters
    swizzles = constants.texture_swizzles
    wrapmodes = constants.texture_wrapmodes

    def __init__(self, data=None, shape=None, dtype=None):
        if any(x is NotImplemented for x in (self._ndim, self._set)):
            raise TypeError("%s is abstract" % self.__class__.__name__)
        super(Texture, self).__init__()
        self.set_data(data, shape, dtype)

    def set_data(self, data=None, shape=None, dtype=None, level=0):
        if data is None:
            if shape is None or dtype is None:
                raise ValueError("must specify either data or both shape and dtype")
        else:
            data = _np.asarray(data, dtype)
            if shape is not None:
                data = data.reshape(shape)
            shape = data.shape
            dtype = data.dtype.type

        if len(shape) != self._ndim:
            raise TypeError("shape must be %d-dimensional" % self._ndim)

        _iformat = constants.numpy_to_gl_iformat[dtype, shape[-1]]
        _format = constants.numpy_to_gl_format[dtype, shape[-1]]
        _type = constants.numpy_to_gl_type[dtype]
        _data = _np.ascontiguousarray(data).ctypes if data is not None else _gl.POINTER(_gl.GLvoid)()
        _gl.glPixelStorei(_gl.GL_UNPACK_ALIGNMENT, 1)
        with self:
            args = [self._target, level, _iformat] + list(reversed(shape[:-1])) + [0, _format, _type, _data]
            self._set(*args)
        if not constants.is_float[self.dtype]:
            self.min_filter = Texture.min_filters.NEAREST
            self.mag_filter = Texture.mag_filters.NEAREST

    def get_data(self, level=0):
        _data = _np.empty(self.shape, dtype=self.dtype)
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
        with self:
            colors = constants.gl_iformat_to_numpy[self._iformat][1]        
            _width = _gl.GLint()
            _gl.glGetTexLevelParameteriv(self._target, 0, _gl.GL_TEXTURE_WIDTH, _gl.pointer(_width))
            if self._ndim == 2:
                return (_width.value, colors)
            _height = _gl.GLint()
            _gl.glGetTexLevelParameteriv(self._target, 0, _gl.GL_TEXTURE_HEIGHT, _gl.pointer(_height))
            if self._ndim == 3:
                return (_height.value, _width.value, colors)
            _depth = _gl.GLint()
            _gl.glGetTexLevelParameteriv(self._target, 0, _gl.GL_TEXTURE_DEPTH, _gl.pointer(_depth))
            if self._ndim == 4:
                return (_depth.value, _height.value, _width.value, colors)

    @property
    def dtype(self):
        return constants.gl_iformat_to_numpy[self._iformat][0]

    @property
    def _iformat(self):
        _iformat = _gl.GLint()
        with self:
            _gl.glGetTexLevelParameteriv(self._target, 0, _gl.GL_TEXTURE_INTERNAL_FORMAT, _gl.pointer(_iformat))
        return _iformat.value

    @property
    def _format(self):
        return constants.numpy_to_gl_format[self.dtype, self.shape[-1]]

    @property
    def _type(self):
        return constants.gl_iformat_to_gl_type[self._iformat]

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
        if constants.is_float[self.dtype]:
            _border_color = (_gl.GLfloat * 4)()
            with self:
                _gl.glGetTexParameterfv(self._target, _gl.GL_TEXTURE_BORDER_COLOR, _border_color)
        elif constants.is_signed[self.dtype]:
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
        if constants.is_float[self.dtype]:
            _border_color = (_gl.GLfloat * 4)()
            for i, v in zip(range(4), border_color):
                _border_color[i] = v
            with self:
                _gl.glTexParameterfv(self._target, _gl.GL_TEXTURE_BORDER_COLOR, _border_color)
        elif constants.is_signed[self.dtype]:
            _border_color = (_gl.GLint * 4)()
            for i, v in zip(range(4), border_color):
                _border_color[i] = v
            with self:
                _gl.glTexParameterIiv(self._target, _gl.GL_TEXTURE_BORDER_COLOR, _border_color)
        else:
            _border_color = (_gl.GLuint * 4)()
            for i, v in zip(range(4), border_color):
                _border_color[i] = v
            with self:
                _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_BORDER_COLOR, _border_color)

    @property
    def compare_func(self):
        _compare_func = _gl.GLenum()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_COMPARE_FUNC, _gl.pointer(_compare_func))
        return Texture.compare_funcs[_compare_func.value]

    @compare_func.setter
    def compare_func(self, compare_func):
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_COMPARE_FUNC, _gl.pointer(_gl.GLenum(compare_func._value)))

    @property
    def compare_mode(self):
        _compare_mode = _gl.GLenum()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_COMPARE_MODE, _gl.pointer(_compare_mode))
        return Texture.compare_modes[_compare_mode.value]

    @compare_mode.setter
    def compare_mode(self, compare_mode):
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_COMPARE_MODE, _gl.pointer(_gl.GLenum(compare_mode._value)))
    
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
        return Texture.min_filters[_min_filter.value]

    @min_filter.setter
    def min_filter(self, min_filter):
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_MIN_FILTER, _gl.pointer(_gl.GLenum(min_filter._value)))

    @property
    def mag_filter(self):
        _mag_filter = _gl.GLenum()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_MAG_FILTER, _gl.pointer(_mag_filter))
        return Texture.mag_filters[_mag_filter.value]

    @mag_filter.setter
    def mag_filter(self, mag_filter):
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_MAG_FILTER, _gl.pointer(_gl.GLenum(mag_filter._value)))

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
        return Texture.swizzles[_swizzle_r.value]

    @swizzle_r.setter
    def swizzle_r(self, swizzle_r):
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_SWIZZLE_R, _gl.pointer(_gl.GLenum(swizzle_r._value)))

    @property
    def swizzle_g(self):
        _swizzle_g = _gl.GLenum()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_SWIZZLE_G, _gl.pointer(_swizzle_g))
        return Texture.swizzles[_swizzle_g.value]

    @swizzle_g.setter
    def swizzle_g(self, swizzle_g):
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_SWIZZLE_G, _gl.pointer(_gl.GLenum(swizzle_g._value)))

    @property
    def swizzle_b(self):
        _swizzle_b = _gl.GLenum()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_SWIZZLE_B, _gl.pointer(_swizzle_b))
        return Texture.swizzles[_swizzle_b.value]

    @swizzle_b.setter
    def swizzle_b(self, swizzle_b):
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_SWIZZLE_B, _gl.pointer(_gl.GLenum(swizzle_b._value)))

    @property
    def swizzle_a(self):
        _swizzle_a = _gl.GLenum()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_SWIZZLE_A, _gl.pointer(_swizzle_a))
        return Texture.swizzles[_swizzle_a.value]

    @swizzle_a.setter
    def swizzle_a(self, swizzle_a):
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_SWIZZLE_A, _gl.pointer(_gl.GLenum(swizzle_a._value)))

    @property
    def swizzle_rgba(self):
        _swizzle_rgba = (_gl.GLenum * 4)()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_SWIZZLE_RGBA, _swizzle_rgba)
        return [Texture.swizzles[_swizzle_rgba[i]] for i in range(4)]

    @swizzle_rgba.setter
    def swizzle_rgba(self, swizzle_rgba):
        _swizzle_rgba = (_gl.GLenum * 4)()
        for i, v in zip(range(4), swizzle_rgba):
            _swizzle_rgba[i] = v._value
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_SWIZZLE_RGBA, _swizzle_rgba)

    @property
    def wrap_s(self):
        _wrap_s = _gl.GLenum()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_WRAP_S, _gl.pointer(_wrap_s))
        return Texture.wrapmodes[_wrap_s.value]

    @wrap_s.setter
    def wrap_s(self, wrap_s):
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_WRAP_S, _gl.pointer(_gl.GLenum(wrap_s._value)))

    @property
    def wrap_t(self):
        _wrap_t = _gl.GLenum()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_WRAP_T, _gl.pointer(_wrap_t))
        return Texture.wrapmodes[_wrap_t.value]

    @wrap_t.setter
    def wrap_t(self, wrap_t):
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_WRAP_T, _gl.pointer(_gl.GLenum(wrap_t._value)))

    @property
    def wrap_r(self):
        _wrap_r = _gl.GLenum()
        with self:
            _gl.glGetTexParameterIuiv(self._target, _gl.GL_TEXTURE_WRAP_R, _gl.pointer(_wrap_r))
        return Texture.wrapmodes[_wrap_r.value]

    @wrap_r.setter
    def wrap_r(self, wrap_r):
        with self:
            _gl.glTexParameterIuiv(self._target, _gl.GL_TEXTURE_WRAP_R, _gl.pointer(_gl.GLenum(wrap_r._value)))

class Texture1D(Texture):
    _target = _gl.GL_TEXTURE_1D
    _binding = _gl.GL_TEXTURE_BINDING_1D
    _ndim = 2
    _set = _gl.glTexImage1D

class Texture2D(Texture):
    _target = _gl.GL_TEXTURE_2D
    _binding = _gl.GL_TEXTURE_BINDING_2D
    _ndim = 3
    _set = _gl.glTexImage2D

class TextureArray1D(Texture):
    _target = _gl.GL_TEXTURE_1D_ARRAY
    _binding = _gl.GL_TEXTURE_BINDING_1D_ARRAY
    _ndim = 3
    _set = _gl.glTexImage2D

class RectangleTexture(Texture):
    _target = _gl.GL_TEXTURE_RECTANGLE
    _binding = _gl.GL_TEXTURE_BINDING_RECTANGLE
    _ndim = 3
    _set = _gl.glTexImage2D

class BufferTexture(Texture): # TODO override constructor, set_data and get_data: glTexBuffer
    _target = _gl.GL_TEXTURE_BUFFER
    _binding = _gl.GL_TEXTURE_BINDING_BUFFER
    _ndim = 3
    _set = _gl.glTexImage2D

class CubeMapTexture(Texture):
    _target = _gl.GL_TEXTURE_CUBE_MAP
    _binding = _gl.GL_TEXTURE_BINDING_CUBE_MAP
    _ndim = 3
    _set = _gl.glTexImage2D

class MultisampleTexture2D(Texture):
    _target = _gl.GL_TEXTURE_2D_MULTISAMPLE
    _binding = _gl.GL_TEXTURE_BINDING_2D_MULTISAMPLE
    _ndim = 3
    _set = _gl.glTexImage2D

class Texture3D(Texture):
    _target = _gl.GL_TEXTURE_3D
    _binding = _gl.GL_TEXTURE_BINDING_3D
    _ndim = 4
    _set = _gl.glTexImage3D

class TextureArray2D(Texture):
    _target = _gl.GL_TEXTURE_2D_ARRAY
    _binding = _gl.GL_TEXTURE_BINDING_2D_ARRAY
    _ndim = 4
    _set = _gl.glTexImage3D

class MultisampleTextureArray2D(Texture):
    _target = _gl.GL_TEXTURE_2D_MULTISAMPLE_ARRAY
    _binding = _gl.GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY
    _ndim = 4
    _set = _gl.glTexImage3D


# nosetests

def check_texture(shape, dtype, vrange):
    minval, maxval = vrange
    data = ((maxval - minval) * _np.random.random(shape) + minval).astype(dtype)
    texture = Texture3D(data)
    assert (texture.data == data).all(), "data is broken"
    assert texture.shape == data.shape, "shape is broken"
    assert texture.dtype == data.dtype, "dtype is broken"
    assert texture._iformat == constants.numpy_to_gl_iformat[data.dtype.type, data.shape[-1]], "_iformat is broken"
    assert texture._format == constants.numpy_to_gl_format[data.dtype.type, data.shape[-1]], "_format is broken"
    assert texture._type == constants.numpy_to_gl_type[data.dtype.type], "_type is broken"

def test_texture_generator():
    shapes = ((4, 4, 4, 4), (4, 4, 4, 3), (4, 16, 8, 3), (5, 4, 4, 3), (5, 5, 5, 3), (6, 6, 6, 3), (7, 13, 5, 3), (1, 1, 3, 3))
    dtypes = (_np.uint8, _np.int8, _np.uint16, _np.int16, _np.uint32, _np.int32, _np.float32)
    vranges = ((0, (1<<8)-1), (-1<<7, (1<<7)-1), (0, (1<<16)-1), (-1<<15, (1<<15)-1), (0, (1<<32)-1), (-1<<31, (1<<31)-1), (-10.0, 10.0))

    for shape in shapes:
        for dtype, vrange in zip(dtypes, vranges):
            yield check_texture, shape, dtype, vrange

def check_property(texture, name):
    from util import EnumConstant
    value = getattr(texture, name)
    if isinstance(value, EnumConstant):
        valid_values = value._enum._reverse_dict.values()
        for value in valid_values:
            setattr(texture, name, value)
            assert getattr(texture, name) == value, "property %s is broken" % name
    else:
        setattr(texture, name, value)
        assert getattr(texture, name) == value, "property %s is broken" % name

def test_property_generator():
    texture = Texture3D(_np.random.random((1, 1, 1, 4)).astype(_np.float32))
    properties = [x for x in dir(texture) if not x.startswith("_") and type(getattr(Texture, x)) == property]

    for p in properties:
        if p in ("data", "shape", "dtype"):
            continue
        if getattr(Texture, p).fset is None:
            continue
        yield check_property, texture, p

