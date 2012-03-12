"""Basic ctypes wrappers around OpenGL 3 (and up).

This module provides very basic wrapping of OpenGL, GLU, GLUT, and GLX. Like
PyOpenGL, it includes typesafe function calls, named constants and automatic
error checking. Since it is mainly intended as a low-level backend for the
glitter package, it does not provide wrapping of return types like PyOpenGL,
but instead includes logging facilities for easier OpenGL debugging through a
high-level API.
"""

from ctypes import *

try:
    from glitter.raw.gl import *
except ImportError:
    pass

try:
    from glitter.raw.glu import *
except ImportError:
    pass

try:
    from glitter.raw.glut import *
except ImportError:
    pass

try:
    from glitter.raw.glx import *
except ImportError:
    pass

from glitter.raw.errcheck import *
from glitter.raw.logger import *
from glitter.raw.constant import *

wrap_constants(d=globals()) # pass d explicitly to avoid infinite import loop
set_error_check(d=globals()) # pass d explicitly to avoid infinite import loop

