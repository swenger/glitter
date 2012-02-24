import logging
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")
#import rawgl
#rawgl.DEBUG_MODE = True

from numpy import array, sin, cos, pi, eye
from numpy.random import random
from rawgl import gl

from dtypes import float32
from glut import GlutWindow, main_loop, get_elapsed_time
from Framebuffer import Framebuffer
from ShaderProgram import ShaderProgram
from Texture import RectangleTexture, Texture2D
from VertexArray import VertexArray

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

fragment_shader = """
#version 410 core
#extension GL_ARB_texture_rectangle : enable

in vec4 ex_color;
in vec2 texcoord;
uniform float scaling;
uniform sampler2D texture_0;
uniform sampler2DRect texture_1;
layout(location=0) out vec4 out_color;

void main() {
    out_color = vec4(0.0)
    //+ ex_color * scaling
    + texture2D(texture_0, texcoord)
    * texture2DRect(texture_1, gl_FragCoord.xy / 10.0)
    ;
}
"""

copy_vertex_shader = """
#version 410 core

layout(location=0) in vec4 in_position;

void main() {
    gl_Position = in_position;
}
"""

copy_fragment_shader = """
#version 410 core
#extension GL_ARB_texture_rectangle : enable

uniform sampler2DRect texture;
layout(location=0) out vec4 out_color;

void main() {
    out_color = texture2DRect(texture, gl_FragCoord.xy);
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

indices = array((
    (0,  1,  3), (0,  3,  2), ( 3,  1,  4), ( 3,  4,  2), # top
    (0,  5,  7), (0,  7,  6), ( 7,  5,  8), ( 7,  8,  6), # bottom
    (0,  9, 11), (0, 11, 10), (11,  9, 12), (11, 12, 10), # left
    (0, 13, 15), (0, 15, 14), (15, 13, 16), (15, 16, 14), # right
    ), dtype="uint8")

def display():
    logging.info("\nusing fbo")
    with fbo:
        fbo._context.draw_buffers = [0] # TODO set automatically in FBO
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT) # TODO
        with shader:
            vao.draw()

    logging.info("\nusing copy shader")
    with copy_shader:
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT) # TODO
        fullscreen_quad.draw()

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

    fbo = Framebuffer([RectangleTexture(shape=(300, 300, 3), dtype=float32)])
    vao = VertexArray([vertices, colors], elements=indices)
    shader = ShaderProgram(vertex=vertex_shader, fragment=fragment_shader)
    shader.texture_0 = Texture2D(random((30, 30, 4)).astype("float32"))
    shader.texture_0.min_filter = Texture2D.min_filters.NEAREST
    shader.texture_0.mag_filter = Texture2D.mag_filters.NEAREST
    shader.texture_1 = RectangleTexture(random((30, 30, 4)).astype("float32"))

    copy_shader = ShaderProgram(vertex=copy_vertex_shader, fragment=copy_fragment_shader)
    copy_shader.texture = fbo[0]
    fullscreen_quad = VertexArray([((-1.0, -1.0), (-1.0, 1.0), (1.0, 1.0), (1.0, -1.0))], array(((0, 1, 2), (0, 2, 3)), dtype="uint8"))

    timer()
    main_loop()

