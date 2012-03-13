#!/usr/bin/env python

"""Viewer for a random point cloud.

@author: Stephan Wenger
@date: 2012-03-13
"""

from numpy import array, sin, cos, pi
from numpy.random import randn

from glitter import VertexArray, State, get_default_program
from glitter.contexts.glut import GlutWindow, main_loop, get_elapsed_time

def display():
    window.clear()
    vao.draw()
    window.swap_buffers()

def timer():
    phi = 2 * pi * get_elapsed_time() / 20.0
    shader.modelview_matrix = array(((cos(phi), 0, sin(phi), 0), (0, 1, 0, 0), (-sin(phi), 0, cos(phi), 0), (0, 0, 0, 5)))
    window.add_timer(10, timer)
    window.post_redisplay()

if __name__ == "__main__":
    n_points = 100000
    window = GlutWindow(double=True, multisample=True)
    window.display_callback = display
    shader = get_default_program()
    vao = VertexArray([randn(n_points, 3), randn(n_points, 3)])
    timer()
    with shader:
        with State(depth_test=True, point_size=3):
            main_loop()

