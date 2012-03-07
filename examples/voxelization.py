#!/usr/bin/env python

"""Voxelize a mesh.

@author: Stephan Wenger
@date: 2012-02-29
"""

from glitter import VertexArray, TextureArray2D, uint32, Framebuffer, State, ShaderProgram

vertex_code = """
#version 400 core

layout(location=0) in vec4 in_position;
out vec4 ex_position;

void main() {
    gl_Position = ex_position = in_position;
}
"""
"""Vertex shader for solid or boundary voxelization."""

fragment_code = """
#version 400 core

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
"""Fragment shader for solid or boundary voxelization."""

def voxelize(mesh, size, solid=True):
    """Voxelize a mesh into a cube of length C{size}.

    @param mesh: The mesh to voxelize.
    @type mesh: L{VertexArray}
    @param size: The length of the resulting cube.
    @type size: C{int}
    @param solid: Whether to perform solid voxelization instead of boundary voxelization.
    @type solid: C{bool}

    @attention: The result of boundary voxelization is likely to have holes. To
    obtain a watertight volume, you can voxelize the volume from different
    directions and combine the results, or use the gradient of a solid volume.
    """

    volume = TextureArray2D(shape=(size // 128, size, size, 4), dtype=uint32)
    with Framebuffer([volume[i] for i in range(len(volume))]) as fbo:
        fbo.clear()
        with State(logic_op_mode="XOR" if solid else "OR", color_logic_op=True):
            with ShaderProgram(vertex=vertex_code, fragment=fragment_code % len(volume), solid=solid):
                mesh.draw()
    return volume

if __name__ == "__main__":
    import sys, h5py
    with h5py.File(sys.argv[1]) as f:
        mesh = VertexArray([f["vertices"]], elements=f["indices"])
    volume = voxelize(mesh, int(sys.argv[3]) if len(sys.argv) > 3 else 128)
    with h5py.File(sys.argv[2], "w") as f:
        f.create_dataset("data", data=volume.data, compression="lzf")

