from rawgl import gl as _gl

from util import BeginEndObject

# TODO

class Query(BeginEndObject):
    _generate_id = _gl.glGenQueries
    _delete_id = _gl.glDeleteQueries
    _begin = _gl.glBeginQuery
    _end = _gl.glEndQuery
    # TODO _target: GL_SAMPLES_PASSED, GL_ANY_SAMPLES_PASSED, GL_PRIMITIVES_GENERATED, GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN, GL_TIME_ELAPSED

