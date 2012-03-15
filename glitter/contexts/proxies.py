"""Generic descriptor classes for per-context state.

@author: Stephan Wenger
@date: 2012-02-29
"""

from weakref import WeakKeyDictionary

import glitter.raw as _gl
from glitter.utils import hints, bool8, int32, int64, float32, Proxy

class BooleanProxy(Proxy):
    def __init__(self, get_args=(), setter=None, set_args=(), shape=()):
        super(BooleanProxy, self).__init__(_gl.glGetBooleanv, get_args, setter, set_args, bool8, shape)

class FloatProxy(Proxy):
    def __init__(self, get_args=(), setter=None, set_args=(), shape=()):
        super(FloatProxy, self).__init__(_gl.glGetFloatv, get_args, setter, set_args, float32, shape)

class IntegerProxy(Proxy):
    def __init__(self, get_args=(), setter=None, set_args=(), shape=()):
        super(IntegerProxy, self).__init__(_gl.glGetIntegerv, get_args, setter, set_args, int32, shape)

class Integer64Proxy(Proxy):
    def __init__(self, get_args=(), setter=None, set_args=(), shape=()):
        super(Integer64Proxy, self).__init__(_gl.glGetInteger64v, get_args, setter, set_args, int64, shape)

class EnableDisableProxy(Proxy):
    def __init__(self, arg):
        super(EnableDisableProxy, self).__init__(name=arg)
        self._arg = arg

    def __get__(self, obj, cls=None):
        with obj:
            return _gl.glIsEnabled(self._arg) == _gl.GL_TRUE

    def __set__(self, obj, value):
        with obj:
            _gl.glEnable(self._arg) if value else _gl.glDisable(self._arg)

class EnumProxy(Proxy):
    def __init__(self, enum, arg, setter=None, set_args=()):
        super(EnumProxy, self).__init__(enum=enum, getter=_gl.glGetIntegerv, get_args=(arg,), setter=setter, set_args=set_args)

class HintProxy(EnumProxy):
    def __init__(self, hint):
        super(HintProxy, self).__init__(hints, hint, _gl.glHint, [hint])

class StringProxy(Proxy):
    def __init__(self, arg, count_attr=None):
        super(StringProxy, self).__init__(name=arg)
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

class BindingProxy(Proxy):
    def __init__(self, setter, set_args=()):
        super(BindingProxy, self).__init__(setter=setter, set_args=set_args)
        self._value = WeakKeyDictionary()

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

