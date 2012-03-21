#!/usr/bin/env python

"""Poisson integration on OpenGL textures using OpenCL.

@todo: Add literate programming comments.

@author: Stephan Wenger
@date: 2012-03-20
"""

from numpy import float32, zeros_like
import pyopencl as cl
from pyopencl.tools import get_gl_sharing_context_properties

from glitter import Texture2D
from glitter.raw.gl import GL_TEXTURE_2D

kernel_code = """
__kernel void laplace(__write_only image2d_t dst, __read_only image2d_t src, __read_only image2d_t lapl_mask, float a) {
    const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;
    int2 coords = (int2)(get_global_id(0), get_global_id(1));

    float4 lapl_val = read_imagef(lapl_mask, sampler, coords);
    if (lapl_val.w < 0.5) {
        write_imagef(dst, coords,
            (1 - a) * read_imagef(src, sampler, coords) + 0.25 * a * (
              - lapl_val
              + read_imagef(src, sampler, coords + (int2)(1, 0))
              + read_imagef(src, sampler, coords - (int2)(1, 0))
              + read_imagef(src, sampler, coords + (int2)(0, 1))
              + read_imagef(src, sampler, coords - (int2)(0, 1))
            )
        );
     }
}
"""

class PoissonIntegrator(object):
    """Solve  Laplace(img) == lapl_mask  wherever lapl_mask.w is smaller than 0.5."""

    use_gl_texture_as_tmp = True # TODO when False, result looks strange; why?

    def __init__(self, gl_image, gl_lapl_mask):
        platform = cl.get_platforms()[0]
        self.ctx = cl.Context(properties=[(cl.context_properties.PLATFORM, platform)] + get_gl_sharing_context_properties(), devices=None)
        self.queue = cl.CommandQueue(self.ctx)
        self.program = cl.Program(self.ctx, kernel_code).build()

        self.shape = gl_image.shape[1], gl_image.shape[0]
        self.cl_image = cl.GLTexture(self.ctx, cl.mem_flags.READ_WRITE, GL_TEXTURE_2D, 0, gl_image._id, 2)
        self.cl_lapl_mask = cl.GLTexture(self.ctx, cl.mem_flags.READ_ONLY, GL_TEXTURE_2D, 0, gl_lapl_mask._id, 2)

        if self.use_gl_texture_as_tmp:
            self.gl_tmp = Texture2D(gl_image.data)
            self.cl_tmp = cl.GLTexture(self.ctx, cl.mem_flags.READ_WRITE, GL_TEXTURE_2D, 0, self.gl_tmp._id, 2)
        else:
            self.cl_tmp = cl.Image(self.ctx, cl.mem_flags.READ_WRITE, self.cl_image.get_image_info(cl.image_info.FORMAT), self.shape)

    def execute(self, a=1.0):
        if self.use_gl_texture_as_tmp:
            cl.enqueue_acquire_gl_objects(self.queue, [self.cl_image, self.cl_lapl_mask, self.cl_tmp])
        else:
            cl.enqueue_acquire_gl_objects(self.queue, [self.cl_image, self.cl_lapl_mask])
        self.program.laplace(self.queue, self.shape, None, self.cl_tmp, self.cl_image, self.cl_lapl_mask, float32(a))
        self.program.laplace(self.queue, self.shape, None, self.cl_image, self.cl_tmp, self.cl_lapl_mask, float32(a))
        if self.use_gl_texture_as_tmp:
            cl.enqueue_release_gl_objects(self.queue, [self.cl_image, self.cl_lapl_mask, self.cl_tmp])
        else:
            cl.enqueue_release_gl_objects(self.queue, [self.cl_image, self.cl_lapl_mask])

if __name__ == "__main__":
    import sys
    from matplotlib.pyplot import imread
    from scipy.misc import imsave

    image = imread(sys.argv[1])
    lapl_mask = zeros_like(image)
    lapl_mask[:, :, 3] = image[:, :, 3]
    lapl_mask[0, :, 3] = lapl_mask[-1, :, 3] = lapl_mask[:, 0, 3] = lapl_mask[:, -1, 3] = 1.0

    gl_image = Texture2D(image)
    gl_lapl_mask = Texture2D(lapl_mask)
    
    poisson_integrator = PoissonIntegrator(gl_image, gl_lapl_mask)
    for i in range(1024):
        poisson_integrator.execute(0.5)

    imsave(sys.argv[2], gl_image.data[:, :, :3])

