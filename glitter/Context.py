from rawgl import gl as _gl

# TODO with statements for state changes, e.g. with context.set(active_texture=0): ...
# TODO default context singleton

class Proxy(object): # TODO __get__, __set__, __delete__, __getitem__, __setitem__, cast to array
    _default_value = 0

    def __init__(self, getter_args, setter=None, shape=(1,)):
        self._getter_args = getter_args
        if setter:
            self._setter = setter if callable(setter) else setter[0]
            self._setter_args = () if callable(setter) else tuple(setter[1:])
        self._shape = shape

    def __get__(self, obj, cls=None):
        with obj:
            return self._getter(self._getter_args)

    def __set__(self, obj, value):
        with obj:
            self._setter(self._setter_args + (value,))

    def __del__(self, obj):
        with obj:
            self._setter(self._setter_args + (self._default_value))

class BooleanProxy(Proxy):
    _getter = _gl.glGetBooleanv # TODO wrap
    _index_getter = _gl.glGetBooleani_v # TODO wrap
    
    def _setter(self, value):
        if value:
            _gl.glEnable(value)
        else:
            _gl.glDisable(value)

class DoubleProxy(Proxy):
    _getter = _gl.glGetDoublev
    _index_getter = _gl.glGetDoublei_v

class FloatProxy(Proxy):
    _getter = _gl.glGetFloatv
    _index_getter = _gl.glGetFloati_v

class IntegerProxy(Proxy):
    _getter = _gl.glGetIntegerv
    _index_getter = _gl.glGetIntegeri_v

class Integer64Proxy(Proxy):
    _getter = _gl.glGetInteger64v
    _index_getter = _gl.glGetInteger64i_v

class Context(object): # TODO this should be bindable, but that is window system dependent
    def __enter__(self): pass
    def __exit__(self, type, value, traceback): pass

    active_texture = IntegerProxy(_gl.GL_ACTIVE_TEXTURE, _gl.glActiveTexture)
    aliased_line_width_range = FloatProxy(_gl.GL_ALIASED_LINE_WIDTH_RANGE, None, (2,))
    array_buffer_binding = IntegerProxy(_gl.GL_ARRAY_BUFFER_BINDING, (_gl.glBindBuffer, _gl.GL_ARRAY_BUFFER))
    blend = BooleanProxy(_gl.GL_BLEND)
    blend_color = FloatProxy(_gl.GL_BLEND_COLOR, _gl.glBlendColor, (4,))

