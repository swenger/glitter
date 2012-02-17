import numpy

from rawgl import gl as _gl

from util import GLObject

# TODO check memory layout
# TODO depth texture, pixel unpack buffer
# TODO __getitem__/__setitem__ for subimages (glTexSubImage3D, glGetTexImage with format = GL_RED etc.)
# TODO glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_WRAP_S, GL_REPEAT); glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
# TODO mipmaps (level != 0) with glGenerateMipmap

_texture_formats = [ # (numpy dtype, number of color channels), OpenGL internal format, (OpenGL type, OpenGL format)
        ((numpy.uint8,   1), _gl.GL_R8UI,     (_gl.GL_UNSIGNED_BYTE,  _gl.GL_RED_INTEGER )),
        ((numpy.int8,    1), _gl.GL_R8I,      (_gl.GL_BYTE,           _gl.GL_RED_INTEGER )),
        ((numpy.uint16,  1), _gl.GL_R16UI,    (_gl.GL_UNSIGNED_SHORT, _gl.GL_RED_INTEGER )),
        ((numpy.int16,   1), _gl.GL_R16I,     (_gl.GL_SHORT,          _gl.GL_RED_INTEGER )),
        ((numpy.uint32,  1), _gl.GL_R32UI,    (_gl.GL_UNSIGNED_INT,   _gl.GL_RED_INTEGER )),
        ((numpy.int32,   1), _gl.GL_R32I,     (_gl.GL_INT,            _gl.GL_RED_INTEGER )),
        ((numpy.float32, 1), _gl.GL_R32F,     (_gl.GL_FLOAT,          _gl.GL_RED         )),
        ((numpy.uint8,   2), _gl.GL_RG8UI,    (_gl.GL_UNSIGNED_BYTE,  _gl.GL_RG_INTEGER  )),
        ((numpy.int8,    2), _gl.GL_RG8I,     (_gl.GL_BYTE,           _gl.GL_RG_INTEGER  )),
        ((numpy.uint16,  2), _gl.GL_RG16UI,   (_gl.GL_UNSIGNED_SHORT, _gl.GL_RG_INTEGER  )),
        ((numpy.int16,   2), _gl.GL_RG16I,    (_gl.GL_SHORT,          _gl.GL_RG_INTEGER  )),
        ((numpy.uint32,  2), _gl.GL_RG32UI,   (_gl.GL_UNSIGNED_INT,   _gl.GL_RG_INTEGER  )),
        ((numpy.int32,   2), _gl.GL_RG32I,    (_gl.GL_INT,            _gl.GL_RG_INTEGER  )),
        ((numpy.float32, 2), _gl.GL_RG32F,    (_gl.GL_FLOAT,          _gl.GL_RG          )),
        ((numpy.uint8,   3), _gl.GL_RGB8UI,   (_gl.GL_UNSIGNED_BYTE,  _gl.GL_RGB_INTEGER )),
        ((numpy.int8,    3), _gl.GL_RGB8I,    (_gl.GL_BYTE,           _gl.GL_RGB_INTEGER )),
        ((numpy.uint16,  3), _gl.GL_RGB16UI,  (_gl.GL_UNSIGNED_SHORT, _gl.GL_RGB_INTEGER )),
        ((numpy.int16,   3), _gl.GL_RGB16I,   (_gl.GL_SHORT,          _gl.GL_RGB_INTEGER )),
        ((numpy.uint32,  3), _gl.GL_RGB32UI,  (_gl.GL_UNSIGNED_INT,   _gl.GL_RGB_INTEGER )),
        ((numpy.int32,   3), _gl.GL_RGB32I,   (_gl.GL_INT,            _gl.GL_RGB_INTEGER )),
        ((numpy.float32, 3), _gl.GL_RGB32F,   (_gl.GL_FLOAT,          _gl.GL_RGB         )),
        ((numpy.uint8,   4), _gl.GL_RGBA8UI,  (_gl.GL_UNSIGNED_BYTE,  _gl.GL_RGBA_INTEGER)),
        ((numpy.int8,    4), _gl.GL_RGBA8I,   (_gl.GL_BYTE,           _gl.GL_RGBA_INTEGER)),
        ((numpy.uint16,  4), _gl.GL_RGBA16UI, (_gl.GL_UNSIGNED_SHORT, _gl.GL_RGBA_INTEGER)),
        ((numpy.int16,   4), _gl.GL_RGBA16I,  (_gl.GL_SHORT,          _gl.GL_RGBA_INTEGER)),
        ((numpy.uint32,  4), _gl.GL_RGBA32UI, (_gl.GL_UNSIGNED_INT,   _gl.GL_RGBA_INTEGER)),
        ((numpy.int32,   4), _gl.GL_RGBA32I,  (_gl.GL_INT,            _gl.GL_RGBA_INTEGER)),
        ((numpy.float32, 4), _gl.GL_RGBA32F,  (_gl.GL_FLOAT,          _gl.GL_RGBA        )),
] # TODO internal formats GL_DEPTH_COMPONENT, GL_DEPTH_STENCIL
_numpy_to_gl_iformat =   dict((x[0],    x[1]   ) for x in _texture_formats)
_gl_iformat_to_numpy =   dict((x[1],    x[0]   ) for x in _texture_formats)
_numpy_to_gl_format =    dict((x[0],    x[2][1]) for x in _texture_formats)
_gl_format_to_numpy =    dict((x[2][1], x[0]   ) for x in _texture_formats)
_numpy_to_gl_type =      dict((x[0][0], x[2][0]) for x in _texture_formats)
_gl_type_to_numpy =      dict((x[2][0], x[0][0]) for x in _texture_formats)
_gl_iformat_to_gl_type = dict((x[1],    x[2][0]) for x in _texture_formats)

class Texture(GLObject):
    _generate_id = _gl.glGenTextures
    _delete_id = _gl.glDeleteTextures
    _bind = _gl.glBindTexture

    _ndim = NotImplemented
    _set = NotImplemented

    def __init__(self, data=None, shape=None, dtype=None):
        super(Texture, self).__init__()

        if any(x is NotImplemented for x in (self._ndim, self._set)):
            raise TypeError("%s is abstract" % self.__class__.__name__)
        
        self.setdata(data, shape, dtype)

    def setdata(self, data=None, shape=None, dtype=None, level=0):
        if data is None:
            if shape is None or dtype is None:
                raise ValueError("must specify either data or both shape and dtype")
        else:
            if shape is not None or dtype is not None:
                raise ValueError("cannot specify both data and either shape and dtype")
            shape = data.shape
            dtype = data.dtype.type

        if len(shape) != self._ndim:
            raise TypeError("shape must be %d-dimensional" % self._ndim)

        _iformat = _numpy_to_gl_iformat[dtype, shape[-1]]
        _format = _numpy_to_gl_format[dtype, shape[-1]]
        _type = _numpy_to_gl_type[dtype]
        _data = numpy.ascontiguousarray(data).ctypes if data is not None else _gl.POINTER(_gl.GLvoid)()
        _gl.glPixelStorei(_gl.GL_UNPACK_ALIGNMENT, 1)
        with self:
            args = [self._target, level, _iformat] + list(reversed(shape[:-1])) + [0, _format, _type, _data]
            self._set(*args)

    def getdata(self, level=0):
        _data = numpy.empty(self.shape, dtype=self.dtype)
        _gl.glPixelStorei(_gl.GL_PACK_ALIGNMENT, 1)
        with self:
            _gl.glGetTexImage(self._target, level, self._format, self._type, _data.ctypes)
        return _data

    @property
    def data(self):
        return self.getdata()

    @data.setter
    def data(self, data):
        self.setdata(data)

    @property
    def shape(self):
        with self:
            colors = _gl_iformat_to_numpy[self._iformat][1]        
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
    def _iformat(self):
        _iformat = _gl.GLint()
        with self:
            _gl.glGetTexLevelParameteriv(self._target, 0, _gl.GL_TEXTURE_INTERNAL_FORMAT, _gl.pointer(_iformat))
        return _iformat.value

    @property
    def _format(self):
        return _numpy_to_gl_format[self.dtype, self.shape[-1]]

    @property
    def _type(self):
        return _gl_iformat_to_gl_type[self._iformat]

    @property
    def dtype(self):
        return _gl_iformat_to_numpy[self._iformat][0]

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

class Texture1DArray(Texture):
    _target = _gl.GL_TEXTURE_1D_ARRAY
    _binding = _gl.GL_TEXTURE_BINDING_1D_ARRAY
    _ndim = 3
    _set = _gl.glTexImage2D

class TextureRectangle(Texture):
    _target = _gl.GL_TEXTURE_RECTANGLE
    _binding = _gl.GL_TEXTURE_BINDING_RECTANGLE
    _ndim = 3
    _set = _gl.glTexImage2D

class TextureBuffer(Texture):
    _target = _gl.GL_TEXTURE_BUFFER
    _binding = _gl.GL_TEXTURE_BINDING_BUFFER
    _ndim = 3
    _set = _gl.glTexImage2D

class TextureCubeMap(Texture):
    _target = _gl.GL_TEXTURE_CUBE_MAP
    _binding = _gl.GL_TEXTURE_BINDING_CUBE_MAP
    _ndim = 3
    _set = _gl.glTexImage2D

class Texture2DMultisample(Texture):
    _target = _gl.GL_TEXTURE_2D_MULTISAMPLE
    _binding = _gl.GL_TEXTURE_BINDING_2D_MULTISAMPLE
    _ndim = 3
    _set = _gl.glTexImage2D

class Texture3D(Texture):
    _target = _gl.GL_TEXTURE_3D
    _binding = _gl.GL_TEXTURE_BINDING_3D
    _ndim = 4
    _set = _gl.glTexImage3D

class Texture2DArray(Texture):
    _target = _gl.GL_TEXTURE_2D_ARRAY
    _binding = _gl.GL_TEXTURE_BINDING_2D_ARRAY
    _ndim = 4
    _set = _gl.glTexImage3D

class Texture2DMultisampleArray(Texture):
    _target = _gl.GL_TEXTURE_2D_MULTISAMPLE_ARRAY
    _binding = _gl.GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY
    _ndim = 4
    _set = _gl.glTexImage3D


# nosetests

def check_texture(shape, dtype, vrange):
    minval, maxval = vrange
    data = ((maxval - minval) * numpy.random.random(shape) + minval).astype(dtype)
    texture = Texture3D(data)
    assert texture.shape == data.shape, "shape is broken"
    assert texture._iformat == _numpy_to_gl_iformat[data.dtype.type, data.shape[-1]], "_iformat is broken"
    assert texture._format == _numpy_to_gl_format[data.dtype.type, data.shape[-1]], "_format is broken"
    assert texture._type == _numpy_to_gl_type[data.dtype.type], "_type is broken"
    assert texture.dtype == data.dtype, "dtype is broken"
    tdata = texture.data
    assert (tdata == data).all(), "data is broken"

def test_generator():
    shapes = ((4, 4, 4, 4), (4, 4, 4, 3), (4, 16, 8, 3), (5, 4, 4, 3), (5, 5, 5, 3), (6, 6, 6, 3), (7, 13, 5, 3), (1, 1, 3, 3))
    dtypes = (numpy.uint8, numpy.int8, numpy.uint16, numpy.int16, numpy.uint32, numpy.int32, numpy.float32)
    vranges = ((0, (1<<8)-1), (-1<<7, (1<<7)-1), (0, (1<<16)-1), (-1<<15, (1<<15)-1), (0, (1<<32)-1), (-1<<31, (1<<31)-1), (-10.0, 10.0))

    for shape in shapes:
        for dtype, vrange in zip(dtypes, vranges):
            yield check_texture, shape, dtype, vrange

