from rawgl import gl as _gl

from GLObject import BindableObject
from util import ShaderLinkError, ShaderValidateError, ListProxy
from Shader import Shader, VertexShader, TesselationControlShader, TesselationEvaluationShader, GeometryShader, FragmentShader

class ShaderProgram(BindableObject):
    _generate_id = _gl.glCreateProgram
    _delete_id = _gl.glDeleteProgram
    _db = "shader_programs"
    _binding = "current_program"

    def __init__(self, shaders=[], vertex=[], tess_control=[], tess_evaluation=[], geometry=[], fragment=[], link=None):
        super(ShaderProgram, self).__init__()
        self._shaders = []

        shaders = list(shaders) if hasattr(shaders, "__iter__") else [shaders]
        if not all(isinstance(x, Shader) for x in shaders):
            raise TypeError("expected Shader instance")
        shaders += [x if isinstance(x, VertexShader) else VertexShader(x)
                for x in (vertex if hasattr(vertex, "__iter__") else [vertex])]
        shaders += [x if isinstance(x, TesselationControlShader) else TesselationControlShader(x)
                for x in (tess_control if hasattr(tess_control, "__iter__") else [tess_control])]
        shaders += [x if isinstance(x, TesselationEvaluationShader) else TesselationEvaluationShader(x)
                for x in (tess_evaluation if hasattr(tess_evaluation, "__iter__") else [tess_evaluation])]
        shaders += [x if isinstance(x, GeometryShader) else GeometryShader(x)
                for x in (geometry if hasattr(geometry, "__iter__") else [geometry])]
        shaders += [x if isinstance(x, FragmentShader) else FragmentShader(x)
                for x in (fragment if hasattr(fragment, "__iter__") else [fragment])]
        self.shaders.extend(shaders)
        
        if link is None:
            link = bool(shaders)
        if link:
            self.link()

    def _attach(self, shader):
        _gl.glAttachShader(self._id, shader._id)

    def _detach(self, shader):
        _gl.glDetachShader(self._id, shader._id)

    @property
    def shaders(self):
        return ListProxy(self._shaders, self._attach, self._detach)

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

