import numpy

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
    _target = NotImplemented
    _binding = NotImplemented
    _bind = NotImplemented

    def __init__(self):
        if any(x is NotImplemented for x in (self._generate_id, self._delete_id, self._target, self._binding, self._bind)):
            raise TypeError("%s is abstract" % self.__class__.__name__)

        _id = _gl.GLuint()
        self._generate_id(1, _gl.pointer(_id))
        self._id = _id.value
        self._stack = []

    def __del__(self):
        try:
            self._delete_id(1, _gl.pointer(_gl.GLuint(self._id)))
            self._id = 0
        except AttributeError:
            pass # avoid error when GL module has already been unloaded

    def bind(self):
        old_binding = _gl.GLint()
        _gl.glGetIntegerv(self._binding, _gl.pointer(old_binding))
        self._bind(self._target, self._id)
        return old_binding.value

    def __enter__(self):
        self._stack.append(self.bind())

    def __exit__(self, type, value, traceback):
        self._bind(self._target, self._stack.pop())

is_float = {
        numpy.uint8: False,
        numpy.int8: False,
        numpy.uint16: False,
        numpy.int16: False,
        numpy.uint32: False,
        numpy.int32: False,
        numpy.float32: True,
}

is_signed = {
        numpy.uint8: False,
        numpy.int8: True,
        numpy.uint16: False,
        numpy.int16: True,
        numpy.uint32: False,
        numpy.int32: True,
        numpy.float32: True,
}

