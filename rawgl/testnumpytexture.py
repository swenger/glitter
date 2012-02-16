import numpy
from glitter import GlutWindow

import gl
from errors import GLError, resolve_constant as _

# TODO check memory layout

def numpy_to_gl_target(shape):
    return [gl.GL_TEXTURE_1D, gl.GL_TEXTURE_2D, gl.GL_TEXTURE_3D][len(shape) - 2]

def texture_target_to_binding(target):
    return {
            gl.GL_TEXTURE_1D: gl.GL_TEXTURE_BINDING_1D,
            gl.GL_TEXTURE_1D_ARRAY: gl.GL_TEXTURE_BINDING_1D_ARRAY,
            gl.GL_TEXTURE_2D: gl.GL_TEXTURE_BINDING_2D,
            gl.GL_TEXTURE_2D_ARRAY: gl.GL_TEXTURE_BINDING_2D_ARRAY,
            gl.GL_TEXTURE_2D_MULTISAMPLE: gl.GL_TEXTURE_BINDING_2D_MULTISAMPLE,
            gl.GL_TEXTURE_2D_MULTISAMPLE_ARRAY: gl.GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY,
            gl.GL_TEXTURE_3D: gl.GL_TEXTURE_BINDING_3D,
            gl.GL_TEXTURE_BUFFER: gl.GL_TEXTURE_BINDING_BUFFER,
            gl.GL_TEXTURE_CUBE_MAP: gl.GL_TEXTURE_BINDING_CUBE_MAP,
            gl.GL_TEXTURE_RECTANGLE: gl.GL_TEXTURE_BINDING_RECTANGLE,
            }[target]

def texture_target_to_dimensions(target):
    return {
            gl.GL_TEXTURE_1D: 2,
            gl.GL_TEXTURE_1D_ARRAY: 3,
            gl.GL_TEXTURE_2D: 3,
            gl.GL_TEXTURE_2D_ARRAY: 4,
            gl.GL_TEXTURE_2D_MULTISAMPLE: None, # TODO
            gl.GL_TEXTURE_2D_MULTISAMPLE_ARRAY: None, # TODO
            gl.GL_TEXTURE_3D: 4,
            gl.GL_TEXTURE_BUFFER: None, # TODO
            gl.GL_TEXTURE_CUBE_MAP: None, # TODO
            gl.GL_TEXTURE_RECTANGLE: 3,
            }[target]

def numpy_to_gl_iformat(colors, dtype):
    channel_code = "RGBA"[:colors]
    type_code = {
            numpy.uint8: "8UI",
            numpy.int8: "8I",
            numpy.uint16: "16UI",
            numpy.int16: "16I",
            numpy.uint32: "32UI",
            numpy.int32: "32I",
            numpy.float32: "32F",
            }[dtype.type if isinstance(dtype, numpy.dtype) else dtype]
    return getattr(gl, "GL_%s%s" % (channel_code, type_code)) # GL_R8UI, ...

def gl_iformat_to_numpy(gl_iformat):
    return {
            gl.GL_R8UI: (numpy.uint8, 1),
            gl.GL_R8I: (numpy.int8, 1),
            gl.GL_R16UI: (numpy.uint16, 1),
            gl.GL_R16I: (numpy.int16, 1),
            gl.GL_R32UI: (numpy.uint32, 1),
            gl.GL_R32I: (numpy.int32, 1),
            gl.GL_R32F: (numpy.float32, 1),

            gl.GL_RG8UI: (numpy.uint8, 2),
            gl.GL_RG8I: (numpy.int8, 2),
            gl.GL_RG16UI: (numpy.uint16, 2),
            gl.GL_RG16I: (numpy.int16, 2),
            gl.GL_RG32UI: (numpy.uint32, 2),
            gl.GL_RG32I: (numpy.int32, 2),
            gl.GL_RG32F: (numpy.float32, 2),

            gl.GL_RGB8UI: (numpy.uint8, 3),
            gl.GL_RGB8I: (numpy.int8, 3),
            gl.GL_RGB16UI: (numpy.uint16, 3),
            gl.GL_RGB16I: (numpy.int16, 3),
            gl.GL_RGB32UI: (numpy.uint32, 3),
            gl.GL_RGB32I: (numpy.int32, 3),
            gl.GL_RGB32F: (numpy.float32, 3),

            gl.GL_RGBA8UI: (numpy.uint8, 4),
            gl.GL_RGBA8I: (numpy.int8, 4),
            gl.GL_RGBA16UI: (numpy.uint16, 4),
            gl.GL_RGBA16I: (numpy.int16, 4),
            gl.GL_RGBA32UI: (numpy.uint32, 4),
            gl.GL_RGBA32I: (numpy.int32, 4),
            gl.GL_RGBA32F: (numpy.float32, 4),
            }[gl_iformat]

def numpy_to_gl_format(colors, dtype):
    if dtype == numpy.float32:
        return [gl.GL_RED, gl.GL_RG, gl.GL_RGB, gl.GL_RGBA][colors - 1]
    else:
        return [gl.GL_RED_INTEGER, gl.GL_RG_INTEGER, gl.GL_RGB_INTEGER, gl.GL_RGBA_INTEGER][colors - 1]

def numpy_to_gl_type(dtype):
    return {
            numpy.uint8: gl.GL_UNSIGNED_BYTE,
            numpy.int8: gl.GL_BYTE,
            numpy.uint16: gl.GL_UNSIGNED_SHORT,
            numpy.int16: gl.GL_SHORT,
            numpy.uint32: gl.GL_UNSIGNED_INT,
            numpy.int32: gl.GL_INT,
            numpy.float32: gl.GL_FLOAT,
            }[dtype.type if isinstance(dtype, numpy.dtype) else dtype]

def gl_type_to_numpy(gl_type):
    return {
            gl.GL_UNSIGNED_BYTE: numpy.uint8,
            gl.GL_BYTE: numpy.int8,
            gl.GL_UNSIGNED_SHORT: numpy.uint16,
            gl.GL_SHORT: numpy.int16,
            gl.GL_UNSIGNED_INT: numpy.uint32,
            gl.GL_INT: numpy.int32,
            gl.GL_FLOAT: numpy.float32,
            }[gl_type]

class Texture(object):
    # TODO depth texture, pixel unpack buffer, glPixelStore, __getitem__/__setitem__ for subimages

    def __init__(self, data=None, shape=None, dtype=None, target=None):
        dtype = dtype or data.dtype
        shape = shape or data.shape

        id = gl.GLuint()
        gl.glGenTextures(1, gl.pointer(id))
        self.id = id.value
        self.stack = []
        self.target = target or numpy_to_gl_target(shape)

        gl_iformat = numpy_to_gl_iformat(shape[-1], dtype)
        gl_format = numpy_to_gl_format(shape[-1], dtype)
        gl_type = numpy_to_gl_type(dtype)
        data = numpy.ctypeslib.as_ctypes(data) if data is not None else gl.POINTER(gl.GLvoid)()
        with self:
            gl.glTexImage3D(self.target, 0, gl_iformat, shape[0], shape[1], shape[2], 0, gl_format, gl_type, data)

    def __del__(self):
        gl.glDeleteTextures(1, gl.pointer(gl.GLuint(self.id)))

    @property
    def shape(self):
        with self:
            width = gl.GLint()
            gl.glGetTexLevelParameteriv(self.target, 0, gl.GL_TEXTURE_WIDTH, gl.pointer(width))
            height = gl.GLint()
            gl.glGetTexLevelParameteriv(self.target, 0, gl.GL_TEXTURE_HEIGHT, gl.pointer(height))
            depth = gl.GLint()
            gl.glGetTexLevelParameteriv(self.target, 0, gl.GL_TEXTURE_DEPTH, gl.pointer(depth))

            colors = gl_iformat_to_numpy(self.gl_iformat)[1] # TODO or:
            """red_gl_type = gl.GLint()
            gl.glGetTexLevelParameteriv(self.target, 0, gl.GL_TEXTURE_RED_TYPE, gl.pointer(red_gl_type))
            green_gl_type = gl.GLint()
            gl.glGetTexLevelParameteriv(self.target, 0, gl.GL_TEXTURE_GREEN_TYPE, gl.pointer(green_gl_type))
            blue_gl_type = gl.GLint()
            gl.glGetTexLevelParameteriv(self.target, 0, gl.GL_TEXTURE_BLUE_TYPE, gl.pointer(blue_gl_type))
            alpha_gl_type = gl.GLint()
            gl.glGetTexLevelParameteriv(self.target, 0, gl.GL_TEXTURE_ALPHA_TYPE, gl.pointer(alpha_gl_type))
            depth_gl_type = gl.GLint()
            gl.glGetTexLevelParameteriv(self.target, 0, gl.GL_TEXTURE_DEPTH_TYPE, gl.pointer(depth_gl_type))
            colors = sum(x.value != gl.GL_NONE for x in (red_gl_type, green_gl_type, blue_gl_type, alpha_gl_type, depth_gl_type))"""
        
        return (width.value, height.value, depth.value, colors)

    @property
    def gl_iformat(self):
        gl_iformat = gl.GLint()
        with self:
            gl.glGetTexLevelParameteriv(self.target, 0, gl.GL_TEXTURE_INTERNAL_FORMAT, gl.pointer(gl_iformat))
        return gl_iformat.value

    @property
    def gl_format(self):
        return numpy_to_gl_format(self.shape[-1], self.dtype)

    @property
    def gl_type(self):
        return numpy_to_gl_type(gl_iformat_to_numpy(self.gl_iformat)[0]) # TODO or:
        """gl_type = gl.GLint()
        with self:
            gl.glGetTexLevelParameteriv(gl.GL_TEXTURE_3D, 0, gl.GL_TEXTURE_RED_TYPE, gl.pointer(gl_type))
        return gl_type.value"""

    @property
    def dtype(self):
        return gl_iformat_to_numpy(self.gl_iformat)[0] # TODO or return gl_type_to_numpy(self.gl_type)

    @property
    def ndim(self):
        return texture_target_to_dimensions(self.target)

    @property
    def data(self):
        data = numpy.empty(self.shape, dtype=self.dtype)
        with self:
            gl.glGetTexImage(self.target, 0, self.gl_format, self.gl_type, numpy.ctypeslib.as_ctypes(data))
        return data

    @data.setter
    def data(self, data):
        data = numpy.ctypeslib.as_ctypes(data) if data is not None else gl.POINTER(gl.GLvoid)()
        with self:
            gl.glTexImage3D(self.target, 0, self.gl_iformat, self.shape[0], self.shape[1], self.shape[2], 0, self.gl_format, self.gl_type, data)

    def __enter__(self):
        old_binding = gl.GLint()
        gl.glGetIntegerv(texture_target_to_binding(self.target), gl.pointer(old_binding))
        self.stack.append(old_binding.value)
        gl.glBindTexture(self.target, self.id)

    def __exit__(self, type, value, traceback):
        gl.glBindTexture(self.target, self.stack.pop())


window = GlutWindow()

def test_texture(shape, dtype):
    warnings = []
    data = numpy.random.random(shape).astype(dtype)
    texture = Texture(data)
    assert texture.shape == data.shape
    assert texture.gl_iformat == numpy_to_gl_iformat(data.shape[-1], data.dtype)
    assert texture.gl_format == numpy_to_gl_format(data.shape[-1], data.dtype)
    if texture.gl_type != numpy_to_gl_type(data.dtype):
        warnings.append("gl_type %s changed to %s" % (_(numpy_to_gl_type(data.dtype)), _(texture.gl_type)))
    if texture.dtype != data.dtype:
        warnings.append("dtype %s changed to %s" % (data.dtype, texture.dtype.__name__))
    assert (texture.data == data).all()
    return warnings

for dtype in reversed((numpy.uint8, numpy.int8, numpy.uint16, numpy.int16, numpy.uint32, numpy.int32, numpy.float32)):
    try:
        warnings = test_texture((4, 4, 4, 4), dtype)
    except (GLError, AssertionError), e:
        print "FAIL for %s: %s" % (dtype.__name__, e)
    else:
        print "PASS for %s (%s)" % (dtype.__name__, ", ".join(warnings) if warnings else "no warnings")

