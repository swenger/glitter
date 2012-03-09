"""Intuitive OpenGL wrappers.

Design principles:
  - Choose inituitive use over performance (no premature optimization; make it
    run, then make it fast). Users should not (need to) use the raw GL/GLUT
    wrappers at any time.
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
        GPU. Exceptions are made where iterables are accepted; numpy
        converts these to 64 bit datatypes, which are silently converted to 32
        bit in some places.
  - Binding and unbinding of objects should be possible automatically (via with
    statements) as well as manually (through properties of the context).
  - The library has a focus on GPGPU computing, but typical use for rendering
    should be as easy.
  - Platform independence should be sought for, although Linux/GLX is the
    primary target.

Build instructions:
  - installing: C{sudo python setup.py install}
  - docs: C{epydoc --html -v -o docs glitter examples tests}
  - tests: C{nosetests tests}

When extending the library:
  - Make sure your class uses methods and properties of its L{Context} where
    possible instead of raw OpenGL calls; the context may cache some values or
    trigger callbacks, and calling OpenGL directly may break functionality in
    weird and unexpected ways. If you need to call raw GL functions, do so
    through the rawgl wrapper. If your raw GL invocations are generic enough,
    think about extending the L{Context} instead. Make sure to derive from
    L{GLObject} and use C{with self._context:} where necessary if your class
    does in any way interact directly with OpenGL. If you derive from
    L{GLObject}, your constructor should take an optional C{context=None}
    parameter and pass it to L{GLObject.__init__}.
  - If your classes can be bound and unbound or change global state in some
    other way, they should act as context managers. Base classes are defined in
    the L{objects} module to help you doing it right.
  - Provide a convenient interface wherever possible. This includes casting
    values into the right types (e.g. to an appropriate array type using
    L{coerce_array}), failing gracefully with descriptive error messages, and
    adhering to conventions set by similar classes (e.g. returning C{self} from
    C{__enter__} methods, providing a C{__call__} method to set attributes by
    inheriting from L{StateMixin}).
  - If your class uses enums from the L{constants} module in a public
    interface, point a class variable of the same name to the enum so users do
    not need to import any constants manually.
  - Use absolute module names when importing other glitter modules. When
    importing from the same subpackage, use fully qualified names for the
    module (e.g. C{from glitter.utils.objects import GLObject}); otherwise,
    rely on the public interface of the subpackage defined in its
    C{__init__.py} and import from the subpackage directly (e.g. C{from
    glitter.utils import GLObject}). Do not import from the global C{glitter}
    module directly as visibility of subpackages may change.
  - Define the public interface of your module in C{__all__} and, if your
    module is meant for external use, C{import *} from your module in the
    C{__init__.py} of its parent. However, if your module is
    platform-dependent, do not C{import *} but have the user import your
    submodule manually.
  - Write docstrings for epydoc (use C{@todo}, C{@note}, C{@attention},
    C{@bug}, C{@warning} as appropriate).
  - Write tests for nosetests (in the C{tests} directory).
  - Write examples (in the C{examples} directory).

@todo: Move examples and tests into glitter tree to simplify packaging?
@todo: Write documentation and tests, expecially for using multiple objects at the same time (e.g., L{Texture}s, L{Context}s).
@todo: Implement NeHe tutorials as examples and tests.
@todo: Use a nicer stylesheet than C{epydoc.css} (maybe something more similar to Sphinx?).
@todo: Keep this file, C{README.txt} and C{long_description} in C{setup.py} in sync.

@todo: Use context property instead of C{_context} where appropriate.
@todo: Use caching to reduce the number of bind and unbind operations caused by C{with} statements.
@todo: Maybe use C{abc} module for abstract classes.
@todo: Make C{rawgl} replaceable, but include it in the package.
@todo: Transparent CUDA and OpenCL interoperability.

@author: Stephan Wenger
@date: 2012-02-29
"""

from glitter.arrays import *
from glitter.contexts import *
from glitter.convenience import *
from glitter.framebuffers import *
from glitter.misc import *
from glitter.shaders import *
from glitter.textures import *
from glitter.utils import *

