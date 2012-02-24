from numpy import array, sin, cos, pi
from numpy.random import random
from rawgl import gl

from glut import GlutWindow, main_loop, get_elapsed_time
from ShaderProgram import ShaderProgram
from Texture import RectangleTexture
from VertexArray import VertexArray

vertex_shader = """
#version 410 core

layout(location=0) in vec4 in_position;
layout(location=1) in vec4 in_color;
uniform mat4 modelview_matrix;
out vec4 ex_color;

void main() {
    gl_Position = modelview_matrix * in_position;
    ex_color = in_color;
}
"""

fragment_shader = """
#version 410 core
#extension GL_ARB_texture_rectangle : enable

in vec4 ex_color;
uniform float scaling;
uniform sampler2DRect texture;
layout(location=0) out vec4 out_color;

void main() {
    out_color = ex_color * scaling + texture2DRect(texture, gl_FragCoord.xy);
}
"""

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
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT) # TODO
    with shader:
        vao.draw()
    window.swap_buffers()

def timer():
    t = get_elapsed_time()
    shader.scaling = 0.5 + 0.5 * sin(2 * pi * t / 1.0)
    phi = 2 * pi * t / 4.0
    shader.modelview_matrix = array(((cos(phi), sin(phi), 0, 0), (-sin(phi), cos(phi), 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)))
    window.add_timer(40, timer)
    window.post_redisplay()

if __name__ == "__main__":
    window = GlutWindow(double=True, multisample=True)
    window.display_callback = display
    window.add_timer(40, timer)

    vao = VertexArray([vertices, colors], elements=indices)
    shader = ShaderProgram(vertex=vertex_shader, fragment=fragment_shader)
    shader.texture = RectangleTexture(random((300, 300, 4)).astype("float32"))

    main_loop()

