"""Descriptors for per-drawbuffer state.

@author: Stephan Wenger
@date: 2012-02-29
"""

import itertools as _itertools
import numpy as _np

import glitter.raw as _gl
from glitter.utils import draw_buffers, bool8, GlitterError

class DrawBufferList(object):
    def __init__(self, _context):
        self._context = _context
        self._num_buffers = _context.max_draw_buffers
        if not 0 < self._num_buffers < 512: # sanity check
            raise GlitterError("implausible number of draw buffers detected; are you sure there is a current OpenGL context?")

    def __set__(self, obj, value):
        """Set all draw buffers.

        @param obj: Ignored.
        @type obj: any type
        @param value: The enum of the draw buffer to bind, a number if it is a color attachment.
        @type value: L{draw_buffers} or C{int}
        """

        _buffers = (_gl.GLenum * self._num_buffers)()
        for i, o in _itertools.islice(_itertools.izip_longest(range(self._num_buffers), value, fillvalue=None), self._num_buffers):
            _buffers[i] = _gl.GL_NONE if o is None else _gl.GL_COLOR_ATTACHMENT0 + o if isinstance(o, int) else draw_buffers(o)._value
        with self._context:
            _gl.glDrawBuffers(self._num_buffers, _buffers)

    def __getitem__(self, index):
        """Get the draw buffer attached to this target.
        
        @param index: Index of the draw buffer to query.
        @type index: C{int}
        @return: The enum of the currently bound draw buffer enum, a number if it is a color attachment.
        @rtype: L{draw_buffers} or C{int}
        """

        if not 0 <= index < self._num_buffers:
            raise IndexError
        _buffer = _gl.GLint()
        with self._context:
            _gl.glGetIntegerv(_gl.GL_DRAW_BUFFER0 + index, _buffer)
        attachment = draw_buffers[_buffer.value]
        if attachment.name.startswith("COLOR_ATTACHMENT"):
            return int(attachment.lstrip("COLOR_ATTACHMENT", 1))
        else:
            return attachment

    def __setitem__(self, index, value):
        """Set a draw buffer.

        @param index: Index of the draw buffer to set.
        @type index: C{int}
        @param value: The enum of the draw buffer to bind, a number if it is a color attachment.
        @type value: L{draw_buffers} or C{int}
        """

        self.__set__(None, [value if i == index else self[i] for i in range(self._num_buffers)])

    def __delitem__(self, index):
        """Unbind a draw buffer.

        @param index: Index of the draw buffer to unbind.
        @type index: C{int}
        """

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
        if not 0 < self._num_buffers < 512: # sanity check
            raise GlitterError("implausible number of draw buffers detected; are you sure there is a current OpenGL context?")

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

