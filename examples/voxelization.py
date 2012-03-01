#!/usr/bin/env python

from glitter import VertexArray, TextureArray2D, uint32, Framebuffer, Reset, current_context, ShaderProgram

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
    uint z = uint(round(128.0 * float(fragmentColor.length()) * 0.5 * (ex_position.z + 1.0)));
    for (int i = 0; i < fragmentColor.length(); ++i)
        fragmentColor[i] = voxelize(z, i, solid ? 0xffffffffu : 0u, solid ? 0xffffffffu : 1u);
}
"""

def voxelize(mesh, size, solid=True):
    volume = TextureArray2D(shape=(size // 128, size, size, 4), dtype=uint32)
    with Framebuffer([volume[i] for i in range(len(volume))]) as fbo:
        fbo.clear()
        with Reset(current_context, "logic_op_mode", current_context.logic_op_modes.XOR if solid else current_context.logic_op_modes.OR):
            with Reset(current_context, "color_logic_op", True):
                with ShaderProgram(vertex=vertex_code, fragment=fragment_code % len(volume), variables=dict(solid=solid)):
                    mesh.draw()
    return volume

if __name__ == "__main__":
    import sys, h5py
    with h5py.File(sys.argv[1]) as f:
        mesh = VertexArray([f["vertices"]], elements=f["indices"])
    volume = voxelize(mesh, int(sys.argv[3]) if len(sys.argv) > 3 else 128)
    with h5py.File(sys.argv[2], "w") as f:
        f.create_dataset("data", data=volume.data, compression="lzf")

