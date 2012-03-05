"""Pipeline class unifying vertex array, shader and framebuffer.

@author: Stephan Wenger
@date: 2012-03-05

@todo: provide a method to specify that no framebuffer / no vertex array should be generated + make pipeline bindable
"""

from glitter.framebuffers.framebuffer import Framebuffer
from glitter.arrays.vertexarray import VertexArray
from glitter.utils.proxy import ItemProxy, InstanceDescriptorMixin
from glitter.shaders.attribute import BaseAttribute
from glitter.shaders.uniform import BaseUniform
from glitter.utils.objects import State

class Pipeline(InstanceDescriptorMixin):
    def __init__(self, shader, elements=None, **bindings): # TODO what if output is to screen?
        self._shader = shader

        buffers = {}
        buffer_names = {}
        textures = {}
        texture_names = {}
        for key, value in bindings.items():
            if self._shader.has_attribute_location(key):
                loc = self._shader.get_attribute_location(key)
                buffers[loc] = value
                buffer_names[key] = loc
            elif self._shader.has_frag_data_location(key):
                loc = self._shader.get_frag_data_location(key)
                textures[loc] = value
                texture_names[key] = loc
            else:
                raise NameError("shader has no active input or output '%s' (is it unused?)" % key)
        self._fbo = Framebuffer(textures)
        self._vao = VertexArray(buffers, elements=elements)

        # add shader properties
        for name, proxy in self._shader.__dict__.items():
            if isinstance(proxy, (BaseUniform, BaseAttribute)):
                setattr(self, name, proxy)

        # add attributes
        for key, value in buffer_names.items():
            setattr(self, key, ItemProxy(self._vao, value))

        # add frag data
        for key, value in texture_names.items():
            setattr(self, key, ItemProxy(self._fbo, value))

    def clear(self, *args, **kwargs): # TODO and other Framebuffer methods
        self._fbo.clear(*args, **kwargs)

    def draw(self, *args, **kwargs): # TODO and other VertexArray methods
        with self:
            self._vao.draw(*args, **kwargs)

    def __call__(self, **kwargs):
        return State(self, **kwargs)

    def __enter__(self):
        self._fbo.__enter__()
        self._shader.__enter__()

    def __exit__(self, type, value, traceback):
        self._shader.__exit__(type, value, traceback)
        self._fbo.__exit__(type, value, traceback)

    def draw_with(self, *args, **kwargs):
        with self(**{key: kwargs.pop(key) for key, value in kwargs.items() if key in self.__dict__}):
            self.draw(*args, **kwargs)

