"""OpenGL context implementations for various platforms.

@todo: Create a raw offscreen GLX context class with context generation and switching and use it as a default context instead of GLUT.
@todo: Qt GL widgets and contexts.

@author: Stephan Wenger
@date: 2012-02-29
"""

from glitter.contexts import glut
from glitter.contexts.context import *
from glitter.contexts.contextmanager import *

