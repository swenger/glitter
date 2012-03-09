"""Descriptors for L{ShaderProgram} uniforms.

End users should typically not need to use this module directly.

@bug: Structs and arrays of structs are currently unimplemented.

@author: Stephan Wenger
@date: 2012-02-29
"""

from collections import OrderedDict as _odict
import numpy as _np

import glitter.raw as _gl

class BaseUniform(object):
    pass

class Uniform(BaseUniform):
    def __init__(self, name, location, dtype, size, parent):
        self.name = name
        self.location = location
        self.dtype = dtype
        self.size = size
        self.parent = parent
        self.textures = []

    def __str__(self):
        return "uniform %s %s[%d];" % (self.dtype, self.name, self.size)

    def __get__(self, obj, cls=None, get_texture_unit_instead_of_object=False):
        if self.dtype.is_texture() and not get_texture_unit_instead_of_object:
            return self.textures[0] if len(self.textures) == 1 else self.textures
        else:
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

class UniformStruct(_odict, BaseUniform):
    def __init__(self, name, parent):
        super(UniformStruct, self).__init__()
        self.name = name
        self.parent = parent

    def __str__(self):
        return "uniform struct { %s } %s;" % (" ".join(str(value) for value in self.values()), self.name)

    def __get__(self, obj, cls=None):
        """@todo: Implement this."""
        raise NotImplementedError

    def __set__(self, obj, value):
        """@todo: Implement this."""
        raise NotImplementedError

    def _on_bind(self):
        """@todo: Implement this: bind textures."""
        pass

    def _on_release(self):
        """@todo: Implement this: restore old texture bindings."""
        pass

class UniformStructArray(_odict, BaseUniform):
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
        """@todo: Implement this."""
        raise NotImplementedError

    def __set__(self, obj, value):
        """@todo: Implement this."""
        raise NotImplementedError

    def _on_bind(self):
        """@todo: Implement this: bind textures."""
        pass

    def _on_release(self):
        """@todo: Implement this: restore old texture bindings."""
        pass

