"""
Creates an OpenGL Window

adapted from NEHE lesson 1:
    http://nehe.gamedev.net/tutorial/creating_an_opengl_window_(win32)/13001/
"""

import glitter.raw as _gl
from glitter.contexts.glut import GlutWindow, main_loop, get_alt_state


def display():
    # clear the screen
    window.clear(color=True, depth=True)
    # display the backbuffer
    window.swap_buffers()

def keyboard(key, x, y):
    # if F1 or ALT-Enter is pressed, toggle fullscreen
    # TODO: could not find GLUT_KEY_F1 but in rawgl, should be available as special key in constants
    if key == _gl.GLUT_KEY_F1 or (get_alt_state() and key == ord('\r')):
        window.toggle_full_screen()
    elif key == 27: # escape key
        raise SystemExit # makes program quit out of main_loop

if __name__ == "__main__":
    # create main window
    window = GlutWindow(name="NeHe's OpenGL Framework", double=True)
    # set background color to black
    # TODO: why do I always have to supply an alpha channel, 
    # it would be nice if window.color_clear_value = (0, 0, 0) would work 
    # (in this case implicitely alpha is set to 1)
    window.color_clear_value = (0, 0, 0, 1)
    # callback for rendering
    window.display_callback = display
    # callback for normal keys and special keys (like F1), both handled by same function here
    window.keyboard_callback = window.special_callback = keyboard
    # render all the time
    window.idle_callback = window.post_redisplay
    # blocks until SystemExit is raised or window is closed
    main_loop()

