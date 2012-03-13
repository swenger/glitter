"""Base class for buffer objects.

@todo: Implement binding as separate object to allow binding buffers to
different targets. This problem is very similar to rebinding L{Sampler}s to
different units and should probably be handled in a similar way.
@todo: Implement slicing with C{glGetBufferSubData}.
@todo: Remember that C{glBindBuffer} and C{glBindBufferRange}/C{glBindBufferBase} interfer with each other!

@author: Stephan Wenger
@date: 2012-02-29

@todo: accept another buffer in constructor, copy _id, proxy shape etc., keep reference to other buffer, disable set_data and __del__
"""

import numpy as _np

import glitter.raw as _gl
from glitter.utils import primitive_types, buffer_usages, Datatype, coerce_array, ManagedObject, BindableObject

class BaseBuffer(ManagedObject, BindableObject):
    _generate_id = _gl.glGenBuffers
    _delete_id = _gl.glDeleteBuffers
    _db = "buffers"

    drawmodes = primitive_types
    usages = buffer_usages

    def __init__(self, data=None, shape=None, dtype=None, usage=None):
        if any(x is NotImplemented for x in (self._target,)):
            raise TypeError("%s is abstract" % self.__class__.__name__)
        super(BaseBuffer, self).__init__()
        if isinstance(usage, basestring):
            usage = getattr(buffer_usages, usage)
        if usage is None:
            usage = BaseBuffer.usages.STATIC_DRAW
        if usage not in buffer_usages.__dict__.values():
            raise TypeError("wrong enum")
        self.set_data(data=data, shape=shape, dtype=dtype, usage=usage)

    def set_data(self, data=None, shape=None, dtype=None, usage=None):
        if data is None:
            if shape is None or dtype is None:
                raise ValueError("must specify either data or both shape and dtype")
            self._shape = shape
            self._dtype = dtype.coerced(force_gl=True)
        else:
            data = coerce_array(data, dtype, force_gl=True)
            if shape is not None:
                data = data.reshape(shape)
            self._shape = data.shape
            self._dtype = Datatype.from_numpy(data.dtype)

        if usage is None:
            usage = self.usage

        _nbytes = _np.prod(self._shape) * self._dtype.nbytes
        _data = data.ctypes if data is not None else _gl.POINTER(_gl.GLvoid)()
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
        return BaseBuffer.usages[_usage.value]

__all__ = ["BaseBuffer"]

