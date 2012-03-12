"""Named constants.
"""

import re
import types

class NamedConstant(object):
    """Named constant.
    """

    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return "%s(%s)" % (self._name, super(NamedConstant, self).__repr__())

    def __str__(self):
        return self._name

class IntConstant(NamedConstant, int):
    """Named integer constant.
    """

    def __new__(cls, name, value):
        return int.__new__(cls, value)

    def __init__(self, name, value):
        NamedConstant.__init__(self, name)

    def __hash__(self):
        return int.__hash__(self)

    def _split_name(self):
        i = 0
        while i < len(self._name) and self._name[-i-1:].isdigit():
            i += 1
        basename = self._name[:-i]
        digit = int(self._name[-i:]) if i > 0 else None
        return basename, digit

    def __add__(self, other):
        if isinstance(other, NamedConstant):
            raise TypeError("cannot add two constants")
        else:
            basename, digit = self._split_name()
            if digit is None:
                raise TypeError("not a numeric constant")
            digit += other
            if digit < 0:
                raise ValueError("range exceeded")
            return type(self)("%s%d" % (basename, digit), super(NamedConstant, self).__add__(other))

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, NamedConstant):
            return super(NamedConstant, self).__sub__(other)
        else:
            basename, digit = self._split_name()
            if digit is None:
                raise TypeError("not a numeric constant")
            digit -= other
            if digit < 0:
                raise ValueError("range exceeded")
            return type(self)("%s%d" % (basename, digit), super(NamedConstant, self).__add__(other))

    def __or__(self, other):
        return type(self)("%s|%s" % (self, other), super(NamedConstant, self).__or__(other))

    def __ror__(self, other):
        return self | other

def make_constant(name, value):
    """Create a named constant with name C{name} and value C{value}.

    An appropriate wrapper class will be generated if necessary.
    """

    dtype = type(value)

    cls_name = "%sConstant" % "".join(x[0].upper() + x[1:] for x in dtype.__name__.split())
    if cls_name not in globals():
        d = {
            "__new__": lambda cls, name, value: dtype.__new__(cls, value),
            "__init__": lambda self, name, value: NamedConstant.__init__(self, name),
            "__hash__": lambda self: dtype.__hash__(self),
        }
        globals()[cls_name] = types.ClassType(cls_name, (NamedConstant, dtype), d)

    return globals()[cls_name](name, value)

def wrap_constants(name_re="^(GL|GLU|GLUT|GLX)_[A-Z][A-Z0-9_]*$", types=(int, long, float), d=None):
    """Convert OpenGL constants to named constants.

    All values in C{d} that match C{name_re} and are of one of the types in
    C{types} will be replaced by corresponding L{NamedConstant}s. By default,
    C{d} is C{glitter.raw.__dict__}.
    """

    if d is None:
        from glitter import raw
        d = raw.__dict__

    for key, value in d.items():
        if re.match(name_re, key) and isinstance(value, tuple(types)):
            d[key] = make_constant(key, value)

__all__ = ["NamedConstant", "wrap_constants"]

