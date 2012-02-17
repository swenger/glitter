from rawgl import gl as _gl

from util import GLObject

# TODO

class VertexArray(GLObject):
    _generate_id = _gl.glGenVertexArrays
    _delete_id = _gl.glDeleteVertexArrays
    _bind = _gl.glBindVertexArray
    # TODO no binding

    # TODO

