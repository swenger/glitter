from rawgl import gl as _gl

import constants
from util import BindableObject

class Sampler(BindableObject):
    _generate_id = _gl.glGenSamplers
    _delete_id = _gl.glDeleteSamplers
    _bind = _gl.glBindSampler
    _binding = _gl.GL_SAMPLER_BINDING

    compare_funcs = constants.texture_compare_funcs
    compare_modes = constants.texture_compare_modes
    min_filters = constants.texture_min_filters
    mag_filters = constants.texture_mag_filters
    wrapmodes = constants.texture_wrapmodes

    def __init__(self, unit):
        self._target = unit # TODO check for 0 <= unit < GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS
        super(Sampler, self).__init__()

    # TODO getters and setters for unit (mind the stack!), binding to several units

    @property
    def compare_func(self):
        _compare_func = _gl.GLint()
        _gl.glGetSamplerParameteriv(self._id, _gl.GL_TEXTURE_COMPARE_FUNC, _gl.pointer(_compare_func))
        return self.compare_funcs[_compare_func.value]

    @compare_func.setter
    def compare_func(self, compare_func):
        _gl.glSamplerParameteriv(self._id, _gl.GL_TEXTURE_COMPARE_FUNC, _gl.pointer(_gl.GLint(compare_func._value)))

    @property
    def compare_mode(self):
        _compare_mode = _gl.GLint()
        _gl.glGetSamplerParameteriv(self._id, _gl.GL_TEXTURE_COMPARE_MODE, _gl.pointer(_compare_mode))
        return self.compare_modes[_compare_mode.value]

    @compare_mode.setter
    def compare_mode(self, compare_mode):
        _gl.glSamplerParameteriv(self._id, _gl.GL_TEXTURE_COMPARE_MODE, _gl.pointer(_gl.GLint(compare_mode._value)))
    
    @property
    def lod_bias(self):
        _lod_bias = _gl.GLfloat()
        _gl.glGetSamplerParameterfv(self._id, _gl.GL_TEXTURE_LOD_BIAS, _gl.pointer(_lod_bias))
        return _lod_bias.value

    @lod_bias.setter
    def lod_bias(self, lod_bias):
        _gl.glSamplerParameterfv(self._id, _gl.GL_TEXTURE_LOD_BIAS, _gl.pointer(_gl.GLfloat(lod_bias)))

    @property
    def min_filter(self):
        _min_filter = _gl.GLint()
        _gl.glGetSamplerParameteriv(self._id, _gl.GL_TEXTURE_MIN_FILTER, _gl.pointer(_min_filter))
        return self.min_filters[_min_filter.value]

    @min_filter.setter
    def min_filter(self, min_filter):
        _gl.glSamplerParameteriv(self._id, _gl.GL_TEXTURE_MIN_FILTER, _gl.pointer(_gl.GLint(min_filter._value)))

    @property
    def mag_filter(self):
        _mag_filter = _gl.GLint()
        _gl.glGetSamplerParameteriv(self._id, _gl.GL_TEXTURE_MAG_FILTER, _gl.pointer(_mag_filter))
        return self.mag_filters[_mag_filter.value]

    @mag_filter.setter
    def mag_filter(self, mag_filter):
        _gl.glSamplerParameteriv(self._id, _gl.GL_TEXTURE_MAG_FILTER, _gl.pointer(_gl.GLint(mag_filter._value)))

    @property
    def min_lod(self):
        _min_lod = _gl.GLint()
        _gl.glGetSamplerParameteriv(self._id, _gl.GL_TEXTURE_MIN_LOD, _gl.pointer(_min_lod))
        return _min_lod.value

    @min_lod.setter
    def min_lod(self, min_lod):
        _gl.glSamplerParameteriv(self._id, _gl.GL_TEXTURE_MIN_LOD, _gl.pointer(_gl.GLint(min_lod)))

    @property
    def max_lod(self):
        _max_lod = _gl.GLint()
        _gl.glGetSamplerParameteriv(self._id, _gl.GL_TEXTURE_MAX_LOD, _gl.pointer(_max_lod))
        return _max_lod.value

    @max_lod.setter
    def max_lod(self, max_lod):
        _gl.glSamplerParameteriv(self._id, _gl.GL_TEXTURE_MAX_LOD, _gl.pointer(_gl.GLint(max_lod)))

    @property
    def wrap_s(self):
        _wrap_s = _gl.GLint()
        _gl.glGetSamplerParameteriv(self._id, _gl.GL_TEXTURE_WRAP_S, _gl.pointer(_wrap_s))
        return self.wrapmodes[_wrap_s.value]

    @wrap_s.setter
    def wrap_s(self, wrap_s):
        _gl.glSamplerParameteriv(self._id, _gl.GL_TEXTURE_WRAP_S, _gl.pointer(_gl.GLint(wrap_s._value)))

    @property
    def wrap_t(self):
        _wrap_t = _gl.GLint()
        _gl.glGetSamplerParameteriv(self._id, _gl.GL_TEXTURE_WRAP_T, _gl.pointer(_wrap_t))
        return self.wrapmodes[_wrap_t.value]

    @wrap_t.setter
    def wrap_t(self, wrap_t):
        _gl.glSamplerParameteriv(self._id, _gl.GL_TEXTURE_WRAP_T, _gl.pointer(_gl.GLint(wrap_t._value)))

    @property
    def wrap_r(self):
        _wrap_r = _gl.GLint()
        _gl.glGetSamplerParameteriv(self._id, _gl.GL_TEXTURE_WRAP_R, _gl.pointer(_wrap_r))
        return self.wrapmodes[_wrap_r.value]

    @wrap_r.setter
    def wrap_r(self, wrap_r):
        _gl.glSamplerParameteriv(self._id, _gl.GL_TEXTURE_WRAP_R, _gl.pointer(_gl.GLint(wrap_r._value)))

def check_property(sampler, name):
    from util import EnumConstant
    value = getattr(sampler, name)
    if isinstance(value, EnumConstant):
        valid_values = value._enum._reverse_dict.values()
        for value in valid_values:
            setattr(sampler, name, value)
            assert getattr(sampler, name) == value, "property %s is broken" % name
    else:
        setattr(sampler, name, value)
        assert getattr(sampler, name) == value, "property %s is broken" % name

def test_property_generator():
    sampler = Sampler(0)
    properties = [x for x in dir(sampler) if not x.startswith("_") and type(getattr(Sampler, x)) == property]

    for p in properties:
        yield check_property, sampler, p

