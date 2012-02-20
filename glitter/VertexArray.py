from rawgl import gl as _gl

from util import BindableObject
from Buffer import Buffer

class VertexArray(BindableObject):
    _generate_id = _gl.glGenVertexArrays
    _delete_id = _gl.glDeleteVertexArrays
    _bind = _gl.glBindVertexArray
    _binding = _gl.GL_VERTEX_ARRAY_BINDING

    def __init__(self): # TODO map *args to __setitem__, elements=None to self.elements
        super(VertexArray, self).__init__()
        self._bound_buffers = {}

    def __getitem__(self, key):
        return self._bound_buffers[key]

    def __setitem__(self, key, value): # TODO cast value to ArrayBuffer
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
        pass # TODO

    @elements.setter
    def elements(self, elements): # TODO cast value to ElementArrayBuffer
        pass # TODO

    @elements.deleter
    def elements(self):
        pass # TODO

    def draw(self, mode=Buffer.drawmodes.TRIANGLES, count=None, offset=0, instances=None, index=None):
        if index is None:
            if self.elements is not None:
                with self:
                    self.elements.draw(mode, count, offset, instances)
            else:
                with self:
                    min(self._bound_buffers.items())[1].draw(mode, count, offset, instances)
        else:
            with self:
                self[index].draw(mode, count, offset, instances)

