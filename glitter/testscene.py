import numpy
from rawgl import gl, glut

from Buffer import ArrayBuffer
from GlutWindow import GlutWindow
from Shader import FragmentShader, VertexShader
from ShaderProgram import ShaderProgram
from VertexArray import VertexArray

def reshape(w, h):
    gl.glViewport(0, 0, w, h)

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glDrawArrays(gl.GL_TRIANGLES, 0, 3)
    glut.glutSwapBuffers()
    glut.glutPostRedisplay()

window = GlutWindow(mode=glut.GLUT_DOUBLE|glut.GLUT_DEPTH|glut.GLUT_RGBA)
window.reshape_func = reshape
window.display_func = display

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

vertices = numpy.array(((-0.8, -0.8, 0.0, 1.0), (0.0, 0.8, 0.0, 1.0), (0.8, -0.8, 0.0, 1.0)), dtype=numpy.float32)
colors = numpy.array(((1.0, 0.0, 0.0, 1.0), (0.0, 1.0, 0.0, 1.0), (0.0, 0.0, 1.0, 1.0)), dtype=numpy.float32)

vao = VertexArray()
vao.bind()

vbo = ArrayBuffer(vertices)
vbo.bind()
vbo.use(0)

cbo = ArrayBuffer(colors)
cbo.bind()
cbo.use(1)

vertex_shader = VertexShader(vertex_shader_code)
fragment_shader = FragmentShader(fragment_shader_code)
shader = ShaderProgram([vertex_shader, fragment_shader])
shader.bind()

window()

