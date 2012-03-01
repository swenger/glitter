#!/usr/bin/env python

from glitter import ShaderProgram, Texture2D, VertexArray
from glitter.contexts.glut import GlutWindow, main_loop

copy_vertex_shader = """
#version 410 core

layout(location=0) in vec4 in_position;
out vec2 ex_texcoord;

void main() {
    gl_Position = in_position;
    ex_texcoord = 0.5 + 0.5 * in_position.xy;
}
"""

copy_fragment_shader = """
#version 410 core

in vec2 ex_texcoord;
uniform usampler2D texture;
uniform uint zslice;
layout(location=0) out vec4 out_color;

void main() {
    uvec4 bits = texture2D(texture, ex_texcoord); // TODO array
    uint z = zslice % 128u;
    out_color = vec4(((
          z >= 96u ? bits.r & (1u << (z - 96u))
        : z >= 64u ? bits.g & (1u << (z - 64u))
        : z >= 32u ? bits.b & (1u << (z - 32u))
                   : bits.a & (1u <<  z       )
    ) != 0u) ? 1.0 : 0.0);
    // TODO bits is broken
    // out_color = vec4(bits == 0 ? 1.0 : 0.0, bits != 0 ? 1.0 : 0.0, 0.0, 1.0); // DEBUG
}
"""

def display():
    window.clear()
    with copy_shader:
        fullscreen_quad.draw()
    window.swap_buffers()

def keyboard(key, x, y):
    if key == ord("+"):
        copy_shader.zslice = min(copy_shader.zslice + 1, num_slices - 1)
    elif key == ord("-"):
        copy_shader.zslice = max(copy_shader.zslice - 1, 0)
    window.window_title = "slice %d/%d" % (copy_shader.zslice, num_slices)
    window.post_redisplay()

if __name__ == "__main__":
    import sys
    import h5py

    infilename = sys.argv[1]

    window = GlutWindow(shape=(128, 128), name="Volume Viewer")
    window.keyboard_callback = keyboard
    window.display_callback = display

    with h5py.File(infilename, "r") as f:
        volume = Texture2D(f["data"]) # TODO TextureArray2D
    num_slices = 128 # TODO volume.shape[0] * ...

    copy_shader = ShaderProgram(vertex=copy_vertex_shader, fragment=copy_fragment_shader)
    copy_shader.texture = volume
    copy_shader.zslice = 0
    fullscreen_quad = VertexArray([((-1.0, -1.0), (-1.0, 1.0), (1.0, 1.0), (1.0, -1.0))], ((0, 1, 2), (0, 2, 3)))

    main_loop()

