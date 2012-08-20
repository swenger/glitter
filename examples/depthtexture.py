#!/usr/bin/env python

"""Mesh viewer that displays the depth instead of color.

@todo: Add literate programming comments.

@author: Stephan Wenger
@date: 2012-03-20
"""

from math import sin, cos, pi
from numpy.random import random
import h5py

from glitter import VertexArray, State, get_default_program, Framebuffer, Texture2D, get_copy_pipeline_2d
from glitter.contexts.glut import GlutWindow, main_loop, get_elapsed_time

class DepthViewer(object):
    def __init__(self, filename):
        self.window = GlutWindow(double=True, multisample=True)
        self.window.display_callback = self.display
        self.shader = get_default_program()
        self.fbo = Framebuffer(depth=Texture2D(shape=self.window.shape + (1,), depth=True))
        self.copy_pipeline = get_copy_pipeline_2d(image=self.fbo.depth, use_framebuffer=False)
        with h5py.File(filename, "r") as f:
            vertices = f["vertices"]
            colors = f.get("colors", None)
            elements = f.get("indices", None)
            if colors is None:
                colors = random((len(vertices), 3))[:, None, :][:, [0] * vertices.shape[1], :]
            self.vao = VertexArray(vertices, colors, elements=elements)

    def display(self):
        try:
            with self.fbo:
                self.fbo.clear()
                self.vao.draw()
            self.window.clear()
            self.copy_pipeline.draw()
            self.window.swap_buffers()
        except Exception as e:
            import traceback
            traceback.print_exc()
            raise SystemExit(e)

    def timer(self):
        phi = 2 * pi * get_elapsed_time() / 20.0
        self.shader.modelview_matrix = ((cos(phi), 0, sin(phi), 0), (0, 1, 0, 0), (-sin(phi), 0, cos(phi), 0), (0, 0, 0, 1))
        self.window.add_timer(10, self.timer)
        self.window.post_redisplay()
    
    def run(self):
        self.timer()
        with self.shader:
            with State(depth_test=True):
                main_loop()

if __name__ == "__main__":
    import sys
    DepthViewer(sys.argv[1]).run()

