"""Intuitive OpenGL wrappers.

Hacking glitter:
  - Make sure your class uses methods and properties of its L{Context} where
    possible instead of raw OpenGL calls; the context may cache some values or
    trigger callbacks, and calling OpenGL directly may break functionality in
    weird and unexpected ways. If you need to call raw GL functions, do so
    through the {glitter.raw} wrapper. If your raw GL invocations are generic
    enough, think about extending the L{Context} instead. Make sure to derive
    from L{GLObject} and use C{with self._context:} where necessary if your
    class does in any way interact directly with OpenGL. If you derive from
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
@todo: Implement NeHe tutorials as tutorials, examples and tests.

@todo: Convert strings into enum constants where appropriate.
@todo: Use context property instead of C{_context} where appropriate.
@todo: Use caching to reduce the number of bind and unbind operations caused by C{with} statements.
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

from glitter.raw import set_error_check, add_logger, GLError, LoggingWrapper, NamedConstant

