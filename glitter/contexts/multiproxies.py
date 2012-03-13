"""Descriptors for per-context state with complicated setters.

@todo: Unify classes (e.g. C{__repr__} and C{lookup} methods).

@author: Stephan Wenger
@date: 2012-02-29
"""

import glitter.raw as _gl
from glitter.utils import blend_functions, blend_equations

class BlendFuncProxy(object):
    def __init__(self, arg):
        self._arg = arg

    def __get__(self, obj, cls=None):
        _value = _gl.GLint()
        with obj:
            _gl.glGetIntegerv(self._arg, _gl.pointer(_value))
        return blend_functions[_value.value]

    def lookup(self, value):
        if isinstance(value, basestring):
            value = getattr(self._enum, value)._value
        if value not in blend_functions.__dict__.values():
            raise TypeError("wrong enum")
        return value

    def __set__(self, obj, value):
        src_rgb = self.lookup(value) if self._arg == _gl.GL_BLEND_SRC_RGB else obj.blend_src_rgb
        dst_rgb = self.lookup(value) if self._arg == _gl.GL_BLEND_DST_RGB else obj.blend_dst_rgb
        src_alpha = self.lookup(value) if self._arg == _gl.GL_BLEND_SRC_ALPHA else obj.blend_src_alpha
        dst_alpha = self.lookup(value) if self._arg == _gl.GL_BLEND_DST_ALPHA else obj.blend_dst_alpha
        with obj:
            _gl.glBlendFuncSeparate(src_rgb._value, dst_rgb._value, src_alpha._value, dst_alpha._value)

    def __repr__(self):
        return "proxy for %s" % self._arg

class BlendEquationProxy(object):
    def __init__(self, arg):
        self._arg = arg

    def __get__(self, obj, cls=None):
        _value = _gl.GLint()
        with obj:
            _gl.glGetIntegerv(self._arg, _gl.pointer(_value))
        return blend_equations[_value.value]

    def lookup(self, value):
        if isinstance(value, basestring):
            value = getattr(self._enum, value)._value
        if value not in blend_equations.__dict__.values():
            raise TypeError("wrong enum")
        return value

    def __set__(self, obj, value):
        mode_rgb = self.lookup(value) if self._arg == _gl.GL_BLEND_EQUATION_RGB else obj.blend_equation_rgb
        mode_alpha = self.lookup(value) if self._arg == _gl.GL_BLEND_EQUATION_ALPHA else obj.blend_equation_alpha
        with obj:
            _gl.glBlendEquationSeparate(mode_rgb._value, mode_alpha._value)

    def __repr__(self):
        return "proxy for %s" % self._arg

class PolygonOffsetProxy(object):
    def __init__(self, arg):
        self._arg = arg

    def __get__(self, obj, cls=None):
        _value = _gl.GLfloat()
        with obj:
            _gl.glGetFloatv(self._arg, _gl.pointer(_value))
        return _value.value

    def __set__(self, obj, value):
        factor = value if self._arg == _gl.GL_POLYGON_OFFSET_FACTOR else obj.polygon_offset_factor
        units = value if self._arg == _gl.GL_POLYGON_OFFSET_UNITS else obj.polygon_offset_units
        with obj:
            _gl.glPolygonOffset(factor, units)

    def __repr__(self):
        return "proxy for %s" % self._arg

