from scipy.misc import imsave

from glitter import ShaderProgram, RectangleTexture, Framebuffer, VertexArray
from glitter.contexts.glut import GlutWindow, main_loop

vertex_shader = """
#version 400 core

layout(location=0) in vec4 in_position;

void main() {
    gl_Position = in_position;
}
"""

fragment_shader = """
#version 400 core

layout(location=0) out vec4 out_color;
uniform float dimx, dimy;

void main() {
    out_color = vec4(gl_FragCoord.x / dimx, gl_FragCoord.y / dimy, 1.0, 1.0);
}
"""

class MinimalFramebufferExample(object):
    def __init__(self):
        self.window = GlutWindow(double=True, multisample=True, shape=(100, 800))
        self.window.display_callback = self.display

        self.shader = ShaderProgram(vertex=vertex_shader, fragment=fragment_shader)
        self.shader.dimy, self.shader.dimx = self.window.shape
        self.fbo = Framebuffer(RectangleTexture(shape=self.window.shape + (3,)))

        self.vao = VertexArray(((-1.0, -1.0), (-1.0, 1.0), (1.0, 1.0), (1.0, -1.0)), elements=((0, 1, 2), (0, 2, 3)))

    def save(self, filename):
        self.fbo.clear()
        with self.shader:
            with self.fbo:
                self.vao.draw()
        imsave(filename, self.fbo[0].data)

    def display(self):
        self.window.clear()
        with self.shader:
            self.vao.draw()
        self.window.swap_buffers()

    def run(self):
        main_loop()

if __name__ == "__main__":
    ie = MinimalFramebufferExample()
    ie.save("test.png")
    ie.run()
    # TODO why do I get a bus error on exit?

