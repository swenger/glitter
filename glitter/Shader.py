from rawgl import gl as _gl

from util import GLObject, BindableObject

class ShaderError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class ShaderCompileError(ShaderError):
    def __init__(self, message):
        super(ShaderCompileError, self).__init__(message)

class ShaderLinkError(ShaderError):
    def __init__(self, message):
        super(ShaderLinkError, self).__init__(message)

class ShaderValidationError(ShaderError):
    def __init__(self, message):
        super(ShaderValidationError, self).__init__(message)

class Shader(GLObject):
    _generate_id = _gl.glCreateShader
    _delete_id = _gl.glDeleteShader

    def __init__(self):
        if any(x is NotImplemented for x in (self._type,)):
            raise TypeError("%s is abstract" % self.__class__.__name__)
        super(Shader, self).__init__()

    def compile(self):
        _gl.glCompileShader(self._id)
        
        _compile_status = _gl.GLint()
        _gl.glGetShaderiv(self._id, _gl.GL_COMPILE_STATUS, _gl.pointer(_compile_status))
        if _compile_status.value != _gl.GL_TRUE:
            raise ShaderCompileError(self._log)

        return self._log or None

    @property
    def _log(self):
        _info_log_length = _gl.GLint()
        _gl.glGetShaderiv(self._id, _gl.GL_INFO_LOG_LENGTH, _gl.pointer(_info_log_length))
        _info_log = _gl.create_string_buffer(_info_log_length.value)
        _gl.glGetShaderInfoLog(self._id, _info_log_length, _gl.POINTER(_gl.GLint)(), _info_log)
        return _info_log.value

    @property
    def source(self):
        _shader_source_length = _gl.GLint()
        _gl.glGetShaderiv(self._id, _gl.GL_SHADER_SOURCE_LENGTH, _gl.pointer(_shader_source_length))
        _source = _gl.create_string_buffer(_shader_source_length.value)
        _gl.glGetShaderSource(self._id, _shader_source_length, _gl.POINTER(_gl.GLint)(), _source)
        return _source.value

    @source.setter
    def source(self, source):
        _gl.glShaderSource(self._id, 1, _gl.pointer(_gl.c_char_p(source)), _gl.POINTER(_gl.GLint)())

class VertexShader(Shader):
    _type = _gl.GL_VERTEX_SHADER

class GeometryShader(Shader):
    _type = _gl.GL_GEOMETRY_SHADER

class FragmentShader(Shader):
    _type = _gl.GL_FRAGMENT_SHADER

class ShaderProgram(BindableObject):
    _generate_id = _gl.glCreateProgram
    _delete_id = _gl.glDeleteProgram
    _bind = _gl.glUseProgram
    _binding = _gl.GL_CURRENT_PROGRAM

    def __init__(self):
        super(ShaderProgram, self).__init__()

    # TODO glAttachShader, glDetachShader, glGetAttachedShaders via proxy object

    def link(self):
        _gl.glLinkProgram(self._id)
        
        _link_status = _gl.GLint()
        _gl.glGetProgramiv(self._id, _gl.GL_LINK_STATUS, _gl.pointer(_link_status))
        if _link_status.value != _gl.GL_TRUE:
            raise ShaderLinkError(self._log)

        return self._log or None

    def validate(self):
        _gl.glValidateProgram(self._id)

        _validate_status = _gl.GLint()
        _gl.glGetProgramiv(self._id, _gl.GL_VALIDATE_STATUS, _gl.pointer(_validate_status))
        if _validate_status.value != _gl.GL_TRUE:
            raise ShaderValidationError(self._log)

        return self._log or None

    @property
    def _log(self):
        _info_log_length = _gl.GLint()
        _gl.glGetProgramiv(self._id, _gl.GL_INFO_LOG_LENGTH, _gl.pointer(_info_log_length))
        _info_log = _gl.create_string_buffer(_info_log_length.value)
        _gl.glGetProgramInfoLog(self._id, _info_log_length, _gl.POINTER(_gl.GLint)(), _info_log)
        return _info_log.value

    # TODO attributes and uniforms

