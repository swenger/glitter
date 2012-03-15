"""Vertex array class.

@todo: Rethink vertex array drawing: e.g., differing number of elements in vertex and color buffer, allow for use of C{glVertexAttribDivisor}.

@author: Stephan Wenger
@date: 2012-02-29
"""

import glitter.raw as _gl
from glitter.utils import ManagedObject, BindableObject
from glitter.arrays.arraybuffer import ArrayBuffer
from glitter.arrays.elementarray import ElementArrayBuffer

class VertexArray(ManagedObject, BindableObject):
    _generate_id = _gl.glGenVertexArrays
    _delete_id = _gl.glDeleteVertexArrays
    _db = "vertex_arrays"
    _binding = "vertex_array_binding"

    def __init__(self, *attributes, **kwargs):
        """

        @param attributes: Buffers to bind to vertex attributes.
        @type attributes: C{list} of L{ArrayBuffer}s or C{numpy.ndarray}s
        @param kwargs: Named arguments.
        @type kwargs: C{dict}
        @keyword context: The context in which to create the vertex array.
        @type context: L{Context}
        @keyword elements: A buffer containing the element indices.
        @type elements: L{ElementArrayBuffer} or C{numpy.ndarray}
        """

        super(VertexArray, self).__init__(context=kwargs.pop("context", None))
        self._attributes = {}

        if isinstance(attributes, dict):
            attributes = dict(attributes)
        else:
            attributes = dict(enumerate(attributes))
        for i in range(self._context.max_vertex_attribs):
            self[i] = attributes.pop(i, None)
        if attributes:
            raise ValueError("vertex array has no attribute(s) %s" % ", ".join("'%s'" % x for x in attributes.keys()))
        
        self.elements = kwargs.pop("elements", None)
        if kwargs:
            raise TypeError("__init__() got an unexpected keyword argument '%s'" % kwargs.keys()[0])

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

    def draw(self, mode=None, count=None, first=0, instances=None, index=None):
        with self:
            if index is None:
                if self.elements is not None:
                    self.elements.draw(mode, count, first, instances)
                else:
                    min(x for x in self._attributes.items() if x[1] is not None)[1].draw(mode, count, first, instances)
            else:
                self[index].draw(mode, count, first, instances)

__all__ = ["VertexArray"]

