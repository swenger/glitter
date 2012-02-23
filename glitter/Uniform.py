from collections import OrderedDict as _odict

class Uniform(object):
    def __init__(self, name, location, type, size):
        self.name = name
        self.location = location
        self.type = type
        self.size = size

    def __str__(self):
        return "uniform %s %s[%d];" % (self.type, self.name, self.size)

    def __get__(self, obj, cls=None):
        pass # TODO

    def __set__(self, obj, value):
        pass # TODO

    def _on_bind(self):
        pass # TODO bind textures and set uniforms

    def _on_release(self):
        pass # TODO restore old texture bindings

class UniformStruct(_odict):
    def __init__(self, name):
        super(UniformStruct, self).__init__()
        self.name = name

    def __str__(self):
        return "uniform struct { %s } %s;" % (" ".join(str(value) for value in self.values()), self.name)

    def __get__(self, obj, cls=None):
        pass # TODO

    def __set__(self, obj, value):
        pass # TODO

    def _on_bind(self):
        pass # TODO bind textures and set uniforms

    def _on_release(self):
        pass # TODO restore old texture bindings

class UniformStructArray(_odict):
    def __init__(self, name):
        super(UniformStructArray, self).__init__()
        self.name = name

    @property
    def size(self):
        return max(index for index, field in self.keys()) + 1

    def __str__(self):
        unique_values = _odict((field, value) for ((index, field), value) in self.items())
        return "uniform struct { %s } %s[%d];" % (" ".join(str(value) for value in unique_values.values()), self.name, self.size)

    def __get__(self, obj, cls=None):
        pass # TODO

    def __set__(self, obj, value):
        pass # TODO

    def _on_bind(self):
        pass # TODO bind textures and set uniforms

    def _on_release(self):
        pass # TODO restore old texture bindings

def make_uniform(name, location, type, size):
    return Uniform(name, location, type, size) # TODO return appropriate type

