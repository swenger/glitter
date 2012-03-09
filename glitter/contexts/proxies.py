"""Generic descriptor classes for per-context state.

@author: Stephan Wenger
@date: 2012-02-29
"""

from weakref import WeakKeyDictionary

import glitter.raw as _gl
from glitter.utils import hints, bool8, int32, int64, float32, Proxy, EnumConstant

class BooleanProxy(Proxy):
    def __init__(self, get_args=(), setter=None, set_args=(), shape=None):
        super(BooleanProxy, self).__init__(_gl.glGetBooleanv, get_args, setter, set_args, bool8, shape)

    def __repr__(self):
        return "proxy for %s" % self._get_args[0]

class FloatProxy(Proxy):
    def __init__(self, get_args=(), setter=None, set_args=(), shape=None):
        super(FloatProxy, self).__init__(_gl.glGetFloatv, get_args, setter, set_args, float32, shape)

    def __repr__(self):
        return "proxy for %s" % self._get_args[0]

class IntegerProxy(Proxy):
    def __init__(self, get_args=(), setter=None, set_args=(), shape=None):
        super(IntegerProxy, self).__init__(_gl.glGetIntegerv, get_args, setter, set_args, int32, shape)

    def __repr__(self):
        return "proxy for %s" % self._get_args[0]

class Integer64Proxy(Proxy):
    def __init__(self, get_args=(), setter=None, set_args=(), shape=None):
        super(Integer64Proxy, self).__init__(_gl.glGetInteger64v, get_args, setter, set_args, int64, shape)

    def __repr__(self):
        return "proxy for %s" % self._get_args[0]

class EnableDisableProxy(object):
    def __init__(self, arg):
        self._arg = arg

    def __get__(self, obj, cls=None):
        with obj:
            return _gl.glIsEnabled(self._arg) == _gl.GL_TRUE

    def __set__(self, obj, value):
        with obj:
            _gl.glEnable(self._arg) if value else _gl.glDisable(self._arg)

    def __repr__(self):
        return "proxy for %s" % self._arg

class EnumProxy(object):
    def __init__(self, enum, arg, setter=None, set_args=()):
        self._enum = enum
        self._setter = setter
        self._arg = arg
        self._set_args = set_args

    def __get__(self, obj, cls=None):
        _value = _gl.GLint()
        with obj:
            _gl.glGetIntegerv(self._arg, _gl.pointer(_value))
        return self._enum[_value.value]

    def __set__(self, obj, value):
        if self._setter is None:
            raise AttributeError("can't set attribute")
        if isinstance(value, basestring):
            value = getattr(self._enum, value)._value
        if isinstance(value, EnumConstant):
            if value not in self._enum.__dict__.values():
                raise TypeError("wrong enum")
            value = value._value
        args = list(self._set_args) + [value]
        with obj:
            self._setter(*args)

    def __repr__(self):
        return "proxy for %s" % self._arg

class HintProxy(EnumProxy):
    def __init__(self, hint):
        super(HintProxy, self).__init__(hints, hint, _gl.glHint, [hint])

    def __repr__(self):
        return "proxy for %s" % self._arg

class StringProxy(object):
    def __init__(self, arg, count_attr=None):
        self._arg = arg
        self._count_attr = count_attr

    def __get__(self, obj, cls=None):
        if self._count_attr is None:
            with obj:
                return _gl.string_at(_gl.glGetString(self._arg))
        else:
            with obj:
                _n = _gl.GLint()
                _gl.glGetIntegerv(self._count_attr, _gl.pointer(_n))
                return [_gl.string_at(_gl.glGetStringi(self._arg, i)) for i in range(_n.value)]

    def __set__(self, obj, value):
        raise AttributeError("can't set attribute")

    def __repr__(self):
        return "proxy for %s" % self._arg

class BindingProxy(object):
    def __init__(self, setter, set_args=()):
        self._value = WeakKeyDictionary()
        self._setter = setter
        self._set_args = set_args

    def __get__(self, obj, cls=None):
        return self._value.get(obj, None)

    def __set__(self, obj, value=None):
        with obj:
            old_value = self._value.get(obj, None)
            self._value[obj] = value
            if old_value is not None and old_value != value and hasattr(old_value, "_on_release") and old_value._on_release is not NotImplemented:
                old_value._on_release()
            try:
                self._setter(*([getattr(obj, x) if isinstance(x, basestring) else x for x in self._set_args] + [0 if value is None else value._id]))
            except:
                self._value[obj] = old_value
                raise
            else:
                if value is not None and value != old_value and hasattr(value, "_on_bind") and value._on_bind is not NotImplemented:
                    value._on_bind()

    def __repr__(self):
        if self._set_args:
            return "proxy for %s(%s)" % (self._setter.__name__, self._set_args[0])
        else:
            return "proxy for %s()" % self._setter.__name__

