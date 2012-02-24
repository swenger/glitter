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
        if elements is not None and not isinstance(elements, ElementArrayBuffer):
            elements = ElementArrayBuffer(elements)
        with self:
            self._context.element_array_buffer_binding = elements
        self._elements = elements

    @elements.deleter
    def elements(self):
        self.elements = None

    def draw(self, mode=Buffer.drawmodes.TRIANGLES, count=None, first=0, instances=None, index=None):
        with self:
            if index is None:
                if self.elements is not None:
                    self.elements.draw(mode, count, first, instances)
                else:
                    min(self._bound_buffers.items())[1].draw(mode, count, first, instances)
            else:
                self[index].draw(mode, count, first, instances)

