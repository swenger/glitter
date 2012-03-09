"""Descriptors for texture image units.

@author: Stephan Wenger
@date: 2012-02-29
"""

import itertools as _itertools

import glitter.raw as _gl
from glitter.utils import BindableObject
from glitter.contexts.proxies import BindingProxy

class TextureUnit(BindableObject):
    """Proxy for a texture unit.
    
    @warning: For internal use by L{TextureUnitList} only. Do not instantiate
    or use directly; use the methods of L{TextureUnitList} instead.
    """

    _binding = "active_texture"

    def __init__(self, _context, _id):
        super(TextureUnit, self).__init__(_context)
        self._context = _context
        self._id = _id
        self._use_count = 0

    def __str__(self):
        return "GL_TEXTURE%d" % (self._id - _gl.GL_TEXTURE0)

    def activate(self):
        self._context.active_texture = self

    def is_available(self):
        return self._use_count == 0

    texture_binding_1d                   = BindingProxy(_gl.glBindTexture,         [_gl.GL_TEXTURE_1D                  ])
    texture_binding_1d_array             = BindingProxy(_gl.glBindTexture,         [_gl.GL_TEXTURE_1D_ARRAY            ])
    texture_binding_2d                   = BindingProxy(_gl.glBindTexture,         [_gl.GL_TEXTURE_2D                  ])
    texture_binding_2d_array             = BindingProxy(_gl.glBindTexture,         [_gl.GL_TEXTURE_2D_ARRAY            ])
    texture_binding_2d_multisample       = BindingProxy(_gl.glBindTexture,         [_gl.GL_TEXTURE_2D_MULTISAMPLE      ])
    texture_binding_2d_multisample_array = BindingProxy(_gl.glBindTexture,         [_gl.GL_TEXTURE_2D_MULTISAMPLE_ARRAY])
    texture_binding_3d                   = BindingProxy(_gl.glBindTexture,         [_gl.GL_TEXTURE_3D                  ])
    texture_binding_buffer               = BindingProxy(_gl.glBindTexture,         [_gl.GL_TEXTURE_BUFFER              ])
    texture_binding_cube_map             = BindingProxy(_gl.glBindTexture,         [_gl.GL_TEXTURE_CUBE_MAP            ])
    texture_binding_rectangle            = BindingProxy(_gl.glBindTexture,         [_gl.GL_TEXTURE_RECTANGLE           ])
    sampler_binding                      = BindingProxy(_gl.glBindSampler,         ["_unit"                            ])

class TextureUnitList(object):
    """Proxy for the list of available texture units.
    
    @warning: C{TextureUnitList}s are created by their respective context only.
    Do not instantiate them directly. Using the C{TextureUnitList}'s L{bind}
    and L{release} methods directly is usually not necessary; L{Shader}s bind
    their textures automatically, and the L{bind<Texture.bind>} method of
    L{Texture}s is delegated to the C{TextureUnitList}.
    """

    def __init__(self, _context):
        self._context = _context
        self._texture_units = [TextureUnit(_context, _gl.GL_TEXTURE0 + i) for i in range(_context.max_combined_texture_image_units)]
        self._context.active_texture = self[0]
        self._bound_textures = dict()

    def __getitem__(self, index):
        return self._texture_units[index]

    def __len__(self):
        return len(self._texture_units)

    def __str__(self):
        return "[%d texture units]" % len(self)

    def __repr__(self):
        return str(self)

    def bind(self, texture):
        """Bind `texture` to a free unit and return the unit id."""
        if texture in self._bound_textures:
            unit = self._bound_textures[texture]
            unit._use_count += 1
        else:
            try:
                unit = _itertools.dropwhile(lambda x: not x.is_available(), self).next()
            except StopIteration:
                raise RuntimeError("no free texture units available")
            setattr(unit, texture._binding, texture)
            self._bound_textures[texture] = unit
            unit._use_count = 1
        return unit._id - _gl.GL_TEXTURE0

    def release(self, texture):
        """Unbind `texture`."""
        unit = self._bound_textures[texture]
        if unit._use_count  == 1:
            setattr(unit, texture._binding, None)
            del self._bound_textures[texture]
            unit._use_count = 0
        else:
            unit._use_count -= 1

