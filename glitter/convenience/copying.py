"""Tools for copying a texture to screen through a shader.

This is useful for GPGPU.

@author: Stephan Wenger
@date: 2012-03-06
"""

from glitter.arrays import VertexArray
from glitter.shaders import ShaderProgram
from glitter.convenience import Pipeline

vertex_code = """
#version 400 core

layout(location=0) in vec4 in_position;
out vec2 ex_texcoord;

void main() {
    gl_Position = in_position;
    ex_texcoord = (0.5 * in_position.xy + 0.5) * vec2(%(xscale)f, %(yscale)f);
}
"""
"""Vertex shader for copying a texture onto the screen."""

fragment_code_rectangle = """
#version 400 core
#extension GL_ARB_texture_rectangle : enable

uniform %(sampler_type)s image;
layout(location=0) out vec4 out_color;

void main() {
    out_color = texture(image, gl_FragCoord.xy) / %(maxval)f;
}
"""
"""Fragment shader for copying a rectangle texture onto the screen."""

fragment_code_2d = """
#version 400 core

in vec2 ex_texcoord;
uniform %(sampler_type)s image;
layout(location=0) out vec4 out_color;

void main() {
    out_color = texture(image, ex_texcoord) / %(maxval)f;
}
"""
"""Fragment shader for copying a 2D texture onto the screen."""

quad_vertices = ((-1.0, -1.0), (-1.0, 1.0), (1.0, 1.0), (1.0, -1.0))
"""Vertices of a fullscreen quad."""

quad_indices = ((0, 1, 2), (0, 2, 3))
"""Indices of a fullscreen quad."""

def get_fullscreen_quad(context=None):
    """Get a vertex array containing the vertices of a fullscreen quad.

    @param context: The context to create the program in, or C{None} for the current context.
    @type context: L{Context}
    @rtype: L{VertexArray}
    """
    return VertexArray(quad_vertices, elements=quad_indices, context=context)

def get_copy_program_rectangle(context=None, sampler_type="sampler2DRect", maxval=1.0, xscale=1.0, yscale=1.0):
    """Get a shader program for copying a rectangle texture onto the screen.

    @param context: The context to create the program in, or C{None} for the current context.
    @type context: L{Context}
    @rtype: L{ShaderProgram}
    """

    return ShaderProgram(vertex=vertex_code % locals(), fragment=fragment_code_rectangle % locals(), context=context)

def get_copy_program_2d(context=None, sampler_type="sampler2D", maxval=1.0, xscale=1.0, yscale=1.0):
    """Get a shader program for copying a 2D texture onto the screen.

    @param context: The context to create the program in, or C{None} for the current context.
    @type context: L{Context}
    @rtype: L{ShaderProgram}
    """

    return ShaderProgram(vertex=vertex_code % locals(), fragment=fragment_code_2d % locals(), context=context)

def get_copy_pipeline_rectangle(context=None, sampler_type="sampler2DRect", maxval=1.0, xscale=1.0, yscale=1.0, **kwargs):
    """Get a pipeline for copying a rectangle texture onto the screen.

    @param context: The context to create the program in, or C{None} for the current context.
    @type context: L{Context}
    @keyword image: The texture to display.
    @type image: L{RectangleTexture}
    @rtype: L{Pipeline}
    """
    
    return Pipeline(get_copy_program_rectangle(context, sampler_type, maxval, xscale, yscale),
            in_position=quad_vertices, elements=quad_indices, **kwargs)

def get_copy_pipeline_2d(context=None, sampler_type="sampler2D", maxval=1.0, xscale=1.0, yscale=1.0, **kwargs):
    """Get a pipeline for copying a 2D texture onto the screen.

    @param context: The context to create the program in, or C{None} for the current context.
    @type context: L{Context}
    @keyword image: The texture to display.
    @type image: L{Texture2D}
    @rtype: L{Pipeline}
    """

    return Pipeline(get_copy_program_2d(context, sampler_type, maxval, xscale, yscale),
            in_position=quad_vertices, elements=quad_indices, **kwargs)

__all__ = [
    "vertex_code",
    "fragment_code_rectangle",
    "fragment_code_2d",
    "quad_vertices",
    "quad_indices",
    "get_fullscreen_quad",
    "get_copy_program_rectangle",
    "get_copy_program_2d",
    "get_copy_pipeline_rectangle",
    "get_copy_pipeline_2d",
]

