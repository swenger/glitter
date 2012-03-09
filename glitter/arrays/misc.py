"""Miscellaneous buffer objects.

@author: Stephan Wenger
@date: 2012-02-29
"""

import glitter.raw as _gl
from glitter.arrays.basebuffer import BaseBuffer

class AtomicCounterBuffer(BaseBuffer):
    _binding = "atomic_counter_buffer_binding"
    _target = _gl.GL_ATOMIC_COUNTER_BUFFER

class CopyReadBuffer(BaseBuffer):
    _binding = "copy_read_buffer_binding"
    _target = _gl.GL_COPY_READ_BUFFER

class CopyWriteBuffer(BaseBuffer):
    _binding = "copy_write_buffer_binding"
    _target = _gl.GL_COPY_WRITE_BUFFER

class DrawIndirectBuffer(BaseBuffer):
    _binding = "draw_indirect_buffer_binding"
    _target = _gl.GL_DRAW_INDIRECT_BUFFER

class PixelPackBuffer(BaseBuffer):
    _binding = "pixel_pack_buffer_binding"
    _target = _gl.GL_PIXEL_PACK_BUFFER

class PixelUnpackBuffer(BaseBuffer):
    _binding = "pixel_unpack_buffer_binding"
    _target = _gl.GL_PIXEL_UNPACK_BUFFER

class TextureBuffer(BaseBuffer):
    _binding = "texture_buffer_binding"
    _target = _gl.GL_TEXTURE_BUFFER

class TransformFeedbackBuffer(BaseBuffer):
    _binding = "transform_feedback_buffer_binding"
    _target = _gl.GL_TRANSFORM_FEEDBACK_BUFFER

class UniformBuffer(BaseBuffer):
    _binding = "uniform_buffer_binding"
    _target = _gl.GL_UNIFORM_BUFFER

__all__ = [
    "AtomicCounterBuffer",
    "CopyReadBuffer",
    "CopyWriteBuffer",
    "DrawIndirectBuffer",
    "PixelPackBuffer",
    "PixelUnpackBuffer",
    "TextureBuffer",
    "TransformFeedbackBuffer",
    "UniformBuffer",
]

