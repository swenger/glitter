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

class Binding(object):
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
    def __init__(self):
        _id = _gl.GLuint()
        self._generate_id(1, _gl.pointer(_id))
        self._id = _id.value

        self._stack = []

    def __del__(self):
        try:
            self._delete_id(1, _gl.pointer(_gl.GLuint(self._id)))
            self._id = 0
        except AttributeError:
            pass # avoid "'NoneType' object has no attribute 'glDeleteTextures'" when GL module has already been unloaded

    def bind(self):
        old_binding = _gl.GLint()
        _gl.glGetIntegerv(self._binding, _gl.pointer(old_binding))
        self._bind(self._target, self._id)
        return old_binding.value

    def __enter__(self):
        self._stack.append(self.bind())

    def __exit__(self, type, value, traceback):
        self._bind(self._target, self._stack.pop())

    _generate_id = NotImplemented
    _delete_id = NotImplemented
    _target = NotImplemented
    _binding = NotImplemented
    _bind = NotImplemented

