#!/usr/bin/env python

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
from glitter.contexts.glut import GlutWindow#, main_loop

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

def voxelize(filename, size, solid=True):
    # TODO set mode: solid or border, set number of textures
    shader = ShaderProgram(vertex=vertex_code, fragment=fragment_code)
    shader.znear = -1
    shader.zfar = 1

    volume = Texture2D(shape=(size, size, 4), dtype=uint32) # TODO TextureArray2D with size // 128 layers, bind layer to FBO
    fbo = Framebuffer([volume])
    fbo.check()

    with h5py.File(filename) as f:
        vao = VertexArray([f["vertices"]], elements=f["indices"])

    with fbo:
        fbo.clear()
        with Reset(window, "logic_op_mode", window.logic_op_modes.XOR if solid else window.logic_op_modes.OR):
            with Reset(window, "color_logic_op", True):
                with shader:
                    vao.draw()

    return volume

if __name__ == "__main__":
    import sys

    infilename = sys.argv[1] # "/local/wenger/data/meshes/armadillo.hdf5"
    outfilename = sys.argv[2] # "/tmp/out.hdf5"
    size = int(sys.argv[3]) if len(sys.argv) > 3 else 128

    window = GlutWindow(shape=(size, size), hide=True) # TODO Framebuffer should handle viewport setup

    volume = voxelize(infilename, size)

    with h5py.File(outfilename, "w") as f:
        f["data"] = volume.data

