#!/usr/bin/env python

#! This file is a literate Python program. You can compile the documentation
#! using mylit (http://pypi.python.org/pypi/mylit/).
## title = "glitter Example: Point Cloud Renderer"
## stylesheet = "pygments_style.css"

# <h1><i>glitter</i> Example: Point Cloud Renderer</h1>

# <h2>Summary</h2>

# This program will open a GLUT window and render a random, colored, rotating point cloud.

# <img src="pointcloud.png">

# <h2>Front matter</h2>

# <h3>Module docstring</h3>

# The module docstring is used as a description of this example in the
# generated documentation:
"""Viewer for a random point cloud.

@author: Stephan Wenger
@date: 2012-03-13
"""

# <h3>Imports</h3>

# Our scene is going to rotate. The rotating modelview matrix is computed using
# the sine and cosine functions from the math module:
from numpy import sin, cos, pi

# <i>glitter</i> uses <a href="http://numpy.scipy.org/">numpy</a> for
# representation of array data. We will use numpy's <code>randn()</code>
# function to generate random point coordinates:
from numpy.random import randn

# We can usually import classes and functions contained in <i>glitter</i>
# submodules directly from glitter:
from glitter import VertexArray, State, get_default_program

# Platform dependent parts like methods for the generation of an OpenGL
# context, however, have to be imported from their respective submodules:
from glitter.contexts.glut import GlutWindow, main_loop, get_elapsed_time

# <h2>Callback functions</h2>

# <h3>Display function</h3>

# Here we define the display function. It will be called by GLUT whenever the
# screen has to be redrawn.
def display():
    # In the initialization code, we will create a GLUT window. In the display
    # function, we first clear this window:
    window.clear()
    
    # We will also create a vertex array holding the vertex positions and
    # colors. To draw this array, we use:
    vao.draw()

    # After all rendering commands have been issued, we swap the back buffer to
    # the front, making the rendered image visible all at once:
    window.swap_buffers()

# <h3>Timer function</h3>

# The animation is controlled by a GLUT timer. The timer callback changes the
# modelview matrix, schedules the next timer event, and causes a screen redraw:
def timer():
    # We first get the elapsed time from GLUT using <code>get_elapsed_time()</code>:
    phi = 2 * pi * get_elapsed_time() / 20.0

    # We then set the <code>modelview_matrix</code> uniform variable of the
    # shader created in the initialization section simply by setting an
    # attribute:
    shader.modelview_matrix = ((cos(phi), 0, sin(phi), 0), (0, 1, 0, 0), (-sin(phi), 0, cos(phi), 0), (0, 0, 0, 5))

    # The following line schedules the next timer event to execute after ten milliseconds.
    window.add_timer(10, timer)

    # Finally, we tell GLUT to redraw the screen.
    window.post_redisplay()

# <h2>Initialization and main loop</h2>

# Finally, if this program is being run from the command line, we set up all
# the previously mentioned objects and start the GLUT main loop.
if __name__ == "__main__":
    # First, wereate a window; this also creates an OpenGL context.
    window = GlutWindow(double=True, multisample=True)

    # Then, we set the GLUT display callback function.
    window.display_callback = display

    # In the OpenGL core profile, there is no such thing as a "standard pipeline"
    # any more. We use the minimalistic <code>defaultpipeline</code> from the
    # <code>glitter.convenience</code> module to create a shader program instead:
    shader = get_default_program()

    # Here, we create a vertex array that contains buffers for two vertex array
    # input variables as well as an index array:
    n_points = 100000
    vao = VertexArray(randn(n_points, 3), randn(n_points, 3))

    # To start the animation, we call the timer once; all subsequent timer
    # calls will be scheduled by the timer function itself.
    timer()

    # The default program is bound by using a <code>with</code> statement:
    with shader:
        # The <code>State</code> class encapsulates state changes in the
        # context. For example, to enable depth testing and set the point size
        # to three for the duration of the following function call, we would
        # write:
        with State(depth_test=True, point_size=3):
            # With the shader bound, depth testing enabled, and the point size
            # set, we enter the GLUT main loop.
            main_loop()

# When the main loop exits, control is handed back to the script.

