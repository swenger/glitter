import numpy

from rawgl import gl as _gl

from util import GLObject, Enum

# TODO one buffer can be bound to different targets; how should this be represented? BufferBinding()?
# TODO buffers likely contain meaningful array data; remember the dtypes and shape
# TODO slicing with glGetBufferSubData

_buffer_targets = [ # target, binding
        (_gl.GL_ARRAY_BUFFER,              _gl.GL_ARRAY_BUFFER_BINDING             ),
        (_gl.GL_ATOMIC_COUNTER_BUFFER,     _gl.GL_ATOMIC_COUNTER_BUFFER_BINDING    ),
        (_gl.GL_COPY_READ_BUFFER,          None                                    ), # XXX why is there no GL_COPY_READ_BUFFER_BINDING?
        (_gl.GL_COPY_WRITE_BUFFER,         None                                    ), # XXX why is there no GL_COPY_WRITE_BUFFER_BINING?
        (_gl.GL_DRAW_INDIRECT_BUFFER,      _gl.GL_DRAW_INDIRECT_BUFFER_BINDING     ),
        (_gl.GL_ELEMENT_ARRAY_BUFFER,      _gl.GL_ELEMENT_ARRAY_BUFFER_BINDING     ),
        (_gl.GL_PIXEL_PACK_BUFFER,         _gl.GL_PIXEL_PACK_BUFFER_BINDING        ),
        (_gl.GL_PIXEL_UNPACK_BUFFER,       _gl.GL_PIXEL_UNPACK_BUFFER_BINDING      ),
        (_gl.GL_TEXTURE_BUFFER,            None                                    ), # XXX why is there no GL_TEXTURE_BUFFER_BINDING?
        (_gl.GL_TRANSFORM_FEEDBACK_BUFFER, _gl.GL_TRANSFORM_FEEDBACK_BUFFER_BINDING),
        (_gl.GL_UNIFORM_BUFFER,            _gl.GL_UNIFORM_BUFFER_BINDING           ),
]
_buffer_target_to_binding = dict((x[0], x[1]) for x in _buffer_targets)

class Buffer(GLObject):
    _generate_id = _gl.glGenBuffers
    _delete_id = _gl.glDeleteBuffers
    _bind = _gl.glBindBuffer

    usages = Enum(
            STREAM_DRAW=_gl.GL_STREAM_DRAW,
            STREAM_READ=_gl.GL_STREAM_READ,
            STREAM_COPY=_gl.GL_STREAM_COPY,
            STATIC_DRAW=_gl.GL_STATIC_DRAW,
            STATIC_READ=_gl.GL_STATIC_READ,
            STATIC_COPY=_gl.GL_STATIC_COPY,
            DYNAMIC_DRAW=_gl.GL_DYNAMIC_DRAW,
            DYNAMIC_READ=_gl.GL_DYNAMIC_READ,
            DYNAMIC_COPY=_gl.GL_DYNAMIC_COPY,
    )

    def __init__(self, data=None, shape=None, dtype=None, usage=usages.STATIC_DRAW):
        self._binding = _buffer_target_to_binding[self._target]
        super(Buffer, self).__init__()
        self.setdata(data=data, shape=shape, dtype=dtype, usage=usage)

    def setdata(self, data=None, shape=None, dtype=None, usage=None):
        if data is None:
            if shape is None or dtype is None:
                raise ValueError("must specify either data or both shape and dtype")
            self._shape = shape
            self._dtype = dtype
        else:
            if shape is not None or dtype is not None:
                raise ValueError("cannot specify both data and either shape and dtype")
            self._shape = data.shape
            self._dtype = data.dtype.type

        if usage is None:
            usage = self.usage

        _nbytes = numpy.prod(self._shape) * self._dtype().nbytes
        _data = numpy.ascontiguousarray(data).ctypes if data is not None else _gl.POINTER(_gl.GLvoid)()
        with self:
            _gl.glBufferData(self._target, _nbytes, _data, usage._value)

    def getdata(self):
        _data = numpy.empty(self.shape, dtype=self.dtype)
        with self:
            _gl.glGetBufferSubData(self._target, 0, _data.nbytes, _data.ctypes)
        return _data

    @property
    def data(self):
        return self.getdata()

    @data.setter
    def data(self, data):
        self.setdata(data)

    @property
    def shape(self):
        return self._shape

    @property
    def dtype(self):
        return self._dtype

    @property
    def _size(self):
        _size = _gl.GLint()
        with self:
            _gl.glGetBufferParameteriv(self._target, _gl.GL_BUFFER_SIZE, _gl.pointer(_size))
        return _size.value

    @property
    def usage(self):
        _usage = _gl.GLint()
        with self:
            _gl.glGetBufferParameteriv(self._target, _gl.GL_BUFFER_USAGE, _gl.pointer(_usage))
        return self.usages[_usage.value]

class ArrayBuffer(Buffer):
    _target = _gl.GL_ARRAY_BUFFER
    # TODO glVertexAttribPointer

class AtomicCounterBuffer(Buffer):
    _target = _gl.GL_ATOMIC_COUNTER_BUFFER
    # TODO glBindBufferBase, glBindBufferRange

class CopyReadBuffer(Buffer):
    _target = _gl.GL_COPY_READ_BUFFER
    # TODO glCopyBufferSubData

class CopyWriteBuffer(Buffer):
    _target = _gl.GL_COPY_WRITE_BUFFER
    # TODO glCopyBufferSubData

class DrawIndirectBuffer(Buffer):
    _target = _gl.GL_DRAW_INDIRECT_BUFFER
    # TODO glDrawArraysIndirect, glDrawElementsIndirect

class ElementArrayBuffer(Buffer):
    _target = _gl.GL_ELEMENT_ARRAY_BUFFER
    # TODO glDrawElements, glDrawElementsInstanced, glDrawElementsBaseVertex, glDrawRangeElements, glDrawRangeElementsBaseVertex, glMultiDrawElements, glMultiDrawElementsBaseVertex

class PixelPackBuffer(Buffer):
    _target = _gl.GL_PIXEL_PACK_BUFFER
    # TODO glGetCompressedTexImage, glGetTexImage, glReadPixels

class PixelUnpackBuffer(Buffer):
    _target = _gl.GL_PIXEL_UNPACK_BUFFER
    # TODO glCompressedTexImage1D, glCompressedTexImage2D, glCompressedTexImage3D, glCompressedTexSubImage1D, glCompressedTexSubImage2D, glCompressedTexSubImage3D, glTexImage1D, glTexImage2D, glTexImage3D, glTexSubImage1D, glTexSubImage2D, glTexSubImage3D

class TextureBuffer(Buffer):
    _target = _gl.GL_TEXTURE_BUFFER

class TransformFeedbackBuffer(Buffer):
    _target = _gl.GL_TRANSFORM_FEEDBACK_BUFFER
    # TODO glBindBufferBase, glBindBufferRange

class UniformBuffer(Buffer):
    _target = _gl.GL_UNIFORM_BUFFER
    # TODO glBindBufferBase, glBindBufferRange


# nosetests

def check_buffer(shape, dtype, vrange):
    minval, maxval = vrange
    data = ((maxval - minval) * numpy.random.random(shape) + minval).astype(dtype)
    buf = ArrayBuffer(data)
    assert (buf.data == data).all(), "data is broken"
    assert buf.shape == data.shape, "shape is broken"
    assert buf.dtype == data.dtype, "dtype is broken"
    assert buf._size == data.nbytes, "_size is broken"

def test_generator():
    shapes = ((4, 4, 4, 4), (4, 4, 4, 3), (4, 16, 8, 3), (5, 4, 4, 3), (5, 5, 5, 3), (6, 6, 6, 3), (7, 13, 5, 3), (1, 1, 3, 3))
    dtypes = (numpy.uint8, numpy.int8, numpy.uint16, numpy.int16, numpy.uint32, numpy.int32, numpy.float32)
    vranges = ((0, (1<<8)-1), (-1<<7, (1<<7)-1), (0, (1<<16)-1), (-1<<15, (1<<15)-1), (0, (1<<32)-1), (-1<<31, (1<<31)-1), (-10.0, 10.0))

    for shape in shapes:
        for dtype, vrange in zip(dtypes, vranges):
            yield check_buffer, shape, dtype, vrange

