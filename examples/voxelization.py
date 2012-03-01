#!/usr/bin/env python

import h5py

from glitter import Framebuffer, ShaderProgram, TextureArray2D, uint32, VertexArray, Reset, get_default_context

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
uniform bool solid;
layout(location=0) out uvec4 fragmentColor[%d];

uvec4 voxelize(uint z, uint offset, uint fill, uint base) {
    if (z >= (offset + 1u) * 128u) return uvec4(0u);
    if (z < offset * 128u) return uvec4(fill);
    z -= offset * 128u;
    return uvec4(
        z < 128u ? (z >= 96u ? base << (z - 96u) : fill) : 0u,
        z <  96u ? (z >= 64u ? base << (z - 64u) : fill) : 0u,
        z <  64u ? (z >= 32u ? base << (z - 32u) : fill) : 0u,
        z <  32u ?             base << (z -  0u)         : 0u
    );
}

void main() { // if solid, switch on all bits >= z; else, switch on bit == z
    uint z = uint(round(128.0 * float(fragmentColor.length()) * (ex_position.z - znear) / (zfar - znear)));
    for (int i = 0; i < fragmentColor.length(); ++i)
        fragmentColor[i] = voxelize(z, i, solid ? 0xffffffffu : 0u, solid ? 0xffffffffu : 1u);
}
"""

def voxelize(filename, size, solid=True):
    num_targets = size // 128

    shader = ShaderProgram(vertex=vertex_code, fragment=fragment_code % num_targets)
    shader.znear = -1
    shader.zfar = 1
    shader.solid = solid

    volume = TextureArray2D(shape=(num_targets, size, size, 4), dtype=uint32)
    fbo = Framebuffer([volume[i] for i in range(len(volume))])

    with h5py.File(filename) as f:
        vao = VertexArray([f["vertices"]], elements=f["indices"])

    with fbo:
        fbo.clear()
        context = get_default_context()
        with Reset(context, "logic_op_mode", context.logic_op_modes.XOR if solid else context.logic_op_modes.OR):
            with Reset(context, "color_logic_op", True):
                with shader:
                    vao.draw()

    return volume

if __name__ == "__main__":
    import sys

    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    size = int(sys.argv[3]) if len(sys.argv) > 3 else 128

    volume = voxelize(infilename, size)

    with h5py.File(outfilename, "w") as f:
        f.create_dataset("data", data=volume.data, compression="lzf")

