from glitter import ArrayBuffer, ElementArrayBuffer

class Mesh(object):
    def __init__(self, vertices, indices):
        self.vertices = vertices
        self.indices = indices

    @property
    def vertices(self):
        return self._vertex_buffer.data

    @vertices.setter
    def vertices(self, vertices):
        self._vertex_buffer = ArrayBuffer(vertices)

    @property
    def indices(self):
        return self._index_buffer.data

    @indices.setter
    def indices(self, indices):
        self._index_buffer = ElementArrayBuffer(indices)

    def render(self):
        with self._vertex_buffer:
            self._index_buffer.draw_triangles()

