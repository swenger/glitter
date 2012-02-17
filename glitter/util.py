import numpy as _np
from rawgl import gl as _gl

class InstanceDescriptorMixin(object):
    def __getattribute__(self, name):
        attr = super(InstanceDescriptorMixin, self).__getattribute__(name)
        if hasattr(attr, "__get__"):
            return attr.__get__(self, self.__class__)
        else:
            return attr

    def __setattr__(self, name, value):
        try:
            attr = super(InstanceDescriptorMixin, self).__getattribute__(name)
            return attr.__set__(self, value)
        except AttributeError:
            return super(InstanceDescriptorMixin, self).__setattr__(name, value)

class Binding(object): # TODO
    def get(self):
        raise NotImplementedError

    def set(self, id):
        raise NotImplementedError
    
    def __enter__(self):
        self.old_id = self.get()
        self.set(self.id)

    def __exit__(self, type, value, traceback):
        self.set(self.old_id)

class GLObject(object):
    _generate_id = NotImplemented
    _delete_id = NotImplemented

    def __init__(self):
        if any(x is NotImplemented for x in (self._generate_id, self._delete_id)):
            raise TypeError("%s is abstract" % self.__class__.__name__)
        if len(self._generate_id.argtypes) == 1:
            self._id = self._generate_id
        else:
            _id = _gl.GLuint()
            self._generate_id(1, _gl.pointer(_id))
            self._id = _id.value

    def __del__(self):
        try:
            if len(self._delete_id.argtypes) == 1:
                self._delete_id(self._id)
            else:
                self._delete_id(1, _gl.pointer(_gl.GLuint(self._id)))
            self._id = 0
        except AttributeError:
            pass # avoid error when GL module has already been unloaded

class BindableObject(GLObject):
    _target = NotImplemented
    _binding = NotImplemented
    _bind = NotImplemented

    def __init__(self):
        super(BindableObject, self).__init__()
        if any(x is NotImplemented for x in (self._bind, self._binding)):
            raise TypeError("%s is abstract" % self.__class__.__name__)
        self._stack = []
    
    def bind(self):
        old_binding = _gl.GLint()
        _gl.glGetIntegerv(self._binding, _gl.pointer(old_binding))
        if self._target is NotImplemented:
            self._bind(self._id)
        else:
            self._bind(self._target, self._id)
        return old_binding.value

    def __enter__(self):
        self._stack.append(self.bind())

    def __exit__(self, type, value, traceback):
        if self._target is NotImplemented:
            self._bind(self._stack.pop())
        else:
            self._bind(self._target, self._stack.pop())

class BeginEndObject(GLObject):
    _target = NotImplemented
    _begin = NotImplemented
    _end = NotImplemented

    def __init__(self):
        super(BeginEndObject, self).__init__()
        if any(x is NotImplemented for x in (self._begin, self._end)):
            raise TypeError("%s is abstract" % self.__class__.__name__)

    def begin(self):
        if self._target is NotImplemented:
            self._begin(self._id)
        else:
            self._begin(self._target, self._id)

    def end(self):
        if self._target is NotImplemented:
            self._end()
        else:
            self._end(self._target)

    def __enter__(self):
        self.begin()

    def __exit__(self, type, value, traceback):
        self.end()

class EnumConstant(object):
    def __init__(self, enum, name, value):
        self._enum = enum
        self._name = name
        self._value = value

    def __str__(self):
        return self._name

    def __repr__(self):
        return self._name

class Enum(object):
    def __init__(self, **kwargs):
        self._reverse_dict = {}
        for key, value in kwargs.items():
            setattr(self, key, EnumConstant(self, key, value))
            self._reverse_dict[value] = getattr(self, key)

    def __getitem__(self, value):
        return self._reverse_dict[value]

is_float = {
        _np.uint8: False,
        _np.int8: False,
        _np.uint16: False,
        _np.int16: False,
        _np.uint32: False,
        _np.int32: False,
        _np.float32: True,
}

is_signed = {
        _np.uint8: False,
        _np.int8: True,
        _np.uint16: False,
        _np.int16: True,
        _np.uint32: False,
        _np.int32: True,
        _np.float32: True,
}

gl_type = {
        _np.uint8: _gl.GL_UNSIGNED_BYTE,
        _np.int8: _gl.GL_BYTE,
        _np.uint16: _gl.GL_UNSIGNED_SHORT,
        _np.int16: _gl.GL_SHORT,
        _np.uint32: _gl.GL_UNSIGNED_INT,
        _np.int32: _gl.GL_INT,
        _np.float32: _gl.GL_FLOAT,
}

