import numpy as _np
from rawgl import gl as _gl

class Datatype(object):
    _nptype_db = {}
    _gltype_db = {}
    _db = {}

    def __init__(self, integer, signed, nptype, _gltype):
        self._integer = bool(integer)
        self._signed = bool(signed)
        self._nptype = nptype
        self._gltype = _gltype
        self._nbytes = nptype().itemsize

        Datatype._nptype_db[self._nptype] = self
        Datatype._gltype_db[self._gltype] = self
        Datatype._db[self._integer, self._signed, self._nbytes] = self

    @classmethod
    def from_numpy(cls, nptype):
        try:
            return cls._nptype_db[nptype]
        except KeyError:
            return cls._nptype_db[nptype.type]

    @classmethod
    def _from_gl(cls, _gltype):
        return cls._gltype_db[_gltype]

    def as_numpy(self):
        return self._nptype

    def _as_gl(self):
        return self._gltype

    def is_signed(self):
        return self._signed

    def is_integer(self):
        return self._integer

    def is_float(self):
        return not self._integer

    @property
    def nbytes(self):
        return self._nbytes

uint8 = Datatype(integer=True, signed=False, nptype=_np.uint8, _gltype=_gl.GL_UNSIGNED_BYTE)
uint16 = Datatype(integer=True, signed=False, nptype=_np.uint16, _gltype=_gl.GL_UNSIGNED_SHORT)
uint32 = Datatype(integer=True, signed=False, nptype=_np.uint32, _gltype=_gl.GL_UNSIGNED_INT)
int8 = Datatype(integer=True, signed=True, nptype=_np.int8, _gltype=_gl.GL_BYTE)
int16 = Datatype(integer=True, signed=True, nptype=_np.int16, _gltype=_gl.GL_SHORT)
int32 = Datatype(integer=True, signed=True, nptype=_np.int32, _gltype=_gl.GL_INT)
float32 = Datatype(integer=False, signed=True, nptype=_np.float32, _gltype=_gl.GL_FLOAT)

