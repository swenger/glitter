"""Base classes for enumerations.

@author: Stephan Wenger
@date: 2012-02-29
"""

class EnumConstant(object):
    def __init__(self, enum, name, value):
        self._enum = enum
        self.name = name
        self._value = value

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Enum(object):
    def __init__(self, **kwargs):
        self._reverse_dict = {}
        for key, value in kwargs.items():
            self._add(key, value)

    def __getitem__(self, value):
        return self._reverse_dict[value]

    def __call__(self, obj):
        """Convert C{obj} into an appropriate L{EnumConstant}.
        """

        if obj in self.__dict__.values(): # A matching EnumConstant is okay.
            return obj
        elif obj in self.__dict__.keys(): # A string is converted to an EnumConstant if possible.
            return self.__dict__[obj]
        else: # Anything else is just wrong.
            raise TypeError("'%s' is not a valid enum constant here" % obj)

    def _add(self, key, value):
        setattr(self, key, EnumConstant(self, key, value))
        self._reverse_dict[value] = getattr(self, key)

    def __repr__(self):
        return "Enum(%s)" % ", ".join(map(str, self._reverse_dict.values()))

