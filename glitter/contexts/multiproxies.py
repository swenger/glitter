"""Descriptors for per-context state with complicated setters.

@author: Stephan Wenger
@date: 2012-02-29
"""

from rawgl import gl as _gl

from glitter.utils import constants

class BlendFuncProxy(object):
    def __init__(self, arg):
        self._arg = arg

    def __get__(self, obj, cls=None):
        _value = _gl.GLint()
        with obj:
            _gl.glGetIntegerv(self._arg, _gl.pointer(_value))
        return constants.blend_functions[_value.value]

    def __set__(self, obj, value):
        src_rgb = value if self._arg == _gl.GL_BLEND_SRC_RGB else obj.blend_src_rgb
        dst_rgb = value if self._arg == _gl.GL_BLEND_DST_RGB else obj.blend_dst_rgb
        src_alpha = value if self._arg == _gl.GL_BLEND_SRC_ALPHA else obj.blend_src_alpha
        dst_alpha = value if self._arg == _gl.GL_BLEND_DST_ALPHA else obj.blend_dst_alpha
        with obj:
            _gl.glBlendFuncSeparate(src_rgb._value, dst_rgb._value, src_alpha._value, dst_alpha._value)

class BlendEquationProxy(object):
    def __init__(self, arg):
        self._arg = arg

    def __get__(self, obj, cls=None):
        _value = _gl.GLint()
        with obj:
            _gl.glGetIntegerv(self._arg, _gl.pointer(_value))
        return constants.blend_equations[_value.value]

    def __set__(self, obj, value):
        mode_rgb = value if self._arg == _gl.GL_BLEND_EQUATION_RGB else obj.blend_equation_rgb
        mode_alpha = value if self._arg == _gl.GL_BLEND_EQUATION_ALPHA else obj.blend_equation_alpha
        with obj:
            _gl.glBlendEquationSeparate(mode_rgb._value, mode_alpha._value)

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

