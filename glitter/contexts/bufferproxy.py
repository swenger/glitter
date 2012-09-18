"""Proxy for access to framebuffer pixels.

@author: Stephan Wenger
@date: 2012-09-18
"""

import numpy as _np

import glitter.raw as _gl
from glitter.utils import float32, format_to_length

class BufferProxy(object):
    def __init__(self, mode, dtype=float32, format=_gl.GL_RGBA, context=None):
        self._context = context
        self._mode = mode
        self._dtype = dtype
        self._format = format

    def __get__(self, obj, cls=None):
        return BufferProxy(mode=self._mode, dtype=self._dtype, format=self._format, context=obj)

    def __set__(self, obj, value):
        self.__get__(obj)[:] = value

    def _parse_slice(self, s, size):
        if isinstance(s, slice):
            start, stop, step = s.start, s.stop, s.step
            if step is None:
                step = 1
            else:
                raise NotImplementedError("step is not supported yet") # TODO support via glPixelStore?
            if start is None:
                start = 0
            elif start < 0:
                start = size + start
            if stop is None:
                stop = size
            elif stop < 0:
                stop = size + stop
            if start is None or stop is None:
                raise NotImplementedError("size of framebuffer cannot yet be inferred, specify a slice manually") # TODO see below
            return start, (stop - start - 1) / step + 1
        else:
            return s, None

    def _parse_slices(self, s):
        if not isinstance(s, tuple):
            s = (s,)
        while len(s) < 2:
            s = s + (slice(None, None, None),)
        if len(s) != 2:
            raise ValueError("need exactly 2 dimensions")

        y, height = self._parse_slice(s[0], None) # TODO pass height of framebuffer
        x, width = self._parse_slice(s[1], None) # TODO pass width of framebuffer

        shape = ()

        if height is not None:
            shape = shape + (height,)
        else:
            height = 1
        
        if width is not None:
            shape = shape + (width,)
        else:
            width = 1

        format_length = format_to_length[self._format]
        if format_length != 1:
            shape = shape + (format_length,)

        return shape, x, y, width, height
        
    def __getitem__(self, s):
        with self._context:
            shape, x, y, width, height = self._parse_slices(s)
            _gl.glReadBuffer(self._mode) # TODO set self._context.read_buffer in a with statement
            # TODO set glPixelStore arguments on self._context in a with statement
            # TODO set glPixelTransfer arguments on self._context in a with statement
            # TODO set glPixelMap arguments on self._context in a with statement
            _data = _np.empty(shape, dtype=self._dtype.as_numpy())
            _gl.glReadPixels(x, y, width, height, self._format, self._dtype._as_gl(), _data.ctypes)
            return _data

    def __setitem__(self, s, value):
        raise NotImplementedError("setting of pixels is unimplemented") # TODO like __getitem__

