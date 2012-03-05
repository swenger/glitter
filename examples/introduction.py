#!/usr/bin/env python

"""Basic example using L{VertexArray}s, L{ShaderProgram}s, L{Framebuffer}s, L{Texture}s and logging.

@author: Stephan Wenger
@date: 2012-02-29
"""

# Setup logging before importing rawgl.
import logging
logger = logging.getLogger("rawgl")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s: %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)

# Import math utilities from numpy.
from numpy import array, sin, cos, pi
from numpy.random import random

# Import glitter; this imports rawgl.
from glitter import ShaderProgram, RectangleTexture, Texture2D, Pipeline
from glitter.contexts.glut import GlutWindow, main_loop, get_elapsed_time

vertex_shader = """
#version 410 core

layout(location=0) in vec4 in_position;
layout(location=1) in vec4 in_color;
uniform mat4 modelview_matrix;
out vec4 ex_color;
out vec2 texcoord;

void main() {
    gl_Position = modelview_matrix * in_position;
    ex_color = in_color;
    texcoord = in_position.xy * 0.5 + 0.5;
}
"""
"""Vertex shader for rendering animated geometry."""

fragment_shader = """
#version 410 core
#extension GL_ARB_texture_rectangle : enable

in vec4 ex_color;
in vec2 texcoord;
uniform sampler2D texture_0;
uniform sampler2DRect texture_1;
layout(location=0) out vec4 out_color;

void main() {
    out_color = 0.5 * ex_color
    + texture2D(texture_0, texcoord)
    * texture2DRect(texture_1, gl_FragCoord.xy / 10.0)
    ;
}
"""
"""Fragment shader for rendering animated geometry."""

copy_vertex_shader = """
#version 410 core

layout(location=0) in vec4 in_position;

void main() {
    gl_Position = in_position;
}
"""
"""Vertex shader for copying a texture onto the screen."""

copy_fragment_shader = """
#version 410 core
#extension GL_ARB_texture_rectangle : enable

uniform sampler2DRect texture;
layout(location=0) out vec4 out_color;

void main() {
    out_color = texture2DRect(texture, gl_FragCoord.xy);
}
"""
"""Fragment shader for copying a texture onto the screen."""

vertices = (
    ( 0.0,  0.0, 0.0, 1.0), # center
    (-0.2,  0.8, 0.0, 1.0), ( 0.2,  0.8, 0.0, 1.0), ( 0.0,  0.8, 0.0, 1.0), ( 0.0,  1.0, 0.0, 1.0), # top
    (-0.2, -0.8, 0.0, 1.0), ( 0.2, -0.8, 0.0, 1.0), ( 0.0, -0.8, 0.0, 1.0), ( 0.0, -1.0, 0.0, 1.0), # bottom
    (-0.8, -0.2, 0.0, 1.0), (-0.8,  0.2, 0.0, 1.0), (-0.8,  0.0, 0.0, 1.0), (-1.0,  0.0, 0.0, 1.0), # left
    ( 0.8, -0.2, 0.0, 1.0), ( 0.8,  0.2, 0.0, 1.0), ( 0.8,  0.0, 0.0, 1.0), ( 1.0,  0.0, 0.0, 1.0), # right
    )
"""Vertices for the animated geometry."""

colors = (
    (1.0, 1.0, 1.0, 1.0), # center
    (0.0, 1.0, 0.0, 1.0), (0.0, 0.0, 1.0, 1.0), (0.0, 1.0, 1.0, 1.0), (1.0, 0.0, 0.0, 1.0), # top
    (0.0, 0.0, 1.0, 1.0), (0.0, 1.0, 0.0, 1.0), (0.0, 1.0, 1.0, 1.0), (1.0, 0.0, 0.0, 1.0), # bottom
    (0.0, 1.0, 0.0, 1.0), (0.0, 0.0, 1.0, 1.0), (0.0, 1.0, 1.0, 1.0), (1.0, 0.0, 0.0, 1.0), # left
    (0.0, 0.0, 1.0, 1.0), (0.0, 1.0, 0.0, 1.0), (0.0, 1.0, 1.0, 1.0), (1.0, 0.0, 0.0, 1.0), # right
    )
"""Colors for the animated geometry."""

indices = (
    (0,  1,  3), (0,  3,  2), ( 3,  1,  4), ( 3,  4,  2), # top
    (0,  5,  7), (0,  7,  6), ( 7,  5,  8), ( 7,  8,  6), # bottom
    (0,  9, 11), (0, 11, 10), (11,  9, 12), (11, 12, 10), # left
    (0, 13, 15), (0, 15, 14), (15, 13, 16), (15, 16, 14), # right
    )
"""Vertex indices for the animated geometry."""

def display():
    """Display function.

    Renders the geometry into a framebuffer, then copies the texture to the screen.

    During the first call, all OpenGL commands will be logged to the console.
    """

    logger.info("enter display()")

    # Render the geometry to a texture.
    render_pipeline.clear()
    render_pipeline.draw()

    # Display the texture.
    window.clear() # TODO redirect clear() call to default FBO
    copy_pipeline.draw()
    window.swap_buffers()

    logger.info("leave display()")

    # Disable logging for all subsequent calls.
    logger.disabled = True

def keyboard(key, x, y):
    """Keyboard handler.

    Any key press will cause the program to exit cleanly.
    """

    raise SystemExit

def timer():
    """Timer callback.

    Animates the modelview matrix, uploads it to the shader and causes a screen redraw.
    """

    # Animate the modelview matrix and upload it to the shader.
    t = get_elapsed_time()
    phi = 2 * pi * t / 4.0
    shader.modelview_matrix = array(((cos(phi), sin(phi), 0, 0), (-sin(phi), cos(phi), 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)))

    # Schedule the next timer event.
    window.add_timer(10, timer)

    # Cause a screen redraw.
    window.post_redisplay()

if __name__ == "__main__":
    # Disable logging during setup.
    logger.disabled = True

    # Create a window; this creates an OpenGL context.
    window = GlutWindow(double=True, multisample=True) #: The main window.
    window.display_callback = display
    window.keyboard_callback = keyboard

    # Create objects that are automatically placed inside the current context.
    shader = ShaderProgram(vertex=vertex_shader, fragment=fragment_shader) #: The shader program for rendering the geometry.
    render_pipeline = Pipeline(shader, indices, in_position=vertices, in_color=colors, out_color=RectangleTexture(shape=(300, 300, 3)))
    copy_shader = ShaderProgram(vertex=copy_vertex_shader, fragment=copy_fragment_shader) #: The shader program for copying a texture to screen.
    quad_vertices = ((-1.0, -1.0), (-1.0, 1.0), (1.0, 1.0), (1.0, -1.0))
    quad_indices = ((0, 1, 2), (0, 2, 3))
    copy_pipeline = Pipeline(copy_shader, in_position=quad_vertices, elements=quad_indices, no_framebuffer=True)

    # Set uniform variables on shader programs.
    shader.texture_0 = Texture2D(random((30, 30, 4)))
    shader.texture_0.min_filter = Texture2D.min_filters.NEAREST
    shader.texture_0.mag_filter = Texture2D.mag_filters.NEAREST
    shader.texture_1 = RectangleTexture(random((30, 30, 4)))
    copy_shader.texture = render_pipeline.out_color

    # Call the timer once; it will trigger the subsequent calls itself.
    timer()

    # Enable logging of OpenGL commands.
    logger.disabled = False

    # Enter the GLUT main loop.
    main_loop()

