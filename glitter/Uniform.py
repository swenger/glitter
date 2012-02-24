from collections import OrderedDict as _odict
import numpy as _np
from rawgl import gl as _gl

class Uniform(object):
    def __init__(self, name, location, dtype, size, parent):
        self.name = name
        self.location = location
        self.dtype = dtype
        self.size = size
        self.parent = parent
        self.textures = []

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
        if self.dtype.is_texture():
            if self.parent._context.current_program == self.parent:
                self._on_release()
            self.textures = value if hasattr(value, "__iter__") else [value]
            if self.parent._context.current_program == self.parent:
                self._on_bind()
        else:
            self.dtype.set_value(obj, self.location, value, self.size)

    def _on_bind(self):
        if self.dtype.is_texture():
            units = [self.parent._context.texture_units.bind(x) for x in self.textures]
            if units:
                self.dtype.set_value(self.parent, self.location, units, self.size)

    def _on_release(self):
        if self.dtype.is_texture():
            for x in self.textures:
                self.parent._context.texture_units.release(x)

class UniformStruct(_odict):
    def __init__(self, name, parent):
        super(UniformStruct, self).__init__()
        self.name = name
        self.parent = parent

    def __str__(self):
        return "uniform struct { %s } %s;" % (" ".join(str(value) for value in self.values()), self.name)

    def __get__(self, obj, cls=None):
        pass # TODO

    def __set__(self, obj, value):
        pass # TODO

    def _on_bind(self):
        pass # TODO bind textures

    def _on_release(self):
        pass # TODO restore old texture bindings

class UniformStructArray(_odict):
    def __init__(self, name, parent):
        super(UniformStructArray, self).__init__()
        self.name = name
        self.parent = parent

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
        pass # TODO bind textures

    def _on_release(self):
        pass # TODO restore old texture bindings
