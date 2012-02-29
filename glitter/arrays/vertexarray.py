"""Vertex array class.

@author: Stephan Wenger
@date: 2012-02-29
"""

from itertools import izip_longest as _zip
from rawgl import gl as _gl

from glitter.utils import BindableObject, ManagedObject
from glitter.arrays import BaseBuffer, ArrayBuffer, ElementArrayBuffer

# TODO glVertexAttribDivisor

class VertexArray(BindableObject, ManagedObject):
    _generate_id = _gl.glGenVertexArrays
    _delete_id = _gl.glDeleteVertexArrays
    _db = "vertex_arrays"
    _binding = "vertex_array_binding"

    def __init__(self, attributes=[], elements=None):
        super(VertexArray, self).__init__()
        self._attributes = {}
        for i, attributes in _zip(range(self._context.max_vertex_attribs), attributes, fillvalue=None):
            self[i] = attributes
        self.elements = elements

    def __getitem__(self, index):
        return self._attributes[index]

    def __setitem__(self, index, value):
        if value is None:
            with self:
                _gl.glVertexAttribPointer(index, 4, _gl.GL_FLOAT, _gl.GL_FALSE, 0, _gl.POINTER(_gl.GLvoid)())
                _gl.glDisableVertexAttribArray(index)
        else:
            if not isinstance(value, ArrayBuffer):
                value = ArrayBuffer(value)
            with self:
                with value:
                    value._use(index)
                _gl.glEnableVertexAttribArray(index)
        self._attributes[index] = value

    def __delitem__(self, index):
        self[index] = None

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

    def draw(self, mode=BaseBuffer.drawmodes.TRIANGLES, count=None, first=0, instances=None, index=None):
        with self:
            if index is None:
                if self.elements is not None:
                    self.elements.draw(mode, count, first, instances)
                else:
                    min(self._attributes.items())[1].draw(mode, count, first, instances)
            else:
                self[index].draw(mode, count, first, instances)

__all__ = ["VertexArray"]

