"""Shader program emulating the traditional OpenGL default pipeline.

@author: Stephan Wenger
@date: 2012-03-06
"""

from glitter.shaders import ShaderProgram

vertex_code = """
#version 400 core

#define MODELVIEW 1
#define COLOR 1

layout(location=0) in vec4 in_position;
#if COLOR
layout(location=1) in vec4 in_color;
#endif
#if MODELVIEW
uniform mat4 modelview_matrix;
#endif
out vec4 ex_color;

void main() {
    #if MODELVIEW
    gl_Position = modelview_matrix * in_position;
    #else
    gl_Position = in_position;
    #endif
    #if COLOR
    ex_color = in_color;
    #else
    ex_color = vec4(1.0);
    #endif
}
"""
"""Default vertex shader."""

fragment_code = """
#version 400 core

in vec4 ex_color;
layout(location=0) out vec4 out_color;

void main() {
    out_color = ex_color;
}
"""
"""Default fragment shader."""

def get_default_program(modelview=True, color=True, context=None):
    """Get a shader program emulating the default pipeline.

    The program has two inputs, C{in_position} and (optionally) C{in_color};
    one output, C{out_color}; and (optionally) one uniform variable,
    C{modelview_matrix}.

    @param modelview: Whether to use the modelview matrix.
    @type modelview: C{bool}
    @param color: Whether to use colors.
    @type color: C{bool}
    @param context: The context to create the program in, or C{None} for the current context.
    @type context: L{Context}
    @rtype: L{ShaderProgram}
    """

    vertex = vertex_code
    if not modelview:
        vertex = vertex.replace("#define MODELVIEW 1", "#define MODELVIEW 0")
    if not color:
        vertex = vertex.replace("#define COLOR 1", "#define COLOR 0")
    return ShaderProgram(vertex=vertex, fragment=fragment_code, context=context)

__all__ = ["vertex_code", "fragment_code", "get_default_program"]

