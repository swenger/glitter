#!/usr/bin/env python

#! This file is a literate Python program. You can compile the documentation
#! using mylit (http://pypi.python.org/pypi/mylit/).
## title = "glitter Example: Volume Renderer"
## stylesheet = "pygments_style.css"

# <h1><i>glitter</i> Example: Volume Renderer</h1>

# <h2>Summary</h2>

# This program will create an invisible OpenGL context to render a volume given
# as an <a href="www.hdfgroup.org/HDF5/">HDF5</a> data file to images that are
# written to files.

# We will use a very simple algorithm for volume rendering. First, the back
# face of the bounding box of the volume will be rendered into a texture using
# front face culling. The texture coordinates (or positions) of the fragments
# are stored in the texture. Then, in a second pass, the front face of the
# bounding box is rendered using back face culling. The shader reads the
# texture coordinates of the previous step from the texture, so that it now
# knows about both the viewing ray entry point to the bounding box (from the
# current texture coordinates) as well as the ray exit point (from the texture
# coordinates stored in the texture). The shader then uniformly samples a 3D
# texture along the line between these points and sums up the intensities. This
# is a valid image formation model for purely emissive volumes. To simulate an
# absorbing volume illuminated uniformly from the back, an exponential
# transform can optionally be applied to the final pixel intensities.

# <h2>Front matter</h2>

# <h3>Module docstring</h3>

# The module docstring is used as a description of this example in the
# generated documentation:
"""Volume renderer that creates a set of image files from different perspectives.

@author: Stephan Wenger
@date: 2012-03-07
"""

# <h3>Imports</h3>

# We will use <a
# href="http://docs.python.org/library/itertools.html">itertools</a> to create
# the vertices of a cube:
import itertools

# <a href="http://numpy.scipy.org/">numpy</a> is used for array operations:
import numpy

# We can usually import classes and functions contained in <i>glitter</i>
# submodules directly from glitter:
from glitter import Framebuffer, ShaderProgram, RectangleTexture, VertexArray, float32, State, Texture3D

# <h2>Shaders</h2>

# The vertex shader transforms the position as usual; additionally, it stores
# the unmodified vertex coordinates for use in the fragment shader:
vertex_code = """
#version 400 core

layout(location=0) in vec4 in_position;
uniform mat4 modelview_matrix;
out vec4 ex_front;

void main() {
	ex_front = in_position;
	gl_Position = modelview_matrix * 2.0 * (in_position - 0.5) * vec4(1.0, 1.0, 0.5, 1.0);
}
"""

# We need to different fragment shaders: one for the back faces, and one for
# the front faces. The shader for the back faces simply stores the
# untransformed position in the color output:
back_fragment_code = """
#version 400 core
#extension GL_ARB_texture_rectangle : enable

in vec4 ex_front;
layout(location=0) out vec4 out_color;

void main() {
    out_color = ex_front;
}
"""

# The fragment shader for the front faces performs the actual integration along
# the viewing ray:
front_fragment_code = """
#version 400 core
#extension GL_ARB_texture_rectangle : enable

#define STEP_SIZE 0.001
#define MAX_LENGTH sqrt(3.0)

in vec4 ex_front;
uniform sampler2DRect back;
uniform sampler3D volume;
uniform float intensity_scale;
uniform bool absorption;
layout(location=0) out vec4 out_color;

void main() {
	vec3 p0 = texture(back, gl_FragCoord.st).xyz;
	vec3 p1 = ex_front.xyz;
	vec4 intensity = vec4(0.0);

	vec3 d = p1 - p0;
	float l = length(d);
	if (l < MAX_LENGTH) {
		vec3 s = d * STEP_SIZE / l;
		vec3 pos = p0 + 0.5 * s;

		for (float f = 0.5 * STEP_SIZE; f < l; f += STEP_SIZE) {
			intensity += texture(volume, pos);
			pos += s;
		}
	}
	
    out_color = absorption ? exp(-intensity_scale * intensity) : intensity_scale * intensity;
}
"""

# <h2>Vertex arrays</h2>

# Here we define the faces of a cube that will serve as a bounding box to the
# volume:
cube_vertices = tuple(itertools.product((0.0, 1.0), (0.0, 1.0), (0.0, 1.0)))
cube_indices = ((0, 1, 3), (0, 2, 6), (0, 3, 2), (0, 6, 4), (3, 1, 5), (3, 5, 7),
        (4, 1, 0), (4, 5, 1), (5, 4, 6), (5, 6, 7), (7, 2, 3), (7, 6, 2))

# <h2>Volume renderer</h2>

# The <code>VolumeRenderer</code> class performs the actual volume rendering:
class VolumeRenderer(object):
    # Some default values for instance variables can be declared as class
    # variables (these values are all immutable, so no problem here):
    modelview_matrix = tuple(map(tuple, numpy.eye(4)))
    intensity_scale = 1.0
    absorption = False

    # <h3>Initialization</h3>
    def __init__(self, volume, **kwargs):
        assert isinstance(volume, Texture3D), "volume must be a 3D texture"

        # We need a vertex array to hold the faces of the cube:
        self.vao = VertexArray(cube_vertices, elements=cube_indices)

        # For rendering the back faces, we create a shader program and a
        # framebuffer with an attached texture:
        self.back_shader = ShaderProgram(vertex=vertex_code, fragment=back_fragment_code)
        self.back_fbo = Framebuffer(RectangleTexture(shape=volume.shape[:2] + (4,), dtype=float32))

        # For the front faces, we do the same. Additionally, the shader
        # receives the texture containing the back face coordinates in a
        # uniform variable <code>back</code>, and the 3D texture containing the
        # volumetric data in a uniform variable <code>volume</code>.
        self.front_shader = ShaderProgram(vertex=vertex_code, fragment=front_fragment_code, back=self.back_fbo[0], volume=volume)
        self.front_fbo = Framebuffer(RectangleTexture(shape=volume.shape[:2] + (4,), dtype=float32))

        # All other parameters are simply set as attributes (this might be
        # <code>modelview_matrix</code>, <code>intensity_scale</code>, or
        # <code>absorption</code>).
        for key, value in kwargs.items():
            setattr(self, key, value)

    # <h3>Rendering</h3>
    def render(self):
        # We first draw the back faces, storing their coordinates into a
        # texture. This means we have to clear and bind the back framebuffer,
        # activate face culling with cull face mode "FRONT", bind the back face
        # shader with the current modelview matrix set, and render the vertex
        # array for the cube:
        self.back_fbo.clear()
        with State(cull_face=True, cull_face_mode="FRONT"):
            with self.back_shader(modelview_matrix=self.modelview_matrix):
                with self.back_fbo:
                    self.vao.draw()

        # We then draw the front faces, accumulating the intensity between
        # front and back face. The setup is very similar to the one stated
        # before, except that the additional uniform variables
        # <code>intensity_scale</code> and <code>absorption</code> are passed
        # to the shader:
        self.front_fbo.clear()
        with State(cull_face=True, cull_face_mode="BACK"):
            with self.front_shader(modelview_matrix=self.modelview_matrix, intensity_scale=self.intensity_scale, absorption=self.absorption):
                with self.front_fbo:
                    self.vao.draw()

        # Finally, we simply return the texture into which we just rendered.
        # The client code might want to display this directly, or to download
        # the data into a numpy array.
        return self.front_fbo[0]

# <h2>Initialization and main loop</h2>

# Finally, if this program is being run from the command line, we set up all
# the previously mentioned objects and start rendering. The program will expect
# two command line parameters: the name of an HDF5 input file, and a
# <code>printf</code>-style format string for the image filenames.
if __name__ == "__main__":
    # We need to read a volume filename from <code>sys.argv</code>, so import
    # <code>sys</code>.
    import sys

    # We assume the volume is stored in a <a
    # href="http://www.hdfgroup.org/HDF5/">HDF5</a> file, so import <a
    # href="h5py.alfven.org"><code>h5py</code></a>.
    import h5py

    # For saving the resulting images, we use <a
    # href="http://scipy.org/">SciPy</a>'s <code>imread</code> function:
    from scipy.misc import imsave

    # We open the HDF5 file specified on the command line for reading:
    with h5py.File(sys.argv[1]) as f:
        # The volumetric data is read from the corresponding dataset in the
        # HDF5 file. Note that the name of the dataset is mere convention.
        volume = Texture3D(f["data"])
        # The data can be either emission densities only or absorption
        # densities only.  If the dataset defines an attribute called
        # "apsorption", we read it; otherwise we assume it's an emission only
        # dataset.
        absorption = f["data"].attrs.get("absorption", False)

    # Now we generate a <code>VolumeRenderer</code> instance for the volumetric
    # data that has just been read.
    renderer = VolumeRenderer(volume, absorption=absorption, intensity_scale=0.1, modelview_matrix=numpy.eye(4))

    # Finally, we iterate over a number of different viewing angles, manipulate
    # the modelview matrix accordingly, render the volume, and save it to an
    # image file:
    maxval = None
    for idx, angle in enumerate(numpy.mgrid[0:2*numpy.pi:100j]):
        renderer.modelview_matrix[::2, ::2] = numpy.array(((numpy.cos(angle), numpy.sin(angle)), (-numpy.sin(angle), numpy.cos(angle))))
        # The <code>render()</code> function returns a <code>Texture</code>
        # object. We can access the texture data via the <code>data</code>
        # attribute. We mirror the image vertically and chop of the alpha
        # channel before storing the image in a file:
        image = renderer.render().data[::-1, :, :3]
        if maxval is None:
            maxval = image.max()
        imsave(sys.argv[2] % idx, image / maxval)

    # Note how we did not need to create an OpenGL context explicitly. The
    # first object that needs an OpenGL context (in this case the
    # <code>VertexArray</code> in the <code>VolumeRenderer</code>) will create
    # an invisible context as soon as it is initialized. This is very
    # convenient; on the other hand, it means that if you create a context
    # manually (e.g., because you need a visible window), you have to
    # initialize it before any other objects. Otherwise, these objects may end
    # up in the wrong context, and sharing data across context is a problem of
    # its own.

