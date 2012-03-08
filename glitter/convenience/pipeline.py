"""Pipeline class unifying vertex array, shader and framebuffer.

@author: Stephan Wenger
@date: 2012-03-05
"""

from glitter.framebuffers import Framebuffer
from glitter.arrays import VertexArray
from glitter.utils import ItemProxy, InstanceDescriptorMixin, State, StateMixin, add_proxies
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
        @param use_framebuffer: If C{True}, render to textures instead of the default framebuffer (the screen).
        @type use_framebuffer: C{bool}
        @param kwargs: Named arguments are translated to setting of attributes.
        """

        self._shader = shader

        # add shader uniforms (attributes are handled by the vertex array)
        for name, proxy in self._shader.__dict__.items():
            if isinstance(proxy, BaseUniform):
                setattr(self, name, proxy)

        # create vertex array
        self._vao = VertexArray()
        add_proxies(self, self._vao)
        
        # create framebuffer
        if use_framebuffer:
            self._fbo = Framebuffer()
            add_proxies(self, self._fbo)
        else:
            # binding self._fbo binds the default framebuffer
            self._fbo = State(draw_framebuffer_binding=None)

            # add clear method for default framebuffer
            self.clear = self._shader._context.clear

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
        return not isinstance(self._fbo, State) and self._shader.has_frag_data_location(name)

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
        attributes will check for vertex attributes and fragment outputs called
        C{name} and create appropriate proxies or raise an error if no such
        attribute or output exists.
        """

        if hasattr(self, name) or name.startswith("_") or not self._frozen:
            super(Pipeline, self).__setattr__(name, value)
        elif self._has_input(name):
            self._add_input(name, value)
        elif self._has_output(name):
            self._add_output(name, value)
        else:
            raise AttributeError("'%s' object has no attribute '%s'" % (self.__class__.__name__, name))

    def __enter__(self):
        """Bind framebuffer and shader."""
        self._fbo.__enter__()
        self._shader.__enter__()
        return self

    def __exit__(self, type, value, traceback):
        """Unbind framebuffer and shader."""
        self._shader.__exit__(type, value, traceback)
        self._fbo.__exit__(type, value, traceback)

    def draw_with(self, *args, **kwargs):
        """Call L{draw<VertexArray.draw>} on C{self} with attributes from C{kwargs} set.

        Keyword arguments that are known attributes or shader input our output
        variable names will be set as properties on C{self}. Any other
        arguments will be passed to L{draw<VertexArray.draw>}.
        """

        def is_valid_property(name):
            return hasattr(self, name) or self._has_input(name) or self._has_output(name)
        with self(**{key: kwargs.pop(key) for key, value in kwargs.items() if is_valid_property(key)}):
            self.draw(*args, **kwargs)

__all__ = ["Pipeline"]

