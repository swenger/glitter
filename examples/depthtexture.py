from math import sin, cos, pi
from numpy.random import random
import sys
import h5py

import logging
logging.basicConfig(level=logging.DEBUG)

from glitter import VertexArray, State, get_default_program, Framebuffer, Texture2D, get_copy_pipeline_2d, add_logger
from glitter.contexts.glut import GlutWindow, main_loop, get_elapsed_time

class MeshViewer(object):
    def __init__(self):
        self.window = GlutWindow(double=True, multisample=True)
        self.window.display_callback = self.display
        self.shader = get_default_program()
        self.fbo = Framebuffer(depth=Texture2D(shape=self.window.shape + (1,), depth=True))
        self.copy_pipeline = get_copy_pipeline_2d(image=self.fbo.depth, use_framebuffer=False)
        with h5py.File(sys.argv[1], "r") as f:
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
        except Exception, e:
            import traceback
            traceback.print_exc()
            raise SystemExit(e)
        add_logger(None)

    def timer(self):
        phi = 2 * pi * get_elapsed_time() / 20.0
        self.shader.modelview_matrix = ((cos(phi), 0, sin(phi), 0), (0, 1, 0, 0), (-sin(phi), 0, cos(phi), 0), (0, 0, 0, 1))
        self.window.add_timer(10, self.timer)
        self.window.post_redisplay()
    
    def run(self):
        self.timer()
        with self.shader:
            with State(depth_test=True):
                add_logger()
                main_loop()

if __name__ == "__main__":
    MeshViewer().run()

