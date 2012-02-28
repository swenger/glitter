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
            self._add(key, value)

    def __getitem__(self, value):
        return self._reverse_dict[value]

    def _add(self, key, value):
        setattr(self, key, EnumConstant(self, key, value))
        self._reverse_dict[value] = getattr(self, key)

