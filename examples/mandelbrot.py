#!/usr/bin/env python

"""Mandelbrot set renderer.

@author: Stephan Wenger
@date: 2012-03-23
"""

from numpy import linspace, array, minimum, maximum, cos, pi
from matplotlib import cm

from glitter import ShaderProgram, get_fullscreen_quad, Texture1D
from glitter.contexts.glut import GlutWindow, main_loop, get_elapsed_time
from glitter.raw import glut

vertex_shader = """
#version 400 core

layout(location=0) in vec4 in_position;
uniform vec2 minval, maxval;
out vec2 ex_texcoord;

void main() {
    gl_Position = in_position;
    ex_texcoord = (in_position.xy * 0.5 + 0.5) * (maxval - minval) + minval;
}
"""

fragment_shader = """
#version 400 core
#extension GL_ARB_texture_rectangle : enable

in vec2 ex_texcoord;
uniform sampler1D colormap;
layout(location=0) out vec4 out_color;

const int max_iteration = 1000;

void main() {
    vec2 xy = vec2(0.0, 0.0);
    int iteration = 0;
    while (xy.x * xy.x + xy.y * xy.y < 4 && iteration < max_iteration) {
        xy = vec2(xy.x * xy.x - xy.y * xy.y + ex_texcoord.x, 2 * xy.x * xy.y + ex_texcoord.y);
        iteration++;
    }
    float c = iteration - log(log(length(xy)));
    out_color = texture(colormap, 0.1 * c);
}
"""

class MandelbrotRenderer(object):
    transition_time = 0.3 # seconds
    update_step = 10 # milliseconds

    def __init__(self):
        self.window = GlutWindow(double=True, multisample=True)
        self.window.display_callback = self.display
        self.window.mouse_callback = self.mouse
        self.shader = ShaderProgram(vertex=vertex_shader, fragment=fragment_shader)
        self.shader.colormap = Texture1D(cm.spectral(linspace(0, 1, 256)), wrap_s="MIRRORED_REPEAT")
        self.shader.minval = (-2.5, -1.75)
        self.shader.maxval = (1.0, 1.75)
        self.vao = get_fullscreen_quad()
        self.history = []

    def display(self):
        self.window.clear()
        self.vao.draw()
        self.window.swap_buffers()

    def timer(self):
        t = min(1.0, (get_elapsed_time() - self.transition_start) / self.transition_time)
        x = 0.5 - 0.5 * cos(pi * t)
        self.shader.minval = self.minstart * (1 - x) + self.minend * x
        self.shader.maxval = self.maxstart * (1 - x) + self.maxend * x
        if t < 1:
            self.window.add_timer(self.update_step, self.timer)
        self.window.post_redisplay()

    def start_transition(self, minval, maxval):
        self.minstart, self.maxstart = self.shader.minval, self.shader.maxval
        self.minend, self.maxend = minval, maxval
        self.transition_start = get_elapsed_time()
        self.timer()

    def mouse(self, button, state, x, y):
        if button == glut.GLUT_LEFT_BUTTON:
            pos = array((x, self.window.shape[0] - y)) / array(self.window.shape[::-1], dtype=float)
            pos = pos * (self.shader.maxval - self.shader.minval) + self.shader.minval
            if state == glut.GLUT_DOWN:
                self.last_pos = pos
            elif state == glut.GLUT_UP and all(pos != self.last_pos):
                self.history.append((self.shader.minval, self.shader.maxval))
                self.start_transition(minimum(pos, self.last_pos), maximum(pos, self.last_pos))
        elif state == glut.GLUT_DOWN and button == glut.GLUT_RIGHT_BUTTON:
            if self.history:
                self.start_transition(*self.history.pop())

    def run(self):
        with self.shader:
            main_loop()

if __name__ == "__main__":
    MandelbrotRenderer().run()

