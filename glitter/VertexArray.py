from rawgl import gl as _gl

from util import BindableObject

# TODO

class VertexArray(BindableObject):
    _generate_id = _gl.glGenVertexArrays
    _delete_id = _gl.glDeleteVertexArrays
    _bind = _gl.glBindVertexArray
    _binding = _gl.GL_VERTEX_ARRAY_BINDING

    # TODO

