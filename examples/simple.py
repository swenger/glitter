#!/usr/bin/env python

from numpy import pi, array, cos, sin

from glitter import VertexArray, get_default_program
from glitter.contexts.glut import GlutWindow, main_loop, get_elapsed_time

vertices = (
    ( 0.0,  0.0, 0.0, 1.0), # center
    (-0.2,  0.8, 0.0, 1.0), ( 0.2,  0.8, 0.0, 1.0), ( 0.0,  0.8, 0.0, 1.0), ( 0.0,  1.0, 0.0, 1.0), # top
    (-0.2, -0.8, 0.0, 1.0), ( 0.2, -0.8, 0.0, 1.0), ( 0.0, -0.8, 0.0, 1.0), ( 0.0, -1.0, 0.0, 1.0), # bottom
    (-0.8, -0.2, 0.0, 1.0), (-0.8,  0.2, 0.0, 1.0), (-0.8,  0.0, 0.0, 1.0), (-1.0,  0.0, 0.0, 1.0), # left
    ( 0.8, -0.2, 0.0, 1.0), ( 0.8,  0.2, 0.0, 1.0), ( 0.8,  0.0, 0.0, 1.0), ( 1.0,  0.0, 0.0, 1.0), # right
    )

colors = (
    (1.0, 1.0, 1.0, 1.0), # center
    (0.0, 1.0, 0.0, 1.0), (0.0, 0.0, 1.0, 1.0), (0.0, 1.0, 1.0, 1.0), (1.0, 0.0, 0.0, 1.0), # top
    (0.0, 0.0, 1.0, 1.0), (0.0, 1.0, 0.0, 1.0), (0.0, 1.0, 1.0, 1.0), (1.0, 0.0, 0.0, 1.0), # bottom
    (0.0, 1.0, 0.0, 1.0), (0.0, 0.0, 1.0, 1.0), (0.0, 1.0, 1.0, 1.0), (1.0, 0.0, 0.0, 1.0), # left
    (0.0, 0.0, 1.0, 1.0), (0.0, 1.0, 0.0, 1.0), (0.0, 1.0, 1.0, 1.0), (1.0, 0.0, 0.0, 1.0), # right
    )

indices = (
    (0,  1,  3), (0,  3,  2), ( 3,  1,  4), ( 3,  4,  2), # top
    (0,  5,  7), (0,  7,  6), ( 7,  5,  8), ( 7,  8,  6), # bottom
    (0,  9, 11), (0, 11, 10), (11,  9, 12), (11, 12, 10), # left
    (0, 13, 15), (0, 15, 14), (15, 13, 16), (15, 16, 14), # right
    )

def display():
    window.clear()
    with shader:
        vao.draw()
    window.swap_buffers()

def timer():
    t = get_elapsed_time()
    phi = 2 * pi * t / 4.0
    shader.modelview_matrix = array(((cos(phi), sin(phi), 0, 0), (-sin(phi), cos(phi), 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)))
    window.add_timer(10, timer)
    window.post_redisplay()

if __name__ == "__main__":
    window = GlutWindow(double=True, multisample=True) #: The main window.
    window.display_callback = display
    shader = get_default_program()
    vao = VertexArray([vertices, colors], elements=indices)
    timer()
    main_loop()

