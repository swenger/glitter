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

def make_dtype(dtype, force_integer=False, force_unsigned=False, force_float=False, force_gl=False, max_width=4):
    return dtype # TODO

def make_array(data, dtype=None, force_integer=False, force_unsigned=False, force_float=False, force_gl=False, max_width=4):
    # TODO produce results with the smallest possible dtype, at most max_width bytes etc.
    return _np.ascontiguousarray(data, dtype.as_numpy() if dtype is not None else None)

__all__ = [
    "Datatype",
    "make_dtype",
    "make_array",
    "bool8",
    "uint8",
    "uint16",
    "uint32",
    "uint64",
    "int8",
    "int16",
    "int32",
    "int64",
    "float32",
    "float64",
]

