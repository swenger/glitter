"""Base classes for OpenGL objects.

@todo: Rethink what C{__del__} and C{__exit__} methods should do when the interpreter exits (e.g. restoring to a deleted object will not work).

@author: Stephan Wenger
@date: 2012-02-29
"""

from functools import wraps as _wraps

import glitter.raw as _gl

def _get_context():
    """Grab the current context from the L{context} module.

    If no current context exists, a new one is created in a window system
    dependent way.

    @note: The import is wrapped in a function definition to avoid infinite
    recursion on import because the L{context} module imports this module.
    """

    from glitter.contexts import context_manager
    return context_manager.current_context or context_manager.create_default_context()

class GLObject(object):
    """Base class for objects that belong to an OpenGL context.

    @ivar _context: The parent context.
    """

    def __init__(self, context=None):
        """Create a new C{GLObject}.

        @param context: The parent context. Uses the current context if C{context} is C{None}.
        @type context: L{Context}
        """

        self._context = context or _get_context()

    @property
    def context(self):
        return self._context

class ManagedObject(GLObject):
    """Base class for objects that can be created and deleted in OpenGL.

    When a C{ManagedObject} instance is garbage collected, the corresponding
    OpenGL object is deleted as well.
    
    For each C{ManagedObject} subclass, the context keeps a database of existing
    objects.

    @ivar _id: ID generated by OpenGL. The ID is only unique per context.
    """

    _generate_id = NotImplemented
    """Constructor function.
    
    Example: C{glGenShader}

    If the function has an C{argtypes} attribute, it may have zero, one, or two
    parameters. If it has one parameter, L{_type} is passed as the parameter,
    and the return value is used as L{_id}.  If it has two parameters, C{1} is
    passed as the first and a C{GLuint} pointer as the second parameter; the
    number returned in this pointer is used as the L{_id}. All other functions
    are simply called and their return values used as L{_id}.
    """
    
    _delete_id = NotImplemented
    """Destructor function.
    
    Example: C{glDeleteShader}

    If the function has an C{argtypes} attribute and two arguments, C{1} is
    passed as the first and a C{GLuint} pointer to L{_id} as the second
    parameter.  Otherwise, L{_id} is passed as the only parameter.
    """

    _type = NotImplemented
    """An optional parameter for C{_generate_id}.
    
    Example: C{GL_VERTEX_SHADER}
    """

    _db = NotImplemented
    """The name of the corresponding object database in the L{Context}.
    
    Example: C{"shaders"}
    """

    def __init__(self, context=None):
        """Create a new C{ManagedObject} using L{_generate_id}.

        @param context: The parent context.
        @type context: L{Context}
        """

        if any(x is NotImplemented for x in (self._generate_id, self._delete_id)):
            raise TypeError("%s is abstract" % self.__class__.__name__)
        super(ManagedObject, self).__init__(context)
        with self._context:
            if hasattr(self._generate_id, "argtypes") and len(self._generate_id.argtypes) == 1:
                self._id = self._generate_id(self._type)
            elif hasattr(self._generate_id, "argtypes") and len(self._generate_id.argtypes) == 2:
                _id = _gl.GLuint()
                self._generate_id(1, _gl.pointer(_id))
                self._id = _id.value
            else:
                self._id = self._generate_id()
        if self._id == 0:
            raise RuntimeError("could not create %s" % self.__class__.__name__)
        if self._db is not NotImplemented:
            getattr(self._context, self._db)._objects[self._id] = self

    def __del__(self):
        """Delete the OpenGL object using L{_delete_id}.

        Any errors will be ignored because the OpenGL module may already have
        been garbage collected when the interpreter exits.
        """

        try:
            with self._context:
                if hasattr(self._delete_id, "argtypes") and len(self._delete_id.argtypes) == 2:
                    self._delete_id(1, _gl.pointer(_gl.GLuint(self._id)))
                else:
                    self._delete_id(self._id)
            self._id = 0
        except:
            pass

class StateMixin(object):
    """Mixin for objects with properties.

    Calling these objects will generate an appropriate L{State} wrapper for use
    in C{with} statements.
    """

    def __call__(self, **kwargs):
        """Return a L{State} wrapper around C{self}."""
        return State(self, do_enter_exit=True, **kwargs)

class BindableObject(GLObject, StateMixin):
    """Base class for objects that can be bound.

    When the object is bound, it returns the object that was previously bound
    to the same target.

    C{BindableObject} instances can be used in C{with} statements so that binding
    and resetting the previous state happens automatically.

    If subclasses define the methods L{_on_bind} or L{_on_release}, these will be
    called by the binding handler in the context whenever the instance is bound
    or unbound, respectively.

    If subclasses define a property C{_bind_value}, this value will be passed to
    the binding function instead of C{self}.

    Binding of an object to different targets (e.g. buffers that are bound to
    different targets, framebuffers that are bound for reading or drawing, and
    textures that are bound to different texture image units) is not covered by
    the C{BindableObject} class.

    @ivar _stack: A stack for storing previous bindings within C{with}
    statements.
    """

    _binding = NotImplemented
    """Name of the corresponding property in the L{Context}.

    Example: C{"array_buffer_binding"}
    """

    _on_bind = NotImplemented
    """Function to call before binding.
    
    L{ShaderProgram}s, for example, bind textures here.
    """
    
    _on_release = NotImplemented
    """Function to call after releasing.

    L{ShaderProgram}s, for example, release textures here.
    """

    _bind_value = NotImplemented
    """Value to pass to the C{_binding} property.

    If C{NotImplemented}, C{self} will be used.
    """

    def __init__(self, context=None):
        """Create a new C{BindableObject}.

        @param context: The parent context.
        @type context: L{Context}
        """

        if any(x is NotImplemented for x in (self._binding,)):
            raise TypeError("%s is abstract" % self.__class__.__name__)
        super(BindableObject, self).__init__(context)
        self._stack = []
    
    def bind(self):
        """Bind the object and return the previously bound object.

        Binding is executed by setting the parent L{Context}'s property named
        in L{_binding}.

        @return: The previous value of the property.
        """

        try:
            old_binding = getattr(self._context, self._binding)
        except AttributeError:
            old_binding = None
        setattr(self._context, self._binding, self if self._bind_value is NotImplemented else self._bind_value)
        return old_binding

    def __enter__(self):
        """Called when a C{with} statement is entered.

        Activates the parent L{Context}, calls L{bind} and stores the returned
        value on the L{_stack}.
        """

        self._context.__enter__()
        self._stack.append(self.bind())
        return self

    def __exit__(self, type, value, traceback):
        """Called when a C{with} statement is exited.

        Restores the previous binding from the L{_stack} by setting the
        attribute named in L{_binding} in the parent L{Context} and deactivates
        the parent L{Context}.
        """

        setattr(self._context, self._binding, self._stack.pop())
        self._context.__exit__(type, value, traceback)

class State(GLObject, StateMixin):
    """Context manager to add binding semantics to context property changes.

    To set properties of the context and automatically reset it to its old
    value later, use a C{with} statement with a C{State} object.
    """

    def __init__(self, context=None, do_enter_exit=False, **kwargs):
        """Create a C{State} object for use in C{with} statements.

        When entering the C{with} statement, the properties of C{context} given
        in C{kwargs} will be set to their respective values. On exiting the
        C{with} statement, the old value will be restored.

        If C{context} defines C{__enter__} and C{__exit__} methods, this will
        be called on entering and exiting the C{with} block, respectively,
        if C{do_enter_exit} is C{True}.

        No guarantee is made about the order in which the properties are set,
        but they are guaranteed to be reset in reverse order.

        For convenience, C{__getattr__} and C{__setattr__} calls are redirected
        to C{context}, so that C{with State(...) as x:} works as expected.

        @param context: The context object on which to set the properties, or the current context if it is C{None}.
        @type context: L{Context} or any other object with attributes
        @param do_enter_exit: Whether to call C{context}'s C{__enter__} and C{__exit__} methods.
        @type do_enter_exit: C{bool}
        @param kwargs: A dictionary of property names and their values.
        @type kwargs: C{dict}
        """

        super(State, self).__init__(context)
        self._do_enter_exit = do_enter_exit
        self._properties = kwargs
        self._stack = []

    def __enter__(self):
        if self._do_enter_exit and hasattr(self._context, "__enter__"):
            self._context.__enter__()
        for key, value in self._properties.items():
            try:
                self._stack.append(getattr(self._context, key))
            except AttributeError:
                self._stack.append(None)
            setattr(self._context, key, value)
        return self

    def __exit__(self, type, value, traceback):
        for key in reversed(self._properties.keys()):
            setattr(self._context, key, self._stack.pop())
        if self._do_enter_exit and hasattr(self._context, "__exit__"):
            self._context.__exit__(type, value, traceback)

    def __getattr__(self, key):
        if not hasattr(self, "_stack"): # constructor not done yet
            return super(State, self).__getattr__(key)
        return getattr(self._context, key)

    def __setattr__(self, key, value):
        if not hasattr(self, "_stack"): # constructor not done yet
            return super(State, self).__setattr__(key, value)
        setattr(self._context, key, value)

class BindReleaseObject(GLObject, StateMixin):
    """Base class for objects that can be bound and released.

    C{BindReleaseObject} should be used instead of L{BindableObject} when binding
    and releasing are not performed by setting a property on a context, but by
    custom L{bind} and L{release} methods.

    Subclasses are responsible for restoring any objects previously bound to
    the same target.
    """

    bind = NotImplemented
    """Method for binding C{self} to L{_context}.

    C{bind} takes no arguments.
    """

    release = NotImplemented
    """Method for releasing C{self} from L{_context}.

    C{release} is responsible for restoring any previous binding.

    C{release} takes no arguments.
    """

    def __init__(self, context=None):
        """Create a new C{BindReleaseObject}.

        @param context: The parent context.
        @type context: L{Context}
        """

        super(BindReleaseObject, self).__init__(context)
        if any(x is NotImplemented for x in (self.bind, self.release)):
            raise TypeError("%s is abstract" % self.__class__.__name__)
    
    def __enter__(self):
        """Called when a C{with} statement is entered.

        Activates the parent L{Context} and calls L{bind}.
        """

        self._context.__enter__()
        self.bind()
        return self

    def __exit__(self, type, value, traceback):
        """Called when a C{with} statement is exited.

        Calls L{release} and deactivates the parent L{Context}.
        """

        self.release()
        self._context.__exit__(type, value, traceback)

def with_obj(obj, f):
    """Create a wrapper that executes C{f} in a C{with obj:} block."""
    @_wraps(f)
    def wrapper(*args, **kwargs):
        with obj:
            return f(*args, **kwargs)
    return wrapper

__all__ = ["GLObject", "ManagedObject", "BindableObject", "BindReleaseObject", "State", "StateMixin", "with_obj"]

