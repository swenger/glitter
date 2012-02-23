import numpy as _np
from rawgl import gl as _gl

import constants
from dtypes import Datatype, uint32
from GLObject import BindableObject

# TODO slicing with glGetBufferSubData

class Buffer(BindableObject):
    _generate_id = _gl.glGenBuffers
    _delete_id = _gl.glDeleteBuffers
    _db = "buffers"

    drawmodes = constants.buffer_drawmodes
    usages = constants.buffer_usages

    def __init__(self, data=None, shape=None, dtype=None, usage=None):
        if any(x is NotImplemented for x in (self._target,)):
            raise TypeError("%s is abstract" % self.__class__.__name__)
        super(Buffer, self).__init__()
        if usage is None:
            usage = Buffer.usages.STATIC_DRAW
        self.set_data(data=data, shape=shape, dtype=dtype, usage=usage)

    def set_data(self, data=None, shape=None, dtype=None, usage=None):
        if data is None:
            if shape is None or dtype is None:
                raise ValueError("must specify either data or both shape and dtype")
            self._shape = shape
            self._dtype = dtype
        else:
            data = _np.ascontiguousarray(data, dtype.as_numpy() if dtype else None)
            if shape is not None:
                data = data.reshape(shape)
            self._shape = data.shape
            self._dtype = Datatype.from_numpy(data.dtype)

        if usage is None:
            usage = self.usage

        _nbytes = _np.prod(self._shape) * self._dtype.nbytes
        _data = _np.ascontiguousarray(data).ctypes if data is not None else _gl.POINTER(_gl.GLvoid)()
        with self:
            _gl.glBufferData(self._target, _nbytes, _data, usage._value)

    def get_data(self):
        _data = _np.empty(self.shape, dtype=self.dtype.as_numpy())
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
    _binding = "array_buffer_binding"
    _target = _gl.GL_ARRAY_BUFFER

    def use(self, index, num_components=None, stride=0, first=0):
        if num_components is None:
            if len(self.shape) == 1:
                num_components = 1
            elif len(self.shape) == 2 and 1 <= self.shape[1] <= 4:
                num_components = self.shape[1]
            else:
                raise ValueError("must specify num_components")
        if self.dtype.is_float():
            with self:
                _gl.glVertexAttribPointer(index, num_components, self.dtype._as_gl(), _gl.GL_FALSE, stride * self.dtype.nbytes, first * self.dtype.nbytes)
        else:
            with self:
                _gl.glVertexAttribIPointer(index, num_components, self.dtype._as_gl(), stride * self.dtype.nbytes, first * self.dtype.nbytes)

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
    _binding = "element_array_buffer_binding"
    _target = _gl.GL_ELEMENT_ARRAY_BUFFER

    def set_data(self, data=None, shape=None, dtype=None, usage=None):
        if data is not None:
            if dtype is None:
                if isinstance(data, _np.ndarray):
                    dtype = Datatype.from_numpy(data.dtype)
                    if not dtype.is_integer():
                        raise TypeError("%s must be of unsigned integer type" % self.__class__.__name__)
                    if not dtype.is_unsigned():
                        dtype = dtype.as_unsigned()
                    if dtype._as_gl() is None:
                        dtype = dtype.as_nbytes(4)
                else:
                    dtype = uint32
            data = _np.ascontiguousarray(data, dtype.as_numpy())
            dtype = Datatype.from_numpy(data.dtype)
        if dtype.is_signed() or not dtype.is_integer():
            raise TypeError("%s must be of unsigned integer type" % self.__class__.__name__)
        super(ElementArrayBuffer, self).set_data(data, shape, dtype, usage)

    def draw(self, mode=None, count=None, first=0, instances=None):
        if mode is None:
            if len(self.shape) >= 2:
                mode = constants.buffer_dimensions_to_primitive.get(self.shape[-1], None)
        if mode is None:
            raise ValueError("must specify mode")
        if count is None:
            count = _np.prod(self.shape)
        if instances is None:
            with self:
                _gl.glDrawElements(mode._value, count, self.dtype._as_gl(), first * self.dtype.nbytes)
        else:
            with self:
                _gl.glDrawElementsInstanced(mode._value, count, self.dtype._as_gl(), first * self.dtype.nbytes, instances)

class AtomicCounterBuffer(Buffer):
    _binding = "atomic_counter_buffer_binding"
    _target = _gl.GL_ATOMIC_COUNTER_BUFFER

class CopyReadBuffer(Buffer):
    _binding = "copy_read_buffer_binding"
    _target = _gl.GL_COPY_READ_BUFFER

class CopyWriteBuffer(Buffer):
    _binding = "copy_write_buffer_binding"
    _target = _gl.GL_COPY_WRITE_BUFFER

class DrawIndirectBuffer(Buffer):
    _binding = "draw_indirect_buffer_binding"
    _target = _gl.GL_DRAW_INDIRECT_BUFFER

class PixelPackBuffer(Buffer):
    _binding = "pixel_pack_buffer_binding"
    _target = _gl.GL_PIXEL_PACK_BUFFER

class PixelUnpackBuffer(Buffer):
    _binding = "pixel_unpack_buffer_binding"
    _target = _gl.GL_PIXEL_UNPACK_BUFFER

class TextureBuffer(Buffer): pass # TODO

class TransformFeedbackBuffer(Buffer):
    _binding = "transform_feedback_buffer_binding"
    _target = _gl.GL_TRANSFORM_FEEDBACK_BUFFER

class UniformBuffer(Buffer):
    _binding = "uniform_buffer_binding"
    _target = _gl.GL_UNIFORM_BUFFER


# nosetests

def check_buffer(shape, dtype, vrange):
    minval, maxval = vrange
    data = ((maxval - minval) * _np.random.random(shape) + minval).astype(dtype.as_numpy())
    buf = ArrayBuffer(data)
    assert (buf.data == data).all(), "data is broken"
    assert buf.shape == data.shape, "shape is broken"
    assert buf.dtype == Datatype.from_numpy(data.dtype), "dtype is broken"
    assert buf._size == data.nbytes, "_size is broken"

def test_generator():
    import dtypes

    shapes = ((4, 4, 4, 4), (4, 4, 4, 3), (4, 16, 8, 3), (5, 4, 4, 3), (5, 5, 5, 3), (6, 6, 6, 3), (7, 13, 5, 3), (1, 1, 3, 3))
    dtypes = (dtypes.uint8, dtypes.int8, dtypes.uint16, dtypes.int16, dtypes.uint32, dtypes.int32, dtypes.float32)
    vranges = ((0, (1<<8)-1), (-1<<7, (1<<7)-1), (0, (1<<16)-1), (-1<<15, (1<<15)-1), (0, (1<<32)-1), (-1<<31, (1<<31)-1), (-10.0, 10.0))

    for shape in shapes:
        for dtype, vrange in zip(dtypes, vranges):
            yield check_buffer, shape, dtype, vrange

