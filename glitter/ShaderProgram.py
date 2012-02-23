from collections import OrderedDict as _odict
import re as _re
from rawgl import gl as _gl

from constants import transform_feedback_buffer_modes, shader_variable_types
from dtypes import int32
from GLObject import ManagedObject, BindableObject
from util import ShaderLinkError, ShaderValidateError, ListProxy, InstanceDescriptorMixin
from Shader import Shader, VertexShader, TesselationControlShader, TesselationEvaluationShader, GeometryShader, FragmentShader
from Proxy import Proxy
from Attribute import make_attribute, AttributeStruct, AttributeStructArray
from Uniform import make_uniform, UniformStruct, UniformStructArray

def _group_structs(lst, make_variable, make_struct, make_array):
    array_of_structs_re = _re.compile("^([a-zA-Z_][a-zA-Z_0-9]*)\[([0-9]+)\]\.([a-zA-Z_][a-zA-Z_0-9]*)$")
    struct_re = _re.compile("^([a-zA-Z_][a-zA-Z_0-9]*)\.([a-zA-Z_][a-zA-Z_0-9]*)$")
    basic_re = _re.compile("^([a-zA-Z_][a-zA-Z_0-9]*)$")
    names = _odict()
    for location, size, type, name in lst:
        m = array_of_structs_re.match(name)
        if m is not None:
            name, index, field = m.groups()
            index = int(index)
            array = names.setdefault(name, make_array(name))
            array[index, field] = make_variable(field, location, type, size)
            continue
        m = struct_re.match(name)
        if m is not None:
            name, field = m.groups()
            struct = names.setdefault(name, make_struct(name))
            struct[field] = make_variable(field, location, type, size)
            continue
        m = basic_re.match(name)
        if m is not None:
            name, = m.groups()
            names[name] = make_variable(name, location, type, size)
            continue
        raise NameError("shader variable '%s' could not be parsed" % name)
    return names

class ProgramProxy(Proxy):
    def __init__(self, _id, arg, enum=None):
        super(ProgramProxy, self).__init__(_gl.glGetProgramiv, [_id, arg], dtype=int32, enum=enum)

class ShaderProgram(ManagedObject, BindableObject, InstanceDescriptorMixin):
    _generate_id = _gl.glCreateProgram
    _delete_id = _gl.glDeleteProgram
    _db = "shader_programs"
    _binding = "current_program"

    def __init__(self, shaders=[], vertex=[], tess_control=[], tess_evaluation=[], geometry=[], fragment=[], link=None):
        super(ShaderProgram, self).__init__()
        self._shaders = []
        self._variable_proxies = []

        self._delete_status = ProgramProxy(self._id, _gl.GL_DELETE_STATUS)
        self._link_status = ProgramProxy(self._id, _gl.GL_LINK_STATUS)
        self._validate_status = ProgramProxy(self._id, _gl.GL_VALIDATE_STATUS)
        self._info_log_length = ProgramProxy(self._id, _gl.GL_INFO_LOG_LENGTH)
        self._attached_shaders = ProgramProxy(self._id, _gl.GL_ATTACHED_SHADERS)
        self._active_attributes = ProgramProxy(self._id, _gl.GL_ACTIVE_ATTRIBUTES)
        self._active_attribute_max_length = ProgramProxy(self._id, _gl.GL_ACTIVE_ATTRIBUTE_MAX_LENGTH)
        self._active_uniforms = ProgramProxy(self._id, _gl.GL_ACTIVE_UNIFORMS)
        self._active_uniform_max_length = ProgramProxy(self._id, _gl.GL_ACTIVE_UNIFORM_MAX_LENGTH)
        self._program_binary_length = ProgramProxy(self._id, _gl.GL_PROGRAM_BINARY_LENGTH)
        self._transform_feedback_buffer_mode = ProgramProxy(self._id, _gl.GL_TRANSFORM_FEEDBACK_BUFFER_MODE, transform_feedback_buffer_modes)
        self._transform_feedback_varyings = ProgramProxy(self._id, _gl.GL_TRANSFORM_FEEDBACK_VARYINGS)
        self._transform_feedback_varying_max_length = ProgramProxy(self._id, _gl.GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH)

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

        for name, proxy in self._get_active_attributes().items():
            setattr(self, name, proxy)
            self._variable_proxies.append(proxy)
        for name, proxy in self._get_active_uniforms().items():
            setattr(self, name, proxy)
            self._variable_proxies.append(proxy)

    def _on_bind(self):
        for proxy in self._variable_proxies:
            proxy._on_bind()

    def _on_release(self):
        for proxy in self._variable_proxies:
            proxy._on_release()

    def _attach(self, shader):
        _gl.glAttachShader(self._id, shader._id)

    def _detach(self, shader):
        _gl.glDetachShader(self._id, shader._id)

    def _get_active_X(self, getter, location_getter, max_length, index):
        _size = _gl.GLint()
        _type = _gl.GLenum()
        _name = _gl.create_string_buffer(max_length)
        with self._context:
            getter(self._id, index, max_length, None, _gl.pointer(_size), _gl.pointer(_type), _name)
            location = location_getter(self._id, _name)
        return location, _size.value, shader_variable_types[_type.value], _name.value

    def _get_active_attribute(self, index):
        return self._get_active_X(_gl.glGetActiveAttrib, _gl.glGetAttribLocation, self._active_attribute_max_length, index)

    def _get_active_attributes(self):
        return _group_structs((self._get_active_attribute(i) for i in range(self._active_attributes)),
                make_attribute, AttributeStruct, AttributeStructArray)

    def _get_active_uniform(self, index):
        return self._get_active_X(_gl.glGetActiveUniform, _gl.glGetUniformLocation, self._active_uniform_max_length, index)

    def _get_active_uniforms(self):
        return _group_structs((self._get_active_uniform(i) for i in range(self._active_uniforms)),
                make_uniform, UniformStruct, UniformStructArray)

    @property
    def shaders(self):
        return ListProxy(self._shaders, self._attach, self._detach)

    def link(self):
        _gl.glLinkProgram(self._id)
        if self._link_status != _gl.GL_TRUE:
            raise ShaderLinkError(self._log)
        return self._log or None

    def validate(self):
        _gl.glValidateProgram(self._id)
        if self._validate_status != _gl.GL_TRUE:
            raise ShaderValidateError(self._log)
        return self._log or None

    @property
    def _log(self):
        _info_log = _gl.create_string_buffer(self._info_log_length)
        _gl.glGetProgramInfoLog(self._id, self._info_log_length, _gl.POINTER(_gl.GLint)(), _info_log)
        return _info_log.value

