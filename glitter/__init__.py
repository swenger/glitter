"""Intuitive OpenGL wrapper.

Design principles:
  - Choose inituitive use over performance (no premature optimization; make it run, then make it fast).
    - The user should not (need to) use the raw GL/GLUT wrappers at any time.
    - Objects should accept convenience constructor parameters (e.g. L{VertexArray}, L{ShaderProgram}) where it makes sense.
  - All GL state changes that are independent of objects should go through a Context object. Other changes go through the corresponding objects:
    - Vertex attribute pointer bindings are performed by vertex array objects only.
    - Settings for draw buffers other than the screen are performed by framebuffer objects only.
    - Texture bindings are performed by shader programs only.
    - If possible, changes in the GL should be reflected in the wrapper, but unchecked caching is okay to keep references to bound objects.
  - Array data is represented in numpy, but objects should convert as appropriate.
    - No loss of precision should occur when copying data to and from the GPU.
  - Binding and unbinding of objects should be possible automatically (via with statements) as well as manually.
  - The library has a focus on GPGPU computing, but typical use for rendering should be as easy.
  - Platform independence should be sought for, although Linux/GLX is the primary target.

Build instructions:
  - installing: C{sudo python setup.py install}
  - docs: C{epydoc --html -v glitter}
  - tests: C{nosetests tests}

@todo: make sure to use C{with self._context} where necessary
@todo: create a raw offscreen GLX context class with context generation and switching
@todo: make C{rawgl} replaceable
@todo: transparent CUDA and OpenCL interoperability
@todo: write documentation and tests
@todo: add convenience tools for loading meshes, rendering a fullscreen quad, displaying a texture
@todo: add listing of all bound textures, buffers, etc.
@todo: rethink what C{__del__} and C{__exit__} methods should do when the interpreter exits (e.g. restoring to a deleted object will not work)
@todo: use C{@todo}, C{@note}, C{@attention}, C{@bug}, C{@warning} in docs

@author: Stephan Wenger
@date: 2012-02-29
"""

from arrays import *
from contexts import *
from framebuffers import *
from misc import *
from shaders import *
from textures import *
from utils import *

