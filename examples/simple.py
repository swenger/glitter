#!/usr/bin/env python

#! This file is a literate Python program. You can compile the documentation
#! using mylit (http://pypi.python.org/pypi/mylit/).
## title = "glitter Example: Simple"
## stylesheet = "pygments_style.css"

# <h1><i>glitter</i> Example: Simple</h1>

# <h2>Summary</h2>

# This program will open a GLUT window and render a colored, rotating quad.

# <img src="simple.png">

# <h2>Front matter</h2>

# <h3>Module docstring</h3>

# The module docstring is used as a description of this example in the
# generated documentation:
"""Simple example displaying a rotating quad.

@author: Stephan Wenger
@date: 2012-02-29
"""

# <h3>Imports</h3>

# Our scene is going to rotate. The rotating modelview matrix is computed using
# the sine and cosine functions from the math module:
from math import cos, sin

# We can usually import classes and functions contained in <i>glitter</i>
# submodules directly from glitter:
from glitter import VertexArray, get_default_program

# Modules with external dependencies other than numpy, such as platform
# dependent parts like methods for the generation of an OpenGL context,
# however, have to be imported from their respective submodules:
from glitter.contexts.glut import GlutWindow, main_loop, get_elapsed_time

# <h2>Vertex arrays</h2>

# The geometry is specified as arrays (or nested lists) of vertices, colors,
# and indices into the vertex and color arrays. Lists are automatically
# converted to appropriate numpy arrays. The shape of these arrays describes
# how the arrays are to be drawn. When an index array is used, as in this
# example, the vertex and color arrays are two-dimensional: the first dimension
# is the number of vertices, the second is the number of values for each vertex
# (e.g. the red, green, blue, and alpha channels for a color array). The shape
# of the index array is also two-dimensional: the first dimension is the number
# of primitives to be drawn, the second is the number of vertices in each
# primitive. Here, we draw four triangles forming a quad.
vertices = ((0, 0, 0), (-1, 1, 0), (1, 1, 0), (1, -1, 0), (-1, -1, 0))
colors = ((1, 1, 1), (0, 1, 0), (0, 0, 1), (0, 1, 1), (1, 0, 0))
indices = ((0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 1))

# <h2>Main class</h2>

# We wrap all the OpenGL interaction in a class. The class will contain an
# <code>__init__()</code> method to set up all OpenGL objects, any required
# callback methods, as well as a <code>run()</code> method to trigger execution
# of the GLUT main loop.
class SimpleExample(object):
    # <h3>Initialization</h3>

    # When a <code>SimpleExample</code> instance is created, we need to
    # initialize a few OpenGL objects.
    def __init__(self):
        # First, we create a window; this also creates an OpenGL context.
        self.window = GlutWindow(double=True, multisample=True)

        # Then, we set the GLUT display callback function which will be defined
        # later.
        self.window.display_callback = self.display

        # In the OpenGL core profile, there is no such thing as a "standard pipeline"
        # any more. We use the minimalistic <code>defaultpipeline</code> from the
        # <code>glitter.convenience</code> module to create a shader program instead:
        self.shader = get_default_program()

        # Here, we create a vertex array that contains buffers for two vertex array
        # input variables as well as an index array:
        self.vao = VertexArray(vertices, colors, elements=indices)

    # <h3>Callback functions</h3>

    # <h4>Display function</h4>

    # Here we define the display function. It will be called by GLUT whenever the
    # screen has to be redrawn.
    def display(self):
        # First we clear the default framebuffer:
        self.window.clear()
        
        # To draw the vertex array, we use:
        self.vao.draw()

        # After all rendering commands have been issued, we swap the back buffer to
        # the front, making the rendered image visible all at once:
        self.window.swap_buffers()

    # <h4>Timer function</h4>

    # The animation is controlled by a GLUT timer. The timer callback changes the
    # modelview matrix, schedules the next timer event, and causes a screen redraw:
    def timer(self):
        # We first get the elapsed time from GLUT using <code>get_elapsed_time()</code>:
        phi = get_elapsed_time()

        # We then set the <code>modelview_matrix</code> uniform variable of the
        # shader created in the initialization section simply by setting an
        # attribute:
        self.shader.modelview_matrix = ((cos(phi), sin(phi), 0, 0), (-sin(phi), cos(phi), 0, 0), (0, 0, 1, 0), (0, 0, 0, 2))

        # The following line schedules the next timer event to execute after ten milliseconds.
        self.window.add_timer(10, self.timer)

        # Finally, we tell GLUT to redraw the screen.
        self.window.post_redisplay()

    # <h3>Running</h3>
    
    # We will call the <code>run()</code> method later to run the OpenGL code.
    def run(self):
        # To start the animation, we call the timer once; all subsequent timer
        # calls will be scheduled by the timer function itself.
        self.timer()

        # The default program is bound by using a <code>with</code> statement:
        with self.shader:
            # With the shader bound, we enter the GLUT main loop.
            main_loop()

        # When the main loop exits, control is handed back to the script.

# <h2>Main section</h2>

# Finally, if this program is being run from the command line, we instanciate
# the main class and run it.
if __name__ == "__main__":
    SimpleExample().run()

