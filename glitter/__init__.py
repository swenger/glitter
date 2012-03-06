"""Intuitive OpenGL wrapper.

Design principles:
  - Choose inituitive use over performance (no premature optimization; make it
    run, then make it fast).
      - The user should not (need to) use the raw GL/GLUT wrappers at any time.
      - Objects should accept convenience constructor parameters (e.g.
        L{VertexArray<VertexArray.__init__>},
        L{ShaderProgram<ShaderProgram.__init__>}) where it makes sense.
  - All GL state changes that are independent of objects should go through a
    Context object. Other changes go through the corresponding objects:
      - Vertex attribute pointer bindings are performed by vertex array objects
        only.
      - Settings for draw buffers other than the screen are performed by
        framebuffer objects only.
      - Texture bindings are performed by shader programs only.
      - If possible, changes in the GL should be reflected in the wrapper, but
        unchecked caching is okay to keep references to bound objects.
  - Array data is represented in numpy, but objects should convert as
    appropriate.
      - No loss of precision should occur when copying data to and from the
        GPU.
  - Binding and unbinding of objects should be possible automatically (via with
    statements) as well as manually.
  - The library has a focus on GPGPU computing, but typical use for rendering
    should be as easy.
  - Platform independence should be sought for, although Linux/GLX is the
    primary target.

Build instructions:
  - installing: C{sudo python setup.py install}
  - docs: C{epydoc --html -v glitter examples tests}
  - tests: C{nosetests tests}

When extending the library:
  - Make sure your class uses methods and properties of its L{Context} where
    possible instead of raw OpenGL calls; the context may cache some values or
    trigger callbacks, and calling OpenGL directly may break functionality in
    weird and unexpected ways. If you need to call raw GL functions, do so
    through the rawgl wrapper. If your raw GL invocations are generic enough,
    think about extending the L{Context} instead. Make sure to derive from
    L{GLObject} and use C{with self._context:} where necessary if your class
    does in any way interact directly with OpenGL.
  - If your classes can be bound and unbound or change global state in some
    other way, they should act as context managers. Base classes are defined in
    the L{objects} module to help you doing it right.
  - Provide a convenient interface wherever possible. This includes casting
    values into the right types (e.g. to an appropriate array type using
    L{coerce_array}), failing gracefully with descriptive error messages, and
    adhering to conventions set by similar classes (e.g. returning C{self} from
    C{__enter__} methods).
  - Write documentation (use C{@todo}, C{@note}, C{@attention}, C{@bug},
    C{@warning} as appropriate).
  - Write tests (for nosetests, in the C{tests} directory).
  - Write examples (in the C{examples} directory).

@todo: Create a raw offscreen GLX context class with context generation and switching.
@todo: Qt GL widgets and contexts.
@todo: Make C{rawgl} replaceable.

@todo: Write documentation and tests, expecially for using multiple objects at the same time (e.g., L{Texture}s, L{Context}s).
@todo: Implement NeHe tutorials as examples and tests.
@todo: Use a nicer stylesheet than C{epydoc.css} (maybe something more similar to Sphinx?).

@todo: Add listing of all bound textures, buffers, etc.
@todo: Derive all objects with meaningful attributes from L{StateMixin}.
@todo: Maybe use C{abc} module for abstract classes.
@todo: Transparent CUDA and OpenCL interoperability.
@todo: Rethink what C{__del__} and C{__exit__} methods should do when the interpreter exits (e.g. restoring to a deleted object will not work).
@todo: Rethink vertex array drawing: e.g., differing number of elements in vertex and color buffer.

@author: Stephan Wenger
@date: 2012-02-29
"""

from arrays import *
from contexts import *
from convenience import *
from framebuffers import *
from misc import *
from shaders import *
from textures import *
from utils import *

