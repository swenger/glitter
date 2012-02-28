from rawgl import gl as _gl

from glitter.utils import constants
from glitter.arrays.basebuffer import BaseBuffer

class ArrayBuffer(BaseBuffer):
    _binding = "array_buffer_binding"
    _target = _gl.GL_ARRAY_BUFFER

    def _use(self, index, num_components=None, stride=0, first=0):
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

    def draw(self, mode=None, count=None, first=0, instances=None):
        if mode is None:
            if len(self.shape) >= 2:
                mode = constants.buffer_dimensions_to_primitive.get(self.shape[-1], None)
        if mode is None:
            raise ValueError("must specify mode")
        if count is None:
            count = self.shape[0]
        if instances is None:
            with self:
                _gl.glDrawArrays(mode._value, first, count)
        else:
            with self:
                _gl.glDrawArraysInstances(mode._value, first, count, instances)

    # TODO slicing to allow for glVertexAttribPointer with size, stride, and pointer

__all__ = ["ArrayBuffer"]

