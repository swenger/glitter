#!/usr/bin/env python

#! This file is a literate Python program. You can compile the documentation
#! using mylit (http://pypi.python.org/pypi/mylit/).
## title = "glitter Example: Voxelization"
## stylesheet = "pygments_style.css"

# <h1><i>glitter</i> Example: Voxelization</h1>

# <h2>Summary</h2>

# This program will create an invisible OpenGL context to voxelize a mesh given
# as an <a href="www.hdfgroup.org/HDF5/">HDF5</a> data file. The resulting
# volume is written to a file.

#! TODO describe voxelization algorithm
#! TODO include spreadbits.py so the data can be viewed in the volume viewer

# <h2>Front matter</h2>

# <h3>Module docstring</h3>

# The module docstring is used as a description of this example in the
# generated documentation:
"""Voxelize a mesh.

@author: Stephan Wenger
@date: 2012-02-29
"""

# We can usually import classes and functions contained in <i>glitter</i>
# submodules directly from glitter:
from glitter import VertexArray, TextureArray2D, uint32, Framebuffer, State, ShaderProgram

# <h2>Shaders</h2>

# The vertex shader transforms the position as usual.
vertex_code = """
#version 400 core

layout(location=0) in vec4 in_position;
out vec4 ex_position;

void main() {
    gl_Position = ex_position = in_position;
}
"""

# The fragment code will perform the actual work. It will quantize each
# fragment into a depth layer, compute a bitmask corresponding to that depth,
# and write the bit mask into the color attachments. The number of color
# attachments is only known at runtime, which is why a <code>%d</code>
# placeholder will have to be filled in just before the shader is compiled.
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

# <h2>Voxelization</h2>

# The function <code>voxelize()</code> performs solid or boundary voxelization
# of a mesh into a volume of given size.
def voxelize(mesh, size, solid=True):
    """Voxelize a mesh into a cube of length C{size}.

    @param mesh: The mesh to voxelize.
    @type mesh: L{VertexArray}
    @param size: The length of the resulting cube. Should be a multiple of 128.
    @type size: C{int}
    @param solid: Whether to perform solid voxelization instead of boundary voxelization.
    @type solid: C{bool}

    @attention: The result of boundary voxelization is likely to have holes. To
    obtain a watertight volume, you can voxelize the volume from different
    directions and combine the results, or use the gradient of a solid volume.
    """

    # An array of 2D integer textures will hold the output volume encoded in
    # its bits:
    volume = TextureArray2D(shape=(size // 128, size, size, 4), dtype=uint32)

    # We create a framebuffer with all layers of the volume attached and
    # directly bind it:
    with Framebuffer([volume[i] for i in range(len(volume))]) as fbo:
        fbo.clear()
        # Depending on the voxelization mode, we set the logic op mode. We then
        # create and activate a shader program and draw the mesh.
        with State(logic_op_mode="XOR" if solid else "OR", color_logic_op=True):
            with ShaderProgram(vertex=vertex_code, fragment=fragment_code % len(volume), solid=solid):
                mesh.draw()

    # Finally, the texture array is returned. The client code can decide to
    # download the data or to process it further on the GPU.
    return volume

# <h2>Initialization and main loop</h2>

# Finally, if this program is being run from the command line, we set up all
# the previously mentioned objects and start rendering. The program will expect
# two command line parameters: the name of an HDF5 input file, and the name of
# an HDF5 output file. An optional third parameter specifies the size of the
# resulting volume.
if __name__ == "__main__":
    # We need to read a mesh filename from <code>sys.argv</code>, so import
    # <code>sys</code>.
    import sys

    # We assume the mesh is stored in a <a
    # href="http://www.hdfgroup.org/HDF5/">HDF5</a> file, so import <a
    # href="h5py.alfven.org"><code>h5py</code></a>.
    import h5py

    # We open the HDF5 file specified on the command line for reading, extract
    # the vertices and indices, and store them in a vertex array:
    with h5py.File(sys.argv[1]) as f:
        mesh = VertexArray(f["vertices"], elements=f["indices"])

    # Now the voxelization is performed and the result is returned as an array
    # of 2D integer textures.
    volume = voxelize(mesh, int(sys.argv[3]) if len(sys.argv) > 3 else 128)

    # Finally, we open the output file, download the data, and store it in a
    # dataset. The dataset can typically be compressed a lot, which is why we
    # enable LZF compression. However, this may take a long time, so you can
    # disable it if you are not short on disk space.
    with h5py.File(sys.argv[2], "w") as f:
        f.create_dataset("data", data=volume.data, compression="lzf")

    # Note how we did not need to create an OpenGL context explicitly. The
    # first object that needs an OpenGL context (in this case the
    # <code>VertexArray</code>) will create an invisible context as soon as it
    # is initialized. This is very convenient; on the other hand, it means that
    # if you create a context manually (e.g., because you need a visible
    # window), you have to initialize it before any other objects. Otherwise,
    # these objects may end up in the wrong context, and sharing data across
    # context is a problem of its own.

