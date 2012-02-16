import numpy

from rawgl import gl as _gl

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

_texture_targets = [ # target, binding, dimensions including color, (name, dimension)
        (_gl.GL_TEXTURE_1D,                   _gl.GL_TEXTURE_BINDING_1D,                   ("texture",           2)),
        (_gl.GL_TEXTURE_2D,                   _gl.GL_TEXTURE_BINDING_2D,                   ("texture",           3)),
        (_gl.GL_TEXTURE_1D_ARRAY,             _gl.GL_TEXTURE_BINDING_1D_ARRAY,             ("array",             3)),
        (_gl.GL_TEXTURE_2D_MULTISAMPLE,       _gl.GL_TEXTURE_BINDING_2D_MULTISAMPLE,       ("multisample",       3)),
        (_gl.GL_TEXTURE_BUFFER,               _gl.GL_TEXTURE_BINDING_BUFFER,               ("buffer",            3)),
        (_gl.GL_TEXTURE_CUBE_MAP,             _gl.GL_TEXTURE_BINDING_CUBE_MAP,             ("cubemap",           3)),
        (_gl.GL_TEXTURE_RECTANGLE,            _gl.GL_TEXTURE_BINDING_RECTANGLE,            ("rectangle",         3)),
        (_gl.GL_TEXTURE_3D,                   _gl.GL_TEXTURE_BINDING_3D,                   ("texture",           4)),
        (_gl.GL_TEXTURE_2D_ARRAY,             _gl.GL_TEXTURE_BINDING_2D_ARRAY,             ("array",             4)),
        (_gl.GL_TEXTURE_2D_MULTISAMPLE_ARRAY, _gl.GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY, ("multisample_array", 4)),
]
_numpy_to_gl_target = dict(reversed([(x[2][0], x[0]   ) for x in _texture_targets]))
_texture_target_to_binding =    dict((x[0],    x[1]   ) for x in _texture_targets)
_texture_target_to_dimensions = dict((x[0],    x[2][1]) for x in _texture_targets)
_name_to_target =               dict((x[2],    x[0]   ) for x in _texture_targets)

class Texture(object):
    # TODO check memory layout: "The first element corresponds to the lower left corner of the texture image. Subsequent elements progress left-to-right through the remaining texels in the lowest row of the texture image, and then in successively higher rows of the texture image. The final element corresponds to the upper right corner of the texture image."
    # TODO depth texture, pixel unpack buffer, glPixelStore
    # TODO __getitem__/__setitem__ for subimages (glTexSubImage3D, glGetTexImage with format = GL_RED etc.)
    # TODO glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_WRAP_S, GL_REPEAT); glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    # TODO mipmaps (level != 0) with glGenerateMipmap

    def __init__(self, data=None, shape=None, dtype=None, target="texture"):
        dtype = dtype or data.dtype.type
        shape = shape or data.shape

        _id = _gl.GLuint()
        _gl.glGenTextures(1, _gl.pointer(_id))
        self._id = _id.value
        self._stack = []
        self._target = _name_to_target[target, len(shape)] or _numpy_to_gl_target[len(shape)]

        _iformat = _numpy_to_gl_iformat[dtype, shape[-1]]
        _format = _numpy_to_gl_format[dtype, shape[-1]]
        _type = _numpy_to_gl_type[dtype]
        _data = data.ctypes if data is not None else _gl.POINTER(_gl.GLvoid)()
        _gl.glPixelStorei(_gl.GL_UNPACK_ALIGNMENT, 1)
        with self:
            _gl.glTexImage3D(self._target, 0, _iformat, shape[0], shape[1], shape[2], 0, _format, _type, _data)

    def __del__(self):
        try:
            _gl.glDeleteTextures(1, _gl.pointer(_gl.GLuint(self._id)))
            self._id = 0
        except AttributeError:
            pass # avoid "'NoneType' object has no attribute 'glDeleteTextures'" when GL module has already been unloaded

    @property
    def shape(self):
        with self:
            _width = _gl.GLint()
            _gl.glGetTexLevelParameteriv(self._target, 0, _gl.GL_TEXTURE_WIDTH, _gl.pointer(_width))
            _height = _gl.GLint()
            _gl.glGetTexLevelParameteriv(self._target, 0, _gl.GL_TEXTURE_HEIGHT, _gl.pointer(_height))
            _depth = _gl.GLint()
            _gl.glGetTexLevelParameteriv(self._target, 0, _gl.GL_TEXTURE_DEPTH, _gl.pointer(_depth))
            colors = _gl_iformat_to_numpy[self._iformat][1]        
        return (_width.value, _height.value, _depth.value, colors)

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

    @property
    def ndim(self):
        return _texture_target_to_dimensions[self._target]

    @property
    def data(self):
        _data = numpy.empty(self.shape, dtype=self.dtype)
        _gl.glPixelStorei(_gl.GL_PACK_ALIGNMENT, 1)
        with self:
            _gl.glGetTexImage(self._target, 0, self._format, self._type, _data.ctypes)
        return _data

    @data.setter
    def data(self, data):
        _data = numpy.ascontiguousarray(data.ctypes) if data is not None else _gl.POINTER(_gl.GLvoid)()
        _gl.glPixelStorei(_gl.GL_UNPACK_ALIGNMENT, 1)
        with self:
            _gl.glTexImage3D(self._target, 0, self._iformat, self.shape[2], self.shape[1], self.shape[0], 0, self._format, self._type, _data)

    def bind(self):
        old_binding = _gl.GLint()
        _gl.glGetIntegerv(_texture_target_to_binding[self._target], _gl.pointer(old_binding))
        _gl.glBindTexture(self._target, self._id)
        return old_binding.value

    def __enter__(self):
        self._stack.append(self.bind())

    def __exit__(self, type, value, traceback):
        _gl.glBindTexture(self._target, self._stack.pop())


def test_texture(shape, dtype):
    data = (255 * numpy.random.random(shape)).astype(dtype) # TODO make this work for float, signed and unsigned integer dtypes
    texture = Texture(data)
    assert texture.shape == data.shape, "shape is broken"
    assert texture._iformat == _numpy_to_gl_iformat[data.dtype.type, data.shape[-1]], "_iformat is broken"
    assert texture._format == _numpy_to_gl_format[data.dtype.type, data.shape[-1]], "_format is broken"
    assert texture._type == _numpy_to_gl_type[data.dtype.type], "_type is broken"
    assert texture.dtype == data.dtype, "dtype is broken"
    tdata = texture.data
    assert (tdata == data).all(), "data is broken"

if __name__ == "__main__":
    from glitter import GlutWindow
    window = GlutWindow()

    shapes = ((4, 4, 4, 4), (4, 4, 4, 3), (4, 16, 8, 3), (5, 4, 4, 3), (5, 5, 5, 3), (6, 6, 6, 3), (7, 13, 5, 3), (1, 1, 3, 3))
    dtypes = (numpy.uint8, numpy.int8, numpy.uint16, numpy.int16, numpy.uint32, numpy.int32, numpy.float32)

    column_headers = ["%20s" % "shape"] + [dtype.__name__ for dtype in dtypes]
    column_formats = ["%%%ds" % max(len(column_header), 7) for column_header in column_headers]

    for column_header, column_format in zip(column_headers, column_formats):
        print column_format % column_header,
    print

    for shape in shapes:
        print column_formats[0] % str(shape),
        for dtype, column_format in zip(dtypes, column_formats[1:]):
            try:
                test_texture(shape, dtype)
            except Exception, e:
                print column_format % "FAIL",
            else:
                print column_format % "PASS",
        print

