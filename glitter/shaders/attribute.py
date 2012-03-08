"""Descriptors for L{ShaderProgram} attributes.

End users should typically not need to use this module directly.

@bug: Attributes are currently unimplemented.

@author: Stephan Wenger
@date: 2012-02-29
"""

from collections import OrderedDict as _odict

class BaseAttribute(object):
    pass

class Attribute(BaseAttribute):
    def __init__(self, name, location, dtype, size, parent):
        self.name = name
        self.location = location
        self.dtype = dtype
        self.size = size
        self.parent = parent

    def __repr__(self):
        if self.size == 1:
            return "%s %s;" % (self.dtype, self.name)
        else:
            return "%s %s[%d];" % (self.dtype, self.name, self.size)

    def __str__(self):
        return "in %r" % self

    def __get__(self, obj, cls=None):
        """@todo: Implement this."""
        raise NotImplementedError

    def __set__(self, obj, value):
        """@todo: Implement this: if the shader is currently bound, set the attribute at once, else store only."""
        raise NotImplementedError

    def _on_bind(self):
        """@todo: Implement this: call C{glVertexAttrib} with C{index=self._location}."""
        pass

    def _on_release(self):
        """@todo: Implement this: restore old vertex attrib values if possible."""
        pass

class AttributeStruct(_odict, BaseAttribute):
    def __init__(self, name, parent):
        super(AttributeStruct, self).__init__()
        self.name = name
        self.parent = parent

    def __repr__(self):
        return "struct { %s } %s;" % (" ".join(str(value) for value in self.values()), self.name)

    def __str__(self):
        return "in %r" % self

    def __get__(self, obj, cls=None):
        """@todo: Implement this."""
        raise NotImplementedError

    def __set__(self, obj, value):
        """@todo: Implement this."""
        raise NotImplementedError

    def _on_bind(self):
        """@todo: Implement this: call C{glVertexAttrib} with C{index=self._location}."""
        pass

    def _on_release(self):
        """@todo: Implement this: restore old vertex attrib values if possible."""
        pass

class AttributeStructArray(_odict, BaseAttribute):
    def __init__(self, name, parent):
        super(AttributeStructArray, self).__init__()
        self.name = name
        self.parent = parent

    @property
    def size(self):
        return max(index for index, field in self.keys()) + 1

    def __repr__(self):
        unique_values = _odict((field, value) for ((index, field), value) in self.items())
        return "struct { %s } %s[%d];" % (" ".join(repr(value) for value in unique_values.values()), self.name, self.size)

    def __str__(self):
        return "in %r" % self

    def __get__(self, obj, cls=None):
        """@todo: Implement this."""
        raise NotImplementedError

    def __set__(self, obj, value):
        """@todo: Implement this."""
        raise NotImplementedError

    def _on_bind(self):
        """@todo: Implement this: call C{glVertexAttrib} with C{index=self._location}."""
        pass

    def _on_release(self):
        """@todo: Implement this: restore old vertex attrib values if possible."""
        pass

