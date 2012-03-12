"""
Draws a white quad and triangle in 2D

adapted from NEHE lesson 2:
    http://nehe.gamedev.net/tutorial/your_first_polygon/13002/
"""

import glitter.raw as _gl
from glitter.contexts.glut import GlutWindow, main_loop, get_alt_state
from glitter import ShaderProgram, VertexArray
from glitter.utils import primitive_types



# TODO: provide some off-the-shelfe vertex/fragment shaders?
vertex_shader = """
#version 400 core

layout(location=0) in vec4 in_position;

void main() {
    // just copy the vertex position directly onto the screen
    gl_Position = in_position;
}
"""

fragment_shader = """
#version 400 core
#extension GL_ARB_texture_rectangle : enable

layout(location=0) out vec4 out_color;

void main() {
    // make all pixels white
    out_color = vec4(1, 1, 1, 1);
}
"""

def display():
    # clear the screen
    window.clear(color=True, depth=True)
    # render the quad and the triangle
    with shader:
        # TODO: Why do I have to specify count here?
        quad.draw(primitive_types.TRIANGLE_STRIP, 4)
        triangle.draw(primitive_types.TRIANGLES, 3)
    # display the backbuffer
    window.swap_buffers()

def keyboard(key, x, y):
    # if F1 or ALT-Enter is pressed, toggle fullscreen
    if key == _gl.GLUT_KEY_F1 or (get_alt_state() and key == ord('\r')):
        window.toggle_full_screen()
    elif key == 27: # escape key
        raise SystemExit # makes program quit out of main_loop

if __name__ == "__main__":
    # create main window
    window = GlutWindow(name="My First Quad and Triangle", double=True)
    # set background color to black
    window.color_clear_value = (0, 0, 0, 1)
    # callback for rendering
    window.display_callback = display
    # callback for normal keys and special keys (like F1), both handled by same function here
    window.keyboard_callback = window.special_callback = keyboard
    # render all the time
    window.idle_callback = window.post_redisplay
    # shader program for rendering
    shader = ShaderProgram(vertex=vertex_shader, fragment=fragment_shader)
    # TODO why do I have to wrap them vertices it into another list if I use only one attribute buffer most of the time?
    quad = VertexArray([[(-0.7,  0.3, 0.0, 1.0), 
                         (-0.1,  0.3, 0.0, 1.0), 
                         (-0.7, -0.3, 0.0, 1.0), 
                         (-0.1, -0.3, 0.0, 1.0) ]])
    triangle = VertexArray([[( 0.1, -0.2, 0.0, 1.0), 
                             ( 0.7, -0.2, 0.0, 1.0), 
                             ( 0.4,  0.2, 0.0, 1.0) ]])
    # blocks until SystemExit is raised or window is closed
    main_loop()

