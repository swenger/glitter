"""Intuitive OpenGL wrappers.

Hacking glitter:
  - Make sure your class uses methods and properties of its L{Context} where
    possible instead of raw OpenGL calls; the context may cache some values or
    trigger callbacks, and calling OpenGL directly may break functionality in
    weird and unexpected ways. If you need to call raw GL functions, do so
    through the {glitter.raw} wrapper. If your raw GL invocations are generic
    enough, think about extending the L{Context} instead. Make sure to derive
    from L{GLObject} and use C{with self._context:} where necessary if your
    class does in any way interact directly with OpenGL. If your object is tied
    to a single context, derive from L{GLObject}. The constructor should take
    an optional C{context=None} parameter and pass it to L{GLObject.__init__}.
    Also be careful to create any additional OpenGL objects within the same
    context, preferably by passing the C{context} parameter to their
    constructors as well.
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
    not need to import any constants manually. Functions that accept enums
    should cast input values into the appropriate constants using
    C{my_enum(value)} first to ensure type safety and to enable using enum
    constant names instead of L{EnumConstant}s.
  - Use absolute module names when importing other glitter modules. When
    importing from the same subpackage, use fully qualified names for the
    module (e.g. C{from glitter.utils.objects import GLObject}); otherwise,
    rely on the public interface of the subpackage defined in its
    C{__init__.py} and import from the subpackage directly (e.g. C{from
    glitter.utils import GLObject}). Do not import from the global C{glitter}
    module directly as visibility of subpackages may change.
  - Define the public interface of your module in C{__all__} and, if your
    module is meant for external use, C{import *} from your module in the
    C{__init__.py} of its parent. However, if your module has external
    dependencies other than numpy, do not C{import *} but have the user import
    your submodule manually.
  - Write docstrings for epydoc (use C{@todo}, C{@note}, C{@attention},
    C{@bug}, C{@warning} as appropriate).
  - Write tests for nosetests (in the C{tests} directory).
  - Write examples (in the C{examples} directory).

@todo: Use C{with self._context} for all GL calls, pass context when creating sub-objects.
@todo: Use caching to reduce the number of bind and unbind operations caused by C{with} statements.
@todo: Implement NeHe tutorials as literate example programs, add an example for PyCUDA interoperability.
@todo: Write documentation and tests, expecially for using multiple objects at the same time (e.g., L{Texture}s, L{Context}s).
@todo: Provide example datasets for the examples (volume and mesh), link to source and to index for examples.

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

