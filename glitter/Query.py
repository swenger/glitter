from rawgl import gl as _gl

from util import GLObject

# TODO

class Query(GLObject):
    _generate_id = _gl.glGenQueries
    _delete_id = _gl.glDeleteQueries
    # TODO glBeginQuery, glEndQuery istead of _bind

