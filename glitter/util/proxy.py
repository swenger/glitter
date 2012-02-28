import numpy as _np
from rawgl import gl as _gl

from glitter.util.dtypes import make_array

class Proxy(object):
    def __init__(self, getter=None, get_args=(), setter=None, set_args=(), dtype=None, shape=None, enum=None):
        self._getter = getter
        self._get_args = get_args
        self._setter = setter
        self._set_args = set_args
        self._dtype = dtype
        self._shape = None if shape is None else tuple(shape) if hasattr(shape, "__iter__") else (shape,)
        self._enum = enum

    def __get__(self, obj, cls=None):
        _value = _np.empty(self._shape, dtype=self._dtype.as_numpy())
        args = list(self._get_args) + [_gl.cast(_value.ctypes, self._getter.argtypes[-1])]
        with obj:
            self._getter(*args)
        value = _value.item() if _value.shape is () else _value
        if self._enum is not None:
            if hasattr(value, "__iter__"):
                value = [self._enum[x] for x in value]
            else:
                value = self._enum[value]
        return value

    def __set__(self, obj, value):
        if self._setter is None:
            raise AttributeError("can't set attribute")
        if self._enum is not None:
            value = [x._value for x in value]
        _value = make_array(value, dtype=self._dtype)
        if len(self._set_args) + len(_value) == len(self._setter.argtypes):
            args = list(self._set_args) + (list(_value) if _value.ndim == 1 else [x.ctypes for x in _value])
        elif len(self._set_args) + 1 == len(self._setter.argtypes):
            args = list(self._set_args) + [_value.ctypes]
        else:
            raise RuntimeError("no valid setter invocation found")
        with obj:
            self._setter(*args)

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

__all__ = ["Proxy", "ListProxy"]
