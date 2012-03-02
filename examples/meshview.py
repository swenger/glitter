#!/usr/bin/env python

"""Simple mesh viewer.

@author: Stephan Wenger
@date: 2012-02-29
"""

# Import math utilities from numpy.
from numpy import array, sin, cos, pi

# Import glitter; this imports rawgl.
from glitter import ShaderProgram, VertexArray, State
from glitter.contexts.glut import GlutWindow, main_loop, get_elapsed_time

vertex_shader = """
#version 410 core

layout(location=0) in vec4 in_position;
uniform mat4 modelview_matrix;
out vec4 ex_color;

void main() {
    gl_Position = modelview_matrix * in_position;
    ex_color = 0.5 + 0.5 * in_position;
}
"""
"""Vertex shader for rendering animated geometry."""

fragment_shader = """
#version 410 core

in vec4 ex_color;
layout(location=0) out vec4 out_color;

void main() {
    out_color = ex_color;
}
"""
"""Fragment shader for rendering animated geometry."""

def display():
    """Display function."""

    window.clear()
    with shader:
        with State(depth_test=True):
            vao.draw()
    window.swap_buffers()

def keyboard(key, x, y):
    """Keyboard handler.

    Any key press will cause the program to exit cleanly.
    """

    raise SystemExit()

def timer():
    """Timer callback.

    Animates the modelview matrix, uploads it to the shader and causes a screen redraw.
    """

    # Animate the modelview matrix and upload it to the shader.
    t = get_elapsed_time()
    phi = 2 * pi * t / 4.0
    shader.modelview_matrix = array(((cos(phi), 0, sin(phi), 0), (0, 1, 0, 0), (-sin(phi), 0, cos(phi), 0), (0, 0, 0, 1)))

    # Schedule the next timer event.
    window.add_timer(10, timer)

    # Cause a screen redraw.
    window.post_redisplay()

if __name__ == "__main__":
    import sys, h5py

    # Create a window; this creates an OpenGL context.
    window = GlutWindow(double=True, multisample=True) #: The main window.
    window.display_callback = display
    window.keyboard_callback = keyboard

    # Create objects that are automatically placed inside the current context.
    with h5py.File(sys.argv[1], "r") as f:
        vao = VertexArray([f["vertices"]], elements=f["indices"] if "indices" in f else None) #: The vertex array to hold the geometry.
    shader = ShaderProgram(vertex=vertex_shader, fragment=fragment_shader) #: The shader program for rendering the geometry.

    # Call the timer once; it will trigger the subsequent calls itself.
    timer()

    # Enter the GLUT main loop.
    main_loop()

