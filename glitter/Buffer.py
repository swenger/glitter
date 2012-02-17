import numpy

from rawgl import gl as _gl

from util import GLObject

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

# TODO one buffer can be bound to different targets; how should this be represented? BufferBinding()?
# TODO buffers likely contain meaningful array data; remember the dtypes and shape

class Buffer(GLObject):
    _generate_id = _gl.glGenBuffers
    _delete_id = _gl.glDeleteBuffers
    _bind = _gl.glBindBuffer

    def __init__(self, data=None, access_frequency="static", access_type="draw"):
        super(Buffer, self).__init__()

        self._binding = _buffer_target_to_binding[self._target]

        self._setdata(data, _buffer_params_to_usage[access_frequency, access_type])

    @property
    def data(self): # TODO slicing with glGetBufferSubData
        pass # TODO

    @data.setter
    def data(self, data): # TODO slicing with glBufferSubData
        self._setdata(data, self._usage)

    def _setdata(self, data, _usage):
        _target = self._target
        if _target not in (_gl.GL_ARRAY_BUFFER, _gl.GL_ELEMENT_ARRAY_BUFFER, _gl.GL_PIXEL_PACK_BUFFER, _gl.GL_PIXEL_UNPACK_BUFFER):
            _target = _gl.GL_ARRAY_BUFFER
        _nbytes = data.nbytes if data is not None else 0
        _data = numpy.ascontiguousarray(data.ctypes) if data is not None else _gl.POINTER(_gl.GLvoid)()
        with self:
            _gl.glBufferData(_target, _nbytes, _data, _usage)

        self._shape = data.shape
        self._dtype = data.dtype

    @property
    def shape(self):
        return self._shape

    @property
    def dtype(self):
        return self._dtype

    @property
    def _size(self):
        _size = _gl.GLint()
        _gl.glGetBufferParameteriv(self._target, _gl.GL_BUFFER_SIZE, _gl.pointer(_size))
        return _size.value

    @property
    def _usage(self):
        _usage = _gl.GLint()
        _gl.glGetBufferParameteriv(self._target, _gl.GL_BUFFER_USAGE, _gl.pointer(_usage))
        return _usage.value

    @property
    def access_frequency(self):
        return _buffer_usage_to_params[self._usage][0]

    @property
    def access_type(self):
        return _buffer_usage_to_params[self._usage][1]

    # TODO bind_as_... and ..._binding()

class ArrayBuffer(Buffer):
    _target = _gl.GL_ARRAY_BUFFER
    # TODO glVertexAttribPointer

class AtomicCounterBuffer(Buffer):
    _target = _gl.GL_ATOMIC_COUNTER_BUFFER
    # TODO glBindBufferBase, glBindBufferRange

class CopyReadBuffer(Buffer):
    _target = _gl.GL_COPY_READ_BUFFER
    # TODO glCopyBufferSubData

class CopyWriteBuffer(Buffer):
    _target = _gl.GL_COPY_WRITE_BUFFER
    # TODO glCopyBufferSubData

class DrawIndirectBuffer(Buffer):
    _target = _gl.GL_DRAW_INDIRECT_BUFFER
    # TODO glDrawArraysIndirect, glDrawElementsIndirect

class ElementArrayBuffer(Buffer):
    _target = _gl.GL_ELEMENT_ARRAY_BUFFER
    # TODO glDrawElements, glDrawElementsInstanced, glDrawElementsBaseVertex, glDrawRangeElements, glDrawRangeElementsBaseVertex, glMultiDrawElements, glMultiDrawElementsBaseVertex

class PixelPackBuffer(Buffer):
    _target = _gl.GL_PIXEL_PACK_BUFFER
    # TODO glGetCompressedTexImage, glGetTexImage, glReadPixels

class PixelUnpackBuffer(Buffer):
    _target = _gl.GL_PIXEL_UNPACK_BUFFER
    # TODO glCompressedTexImage1D, glCompressedTexImage2D, glCompressedTexImage3D, glCompressedTexSubImage1D, glCompressedTexSubImage2D, glCompressedTexSubImage3D, glTexImage1D, glTexImage2D, glTexImage3D, glTexSubImage1D, glTexSubImage2D, glTexSubImage3D

class TextureBuffer(Buffer):
    _target = _gl.GL_TEXTURE_BUFFER

class TransformFeedbackBuffer(Buffer):
    _target = _gl.GL_TRANSFORM_FEEDBACK_BUFFER
    # TODO glBindBufferBase, glBindBufferRange

class UniformBuffer(Buffer):
    _target = _gl.GL_UNIFORM_BUFFER
    # TODO glBindBufferBase, glBindBufferRange


# nosetests

# TODO tests as in Texture

