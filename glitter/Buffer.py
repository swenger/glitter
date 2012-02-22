import numpy as _np
from rawgl import gl as _gl

import constants
from util import BindableObject, is_float, gl_type

# TODO one buffer can be bound to different targets; how should this be represented? BufferBinding()?
# TODO buffers should be castable into each other, refcount!
# TODO buffers likely contain meaningful array data; remember the dtypes and shape
# TODO slicing with glGetBufferSubData

class Buffer(BindableObject):
    _generate_id = _gl.glGenBuffers
    _delete_id = _gl.glDeleteBuffers
    _bind = _gl.glBindBuffer

    drawmodes = constants.buffer_drawmodes
    usages = constants.buffer_usages

    def __init__(self, data=None, shape=None, dtype=None, usage=usages.STATIC_DRAW):
        self._binding = constants.buffer_target_to_binding[self._target]
        super(Buffer, self).__init__()
        self.set_data(data=data, shape=shape, dtype=dtype, usage=usage)

    def set_data(self, data=None, shape=None, dtype=None, usage=None):
        if data is None:
            if shape is None or dtype is None:
                raise ValueError("must specify either data or both shape and dtype")
            self._shape = shape
            self._dtype = dtype
        else:
            data = _np.asarray(data, dtype)
            if shape is not None:
                data = data.reshape(shape)
            self._shape = data.shape
            self._dtype = data.dtype.type

        if usage is None:
            usage = self.usage

        _nbytes = _np.prod(self._shape) * self._dtype().nbytes
        _data = _np.ascontiguousarray(data).ctypes if data is not None else _gl.POINTER(_gl.GLvoid)()
        with self:
            _gl.glBufferData(self._target, _nbytes, _data, usage._value)

    def get_data(self):
        _data = _np.empty(self.shape, dtype=self.dtype)
        with self:
            _gl.glGetBufferSubData(self._target, 0, _data.nbytes, _data.ctypes)
        return _data

    @property
    def data(self):
        return self.get_data()

    @data.setter
    def data(self, data):
        self.set_data(data)

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
        return Buffer.usages[_usage.value]

class ArrayBuffer(Buffer):
    _target = _gl.GL_ARRAY_BUFFER

    def use(self, index, num_components=None, byte_stride=0, byte_offset=0):
        if num_components is None:
            if len(self.shape) == 1:
                num_components = 1
            elif len(self.shape) == 2 and 1 <= self.shape[1] <= 4:
                num_components = self.shape[1]
            else:
                raise ValueError("must specify num_components") # TODO check for correct shape in the data setter
        if is_float[self.dtype]:
            with self:
                _gl.glVertexAttribPointer(index, num_components, gl_type[self.dtype], _gl.GL_FALSE, byte_stride, byte_offset)
        else:
            with self:
                _gl.glVertexAttribIPointer(index, num_components, gl_type[self.dtype], byte_stride, byte_offset)

        _gl.glEnableVertexAttribArray(index) # TODO this should have __enter__/__exit__ semantics

    def draw(self, mode=Buffer.drawmodes.TRIANGLES, count=None, first=0, instances=None):
        if count is None:
            count = self.shape[0]
        if instances is None:
            with self:
                _gl.glDrawArrays(mode._value, first, count)
        else:
            with self:
                _gl.glDrawArraysInstances(mode._value, first, count, instances)

    # TODO slicing to allow for glVertexAttribPointer with size, stride, and pointer

class ElementArrayBuffer(Buffer):
    _target = _gl.GL_ELEMENT_ARRAY_BUFFER
    # TODO check for dtype of GL_UNSIGNED_BYTE, GL_UNSIGNED_SHORT, or GL_UNSIGNED_INT in data setter
    # TODO if shape[1] == 1: points, == 2: lines, == 3: triangles, ndim == 1: default

    def draw(self, mode=Buffer.drawmodes.TRIANGLES, count=None, byte_offset=0, instances=None): # TODO byte_offset should be element count
        if count is None:
            count = _np.prod(self.shape)
        if instances is None:
            with self:
                _gl.glDrawElements(mode._value, count, gl_type[self.dtype], byte_offset)
        else:
            with self:
                _gl.glDrawElementsInstanced(mode._value, count, gl_type[self.dtype], byte_offset, instances)

class AtomicCounterBuffer(Buffer):
    _target = _gl.GL_ATOMIC_COUNTER_BUFFER

class CopyReadBuffer(Buffer):
    _target = _gl.GL_COPY_READ_BUFFER

class CopyWriteBuffer(Buffer):
    _target = _gl.GL_COPY_WRITE_BUFFER

class DrawIndirectBuffer(Buffer):
    _target = _gl.GL_DRAW_INDIRECT_BUFFER

class PixelPackBuffer(Buffer):
    _target = _gl.GL_PIXEL_PACK_BUFFER

class PixelUnpackBuffer(Buffer):
    _target = _gl.GL_PIXEL_UNPACK_BUFFER

class TextureBuffer(Buffer):
    _target = _gl.GL_TEXTURE_BUFFER

class TransformFeedbackBuffer(Buffer):
    _target = _gl.GL_TRANSFORM_FEEDBACK_BUFFER

class UniformBuffer(Buffer):
    _target = _gl.GL_UNIFORM_BUFFER


# nosetests

def check_buffer(shape, dtype, vrange):
    minval, maxval = vrange
    data = ((maxval - minval) * _np.random.random(shape) + minval).astype(dtype)
    buf = ArrayBuffer(data)
    assert (buf.data == data).all(), "data is broken"
    assert buf.shape == data.shape, "shape is broken"
    assert buf.dtype == data.dtype, "dtype is broken"
    assert buf._size == data.nbytes, "_size is broken"

def test_generator():
    shapes = ((4, 4, 4, 4), (4, 4, 4, 3), (4, 16, 8, 3), (5, 4, 4, 3), (5, 5, 5, 3), (6, 6, 6, 3), (7, 13, 5, 3), (1, 1, 3, 3))
    dtypes = (_np.uint8, _np.int8, _np.uint16, _np.int16, _np.uint32, _np.int32, _np.float32)
    vranges = ((0, (1<<8)-1), (-1<<7, (1<<7)-1), (0, (1<<16)-1), (-1<<15, (1<<15)-1), (0, (1<<32)-1), (-1<<31, (1<<31)-1), (-10.0, 10.0))

    for shape in shapes:
        for dtype, vrange in zip(dtypes, vranges):
            yield check_buffer, shape, dtype, vrange

