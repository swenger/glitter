import numpy
from rawgl import gl, glut

from Buffer import ArrayBuffer, ElementArrayBuffer
from GlutWindow import GlutWindow
from Shader import FragmentShader, VertexShader
from ShaderProgram import ShaderProgram
from VertexArray import VertexArray

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    with shader:
        vao.draw()
    glut.glutSwapBuffers()
    glut.glutPostRedisplay()

vertex_shader_code = """
#version 400

layout(location=0) in vec4 in_position;
layout(location=1) in vec4 in_color;
out vec4 ex_color;

void main() {
    gl_Position = in_position;
    ex_color = in_color;
}
"""

fragment_shader_code = """
#version 400

in vec4 ex_color;
out vec4 out_color;

void main() {
    out_color = ex_color;
}
"""

vertices = numpy.array((
    ((0.0, 0.0, 0.0, 1.0), (1.0, 1.0, 1.0, 1.0)),
    # Top
    ((-0.2, 0.8, 0.0, 1.0), (0.0, 1.0, 0.0, 1.0)),
    ((0.2, 0.8, 0.0, 1.0), (0.0, 0.0, 1.0, 1.0)),
    ((0.0, 0.8, 0.0, 1.0), (0.0, 1.0, 1.0, 1.0)),
    ((0.0, 1.0, 0.0, 1.0), (1.0, 0.0, 0.0, 1.0)),
    # Bottom
    ((-0.2, -0.8, 0.0, 1.0), (0.0, 0.0, 1.0, 1.0)),
    ((0.2, -0.8, 0.0, 1.0), (0.0, 1.0, 0.0, 1.0)),
    ((0.0, -0.8, 0.0, 1.0), (0.0, 1.0, 1.0, 1.0)),
    ((0.0, -1.0, 0.0, 1.0), (1.0, 0.0, 0.0, 1.0)),
    # Left
    ((-0.8, -0.2, 0.0, 1.0), (0.0, 1.0, 0.0, 1.0)),
    ((-0.8, 0.2, 0.0, 1.0), (0.0, 0.0, 1.0, 1.0)),
    ((-0.8, 0.0, 0.0, 1.0), (0.0, 1.0, 1.0, 1.0)),
    ((-1.0, 0.0, 0.0, 1.0), (1.0, 0.0, 0.0, 1.0)),
    # Right
    ((0.8, -0.2, 0.0, 1.0), (0.0, 0.0, 1.0, 1.0)),
    ((0.8, 0.2, 0.0, 1.0), (0.0, 1.0, 0.0, 1.0)),
    ((0.8, 0.0, 0.0, 1.0), (0.0, 1.0, 1.0, 1.0)),
    ((1.0, 0.0, 0.0, 1.0), (1.0, 0.0, 0.0, 1.0)),
    ), dtype=numpy.float32)

indices = numpy.array((
    # Top
    (0, 1, 3),
    (0, 3, 2),
    (3, 1, 4),
    (3, 4, 2),
    # Bottom
    (0, 5, 7),
    (0, 7, 6),
    (7, 5, 8),
    (7, 8, 6),
    # Left
    (0, 9, 11),
    (0, 11, 10),
    (11, 9, 12),
    (11, 12, 10),
    # Right
    (0, 13, 15),
    (0, 15, 14),
    (15, 13, 16),
    (15, 16, 14),
    ), dtype=numpy.uint8)

window = GlutWindow(mode=glut.GLUT_DOUBLE|glut.GLUT_DEPTH|glut.GLUT_RGBA)
window.display_func = display

vao = VertexArray() # TODO vao = VertexArray([(-0.8, ...)]) should work
vao[0] = ArrayBuffer(vertices[:, 0, :])
vao[1] = ArrayBuffer(vertices[:, 1, :])
vao.elements = ElementArrayBuffer(indices)

vertex_shader = VertexShader(vertex_shader_code)
fragment_shader = FragmentShader(fragment_shader_code)
shader = ShaderProgram([vertex_shader, fragment_shader])

window()

