"""Base classes for descriptors and descriptor owners.

@bug: L{Proxy} is currently unaware of its context.
@author: Stephan Wenger
@date: 2012-02-29
"""

from inspect import getmembers as _getmembers
import types as _types
import numpy as _np

import glitter.raw as _gl
from glitter.utils.dtypes import coerce_array, int32
from glitter.utils.objects import with_obj

class Proxy(object):
    def __init__(self, getter=None, get_args=(), setter=None, set_args=(), dtype=None, shape=(), enum=None, name=None):
        self._getter = getter
        self._get_args = get_args
        self._setter = setter
        self._set_args = set_args
        self._dtype = dtype if dtype else int32
        self._shape = None if shape is None else tuple(shape) if hasattr(shape, "__iter__") else (shape,)
        self._enum = enum
        self._name = name

    def __get__(self, obj, cls):
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
            if hasattr(value, "__iter__"):
                _value = [self._enum(x)._value for x in value]
            else:
                _value = self._enum(value)._value
        else:
            _value = value
        _value = coerce_array(_value, dtype=self._dtype)
        if len(self._set_args) + len(_value) == len(self._setter.argtypes):
            args = list(self._set_args) + (list(_value) if _value.ndim == 1 else [x.ctypes for x in _value])
        elif len(self._set_args) + 1 == len(self._setter.argtypes):
            args = list(self._set_args) + [_value.ctypes]
        else:
            raise RuntimeError("no valid setter invocation found")
        with obj:
            self._setter(*args)

    def __repr__(self):
        if self._name:
            return "proxy for %s" % self._name
        elif self._getter and self._setter:
            return "proxy for %s(%s) / %s(%s)" % (
                    self._getter.__name__, ", ".join(map(str, self._get_args)),
                    self._setter.__name__, ", ".join(map(str, self._set_args)))
        elif self._getter:
            return "proxy for %s(%s)" % (self._getter.__name__, ", ".join(map(str, self._get_args)))
        elif self._setter:
            return "proxy for %s(%s)" % (self._setter.__name__, ", ".join(map(str, self._set_args)))
        else:
            return "proxy object"

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

class InstanceDescriptorMixin(object):
    """Mixin to enable runtime-added descriptors."""

    def __getattribute__(self, name):
        attr = super(InstanceDescriptorMixin, self).__getattribute__(name)
        if hasattr(attr, "__get__") and not callable(attr):
            return attr.__get__(self, self.__class__)
        else:
            return attr

    def __setattr__(self, name, value):
        try:
            attr = super(InstanceDescriptorMixin, self).__getattribute__(name)
            return attr.__set__(self, value)
        except AttributeError:
            return super(InstanceDescriptorMixin, self).__setattr__(name, value)

class PropertyProxy(object):
    def __init__(self, obj, name):
        self._obj = obj
        self._name = name

    def __get__(self, obj, cls):
        return getattr(self._obj, self._name)

    def __set__(self, obj, value):
        setattr(self._obj, self._name, value)

    def __delete__(self, obj):
        delattr(self._obj, self._name)

class ItemProxy(object):
    def __init__(self, obj, idx):
        self._obj = obj
        self._idx = idx

    def __get__(self, obj, cls):
        return self._obj[self._idx]

    def __set__(self, obj, value):
        self._obj[self._idx] = value

    def __delete__(self, obj):
        del self._obj[self._idx]

def add_proxies(parent, obj):
    """Add proxies for methods and properties of C{obj} to C{parent}."""

    # add functions and methods
    for key, value in _getmembers(obj):
        if key.startswith("_"):
            continue
        if isinstance(value, (_types.FunctionType, _types.MethodType)):
            setattr(parent, key, with_obj(parent, value))

    # add properties and other descriptors (can be accessed via the class only)
    for key, value in _getmembers(type(obj)):
        if key.startswith("_"):
            continue
        if hasattr(value, "__get__") and not callable(value): # exclude member functions
            setattr(parent, key, PropertyProxy(obj, key))

    # add instance descriptors if applicable
    if isinstance(obj, InstanceDescriptorMixin):
        for key, value in obj.__dict__.items():
            if key.startswith("_"):
                continue
            if hasattr(value, "__get__"):
                setattr(parent, key, PropertyProxy(obj, key))
        
__all__ = ["Proxy", "ListProxy", "InstanceDescriptorMixin", "PropertyProxy", "ItemProxy", "add_proxies"]

