from weakref import WeakSet
from rawgl import gl as _gl

class GlitterError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class ShaderError(GlitterError):
    pass

class ShaderCompileError(ShaderError):
    pass

class ShaderLinkError(ShaderError):
    pass

class ShaderValidateError(ShaderError):
    pass

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

class GLObject(object):
    _generate_id = NotImplemented
    _delete_id = NotImplemented
    _type = NotImplemented
    _db = {}

    def __init__(self, other=None):
        if any(x is NotImplemented for x in (self._generate_id, self._delete_id)):
            raise TypeError("%s is abstract" % self.__class__.__name__)
        if other is None:
            if len(self._generate_id.argtypes) == 0:
                self._id = self._generate_id()
            elif len(self._generate_id.argtypes) == 1:
                self._id = self._generate_id(self._type)
            else:
                _id = _gl.GLuint()
                self._generate_id(1, _gl.pointer(_id))
                self._id = _id.value
        else:
            if other._generate_id != self._generate_id:
                raise TypeError("cannot cast %s into %s" % (other.__class__.__name__, self.__class__.__name__))
            if other._clone_into.im_func == GLObject._clone_into.im_func: # _clone_into has not been overridden
                raise TypeError("cannot clone %s" % other.__class__.__name__)
            self._id = other._id
            other._clone_into(self)
        self._db.setdefault((self._generate_id.__name__, self._id), WeakSet()).add(self)

    @classmethod
    def _retrieve(cls, _id):
        return cls._db.get((cls._generate_id.__name__, _id), None)

    def __del__(self):
        try:
            self._db[self._generate_id.__name__, self._id].remove(self) # TODO will self have been removed from the WeakSet anyway by now?
        except:
            pass
        try:
            if not self._db[self._generate_id.__name__, self._id]: # nobody uses the _id any more, so free it
                if len(self._delete_id.argtypes) == 1:
                    self._delete_id(self._id)
                else:
                    self._delete_id(1, _gl.pointer(_gl.GLuint(self._id)))
                self._id = 0
        except:
            pass

    def _clone_into(self, other):
        pass

class BindableObject(GLObject):
    _target = NotImplemented
    _binding = NotImplemented
    _bind = NotImplemented

    def __init__(self, other=None):
        super(BindableObject, self).__init__(other)
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

    def __init__(self, other=None):
        super(BeginEndObject, self).__init__(other)
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

