import itertools as _itertools
import numpy as _np
from rawgl import gl as _gl

from glitter.utils import constants, EnumConstant, bool8

class DrawBufferList(object):
    def __init__(self, _context):
        self._context = _context
        self._num_buffers = _context.max_draw_buffers

    def __set__(self, obj, value):
        _buffers = (_gl.GLenum * self._num_buffers)()
        for i, o in _itertools.islice(_itertools.izip_longest(range(self._num_buffers), value, fillvalue=None), self._num_buffers):
            _buffers[i] = _gl.GL_NONE if o is None else o._value if isinstance(o, EnumConstant) else _gl.GL_COLOR_ATTACHMENT0 + o
        with self._context:
            _gl.glDrawBuffers(self._num_buffers, _buffers)

    def __getitem__(self, index): # TODO return color attachments as integers
        if not 0 <= index < self._num_buffers:
            raise IndexError
        _buffer = _gl.GLint()
        with self._context:
            _gl.glGetIntegerv(_gl.GL_DRAW_BUFFER0 + index, _buffer)
        return constants.read_buffers[_buffer.value]

    def __setitem__(self, index, value): # TODO set color attachments as integers
        _buffers = (_gl.GLenum * self._num_buffers)()
        for i in range(self._num_buffers):
            if i == index:
                _buffers[i] = value._value if value is not None else _gl.GL_NONE
            else:
                _buffers[i] = self[i]._value
        with self._context:
            _gl.glDrawBuffers(self._num_buffers, _buffers)

    def __delitem__(self, index):
        self[index] = None

    def __len__(self):
        return self._num_buffers

    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return str(self)

class ColorWritemaskList(object):
    def __init__(self, _context):
        self._context = _context
        self._num_buffers = _context.max_draw_buffers

    def __set__(self, obj, value):
        if len(value) != self._num_buffers:
            raise ValueError("wrong size")
        for i, v in enumerate(value):
            self[i] = v

    def __getitem__(self, index):
        if not 0 <= index < self._num_buffers:
            raise IndexError
        mask = _np.empty(4, bool8.as_numpy())
        with self._context:
            _gl.glGetBooleani_v(_gl.GL_COLOR_WRITEMASK, index, _gl.cast(mask.ctypes, _gl.glGetBooleani_v.argtypes[-1]))
        return mask

    def __setitem__(self, index, value):
        with self._context:
            _gl.glColorMaski(index, *value)

    def __delitem__(self, index):
        self[index] = (True, True, True, True)

    def __len__(self):
        return self._num_buffers

    def __str__(self):
        return str(_np.array(self))

    def __repr__(self):
        return str(self)

