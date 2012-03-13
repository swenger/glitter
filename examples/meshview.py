#!/usr/bin/env python

"""Simple mesh viewer.

@author: Stephan Wenger
@date: 2012-02-29
"""

from numpy import array, sin, cos, pi
from numpy.random import random

from glitter import VertexArray, State, get_default_program
from glitter.contexts.glut import GlutWindow, main_loop, get_elapsed_time

def display():
    """Display function."""

    window.clear()
    with shader:
        with State(depth_test=True):
            vao.draw()
    window.swap_buffers()

def timer():
    phi = 2 * pi * get_elapsed_time() / 20.0
    shader.modelview_matrix = array(((cos(phi), 0, sin(phi), 0), (0, 1, 0, 0), (-sin(phi), 0, cos(phi), 0), (0, 0, 0, 1)))
    window.add_timer(10, timer)
    window.post_redisplay()

if __name__ == "__main__":
    import sys, h5py

    window = GlutWindow(double=True, multisample=True)
    window.display_callback = display
    shader = get_default_program()

    with h5py.File(sys.argv[1], "r") as f:
        vertices = f["vertices"]
        colors = f.get("colors", None)
        elements = f.get("indices", None)
        if colors is None:
            colors = random((len(vertices), 3))[:, None, :][:, [0] * vertices.shape[1], :]
        vao = VertexArray([vertices, colors], elements=elements)

    timer()
    main_loop()

