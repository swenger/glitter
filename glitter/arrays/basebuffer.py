"""Base class for buffer objects.

@author: Stephan Wenger
@date: 2012-02-29
"""

import numpy as _np
from rawgl import gl as _gl

from glitter.utils import constants, Datatype, make_dtype, make_array, BindableObject, ManagedObject

# TODO slicing with glGetBufferSubData
# TODO binding as separate object to allow binding buffers to different targets
# TODO remember that glBindBuffer and glBindBufferRange/glBindBufferBase interfer with each other!

class BaseBuffer(BindableObject, ManagedObject):
    _generate_id = _gl.glGenBuffers
    _delete_id = _gl.glDeleteBuffers
    _db = "buffers"

    drawmodes = constants.primitive_types
    usages = constants.buffer_usages

    def __init__(self, data=None, shape=None, dtype=None, usage=None):
        if any(x is NotImplemented for x in (self._target,)):
            raise TypeError("%s is abstract" % self.__class__.__name__)
        super(BaseBuffer, self).__init__()
        if usage is None:
            usage = BaseBuffer.usages.STATIC_DRAW
        self.set_data(data=data, shape=shape, dtype=dtype, usage=usage)

    def set_data(self, data=None, shape=None, dtype=None, usage=None):
        if data is None:
            if shape is None or dtype is None:
                raise ValueError("must specify either data or both shape and dtype")
            if dtype._as_gl() is None:
                raise ValueError("dtype cannot be represented in OpenGL")
            self._shape = shape
            self._dtype = make_dtype(dtype, force_gl=True)
        else:
            data = make_array(data, dtype, force_gl=True)
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

