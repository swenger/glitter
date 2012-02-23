from collections import OrderedDict as _odict

class Attribute(object):
    def __init__(self, name, location, dtype, size):
        self.name = name
        self.location = location
        self.dtype = dtype
        self.size = size

    def __repr__(self):
        if self.size == 1:
            return "%s %s;" % (self.dtype, self.name)
        else:
            return "%s %s[%d];" % (self.dtype, self.name, self.size)

    def __str__(self):
        return "in %r" % self

    def __get__(self, obj, cls=None):
        pass # TODO

    def __set__(self, obj, value):
        pass # TODO if the shader is currently bound, set the attribute at once, else store only

    def _on_bind(self):
        pass # TODO call glVertexAttrib; where do we know the index from, glBindAttribLocation? how about layout qualifiers?

    def _on_release(self):
        pass # TODO restore old vertex attrib values if possible

class AttributeStruct(_odict):
    def __init__(self, name):
        super(AttributeStruct, self).__init__()
        self.name = name

    def __repr__(self):
        return "struct { %s } %s;" % (" ".join(str(value) for value in self.values()), self.name)

    def __str__(self):
        return "in %r" % self

    def __get__(self, obj, cls=None):
        pass # TODO

    def __set__(self, obj, value):
        pass # TODO

    def _on_bind(self):
        pass # TODO call glVertexAttrib; where do we know the index from, glBindAttribLocation? how about layout qualifiers?

    def _on_release(self):
        pass # TODO restore old vertex attrib values if possible

class AttributeStructArray(_odict):
    def __init__(self, name):
        super(AttributeStructArray, self).__init__()
        self.name = name

    @property
    def size(self):
        return max(index for index, field in self.keys()) + 1

    def __repr__(self):
        unique_values = _odict((field, value) for ((index, field), value) in self.items())
        return "struct { %s } %s[%d];" % (" ".join(repr(value) for value in unique_values.values()), self.name, self.size)

    def __str__(self):
        return "in %r" % self

    def __get__(self, obj, cls=None):
        pass # TODO

    def __set__(self, obj, value):
        pass # TODO

    def _on_bind(self):
        pass # TODO call glVertexAttrib; where do we know the index from, glBindAttribLocation? how about layout qualifiers?

    def _on_release(self):
        pass # TODO restore old vertex attrib values if possible

