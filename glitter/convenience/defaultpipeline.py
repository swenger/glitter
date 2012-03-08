"""Shader program emulating the traditional OpenGL default pipeline.

@author: Stephan Wenger
@date: 2012-03-06
"""

from glitter.shaders import ShaderProgram

vertex_code = """
#version 400 core

layout(location=0) in vec4 in_position;
layout(location=1) in vec4 in_color;
uniform mat4 modelview_matrix;
out vec4 ex_color;

void main() {
    gl_Position = modelview_matrix * in_position;
    ex_color = in_color;
}
"""
"""Default vertex shader with vertex colors."""

fragment_code = """
#version 400 core

in vec4 ex_color;
layout(location=0) out vec4 out_color;

void main() {
    out_color = ex_color;
}
"""
"""Default fragment shader with vertex colors."""

def get_default_program(context=None):
    """Get a shader program emulating the default pipeline.

    The program has two inputs, C{in_position} and C{in_color}, and one output,
    C{out_color}.

    @param context: The context to create the program in, or C{None} for the current context.
    @type context: L{Context}
    @rtype: L{ShaderProgram}
    """
    return ShaderProgram(vertex=vertex_code, fragment=fragment_code, context=context)

__all__ = ["vertex_code", "fragment_code", "get_default_program"]

