import numpy
from glitter import GlutWindow

import gl


def numpy_to_gl_internalformat(colors, dtype):
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


width = 4
height = 4
depth = 4
colors = 4

data = numpy.random.random((width, height, depth, colors)).astype(numpy.float32)


window = GlutWindow()

texture = gl.GLuint()
gl.glGenTextures(1, gl.pointer(texture))
gl.glBindTexture(gl.GL_TEXTURE_3D, texture)

ifmt = numpy_to_gl_internalformat(data.shape[-1], data.dtype)
fmt = numpy_to_gl_format(data.shape[-1])
tpe = numpy_to_gl_type(data.dtype)
gl.glTexImage3D(gl.GL_TEXTURE_3D, 0, ifmt, data.shape[0], data.shape[1], data.shape[2], 0, fmt, tpe, numpy.ctypeslib.as_ctypes(data))

data2 = numpy.empty_like(data)

gl.glGetTexImage(gl.GL_TEXTURE_3D, 0, fmt, tpe, numpy.ctypeslib.as_ctypes(data2))

assert (data == data2).all()

gl_width = gl.GLint()
gl.glGetTexLevelParameteriv(gl.GL_TEXTURE_3D, 0, gl.GL_TEXTURE_WIDTH, gl.pointer(gl_width))
assert gl_width.value == width

gl_height = gl.GLint()
gl.glGetTexLevelParameteriv(gl.GL_TEXTURE_3D, 0, gl.GL_TEXTURE_HEIGHT, gl.pointer(gl_height))
assert gl_height.value == height

gl_depth = gl.GLint()
gl.glGetTexLevelParameteriv(gl.GL_TEXTURE_3D, 0, gl.GL_TEXTURE_DEPTH, gl.pointer(gl_depth))
assert gl_depth.value == height

gl_ifmt = gl.GLint()
gl.glGetTexLevelParameteriv(gl.GL_TEXTURE_3D, 0, gl.GL_TEXTURE_INTERNAL_FORMAT, gl.pointer(gl_ifmt))
assert gl_ifmt.value == ifmt

gl_tpe = gl.GLint()
gl.glGetTexLevelParameteriv(gl.GL_TEXTURE_3D, 0, gl.GL_TEXTURE_RED_TYPE, gl.pointer(gl_tpe))
assert gl_tpe.value == tpe # TODO GL_FLOAT, GL_INT, and GL_UNSIGNED_INT are returned, no SHORT / BYTE

gl_size = gl.GLint()
gl.glGetTexLevelParameteriv(gl.GL_TEXTURE_3D, 0, gl.GL_TEXTURE_RED_SIZE, gl.pointer(gl_size))
assert gl_size.value == data.dtype.itemsize * 8 # TODO "will be a close match"

