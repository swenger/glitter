from rawgl import gl as _gl

from util import BindableObject, ShaderLinkError, ShaderValidateError

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
            raise ShaderValidateError(self._log)

        return self._log or None

    @property
    def _log(self):
        _info_log_length = _gl.GLint()
        _gl.glGetProgramiv(self._id, _gl.GL_INFO_LOG_LENGTH, _gl.pointer(_info_log_length))
        _info_log = _gl.create_string_buffer(_info_log_length.value)
        _gl.glGetProgramInfoLog(self._id, _info_log_length, _gl.POINTER(_gl.GLint)(), _info_log)
        return _info_log.value

    # TODO attributes and uniforms

