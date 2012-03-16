"""Pipeline class unifying vertex array, shader and framebuffer.

@author: Stephan Wenger
@date: 2012-03-05
"""

from glitter.framebuffers import Framebuffer
from glitter.arrays import VertexArray
from glitter.utils import ItemProxy, InstanceDescriptorMixin, State, StateMixin, add_proxies, PropertyProxy
from glitter.shaders.uniform import BaseUniform # BaseUniform is an implementation detail of the shaders package

class Pipeline(InstanceDescriptorMixin, StateMixin):
    """Convenience class for rendering pipelines.

    C{Pipeline}s contain a vertex array, a shader, and an optional framebuffer.
    Property access and method calls are appropriately redirected to these
    objects. Vertex attributes, shader uniforms, and fragment outputs can be
    set by their name either in the constructor or by accessing the
    corresponding properties on the pipeline.

    Vertex attributes can be set to buffer objects or anything that can be
    converted to an C{ArrayBuffer}.

    Shader uniforms behave as usual.

    Fragment outputs can be set to texture objects.

    @attention: In order to guarantee correct functioning of vertex attribute,
    uniform and fragment output variables, their names must be unique, must not
    begin with an underscore, and must not collide with the names of any vertex
    array or framebuffer methods.

    Usage examples:

    >>> shader = ShaderProgram(...)
    >>> vertices = [...]
    >>> colors = [...]
    >>> elements = [...]
    >>> texture = Texture2D(...)

    >>> pipeline = Pipeline(shader, in_position=vertices, in_color=colors, elements=elements, out_color=texture)
    >>> pipeline.clear()
    >>> pipeline.draw()

    >>> pipeline = Pipeline(shader, use_framebuffer=False)
    >>> with pipeline(in_position=vertices, in_color=colors, elements=elements):
    ...     pipeline.draw()
    >>> with pipeline(in_position=vertices, in_color=colors, elements=elements) as p:
    ...     p.draw()
    >>> pipeline.draw_with(in_position=vertices, in_color=colors, elements=elements)

    >>> pipeline = Pipeline(shader, use_framebuffer=False)
    >>> vertex_array = VertexArray(...)
    >>> with pipeline:
    ...     vertex_array.draw()
    """

    _frozen = False
    """Whether setting of unknown attributes should be interpreted literally or as accessing vertex array and framebuffer properties."""

    def __init__(self, shader, use_framebuffer=True, **kwargs):
        """Create a new C{Pipeline}.

        @param shader: The compiled and linked shader program object to use.
        @type shader: L{ShaderProgram}
        @param use_framebuffer: If C{True}, render to textures instead of the currently bound framebuffer.
        @type use_framebuffer: C{bool}
        @param kwargs: Named arguments are translated to setting of attributes.

        @todo: C{_vao} and C{_fbo} should be created dynamically when (and if)
        attributes and attachments are accessed, respectively;
        C{use_framebuffer} should not be necessary then.
        """

        self._shader = shader
        self._context = self._shader._context
        self._lazy_context_properties = {}
        self._lazy_context_property_stack = []

        # add shader uniforms (attributes are handled by the vertex array)
        for name, proxy in self._shader.__dict__.items():
            if isinstance(proxy, BaseUniform):
                setattr(self, name, PropertyProxy(self._shader, name))

        # create vertex array
        self._vao = VertexArray(context=self._context)
        add_proxies(self, self._vao)
        
        # create framebuffer
        if use_framebuffer:
            self._fbo = Framebuffer(context=self._context)
            add_proxies(self, self._fbo)
        else:
            self._fbo = None

        self._frozen = True
        
        # translate kwargs to setters on self
        for key, value in kwargs.items():
            setattr(self, key, value)

    def _has_input(self, name):
        """Determine whether the shader as an attribute named C{name}."""
        return self._shader.has_attribute_location(name)

    def _add_input(self, name, value=None):
        """Add a proxy for the attribute named C{name}."""
        index = self._shader.get_attribute_location(name)
        with State(self, _frozen=False):
            setattr(self, name, ItemProxy(self._vao, index))
        setattr(self, name, value)

    def _has_output(self, name):
        """Determine whether the shader as a fragment output named C{name}."""
        return self._fbo is not None and self._shader.has_frag_data_location(name)

    def _add_output(self, name, value):
        """Add a proxy for the fragment output named C{name}."""
        index = self._shader.get_frag_data_location(name)
        with State(self, _frozen=False):
            setattr(self, name, ItemProxy(self._fbo, index))
        setattr(self, name, value)

    def __setattr__(self, name, value):
        """Set an attribute.

        When C{name} is a known attribute or starts with an underscore, or when
        C{self} is not in L{_frozen} state, C{__setattr__} works as usual.

        When C{self} is in L{_frozen} state (default), setting of unknown
        attributes will check for vertex attributes, fragment outputs and
        context properties called C{name} and create appropriate proxies or
        raise an error if no such attribute or output exists.

        Context properties set here will be set on binding and reset on
        unbinding the pipeline.
        """

        if hasattr(self, name) or name.startswith("_") or not self._frozen:
            super(Pipeline, self).__setattr__(name, value)
        elif self._has_input(name):
            self._add_input(name, value)
        elif self._has_output(name):
            self._add_output(name, value)
        elif hasattr(self._context, name):
            self._lazy_context_properties[name] = value
        else:
            raise AttributeError("'%s' object has no attribute '%s'" % (self.__class__.__name__, name))

    def __delattr__(self, name, value):
        """Delete an attribute.

        When C{name} is a known attribute or starts with an underscore, or when
        C{self} is not in L{_frozen} state, C{__delattr__} works as usual.

        Otherwise, if the attribute is a previously set context property, it
        will be removed from the pipeline.
        """

        if hasattr(self, name) or name.startswith("_") or not self._frozen:
            super(Pipeline, self).__delattr__(name, value)
        elif name in self._lazy_context_properties:
            del self._lazy_context_properties[name]
        else:
            raise AttributeError("'%s' object has no attribute '%s'" % (self.__class__.__name__, name))

    def __enter__(self):
        """Bind framebuffer and shader."""
        
        stack_frame = []
        for key, value in self._lazy_context_properties.items():
            stack_frame.append((key, getattr(self._context, key)))
            setattr(self._context, key, value)
        self._lazy_context_property_stack.append(stack_frame)

        if self._fbo is not None:
            self._fbo.__enter__()
        self._shader.__enter__()
        return self

    def __exit__(self, type, value, traceback):
        """Unbind framebuffer and shader."""
        self._shader.__exit__(type, value, traceback)
        if self._fbo is not None:
            self._fbo.__exit__(type, value, traceback)

        for key, value in self._lazy_context_property_stack.pop():
            setattr(self._context, key, value)

    def draw_with(self, *args, **kwargs):
        """Call L{draw<VertexArray.draw>} on C{self} with attributes from C{kwargs} set.

        Keyword arguments that are known attributes or shader input our output
        variable names will be set as properties on C{self}. Context properties
        are set before drawing and reset afterwards. Any other arguments will
        be passed to L{draw<VertexArray.draw>}.

        @todo C{kwargs} context properties should override L{_lazy_context_properties}.
        """

        def is_valid_property(name):
            return hasattr(self, name) or self._has_input(name) or self._has_output(name)
        with self(**{key: kwargs.pop(key) for key, value in kwargs.items() if is_valid_property(key)}):
            with State(context=self._context, **{key: kwargs.pop(key) for key, value in kwargs.items() if hasattr(self._context, key)}):
                self.draw(*args, **kwargs)

__all__ = ["Pipeline"]

