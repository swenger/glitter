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

class ListProxy(object):
    def __init__(self, lst, insert_callback=None, delete_callback=None):
        self._lst = lst
        self._insert_callback = insert_callback
        self._delete_callback = delete_callback

    def append(self, x):
        self._lst.append(x)
        self._insert_callback(x)

    def extend(self, xs):
        for x in xs:
            self.append(x)

    def remove(self, x):
        self._lst.remove(x)
        self._delete_callback(x)

    def __iadd__(self, xs):
        self.extend(xs)

    def __getitem__(self, key):
        return self._lst[key]

    def __len__(self):
        return len(self._lst)

