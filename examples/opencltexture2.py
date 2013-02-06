#!/usr/bin/env/python

"""Minimal example of OpenGL/CL interaction using textures.

@author: Kai Ruhl
@since 2013-02"""

import sys
import numpy as np
import pyopencl as cl

from glitter import Texture2D
from glitter.raw import gl

cl_source = """
const sampler_t T_RAW_SAMPLER = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void run(uint wid, uint hei, __read_only image2d_t img0) {
}
"""


def get_gl_context(option="g"):
    """Returns an OpenGL context. Options: g(lut), q(t)"""
    if "g" == option:
        print "Creating GLUT context."
        from glitter.contexts.glut import GlutWindow
        gl_context = GlutWindow(shape=(1,1), hide=True)
    elif "q" == option:
        print "Creating QT context."
        from PySide import QtGui
        from glitter.contexts.qt import QtWidget
        app = QtGui.QApplication(sys.argv)
        gl_context = QtWidget(None)
    else:
        raise Exception("Unknown option: %s" % option)
    return gl_context


def get_cl_context(gl_context):
    """Creates a CL context, with or without given GL context."""
    if gl_context is not None: # ... with OpenGL interop?
        with gl_context:
            assert cl.have_gl(), "GL interoperability not enabled."
            from pyopencl.tools import get_gl_sharing_context_properties
            cl_platform = cl.get_platforms()[0]
            cl_properties = [(cl.context_properties.PLATFORM, cl_platform)] + get_gl_sharing_context_properties()
            cl_devices = [cl_platform.get_devices()[-1]]  # Only one is allowed!
            cl_context = cl.Context(properties=cl_properties, devices=cl_devices)
    else: # ... or in stand-alone mode, CL context without GL?
        cl_platform = cl.get_platforms()[0]  # @UndefinedVariable
        cl_properties = [(cl.context_properties.PLATFORM, cl_platform)]
        cl_devices = [cl_platform.get_devices()[-1]]  # Only one is allowed!
        cl_context = cl.Context(properties=cl_properties, devices=cl_devices)
    return cl_context


if __name__ == "__main__":
    gl_context = get_gl_context("g" if len(sys.argv) < 2 else sys.argv[1])
    cl_context = get_cl_context(gl_context)
    from scipy.misc import lena;
    img = np.dstack([lena() / 256.] * 3).astype(np.float32); hei, wid = img.shape[:2]
    gl_img = Texture2D(img, mipmap=True, context=gl_context)
    cl_img = cl.GLTexture(cl_context, cl.mem_flags.READ_ONLY, gl.GL_TEXTURE_2D, 1, gl_img._id, 2)
    cl_queue = cl.CommandQueue(cl_context)
    cl_program = cl.Program(cl_context, cl_source).build()
    if True: # usable in loop
        cl_gl_data = [cl_img]
        cl.enqueue_acquire_gl_objects(cl_queue, cl_gl_data)
        cl_args = [np.uint32(wid), np.uint32(hei), cl_img]; assert 3 == len(cl_args)
        cl_program.run(cl_queue, (wid, hei), None, *cl_args)
        cl.enqueue_release_gl_objects(cl_queue, cl_gl_data)
        cl_queue.flush()
    cl_queue.finish()
    print "Finished."
