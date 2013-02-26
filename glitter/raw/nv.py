"""Nvidia-only functions.

@author: Kai Ruhl
@since: 2013-02"""

import glew as _glew
import gl as _gl


def get_nv_memory_total():
    """Returns the total memory (Nvidia only), in MB."""
    total = _gl.GLint()
    _gl.glGetIntegerv(_glew.GL_GPU_MEMORY_INFO_TOTAL_AVAILABLE_MEMORY_NVX, _gl.pointer(total))
    return total.value / 1024


def get_nv_memory_avail():
    """Returns the available memory (Nvidia only), in MB."""
    avail = _gl.GLint()
    _gl.glGetIntegerv(_glew.GL_GPU_MEMORY_INFO_CURRENT_AVAILABLE_VIDMEM_NVX, _gl.pointer(avail))
    return avail.value / 1024


if __name__  == "__main__":
    from glitter.contexts.glut import GlutWindow
    gl_context = GlutWindow(shape=(1, 1), hide=True)
    print "Total     GPU memory: %d MB" % (get_nv_memory_total())
    print "Available GPU memory: %d MB" % (get_nv_memory_avail())
