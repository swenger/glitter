import numpy
from glitter import GlutWindow

import gl
from errors import GLError

# TODO convert constants to readable format
# TODO check integer textures
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
            }[dtype.type]
    return getattr(gl, "GL_%s%s" % (channel_code, type_code)) # GL_R8UI, ...

def gl_iformat_to_numpy(gl_iformat):
    raise NotImplementedError # TODO

def numpy_to_gl_format(colors):
    return [gl.GL_RED, gl.GL_RG, gl.GL_RGB, gl.GL_RGBA][colors - 1]

def numpy_to_gl_type(dtype):
    return {
            numpy.uint8: gl.GL_UNSIGNED_BYTE,
            numpy.int8: gl.GL_BYTE,
            numpy.uint16: gl.GL_UNSIGNED_SHORT,
            numpy.int16: gl.GL_SHORT,
            numpy.uint32: gl.GL_UNSIGNED_INT,
            numpy.int32: gl.GL_INT,
            numpy.float32: gl.GL_FLOAT,
            }[dtype.type]

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
        gl_format = numpy_to_gl_format(shape[-1])
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

            red_gl_type = gl.GLint()
            gl.glGetTexLevelParameteriv(self.target, 0, gl.GL_TEXTURE_RED_TYPE, gl.pointer(red_gl_type))
            green_gl_type = gl.GLint()
            gl.glGetTexLevelParameteriv(self.target, 0, gl.GL_TEXTURE_GREEN_TYPE, gl.pointer(green_gl_type))
            blue_gl_type = gl.GLint()
            gl.glGetTexLevelParameteriv(self.target, 0, gl.GL_TEXTURE_BLUE_TYPE, gl.pointer(blue_gl_type))
            alpha_gl_type = gl.GLint()
            gl.glGetTexLevelParameteriv(self.target, 0, gl.GL_TEXTURE_ALPHA_TYPE, gl.pointer(alpha_gl_type))
            depth_gl_type = gl.GLint()
            gl.glGetTexLevelParameteriv(self.target, 0, gl.GL_TEXTURE_DEPTH_TYPE, gl.pointer(depth_gl_type))
            colors = sum(x.value != gl.GL_NONE for x in (red_gl_type, green_gl_type, blue_gl_type, alpha_gl_type, depth_gl_type))
        
        return (width.value, height.value, depth.value, colors)

    @property
    def gl_iformat(self):
        gl_iformat = gl.GLint()
        with self:
            gl.glGetTexLevelParameteriv(self.target, 0, gl.GL_TEXTURE_INTERNAL_FORMAT, gl.pointer(gl_iformat))
        return gl_iformat.value

    @property
    def gl_format(self):
        return numpy_to_gl_format(self.shape[-1])

    @property
    def gl_type(self):
        gl_type = gl.GLint()
        with self:
            gl.glGetTexLevelParameteriv(gl.GL_TEXTURE_3D, 0, gl.GL_TEXTURE_RED_TYPE, gl.pointer(gl_type))
        return gl_type.value

    @property
    def dtype(self):
        return gl_type_to_numpy(self.gl_type) # TODO should be iformat for better accuracy

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
    data = numpy.random.random(shape).astype(dtype)
    texture = Texture(data)
    assert texture.shape == data.shape
    assert texture.gl_iformat == numpy_to_gl_iformat(data.shape[-1], data.dtype)
    assert texture.gl_format == numpy_to_gl_format(data.shape[-1])
    assert texture.gl_type == numpy_to_gl_type(data.dtype)
    assert texture.dtype == data.dtype
    assert (texture.data == data).all()

for dtype in (numpy.uint8, numpy.int8, numpy.uint16, numpy.int16, numpy.uint32, numpy.int32, numpy.float32):
    try:
        test_texture((4, 4, 4, 4), dtype)
    except GLError, e:
        print e

