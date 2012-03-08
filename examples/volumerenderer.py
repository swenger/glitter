#!/usr/bin/env python

"""Volume renderer that creates a set of image files from different perspectives.

@author: Stephan Wenger
@date: 2012-03-07
"""

import itertools
import numpy

from glitter import Framebuffer, ShaderProgram, RectangleTexture, VertexArray, float32, State, Texture3D

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

back_fragment_code = """
#version 400 core
#extension GL_ARB_texture_rectangle : enable

in vec4 ex_front;
layout(location=0) out vec4 out_color;

void main() {
    out_color = ex_front;
}
"""

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

cube_vertices = tuple(itertools.product((0.0, 1.0), (0.0, 1.0), (0.0, 1.0)))
cube_indices = (0, 1, 3), (0, 2, 6), (0, 3, 2), (0, 6, 4), (3, 1, 5), (3, 5, 7), (4, 1, 0), (4, 5, 1), (5, 4, 6), (5, 6, 7), (7, 2, 3), (7, 6, 2)

class VolumeRenderer(object):
    modelview_matrix = tuple(map(tuple, numpy.eye(4)))
    intensity_scale = 1.0
    absorption = False

    def __init__(self, volume, **kwargs):
        assert isinstance(volume, Texture3D), "volume must be a 3D texture"

        self.vao = VertexArray([cube_vertices], elements=cube_indices)
        self.back_shader = ShaderProgram(vertex=vertex_code, fragment=back_fragment_code)
        self.back_fbo = Framebuffer([RectangleTexture(shape=volume.shape[:2] + (4,), dtype=float32)])
        self.front_shader = ShaderProgram(vertex=vertex_code, fragment=front_fragment_code, volume=volume, back=self.back_fbo[0])
        self.front_fbo = Framebuffer([RectangleTexture(shape=volume.shape[:2] + (4,), dtype=float32)])

        for key, value in kwargs.items():
            setattr(self, key, value)

    def render(self):
        # draw back faces, store coordinates into texture
        self.back_fbo.clear()
        with State(cull_face=True, cull_face_mode="FRONT"):
            with self.back_shader(modelview_matrix=self.modelview_matrix):
                with self.back_fbo:
                    self.vao.draw()

        # draw front faces, accumulate intensity between front and back face
        self.front_fbo.clear()
        with State(cull_face=True, cull_face_mode="BACK"):
            with self.front_shader(modelview_matrix=self.modelview_matrix, intensity_scale=self.intensity_scale, absorption=self.absorption):
                with self.front_fbo:
                    self.vao.draw()

        return self.front_fbo[0]

if __name__ == "__main__":
    import sys, h5py
    from scipy.misc import imsave
    with h5py.File(sys.argv[1]) as f:
        volume = Texture3D(f["data"])
        absorption = f["data"].attrs.get("absorption", False)
    renderer = VolumeRenderer(volume, absorption=absorption, intensity_scale=0.1, modelview_matrix=numpy.eye(4))
    maxval = None
    for idx, angle in enumerate(numpy.mgrid[0:2*numpy.pi:100j]):
        renderer.modelview_matrix[::2, ::2] = numpy.array(((numpy.cos(angle), numpy.sin(angle)), (-numpy.sin(angle), numpy.cos(angle))))
        image = renderer.render().data[::-1, :, :3]
        if maxval is None:
            maxval = image.max()
        imsave(sys.argv[2] % idx, image / maxval)

