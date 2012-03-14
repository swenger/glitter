#!/usr/bin/env python

"""Simple example displaying a rotating quad.

@author: Stephan Wenger
@date: 2012-02-29
"""

from math import cos, sin
from glitter import VertexArray, get_default_program
from glitter.contexts.glut import GlutWindow, main_loop, get_elapsed_time

vertices = ((0, 0, 0), (-1, 1, 0), (1, 1, 0), (1, -1, 0), (-1, -1, 0))
colors = ((1, 1, 1), (0, 1, 0), (0, 0, 1), (0, 1, 1), (1, 0, 0))
indices = ((0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 1))

def display():
    window.clear()
    vao.draw()
    window.swap_buffers()

def timer():
    phi = get_elapsed_time()
    shader.modelview_matrix = ((cos(phi), sin(phi), 0, 0), (-sin(phi), cos(phi), 0, 0), (0, 0, 1, 0), (0, 0, 0, 2))
    window.add_timer(10, timer)
    window.post_redisplay()

if __name__ == "__main__":
    window = GlutWindow(double=True, multisample=True)
    window.display_callback = display
    shader = get_default_program()
    vao = VertexArray([vertices, colors], elements=indices)
    timer()
    with shader:
        main_loop()

