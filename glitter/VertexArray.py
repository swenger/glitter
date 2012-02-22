from rawgl import gl as _gl

from util import BindableObject
from Buffer import Buffer, ArrayBuffer, ElementArrayBuffer

class VertexArray(BindableObject):
    _generate_id = _gl.glGenVertexArrays
    _delete_id = _gl.glDeleteVertexArrays
    _bind = _gl.glBindVertexArray
    _binding = _gl.GL_VERTEX_ARRAY_BINDING

    def __init__(self, arrays=[], elements=None):
        super(VertexArray, self).__init__()
        self._bound_buffers = {}
        for i, array in enumerate(arrays):
            self[i] = array
        if elements is not None:
            self.elements = elements

    def __getitem__(self, key):
        return self._bound_buffers[key]

    def __setitem__(self, key, value):
        if not isinstance(value, ArrayBuffer):
            pass # TODO cast to ArrayBuffer
        with self:
            with value:
                value.use(key)
        self._bound_buffers[key] = value

    def __delitem__(self, key):
        with self:
            _gl.glVertexAttribPointer(key, 0, _gl.GL_FLOAT, _gl.GL_FALSE, 0, _gl.POINTER(_gl.GLvoid)())
        del self._bound_buffers[key]

    @property
    def elements(self):
        return self._elements

    @elements.setter
    def elements(self, elements):
        if not isinstance(elements, ElementArrayBuffer):
            pass # TODO cast to ElementArrayBuffer
        with self:
            elements.bind()
        self._elements = elements

    @elements.deleter
    def elements(self):
        with self:
            self._elements._bind(self._elements._target, 0)
        del self._elements

    def draw(self, mode=Buffer.drawmodes.TRIANGLES, count=None, offset=0, instances=None, index=None):
        if index is None:
            if hasattr(self, "_elements"):
                with self:
                    self.elements.draw(mode, count, offset, instances)
            else:
                with self:
                    min(self._bound_buffers.items())[1].draw(mode, count, offset, instances)
        else:
            with self:
                self[index].draw(mode, count, offset, instances)

