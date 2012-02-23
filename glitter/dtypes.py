import numpy as _np
from rawgl import gl as _gl

class Datatype(object):
    _nptype_db = {}
    _gltype_db = {}
    _db = {}

    def __init__(self, integer, signed, nptype, _gltype=None, charcode=None):
        self._integer = bool(integer)
        self._signed = bool(signed)
        self._nptype = nptype
        self._gltype = _gltype
        self._charcode = charcode
        self._nbytes = nptype().itemsize

        Datatype._nptype_db[self._nptype] = self
        Datatype._gltype_db[self._gltype] = self
        Datatype._db[self._integer, self._signed, self._nbytes] = self

    @classmethod
    def from_numpy(cls, nptype):
        try:
            return Datatype._nptype_db[nptype]
        except KeyError:
            return Datatype._nptype_db[nptype.type]

    @classmethod
    def _from_gl(cls, _gltype):
        return Datatype._gltype_db[_gltype]

    def as_numpy(self):
        return self._nptype

    def _as_gl(self):
        return self._gltype

    def as_signed(self):
        return Datatype._db[self.is_integer(), True, self.nbytes]

    def as_unsigned(self):
        return Datatype._db[self.is_integer(), False, self.nbytes]

    def as_nbytes(self, nbytes):
        return Datatype._db[self.is_integer(), self.is_signed(), nbytes]

    def is_signed(self):
        return self._signed

    def is_unsigned(self):
        return not self._signed

    def is_integer(self):
        return self._integer

    def is_float(self):
        return not self._integer

    def is_boolean(self):
        return self == bool8

    @property
    def charcode(self):
        return self._charcode

    @property
    def nbytes(self):
        return self._nbytes

    def __str__(self):
        return "%s%s%d" % ("u" if self.is_unsigned() else "", "int" if self.is_integer() else "float", 8 * self.nbytes)

bool8 = Datatype(integer=True, signed=True, nptype=_np.bool8, _gltype=_gl.GL_BOOL, charcode="b")
uint8 = Datatype(integer=True, signed=False, nptype=_np.uint8, _gltype=_gl.GL_UNSIGNED_BYTE, charcode="ub")
uint16 = Datatype(integer=True, signed=False, nptype=_np.uint16, _gltype=_gl.GL_UNSIGNED_SHORT)
uint32 = Datatype(integer=True, signed=False, nptype=_np.uint32, _gltype=_gl.GL_UNSIGNED_INT, charcode="ui")
uint64 = Datatype(integer=True, signed=False, nptype=_np.uint64, charcode="ui64")
int8 = Datatype(integer=True, signed=True, nptype=_np.int8, _gltype=_gl.GL_BYTE)
int16 = Datatype(integer=True, signed=True, nptype=_np.int16, _gltype=_gl.GL_SHORT)
int32 = Datatype(integer=True, signed=True, nptype=_np.int32, _gltype=_gl.GL_INT, charcode="i")
int64 = Datatype(integer=True, signed=True, nptype=_np.int64, charcode="i64")
float32 = Datatype(integer=False, signed=True, nptype=_np.float32, _gltype=_gl.GL_FLOAT, charcode="f")
float64 = Datatype(integer=False, signed=True, nptype=_np.float64, _gltype=_gl.GL_DOUBLE, charcode="d")

class ShaderDatatype(object):
    _gltype_db = {}
    _db = {}

    def __init__(self, name, _gltype, dtype=int32, shape=1, texture=False, atomic=True):
        self._name = name
        self._gltype = _gltype
        self._dtype = dtype
        self._shape = (shape,) if not hasattr(shape, "__iter__") else tuple(shape)
        self._texture = texture
        self._atomic = atomic

        Datatype._gltype_db[self._gltype] = self
        Datatype._db[self._dtype, self._shape, self._texture, self._atomic] = self

    @classmethod
    def _from_gl(cls, _gltype):
        return Datatype._gltype_db[_gltype]

    def get_value(self, program, location):
        data = _np.empty(self._shape, int32.as_numpy() if self._dtype.is_boolean() else self._dtype.as_numpy())
        if self._dtype == int32 or self._dtype == bool8:
            _gl.glGetUniformiv(program._id, location, _gl.cast(data.ctypes, _gl.glGetUniformiv.argtypes[-1]))
        elif self._dtype == uint32:
            _gl.glGetUniformuiv(program._id, location, _gl.cast(data.ctypes, _gl.glGetUniformuiv.argtypes[-1]))
        elif self._dtype == float32:
            _gl.glGetUniformfv(program._id, location, _gl.cast(data.ctypes, _gl.glGetUniformfv.argtypes[-1]))
        elif self._dtype == float64:
            _gl.glGetUniformdv(program._id, location, _gl.cast(data.ctypes, _gl.glGetUniformdv.argtypes[-1]))
        else:
            raise TypeError("cannot get uniform variable of type %s" % self)
        return data.astype(self._dtype.as_numpy())

    def set_value(self, program, location, value, count):
        dtype = int32 if self._dtype.is_boolean() else self._dtype
        value = _np.ascontiguousarray(value, dtype.as_numpy())
        if count == 1:
            if value.shape != self._shape and value.shape != (count,) + self._shape:
                raise TypeError("shapes do not match")
        elif self._shape == (1,):
            if value.shape != (count,) and value.shape != (count,) + self._shape:
                raise TypeError("shapes do not match")
        else:
            if value.shape != (count,) + self._shape:
                raise TypeError("shapes do not match")
        if len(self._shape) == 1:
            setter = getattr(_gl, "glUniform%d%sv" % (self._shape[0], dtype.charcode))
            with program:
                setter(location, count, _gl.cast(value.ctypes, setter.argtypes[-1]))
        else:
            setter = getattr(_gl, "glUniformMatrix%dx%d%sv" % (self._shape[1], self._shape[0], dtype.charcode))
            with program:
                setter(location, count, _gl.GL_TRUE, _gl.cast(value.ctypes, setter.argtypes[-1]))

    def is_signed(self):
        return self.dtype.is_signed

    def is_unsigned(self):
        return not self.dtype.is_unsigned()

    def is_integer(self):
        return self.dtype.is_integer()

    def is_float(self):
        return self.dtype.is_float()

    def is_boolean(self):
        return self.dtype.is_boolean()

    def __str__(self):
        return self._name

shader_float = ShaderDatatype("float", _gl.GL_FLOAT, dtype=float32)
shader_vec2 = ShaderDatatype("vec2", _gl.GL_FLOAT_VEC2, dtype=float32, shape=2)
shader_vec3 = ShaderDatatype("vec3", _gl.GL_FLOAT_VEC3, dtype=float32, shape=3)
shader_vec4 = ShaderDatatype("vec4", _gl.GL_FLOAT_VEC4, dtype=float32, shape=4)
shader_double = ShaderDatatype("double", _gl.GL_DOUBLE, dtype=float64)
shader_dvec2 = ShaderDatatype("dvec2", _gl.GL_DOUBLE_VEC2, dtype=float64, shape=2)
shader_dvec3 = ShaderDatatype("dvec3", _gl.GL_DOUBLE_VEC3, dtype=float64, shape=3)
shader_dvec4 = ShaderDatatype("dvec4", _gl.GL_DOUBLE_VEC4, dtype=float64, shape=4)
shader_int = ShaderDatatype("int", _gl.GL_INT, dtype=int32)
shader_ivec2 = ShaderDatatype("ivec2", _gl.GL_INT_VEC2, dtype=int32, shape=2)
shader_ivec3 = ShaderDatatype("ivec3", _gl.GL_INT_VEC3, dtype=int32, shape=3)
shader_ivec4 = ShaderDatatype("ivec4", _gl.GL_INT_VEC4, dtype=int32, shape=4)
shader_unsigned_int = ShaderDatatype("unsigned int", _gl.GL_UNSIGNED_INT, dtype=uint32)
shader_uvec2 = ShaderDatatype("uvec2", _gl.GL_UNSIGNED_INT_VEC2, dtype=uint32, shape=2)
shader_uvec3 = ShaderDatatype("uvec3", _gl.GL_UNSIGNED_INT_VEC3, dtype=uint32, shape=3)
shader_uvec4 = ShaderDatatype("uvec4", _gl.GL_UNSIGNED_INT_VEC4, dtype=uint32, shape=4)
shader_bool = ShaderDatatype("bool", _gl.GL_BOOL, dtype=bool8)
shader_bvec2 = ShaderDatatype("bvec2", _gl.GL_BOOL_VEC2, dtype=bool8, shape=2)
shader_bvec3 = ShaderDatatype("bvec3", _gl.GL_BOOL_VEC3, dtype=bool8, shape=3)
shader_bvec4 = ShaderDatatype("bvec4", _gl.GL_BOOL_VEC4, dtype=bool8, shape=4)
shader_mat2 = ShaderDatatype("mat2", _gl.GL_FLOAT_MAT2, dtype=float32, shape=(2, 2))
shader_mat3 = ShaderDatatype("mat3", _gl.GL_FLOAT_MAT3, dtype=float32, shape=(3, 3))
shader_mat4 = ShaderDatatype("mat4", _gl.GL_FLOAT_MAT4, dtype=float32, shape=(4, 4))
shader_dmat2 = ShaderDatatype("dmat2", _gl.GL_DOUBLE_MAT2, dtype=float64, shape=(2, 2))
shader_dmat3 = ShaderDatatype("dmat3", _gl.GL_DOUBLE_MAT3, dtype=float64, shape=(3, 3))
shader_dmat4 = ShaderDatatype("dmat4", _gl.GL_DOUBLE_MAT4, dtype=float64, shape=(4, 4))
shader_sampler1D = ShaderDatatype("sampler1D", _gl.GL_SAMPLER_1D, texture=True)
shader_sampler2D = ShaderDatatype("sampler2D", _gl.GL_SAMPLER_2D, texture=True)
shader_sampler3D = ShaderDatatype("sampler3D", _gl.GL_SAMPLER_3D, texture=True)
shader_samplerCube = ShaderDatatype("samplerCube", _gl.GL_SAMPLER_CUBE, texture=True)
shader_sampler1DShadow = ShaderDatatype("sampler1DShadow", _gl.GL_SAMPLER_1D_SHADOW, texture=True)
shader_sampler2DShadow = ShaderDatatype("sampler2DShadow", _gl.GL_SAMPLER_2D_SHADOW, texture=True)
shader_sampler1DArray = ShaderDatatype("sampler1DArray", _gl.GL_SAMPLER_1D_ARRAY, texture=True)
shader_sampler2DArray = ShaderDatatype("sampler2DArray", _gl.GL_SAMPLER_2D_ARRAY, texture=True)
shader_sampler1DArrayShadow = ShaderDatatype("sampler1DArrayShadow", _gl.GL_SAMPLER_1D_ARRAY_SHADOW, texture=True)
shader_sampler2DArrayShadow = ShaderDatatype("sampler2DArrayShadow", _gl.GL_SAMPLER_2D_ARRAY_SHADOW, texture=True)
shader_sampler2DMS = ShaderDatatype("sampler2DMS", _gl.GL_SAMPLER_2D_MULTISAMPLE, texture=True)
shader_sampler2DMSArray = ShaderDatatype("sampler2DMSArray", _gl.GL_SAMPLER_2D_MULTISAMPLE_ARRAY, texture=True)
shader_samplerCubeShadow = ShaderDatatype("samplerCubeShadow", _gl.GL_SAMPLER_CUBE_SHADOW, texture=True)
shader_samplerBuffer = ShaderDatatype("samplerBuffer", _gl.GL_SAMPLER_BUFFER, texture=True)
shader_sampler2DRect = ShaderDatatype("sampler2DRect", _gl.GL_SAMPLER_2D_RECT, texture=True)
shader_sampler2DRectShadow = ShaderDatatype("sampler2DRectShadow", _gl.GL_SAMPLER_2D_RECT_SHADOW, texture=True)
shader_isampler1D = ShaderDatatype("isampler1D", _gl.GL_INT_SAMPLER_1D, texture=True)
shader_isampler2D = ShaderDatatype("isampler2D", _gl.GL_INT_SAMPLER_2D, texture=True)
shader_isampler3D = ShaderDatatype("isampler3D", _gl.GL_INT_SAMPLER_3D, texture=True)
shader_isamplerCube = ShaderDatatype("isamplerCube", _gl.GL_INT_SAMPLER_CUBE, texture=True)
shader_isampler1DArray = ShaderDatatype("isampler1DArray", _gl.GL_INT_SAMPLER_1D_ARRAY, texture=True)
shader_isampler2DArray = ShaderDatatype("isampler2DArray", _gl.GL_INT_SAMPLER_2D_ARRAY, texture=True)
shader_isampler2DMS = ShaderDatatype("isampler2DMS", _gl.GL_INT_SAMPLER_2D_MULTISAMPLE, texture=True)
shader_isampler2DMSArray = ShaderDatatype("isampler2DMSArray", _gl.GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY, texture=True)
shader_isamplerBuffer = ShaderDatatype("isamplerBuffer", _gl.GL_INT_SAMPLER_BUFFER, texture=True)
shader_isampler2DRect = ShaderDatatype("isampler2DRect", _gl.GL_INT_SAMPLER_2D_RECT, texture=True)
shader_usampler1D = ShaderDatatype("usampler1D", _gl.GL_UNSIGNED_INT_SAMPLER_1D, texture=True)
shader_usampler2D = ShaderDatatype("usampler2D", _gl.GL_UNSIGNED_INT_SAMPLER_2D, texture=True)
shader_usampler3D = ShaderDatatype("usampler3D", _gl.GL_UNSIGNED_INT_SAMPLER_3D, texture=True)
shader_usamplerCube = ShaderDatatype("usamplerCube", _gl.GL_UNSIGNED_INT_SAMPLER_CUBE, texture=True)
shader_usampler1DArray = ShaderDatatype("usampler1DArray", _gl.GL_UNSIGNED_INT_SAMPLER_1D_ARRAY, texture=True)
shader_usampler2DArray = ShaderDatatype("usampler2DArray", _gl.GL_UNSIGNED_INT_SAMPLER_2D_ARRAY, texture=True)
shader_usampler2DMS = ShaderDatatype("usampler2DMS", _gl.GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE, texture=True)
shader_usampler2DMSArray = ShaderDatatype("usampler2DMSArray", _gl.GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY, texture=True)
shader_usamplerBuffer = ShaderDatatype("usamplerBuffer", _gl.GL_UNSIGNED_INT_SAMPLER_BUFFER, texture=True)
shader_usampler2DRect = ShaderDatatype("usampler2DRect", _gl.GL_UNSIGNED_INT_SAMPLER_2D_RECT, texture=True)
shader_image1D = ShaderDatatype("image1D", _gl.GL_IMAGE_1D, texture=True)
shader_image2D = ShaderDatatype("image2D", _gl.GL_IMAGE_2D, texture=True)
shader_image3D = ShaderDatatype("image3D", _gl.GL_IMAGE_3D, texture=True)
shader_image2DRect = ShaderDatatype("image2DRect", _gl.GL_IMAGE_2D_RECT, texture=True)
shader_imageCube = ShaderDatatype("imageCube", _gl.GL_IMAGE_CUBE, texture=True)
shader_imageBuffer = ShaderDatatype("imageBuffer", _gl.GL_IMAGE_BUFFER, texture=True)
shader_image1DArray = ShaderDatatype("image1DArray", _gl.GL_IMAGE_1D_ARRAY, texture=True)
shader_image2DArray = ShaderDatatype("image2DArray", _gl.GL_IMAGE_2D_ARRAY, texture=True)
shader_image2DMS = ShaderDatatype("image2DMS", _gl.GL_IMAGE_2D_MULTISAMPLE, texture=True)
shader_image2DMSArray = ShaderDatatype("image2DMSArray", _gl.GL_IMAGE_2D_MULTISAMPLE_ARRAY, texture=True)
shader_iimage1D = ShaderDatatype("iimage1D", _gl.GL_INT_IMAGE_1D, texture=True)
shader_iimage2D = ShaderDatatype("iimage2D", _gl.GL_INT_IMAGE_2D, texture=True)
shader_iimage3D = ShaderDatatype("iimage3D", _gl.GL_INT_IMAGE_3D, texture=True)
shader_iimage2DRect = ShaderDatatype("iimage2DRect", _gl.GL_INT_IMAGE_2D_RECT, texture=True)
shader_iimageCube = ShaderDatatype("iimageCube", _gl.GL_INT_IMAGE_CUBE, texture=True)
shader_iimageBuffer = ShaderDatatype("iimageBuffer", _gl.GL_INT_IMAGE_BUFFER, texture=True)
shader_iimage1DArray = ShaderDatatype("iimage1DArray", _gl.GL_INT_IMAGE_1D_ARRAY, texture=True)
shader_iimage2DArray = ShaderDatatype("iimage2DArray", _gl.GL_INT_IMAGE_2D_ARRAY, texture=True)
shader_iimage2DMS = ShaderDatatype("iimage2DMS", _gl.GL_INT_IMAGE_2D_MULTISAMPLE, texture=True)
shader_iimage2DMSArray = ShaderDatatype("iimage2DMSArray", _gl.GL_INT_IMAGE_2D_MULTISAMPLE_ARRAY, texture=True)
shader_uimage1D = ShaderDatatype("uimage1D", _gl.GL_UNSIGNED_INT_IMAGE_1D, texture=True)
shader_uimage2D = ShaderDatatype("uimage2D", _gl.GL_UNSIGNED_INT_IMAGE_2D, texture=True)
shader_uimage3D = ShaderDatatype("uimage3D", _gl.GL_UNSIGNED_INT_IMAGE_3D, texture=True)
shader_uimage2DRect = ShaderDatatype("uimage2DRect", _gl.GL_UNSIGNED_INT_IMAGE_2D_RECT, texture=True)
shader_uimageCube = ShaderDatatype("uimageCube", _gl.GL_UNSIGNED_INT_IMAGE_CUBE, texture=True)
shader_uimageBuffer = ShaderDatatype("uimageBuffer", _gl.GL_UNSIGNED_INT_IMAGE_BUFFER, texture=True)
shader_uimage1DArray = ShaderDatatype("uimage1DArray", _gl.GL_UNSIGNED_INT_IMAGE_1D_ARRAY, texture=True)
shader_uimage2DArray = ShaderDatatype("uimage2DArray", _gl.GL_UNSIGNED_INT_IMAGE_2D_ARRAY, texture=True)
shader_uimage2DMS = ShaderDatatype("uimage2DMS", _gl.GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE, texture=True)
shader_uimage2DMSArray = ShaderDatatype("uimage2DMSArray", _gl.GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_ARRAY, texture=True)
shader_atomic_uint = ShaderDatatype("atomic_uint", _gl.GL_UNSIGNED_INT_ATOMIC_COUNTER, dtype=uint32, atomic=True)

