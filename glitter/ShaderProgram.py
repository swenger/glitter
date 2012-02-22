from rawgl import gl as _gl

from util import BindableObject, ShaderLinkError, ShaderValidateError
from Shader import Shader, VertexShader, GeometryShader, FragmentShader

class ShaderProgram(BindableObject):
    _generate_id = _gl.glCreateProgram
    _delete_id = _gl.glDeleteProgram
    _bind = _gl.glUseProgram
    _binding = _gl.GL_CURRENT_PROGRAM

    def __init__(self, vertex=[], geometry=[], fragment=[], link=None):
        super(ShaderProgram, self).__init__()
        self._shaders = []

        if not hasattr(vertex, "__iter__"):
            vertex = [vertex]
        for shader in vertex:
            if not isinstance(shader, VertexShader):
                shader = VertexShader(shader)
            self._attach(shader)
        
        if not hasattr(geometry, "__iter__"):
            geometry = [geometry]
        for shader in geometry:
            if not isinstance(shader, GeometryShader):
                shader = GeometryShader(shader)
            self._attach(shader)
        
        if not hasattr(fragment, "__iter__"):
            fragment = [fragment]
        for shader in fragment:
            if not isinstance(shader, FragmentShader):
                shader = FragmentShader(shader)
            self._attach(shader)
        
        if link is None:
            link = bool(vertex) or bool(geometry) or bool(fragment)
        if link:
            self.link()

    def _attach(self, shader):
        _gl.glAttachShader(self._id, shader._id)
        self._shaders.append(shader)

    def _detach(self, shader):
        _gl.glDetachShader(self._id, shader._id)
        self._shaders.remove(shader)

    @property
    def _attached_shaders(self):
        _attached_shaders = _gl.GLint()
        _gl.glGetProgramiv(self._id, _gl.GL_ATTACHED_SHADERS, _attached_shaders)
        _shaders = (_gl.GLuint * _attached_shaders.value)()
        _gl.glGetAttachedShaders(self._id, _attached_shaders, _gl.POINTER(_gl.GLsizei)(), _shaders)
        return [Shader._retrieve(_shaders[i]) for i in range(_attached_shaders.value)]

    @property
    def shaders(self):
        return AttachedShadersProxy(self)

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

class AttachedShadersProxy(object):
    def __init__(self, program):
        self._program = program

    def append(self, shader):
        self._program._attach(shader)

    def extend(self, shaders):
        for shader in shaders:
            self.append(shader)

    def remove(self, shader):
        self._program._detach(shader)

    def __iadd__(self, shaders):
        self.extend(shaders)

    def __getitem__(self, key):
        #return self._program._attached_shaders[key]
        return self._program._shaders[key]

    def __len__(self):
        #_attached_shaders = _gl.GLint()
        #_gl.glGetProgramiv(self._program._id, _gl.GL_ATTACHED_SHADERS, _attached_shaders)
        #return _attached_shaders.value
        return len(self._program._shaders)

