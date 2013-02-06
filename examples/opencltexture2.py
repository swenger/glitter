#!/usr/bin/env/python

"""Minimal example of OpenGL/CL interaction using textures.

@author: Kai Ruhl
@since 2013-02"""

import sys
import numpy as np
import pyopencl as cl

from glitter import Texture2D
from glitter.raw import gl


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
            cl_devices = [cl_platform.get_devices()[0]]  # Only one is allowed!
            cl_context = cl.Context(properties=cl_properties, devices=cl_devices)
    else: # ... or in stand-alone mode, CL context without GL?
        cl_platform = cl.get_platforms()[0]  # @UndefinedVariable
        cl_properties = [(cl.context_properties.PLATFORM, cl_platform)]
        cl_devices = [cl_platform.get_devices()[0]]  # Only one is allowed!
        cl_context = cl.Context(properties=cl_properties, devices=cl_devices)
    return cl_context


#if __name__ == "__main__":
gl_context = get_gl_context("q" if len(sys.argv) < 2 else sys.argv[1]) # fails with g, works with q
cl_context = get_cl_context(gl_context)
from scipy.misc import lena; img = np.dstack([lena() / 256.] * 3).astype(np.float32)
gl_img = Texture2D(img, mipmap=False, context=gl_context)
cl_img = cl.GLTexture(cl_context, cl.mem_flags.READ_ONLY, gl.GL_TEXTURE_2D, 0, gl_img._id, 2)
