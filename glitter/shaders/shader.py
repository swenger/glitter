"""Shader classes.

@author: Stephan Wenger
@date: 2012-02-29
"""

import glitter.raw as _gl
from glitter.utils import ManagedObject, ShaderCompileError

class Shader(ManagedObject):
    _generate_id = _gl.glCreateShader
    _delete_id = _gl.glDeleteShader
    _db = "shaders"

    def __init__(self, source=None, compile=None):
        if any(x is NotImplemented for x in (self._type,)):
            raise TypeError("%s is abstract" % self.__class__.__name__)
        super(Shader, self).__init__()
        if source:
            self.source = source
        if compile is None:
            compile = bool(source)
        if compile:
            self.compile()

    def compile(self):
        with self._context:
            _gl.glCompileShader(self._id)
        
            _compile_status = _gl.GLint()
            _gl.glGetShaderiv(self._id, _gl.GL_COMPILE_STATUS, _gl.pointer(_compile_status))
            if _compile_status.value != _gl.GL_TRUE:
                raise ShaderCompileError(self._log)

            return self._log or None

    @property
    def _log(self):
        with self._context:
            _info_log_length = _gl.GLint()
            _gl.glGetShaderiv(self._id, _gl.GL_INFO_LOG_LENGTH, _gl.pointer(_info_log_length))
            _info_log = _gl.create_string_buffer(_info_log_length.value)
            _gl.glGetShaderInfoLog(self._id, _info_log_length, _gl.POINTER(_gl.GLint)(), _info_log)
            return _info_log.value

    @property
    def source(self):
        with self._context:
            _shader_source_length = _gl.GLint()
            _gl.glGetShaderiv(self._id, _gl.GL_SHADER_SOURCE_LENGTH, _gl.pointer(_shader_source_length))
            _source = _gl.create_string_buffer(_shader_source_length.value)
            _gl.glGetShaderSource(self._id, _shader_source_length, _gl.POINTER(_gl.GLint)(), _source)
            return _source.value

    @source.setter
    def source(self, source):
        with self._context:
            _gl.glShaderSource(self._id, 1, _gl.pointer(_gl.c_char_p(source)), _gl.POINTER(_gl.GLint)())

class VertexShader(Shader):
    """Vertes shader.

    @todo: wrap C{glGetShaderPrecisionFormat}.
    """

    _type = _gl.GL_VERTEX_SHADER

class TesselationControlShader(Shader):
    _type = _gl.GL_TESS_CONTROL_SHADER

class TesselationEvaluationShader(Shader):
    _type = _gl.GL_TESS_EVALUATION_SHADER

class GeometryShader(Shader):
    _type = _gl.GL_GEOMETRY_SHADER

class FragmentShader(Shader):
    """Fragment shader.
    
    @todo: wrap C{glGetShaderPrecisionFormat}.
    """
    
    _type = _gl.GL_FRAGMENT_SHADER

__all__ = [
    "Shader",
    "VertexShader",
    "TesselationControlShader",
    "TesselationEvaluationShader",
    "GeometryShader",
    "FragmentShader",
]

