import numpy

from rawgl import gl as _gl

_buffer_targets = [ # target, binding
        (_gl.GL_ARRAY_BUFFER,              _gl.GL_ARRAY_BUFFER_BINDING             ),
        (_gl.GL_ATOMIC_COUNTER_BUFFER,     _gl.GL_ATOMIC_COUNTER_BUFFER_BINDING    ),
        (_gl.GL_COPY_READ_BUFFER,          _gl.GL_COPY_READ_BUFFER_BINDING         ),
        (_gl.GL_COPY_WRITE_BUFFER,         _gl.GL_COPY_WRITE_BUFFER_BINDING        ),
        (_gl.GL_DRAW_INDIRECT_BUFFER,      _gl.GL_DRAW_INDIRECT_BUFFER_BINDING     ),
        (_gl.GL_ELEMENT_ARRAY_BUFFER,      _gl.GL_ELEMENT_ARRAY_BUFFER_BINDING     ),
        (_gl.GL_PIXEL_PACK_BUFFER,         _gl.GL_PIXEL_PACK_BUFFER_BINDING        ),
        (_gl.GL_PIXEL_UNPACK_BUFFER,       _gl.GL_PIXEL_UNPACK_BUFFER_BINDING      ),
        (_gl.GL_TEXTURE_BUFFER,            None                                    ), # XXX why is there no GL_TEXTURE_BUFFER_BINDING?
        (_gl.GL_TRANSFORM_FEEDBACK_BUFFER, _gl.GL_TRANSFORM_FEEDBACK_BUFFER_BINDING),
        (_gl.GL_UNIFORM_BUFFER,            _gl.GL_UNIFORM_BUFFER_BINDING           ),
]
_buffer_target_to_binding = dict((x[0], x[1]) for x in _buffer_targets)

_buffer_usage = [ # (access_frequency, access_type), usage
        (("stream",  "draw"), _gl.GL_STREAM_DRAW),
        (("stream",  "read"), _gl.GL_STREAM_READ),
        (("stream",  "copy"), _gl.GL_STREAM_COPY),
        (("static",  "draw"), _gl.GL_STATIC_DRAW),
        (("static",  "read"), _gl.GL_STATIC_READ),
        (("static",  "copy"), _gl.GL_STATIC_COPY),
        (("dynamic", "draw"), _gl.GL_DYNAMIC_DRAW),
        (("dynamic", "read"), _gl.GL_DYNAMIC_READ),
        (("dynamic", "copy"), _gl.GL_DYNAMIC_COPY),
]
_buffer_params_to_usage = dict((x[0], x[1]) for x in _buffer_usage)
_buffer_usage_to_params = dict((x[1], x[0]) for x in _buffer_usage)

class Buffer(object): # TODO
    def __init__(self, data=None, access_frequency="static", access_type="draw"): # TODO allow copy-less initialization from another buffer
        self._stack = []

        _id = _gl.GLuint()
        _gl.glGenBuffers(1, _gl.pointer(_id))
        self._id = _id.value

        _target = self._target
        if _target not in (_gl.GL_ARRAY_BUFFER, _gl.GL_ELEMENT_ARRAY_BUFFER, _gl.GL_PIXEL_PACK_BUFFER, _gl.GL_PIXEL_UNPACK_BUFFER):
            _target = _gl.GL_ARRAY_BUFFER
        _nbytes = data.nbytes if data is not None else 0
        _data = numpy.ascontiguousarray(data.ctypes) if data is not None else _gl.POINTER(_gl.GLvoid)()
        with self:
            _gl.glBufferData(_target, _nbytes, _data, _buffer_params_to_usage[access_frequency, access_type])

    def __del__(self):
        try:
            _gl.glDeleteBuffers(1, _gl.pointer(_gl.GLuint(self._id)))
            self._id = 0
        except AttributeError:
            pass # avoid "'NoneType' object has no attribute 'glDeleteTextures'" when GL module has already been unloaded

    @property
    def data(self):
        pass # TODO

    @data.setter
    def data(self, data):
        _target = self._target
        if _target not in (_gl.GL_ARRAY_BUFFER, _gl.GL_ELEMENT_ARRAY_BUFFER, _gl.GL_PIXEL_PACK_BUFFER, _gl.GL_PIXEL_UNPACK_BUFFER):
            _target = _gl.GL_ARRAY_BUFFER
        _nbytes = data.nbytes if data is not None else 0
        _data = numpy.ascontiguousarray(data.ctypes) if data is not None else _gl.POINTER(_gl.GLvoid)()
        with self:
            _gl.glBufferData(_target, _nbytes, _data, self._usage)

    @property
    def _usage(self):
        pass # TODO

    @property
    def access_frequency(self):
        return _buffer_usage_to_params[self._usage][0]

    @property
    def access_type(self):
        return _buffer_usage_to_params[self._usage][1]

    def bind(self):
        _old_binding = _gl.GLint()
        _gl.glGetIntegerv(_buffer_target_to_binding[self._target], _gl.pointer(_old_binding))
        _gl.glBindBuffer(self._target, self._id)
        return _old_binding.value

    # TODO bind_as_... and ..._binding()

    def __enter__(self):
        self._stack.append(self.bind())

    def __exit__(self, type, value, traceback):
        _gl.glBindBuffer(self._target, self._stack.pop())

class ArrayBuffer(Buffer):
    def __init__(self):
        self._target = _gl.GL_ARRAY_BUFFER
        super(ArrayBuffer, self).__init__()
    # TODO glVertexAttribPointer

class AtomicCounterBuffer(Buffer):
    def __init__(self):
        self._target = _gl.GL_ATOMIC_COUNTER_BUFFER
        super(AtomicCounterBuffer, self).__init__()
    # TODO glBindBufferBase, glBindBufferRange

class CopyReadBuffer(Buffer):
    def __init__(self):
        self._target = _gl.GL_COPY_READ_BUFFER
        super(CopyReadBuffer, self).__init__()
    # TODO glCopyBufferSubData

class CopyWriteBuffer(Buffer):
    def __init__(self):
        self._target = _gl.GL_COPY_WRITE_BUFFER
        super(CopyWriteBuffer, self).__init__()
    # TODO glCopyBufferSubData

class DrawIndirectBuffer(Buffer):
    def __init__(self):
        self._target = _gl.GL_DRAW_INDIRECT_BUFFER
        super(DrawIndirectBuffer, self).__init__()
    # TODO glDrawArraysIndirect, glDrawElementsIndirect

class ElementArrayBuffer(Buffer):
    def __init__(self):
        self._target = _gl.GL_ELEMENT_ARRAY_BUFFER
        super(ElementArrayBuffer, self).__init__()
    # TODO glDrawElements, glDrawElementsInstanced, glDrawElementsBaseVertex, glDrawRangeElements, glDrawRangeElementsBaseVertex, glMultiDrawElements, glMultiDrawElementsBaseVertex

class PixelPackBuffer(Buffer):
    def __init__(self):
        self._target = _gl.GL_PIXEL_PACK_BUFFER
        super(PixelPackBuffer, self).__init__()
    # TODO glGetCompressedTexImage, glGetTexImage, glReadPixels

class PixelUnpackBuffer(Buffer):
    def __init__(self):
        self._target = _gl.GL_PIXEL_UNPACK_BUFFER
        super(PixelUnpackBuffer, self).__init__()
    # TODO glCompressedTexImage1D, glCompressedTexImage2D, glCompressedTexImage3D, glCompressedTexSubImage1D, glCompressedTexSubImage2D, glCompressedTexSubImage3D, glTexImage1D, glTexImage2D, glTexImage3D, glTexSubImage1D, glTexSubImage2D, glTexSubImage3D

class TextureBuffer(Buffer):
    def __init__(self):
        self._target = _gl.GL_TEXTURE_BUFFER
        super(TextureBuffer, self).__init__()

class TransformFeedbackBuffer(Buffer):
    def __init__(self):
        self._target = _gl.GL_TRANSFORM_FEEDBACK_BUFFER
        super(TransformFeedbackBuffer, self).__init()
    # TODO glBindBufferBase, glBindBufferRange

class UniformBuffer(Buffer):
    def __init__(self):
        self._target = _gl.GL_UNIFORM_BUFFER
        super(UniformBuffer, self).__init__()
    # TODO glBindBufferBase, glBindBufferRange

