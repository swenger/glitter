import numpy as _np
from rawgl import gl as _gl

from glitter.util import constants, Datatype, make_array
from glitter.array.basebuffer import BaseBuffer

class ElementArrayBuffer(BaseBuffer):
    _binding = "element_array_buffer_binding"
    _target = _gl.GL_ELEMENT_ARRAY_BUFFER

    def set_data(self, data=None, shape=None, dtype=None, usage=None):
        if data is not None:
            data = make_array(data, dtype, force_integer=True, force_unsigned=True)
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

__all__ = ["ElementArrayBuffer"]

