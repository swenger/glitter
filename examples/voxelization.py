"""
import logging
logger = logging.getLogger("rawgl")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s: %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)
"""

import h5py

from glitter import Framebuffer, ShaderProgram, Texture2D, uint32, VertexArray, Reset
from glitter.contexts.glut import GlutWindow, main_loop

vertex_code = """
#version 410 core

layout(location=0) in vec4 in_position;
out vec4 ex_position;

void main() {
    gl_Position = ex_position = in_position;
}
"""

fragment_code = """
#version 410 core
#extension GL_EXT_gpu_shader4 : enable

in vec4 ex_position;
uniform float znear, zfar;
layout(location=0) out uvec4 fragmentColor; // TODO multiple targets

uvec4 border_voxelize(uint z, uint offset) {
    if (z >= (offset + 1u) * 128u) return uvec4(0u);
    if (z < offset * 128u) return uvec4(0u);
    z -= offset * 128u;
    return uvec4(
        z < 128u && z >= 96u ? 1u << (z - 96u) : 0u,
        z <  96u && z >= 64u ? 1u << (z - 64u) : 0u,
        z <  64u && z >= 32u ? 1u << (z - 32u) : 0u,
        z <  32u             ? 1u <<  z        : 0u
    );
}

uvec4 solid_voxelize(uint z, uint offset) {
    // switch on all bits >= z
    if (z >= (offset + 1u) * 128u) return uvec4(0u);
    if (z < offset * 128u) return uvec4(0xffffffffu);
    z -= offset * 128u;
    return uvec4(
        z < 128u ? 0xffffffffu << (z >= 96u ? z - 96u : 0u) : 0u,
        z <  96u ? 0xffffffffu << (z >= 64u ? z - 64u : 0u) : 0u,
        z <  64u ? 0xffffffffu << (z >= 32u ? z - 32u : 0u) : 0u,
        z <  32u ? 0xffffffffu <<             z             : 0u
    );
}

void main() {
    uint z = uint(round(128.0 * (ex_position.z - znear) / (zfar - znear)));
    fragmentColor = solid_voxelize(z, 0); // TODO multiple targets
}
"""

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
    out_color = vec4(bits == 0 ? 1.0 : 0.0, bits != 0 ? 1.0 : 0.0, 0.0, 1.0); // DEBUG
    // TODO bits is broken
}
"""

def display():
    window.clear()
    with copy_shader:
        fullscreen_quad.draw()
    window.swap_buffers()

def keyboard(key, x, y):
    if key == ord("+"):
        copy_shader.zslice = min(copy_shader.zslice + 1, 127)
    elif key == ord("-"):
        copy_shader.zslice = max(copy_shader.zslice - 1, 0)
    print copy_shader.zslice
    window.post_redisplay()

def voxelize(filename):
    shader = ShaderProgram(vertex=vertex_code, fragment=fragment_code)
    shader.znear = -1
    shader.zfar = 1

    volume = Texture2D(shape=(128, 128, 4), dtype=uint32) # TODO TextureArray2D, bind layer to FBO
    fbo = Framebuffer([volume])
    fbo.check()

    f = h5py.File(filename)
    vao = VertexArray([f["vertices"]], elements=f["indices"])
    f.close()

    with fbo:
        fbo.clear()
        with Reset(window, "logic_op_mode", window.logic_op_modes.XOR): # OR for border voxelization, XOR for solid voxelization
            with Reset(window, "color_logic_op", True):
                with shader:
                    vao.draw()

    f = h5py.File("/tmp/out.hdf5", "w")
    f["data"] = volume.data
    f.close()

    return volume

if __name__ == "__main__":
    window = GlutWindow(shape=(128, 128))
    window.keyboard_callback = keyboard
    window.display_callback = display

    volume = voxelize("/local/wenger/data/meshes/armadillo.hdf5")

    copy_shader = ShaderProgram(vertex=copy_vertex_shader, fragment=copy_fragment_shader)
    copy_shader.texture = volume
    copy_shader.zslice = 64
    fullscreen_quad = VertexArray([((-1.0, -1.0), (-1.0, 1.0), (1.0, 1.0), (1.0, -1.0))], ((0, 1, 2), (0, 2, 3)))

    main_loop()

