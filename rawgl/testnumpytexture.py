import numpy
from glitter import GlutWindow

import gl

texture_formats = [ # (numpy dtype, number of color channels), OpenGL internal format, (OpenGL type, OpenGL format)
        ((numpy.uint8,   1), gl.GL_R8UI,     (gl.GL_UNSIGNED_BYTE,  gl.GL_RED_INTEGER )),
        ((numpy.int8,    1), gl.GL_R8I,      (gl.GL_BYTE,           gl.GL_RED_INTEGER )),
        ((numpy.uint16,  1), gl.GL_R16UI,    (gl.GL_UNSIGNED_SHORT, gl.GL_RED_INTEGER )),
        ((numpy.int16,   1), gl.GL_R16I,     (gl.GL_SHORT,          gl.GL_RED_INTEGER )),
        ((numpy.uint32,  1), gl.GL_R32UI,    (gl.GL_UNSIGNED_INT,   gl.GL_RED_INTEGER )),
        ((numpy.int32,   1), gl.GL_R32I,     (gl.GL_INT,            gl.GL_RED_INTEGER )),
        ((numpy.float32, 1), gl.GL_R32F,     (gl.GL_FLOAT,          gl.GL_RED         )),
        ((numpy.uint8,   2), gl.GL_RG8UI,    (gl.GL_UNSIGNED_BYTE,  gl.GL_RG_INTEGER  )),
        ((numpy.int8,    2), gl.GL_RG8I,     (gl.GL_BYTE,           gl.GL_RG_INTEGER  )),
        ((numpy.uint16,  2), gl.GL_RG16UI,   (gl.GL_UNSIGNED_SHORT, gl.GL_RG_INTEGER  )),
        ((numpy.int16,   2), gl.GL_RG16I,    (gl.GL_SHORT,          gl.GL_RG_INTEGER  )),
        ((numpy.uint32,  2), gl.GL_RG32UI,   (gl.GL_UNSIGNED_INT,   gl.GL_RG_INTEGER  )),
        ((numpy.int32,   2), gl.GL_RG32I,    (gl.GL_INT,            gl.GL_RG_INTEGER  )),
        ((numpy.float32, 2), gl.GL_RG32F,    (gl.GL_FLOAT,          gl.GL_RG          )),
        ((numpy.uint8,   3), gl.GL_RGB8UI,   (gl.GL_UNSIGNED_BYTE,  gl.GL_RGB_INTEGER )),
        ((numpy.int8,    3), gl.GL_RGB8I,    (gl.GL_BYTE,           gl.GL_RGB_INTEGER )),
        ((numpy.uint16,  3), gl.GL_RGB16UI,  (gl.GL_UNSIGNED_SHORT, gl.GL_RGB_INTEGER )),
        ((numpy.int16,   3), gl.GL_RGB16I,   (gl.GL_SHORT,          gl.GL_RGB_INTEGER )),
        ((numpy.uint32,  3), gl.GL_RGB32UI,  (gl.GL_UNSIGNED_INT,   gl.GL_RGB_INTEGER )),
        ((numpy.int32,   3), gl.GL_RGB32I,   (gl.GL_INT,            gl.GL_RGB_INTEGER )),
        ((numpy.float32, 3), gl.GL_RGB32F,   (gl.GL_FLOAT,          gl.GL_RGB         )),
        ((numpy.uint8,   4), gl.GL_RGBA8UI,  (gl.GL_UNSIGNED_BYTE,  gl.GL_RGBA_INTEGER)),
        ((numpy.int8,    4), gl.GL_RGBA8I,   (gl.GL_BYTE,           gl.GL_RGBA_INTEGER)),
        ((numpy.uint16,  4), gl.GL_RGBA16UI, (gl.GL_UNSIGNED_SHORT, gl.GL_RGBA_INTEGER)),
        ((numpy.int16,   4), gl.GL_RGBA16I,  (gl.GL_SHORT,          gl.GL_RGBA_INTEGER)),
        ((numpy.uint32,  4), gl.GL_RGBA32UI, (gl.GL_UNSIGNED_INT,   gl.GL_RGBA_INTEGER)),
        ((numpy.int32,   4), gl.GL_RGBA32I,  (gl.GL_INT,            gl.GL_RGBA_INTEGER)),
        ((numpy.float32, 4), gl.GL_RGBA32F,  (gl.GL_FLOAT,          gl.GL_RGBA        )),
] # TODO internal formats GL_DEPTH_COMPONENT, GL_DEPTH_STENCIL

numpy_to_gl_iformat =   dict((fmt[0],    fmt[1]   ) for fmt in texture_formats)
gl_iformat_to_numpy =   dict((fmt[1],    fmt[0]   ) for fmt in texture_formats)
numpy_to_gl_format =    dict((fmt[0],    fmt[2][1]) for fmt in texture_formats)
gl_format_to_numpy =    dict((fmt[2][1], fmt[0]   ) for fmt in texture_formats)
numpy_to_gl_type =      dict((fmt[0][0], fmt[2][0]) for fmt in texture_formats)
gl_type_to_numpy =      dict((fmt[2][0], fmt[0][0]) for fmt in texture_formats)
gl_iformat_to_gl_type = dict((fmt[1],    fmt[2][0]) for fmt in texture_formats)

texture_targets = [ # target, binding, dimensions including color
        (gl.GL_TEXTURE_1D,                   gl.GL_TEXTURE_BINDING_1D,                   2),
        (gl.GL_TEXTURE_2D,                   gl.GL_TEXTURE_BINDING_2D,                   3),
        (gl.GL_TEXTURE_1D_ARRAY,             gl.GL_TEXTURE_BINDING_1D_ARRAY,             3),
        (gl.GL_TEXTURE_2D_MULTISAMPLE,       gl.GL_TEXTURE_BINDING_2D_MULTISAMPLE,       3),
        (gl.GL_TEXTURE_BUFFER,               gl.GL_TEXTURE_BINDING_BUFFER,               3),
        (gl.GL_TEXTURE_CUBE_MAP,             gl.GL_TEXTURE_BINDING_CUBE_MAP,             3),
        (gl.GL_TEXTURE_RECTANGLE,            gl.GL_TEXTURE_BINDING_RECTANGLE,            3),
        (gl.GL_TEXTURE_3D,                   gl.GL_TEXTURE_BINDING_3D,                   4),
        (gl.GL_TEXTURE_2D_ARRAY,             gl.GL_TEXTURE_BINDING_2D_ARRAY,             4),
        (gl.GL_TEXTURE_2D_MULTISAMPLE_ARRAY, gl.GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY, 4),
]

numpy_to_gl_target = dict(reversed([(tgt[2], tgt[0]) for tgt in texture_targets]))
texture_target_to_binding = dict((tgt[0], tgt[1]) for tgt in texture_targets)
texture_target_to_dimensions = dict((tgt[0], tgt[2]) for tgt in texture_targets)

class Texture(object):
    # TODO check memory layout: "The first element corresponds to the lower left corner of the texture image. Subsequent elements progress left-to-right through the remaining texels in the lowest row of the texture image, and then in successively higher rows of the texture image. The final element corresponds to the upper right corner of the texture image."
    # TODO depth texture, pixel unpack buffer, glPixelStore
    # TODO __getitem__/__setitem__ for subimages (glTexSubImage3D, glGetTexImage with format = GL_RED etc.)
    # TODO glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_WRAP_S, GL_REPEAT); glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    # TODO mipmaps (level != 0) with glGenerateMipmap

    def __init__(self, data=None, shape=None, dtype=None, target=None):
        dtype = dtype or data.dtype.type
        shape = shape or data.shape

        id = gl.GLuint()
        gl.glGenTextures(1, gl.pointer(id))
        self.id = id.value
        self.stack = []
        self.target = target or numpy_to_gl_target[len(shape)]

        gl_iformat = numpy_to_gl_iformat[dtype, shape[-1]]
        gl_format = numpy_to_gl_format[dtype, shape[-1]]
        gl_type = numpy_to_gl_type[dtype]
        data = data.ctypes if data is not None else gl.POINTER(gl.GLvoid)()
        with self:
            gl.glTexImage3D(self.target, 0, gl_iformat, shape[0], shape[1], shape[2], 0, gl_format, gl_type, data)

    def __del__(self):
        try:
            gl.glDeleteTextures(1, gl.pointer(gl.GLuint(self.id)))
        except AttributeError:
            pass # "'NoneType' object has no attribute 'glDeleteTextures'" when GL module has already been unloaded

    @property
    def shape(self):
        with self:
            width = gl.GLint()
            gl.glGetTexLevelParameteriv(self.target, 0, gl.GL_TEXTURE_WIDTH, gl.pointer(width))
            height = gl.GLint()
            gl.glGetTexLevelParameteriv(self.target, 0, gl.GL_TEXTURE_HEIGHT, gl.pointer(height))
            depth = gl.GLint()
            gl.glGetTexLevelParameteriv(self.target, 0, gl.GL_TEXTURE_DEPTH, gl.pointer(depth))
            colors = gl_iformat_to_numpy[self.gl_iformat][1]        
        return (width.value, height.value, depth.value, colors)

    @property
    def gl_iformat(self):
        gl_iformat = gl.GLint()
        with self:
            gl.glGetTexLevelParameteriv(self.target, 0, gl.GL_TEXTURE_INTERNAL_FORMAT, gl.pointer(gl_iformat))
        return gl_iformat.value

    @property
    def gl_format(self):
        return numpy_to_gl_format[self.dtype, self.shape[-1]]

    @property
    def gl_type(self):
        return gl_iformat_to_gl_type[self.gl_iformat]

    @property
    def dtype(self):
        return gl_iformat_to_numpy[self.gl_iformat][0]

    @property
    def ndim(self):
        return texture_target_to_dimensions[self.target]

    @property
    def data(self):
        data = numpy.empty(self.shape, dtype=self.dtype)
        gl.glPixelStorei(gl.GL_PACK_ALIGNMENT, 1)
        with self:
            gl.glGetTexImage(self.target, 0, self.gl_format, self.gl_type, data.ctypes)
        return data

    @data.setter
    def data(self, data):
        data = data.ctypes if data is not None else gl.POINTER(gl.GLvoid)() # TODO ascontiguousarray?
        gl.glPixelStorei(gl.GL_UNPACK_ALIGNMENT, 1)
        with self:
            gl.glTexImage3D(self.target, 0, self.gl_iformat, self.shape[0], self.shape[1], self.shape[2], 0, self.gl_format, self.gl_type, data)

    def __enter__(self):
        old_binding = gl.GLint()
        gl.glGetIntegerv(texture_target_to_binding[self.target], gl.pointer(old_binding))
        self.stack.append(old_binding.value)
        gl.glBindTexture(self.target, self.id)

    def __exit__(self, type, value, traceback):
        gl.glBindTexture(self.target, self.stack.pop())


window = GlutWindow()

def test_texture(shape, dtype):
    data = numpy.random.random(shape).astype(dtype)
    texture = Texture(data)
    assert texture.shape == data.shape, "shape is broken"
    assert texture.gl_iformat == numpy_to_gl_iformat[data.dtype.type, data.shape[-1]], "gl_iformat is broken"
    assert texture.gl_format == numpy_to_gl_format[data.dtype.type, data.shape[-1]], "gl_format is broken"
    assert texture.gl_type == numpy_to_gl_type[data.dtype.type], "gl_type is broken"
    assert texture.dtype == data.dtype, "dtype is broken"
    assert (texture.data == data).all(), "data is broken"

for shape in ((4, 4, 4, 4), (4, 4, 4, 3), (4, 16, 8, 3), (5, 4, 4, 3), (5, 5, 5, 3), (6, 6, 6, 3), (7, 13, 5, 3)):
    for dtype in reversed((numpy.uint8, numpy.int8, numpy.uint16, numpy.int16, numpy.uint32, numpy.int32, numpy.float32)):
        try:
            test_texture(shape, dtype)
        except Exception, e:
            print "%9s %18s: FAIL (%s: %s)" % (dtype.__name__, shape, type(e).__name__, e)
        else:
            print "%9s %18s: PASS" % (dtype.__name__, shape)

