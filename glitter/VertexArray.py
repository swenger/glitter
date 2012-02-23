from rawgl import gl as _gl

from GLObject import BindableObject, ManagedObject
from Buffer import Buffer, ArrayBuffer, ElementArrayBuffer

class VertexArray(BindableObject, ManagedObject):
    _generate_id = _gl.glGenVertexArrays
    _delete_id = _gl.glDeleteVertexArrays
    _db = "vertex_arrays"
    _binding = "vertex_array_binding"

    def __init__(self, arrays=[], elements=None):
        super(VertexArray, self).__init__()
        self._bound_buffers = {}
        for i, array in enumerate(arrays):
            self[i] = array
        if elements is not None:
            self.elements = elements

    def __getitem__(self, index):
        return self._bound_buffers[index]

    def __setitem__(self, index, value):
        if not isinstance(value, ArrayBuffer):
            value = ArrayBuffer(value)
        with self:
            with value:
                value._use(index)
            _gl.glEnableVertexAttribArray(index)
        self._bound_buffers[index] = value

    def __delitem__(self, index):
        with self:
            _gl.glVertexAttribPointer(index, 0, _gl.GL_FLOAT, _gl.GL_FALSE, 0, _gl.POINTER(_gl.GLvoid)())
            _gl.glDisableVertexAttribArray(index)
        del self._bound_buffers[index]

    @property
    def elements(self):
        return self._elements

    @elements.setter
    def elements(self, elements):
        if not isinstance(elements, ElementArrayBuffer):
            elements = ElementArrayBuffer(elements)
        with self:
            elements.bind()
        self._elements = elements

    @elements.deleter
    def elements(self):
        with self:
            self._elements._bind(self._elements._target, 0)
        del self._elements

    def draw(self, mode=Buffer.drawmodes.TRIANGLES, count=None, first=0, instances=None, index=None):
        if index is None:
            if hasattr(self, "_elements"):
                with self:
                    self.elements.draw(mode, count, first, instances)
            else:
                with self:
                    min(self._bound_buffers.items())[1].draw(mode, count, first, instances)
        else:
            with self:
                self[index].draw(mode, count, first, instances)

