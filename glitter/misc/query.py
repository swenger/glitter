"""Query classes.

@warning: The C{Query} class is currently untested.

@author: Stephan Wenger
@date: 2012-02-29
"""

import glitter.raw as _gl
from glitter.utils import ManagedObject, BindReleaseObject

class Query(ManagedObject, BindReleaseObject):
    _generate_id = _gl.glGenQueries
    _delete_id = _gl.glDeleteQueries
    _db = "queries"

    def __init__(self, context=None):
        if any(x is NotImplemented for x in (self._target,)):
            raise TypeError("%s is abstract" % self.__class__.__name__)
        super(Query, self).__init__(context=context)
        if self._counter_bits == 0:
            raise RuntimeError("%s not supported" % self.__class__.__name__)

    def bind(self):
        _gl.glBeginQuery(self._id)

    def release(self):
        _gl.glEndQuery()

    @property
    def _current_query(self):
        _current_query = _gl.GLint()
        _gl.glGetQueryiv(self._target, _gl.GL_CURRENT_QUERY, _gl.pointer(_current_query))
        return _current_query.value

    @property
    def _counter_bits(self):
        _counter_bits = _gl.GLint()
        _gl.glGetQueryiv(self._target, _gl.GL_QUERY_COUNTER_BITS, _gl.pointer(_counter_bits))
        return _counter_bits.value

    @property
    def result_available(self):
        _result_available = _gl.GLint()
        _gl.glGetQueryObjectiv(self._id, _gl.GL_QUERY_RESULT_AVAILABLE, _gl.pointer(_result_available))
        return bool(_result_available.value)

    @property
    def result(self):
        if self._counter_bits <= 32:
            _result = _gl.GLuint()
            _gl.glGetQueryObjectuiv(self._id, _gl.GL_QUERY_RESULT_AVAILABLE, _gl.pointer(_result))
        else:
            _result = _gl.GLuint64()
            _gl.glGetQueryObjectui64v(self._id, _gl.GL_QUERY_RESULT_AVAILABLE, _gl.pointer(_result))
        return _result.value

class SamplesPassedQuery(Query):
    """@todo: Wrap C{glBeginConditionalRender} and C{glEndConditionalRender}."""
    _target = _gl.GL_SAMPLES_PASSED

class AnySamplesPassedQuery(Query):
    """@todo: Wrap C{glBeginConditionalRender} and C{glEndConditionalRender}."""
    _target = _gl.GL_ANY_SAMPLES_PASSED
    result = property(lambda self: bool(Query.result.fget(self)))

class PrimitivesGeneratedQuery(Query):
    _target = _gl.GL_PRIMITIVES_GENERATED

class TransformFeedbackPrimitivesWrittenQuery(Query):
    _target = _gl.GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN

class TimeElapsedQuery(Query):
    _target = _gl.GL_TIME_ELAPSED

__all__ = [
    "Query",
    "SamplesPassedQuery",
    "AnySamplesPassedQuery",
    "PrimitivesGeneratedQuery",
    "TransformFeedbackPrimitivesWrittenQuery",
    "TimeElapsedQuery",
]

