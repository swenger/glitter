"""Memory barrier function.

@author: Stephan Wenger
@date: 2012-02-29
"""

import glitter.raw as _gl

def memory_barrier(
    vertex_attrib_array=False, element_array=False, uniform=False,
    texture_fetch=False, shader_image_access=False, command=False,
    pixel_buffer=False, texture_update=False, buffer_update=False,
    framebuffer=False, transform_feedback=False, atomic_counter=False):
    bits = ((_gl.GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT if vertex_attrib_array else 0) |
            (_gl.GL_ELEMENT_ARRAY_BARRIER_BIT if element_array else 0) |
            (_gl.GL_UNIFORM_BARRIER_BIT if uniform else 0) |
            (_gl.GL_TEXTURE_FETCH_BARRIER_BIT if texture_fetch else 0) |
            (_gl.GL_SHADER_IMAGE_ACCESS_BARRIER_BIT if shader_image_access else 0) |
            (_gl.GL_COMMAND_BARRIER_BIT if command else 0) |
            (_gl.GL_PIXEL_BUFFER_BARRIER_BIT if pixel_buffer else 0) |
            (_gl.GL_TEXTURE_UPDATE_BARRIER_BIT if texture_update else 0) |
            (_gl.GL_BUFFER_UPDATE_BARRIER_BIT if buffer_update else 0) |
            (_gl.GL_FRAMEBUFFER_BARRIER_BIT if framebuffer else 0) |
            (_gl.GL_TRANSFORM_FEEDBACK_BARRIER_BIT if transform_feedback else 0) |
            (_gl.GL_ATOMIC_COUNTER_BARRIER_BIT if atomic_counter else 0))
    if bits == 0:
        bits = _gl.GL_ALL_BARRIER_BITS
    _gl.glMemoryBarrier(bits)

