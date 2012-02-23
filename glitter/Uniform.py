from collections import OrderedDict as _odict
import numpy as _np
from rawgl import gl as _gl

class Uniform(object):
    def __init__(self, name, location, dtype, size):
        self.name = name
        self.location = location
        self.dtype = dtype
        self.size = size

    def __str__(self):
        return "uniform %s %s[%d];" % (self.dtype, self.name, self.size)

    def __get__(self, obj, cls=None):
        with obj._context:
            if self.size == 1:
                data = self.dtype.get_value(obj, self.location)
                return data.item() if len(data) == 1 else data
            else:
                data = [self.dtype.get_value(obj, _gl.glGetUniformLocation(obj._id, "%s[%d]" % (self.name, i))) for i in range(self.size)]
                return _np.concatenate([x.squeeze()[None] for x in data])

    def __set__(self, obj, value):
        self.dtype.set_value(obj, self.location, value, self.size)

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

