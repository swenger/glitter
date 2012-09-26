from glitter import ShaderProgram, RectangleTexture, Framebuffer, VertexArray
from glitter.contexts.glut import GlutWindow, main_loop

vertex_shader = """
#version 400 core

layout(location=0) in vec4 in_position;
out vec2 ex_texcoord;

void main() {
    gl_Position = in_position;
    ex_texcoord = in_position.xy * 0.5 + 0.5;
}
"""

fragment_shader = """
#version 400 core
#extension GL_ARB_texture_rectangle : enable

in vec2 ex_texcoord;
layout(location=0) out vec4 out_color;

void main() {
    out_color = vec4(gl_FragCoord.xy / 800, 0, 1);
}
"""

copy_vertex_shader = """
#version 400 core

layout(location=0) in vec4 in_position;

void main() {
    gl_Position = in_position;
}
"""

copy_fragment_shader = """
#version 400 core
#extension GL_ARB_texture_rectangle : enable

uniform sampler2DRect image;
layout(location=0) out vec4 out_color;

void main() {
    out_color = texture(image, gl_FragCoord.yx);
}
"""

class IntroductionExample(object):
    def __init__(self):
        self.window = GlutWindow(double=True, multisample=True, shape=(600, 800))
        self.window.display_callback = self.display

        self.shader = ShaderProgram(vertex=vertex_shader, fragment=fragment_shader)
        self.copy_shader = ShaderProgram(vertex=copy_vertex_shader, fragment=copy_fragment_shader)
        
        self.copy_shader.image = RectangleTexture(shape=self.window.shape + (3,))
        self.fbo = Framebuffer(self.copy_shader.image)

        self.vao = VertexArray(((-1.0, -1.0), (-1.0, 1.0), (1.0, 1.0), (1.0, -1.0)), elements=((0, 1, 2), (0, 2, 3)))

    def display(self, use_texture=False):
        self.window.clear()

        if use_texture:
            self.fbo.clear()
            with self.fbo:
                with self.shader:
                    self.vao.draw()
            with self.copy_shader:
                self.vao.draw()
        else:
            with self.shader:
                self.vao.draw()
        
        self.window.swap_buffers()

    def run(self):
        main_loop()

if __name__ == "__main__":
    IntroductionExample().run()

