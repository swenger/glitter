"""Framebuffer object class.

@warn: Framebuffers are currently bound for drawing only (C{GL_DRAW_FRAMEBUFFER}, not C{GL_READ_FRAMEBUFFER}).
@todo: Implement binding for reading; wrap C{glReadPixels}, C{glBlitFramebuffer}, C{glCopyTexSubImage} and related framebuffer copy functions.
@todo: Add properties for C{viewport}, C{color_writemask}, C{depth_writemask},
C{blend_func}, C{blend_equation}, and C{depth_range} (using
C{glDepthRangeArray} and C{glDepthRangeIndexed}).

@author: Stephan Wenger
@date: 2012-02-29
"""

import glitter.raw as _gl
from glitter.utils import ManagedObject, BindableObject, framebuffer_status

class Framebuffer(ManagedObject, BindableObject):
    _generate_id = _gl.glGenFramebuffers
    _delete_id = _gl.glDeleteBuffers
    _db = "framebuffers"
    _binding = "draw_framebuffer_binding"
    _target = _gl.GL_DRAW_FRAMEBUFFER

    framebuffer_status = framebuffer_status
    _initialized = False

    def __init__(self, *attachments, **kwargs):
        """Create a new framebuffer.

        @param attachments: Textures to bind to color attachments.
        @type attachments: C{list} of L{Texture}s
        @param kwargs: Named arguments.
        @type kwargs: C{dict}
        @keyword context: The context in which to create the framebuffer.
        @type context: L{Context}
        @keyword depth: An optional depth buffer attachment.
        @type depth: L{Texture}
        @keyword stencil: An optional stencil buffer attachment.
        @type stencil: L{Texture}
        """

        super(Framebuffer, self).__init__(context=kwargs.pop("context", None))
        self._attachments = {}
        
        if isinstance(attachments, dict):
            attachments = dict(attachments)
        else:
            attachments = dict(enumerate(attachments))
        for i in range(self._context.max_color_attachments):
            self[i] = attachments.pop(i, None)
        if attachments:
            raise ValueError("framebuffer has no attachment(s) %s" % ", ".join("'%s'" % x for x in attachments.keys()))

        self.depth = kwargs.pop("depth", None)
        self.stencil = kwargs.pop("stencil", None)

        if kwargs:
            raise TypeError("__init__() got an unexpected keyword argument '%s'" % kwargs.keys()[0])

        self._initialized = True

    def __getitem__(self, index):
        return self._attachments[index]

    def __setitem__(self, index, value):
        self.attach(index, value)

    def __delitem__(self, index):
        self.attach(index, None)

    def _on_bind(self):
        """Setup global framebuffer related state.

        @todo: Setup C{color_writemasks}, C{depth_writemasks}, C{blend_funcs}, C{blend_equations}, and C{depth_ranges} after C{viewport}.
        """

        if self._initialized:
            self._stack.append(self._context.draw_buffers)
            self._context.draw_buffers = [i if self[i] is not None else None for i in range(self._context.max_color_attachments)]

            self._stack.append(self._context.viewport)
            if self.shape is not None:
                self._context.viewport = (0, 0) + self.shape

    def _on_release(self):
        """Restore global framebuffer related state.

        @todo: Restore C{depth_ranges}, C{blend_equations}, C{blend_funcs}, C{depth_writemasks}, and C{color_writemasks} before C{viewport}.
        """

        if self._initialized:
            self._context.viewport = self._stack.pop()
            self._context.draw_buffers = self._stack.pop()

    def _attach(self, attachment, texture=None, layer=None, level=0):
        """Attach a texture to an attachment.

        C{texture} may be a (texture, layer) tuple generated by
        L{Texture}C{.__getitem__()}.
        """

        if type(texture) is tuple:
            if layer is not None:
                raise ValueError("cannot provide layer as both keyword and texture tuple")
            texture, layer = texture
            return self._attach(attachment, texture, layer, level)

        with self:
            if texture is None:
                _gl.glFramebufferTextureLayer(self._target, attachment, 0, level, 0)
            elif layer is None:
                _gl.glFramebufferTexture(self._target, attachment, texture._id, level)
            else:
                _gl.glFramebufferTextureLayer(self._target, attachment, texture._id, level, layer)

    def attach(self, index, texture=None, layer=None, level=0):
        """Attach a texture to color attachment C{index}.

        C{texture} may be a (texture, layer) tuple generated by
        L{Texture}C{.__getitem__()}.  Otherwise, C{layer} specifies which
        texture layer is to be bound. All layers are bound when C{layer} is
        C{None}.

        C{level} specifies which resolution level of the texture is to be
        bound.

        If C{texture} is C{None}, the attachment will be unbound.
        """

        self._attach(_gl.GL_COLOR_ATTACHMENT0 + index, texture, layer, level)
        self._attachments[index] = texture

    @property
    def depth(self):
        if not hasattr(self, "_depth"):
            return None
        return self._depth

    @depth.setter
    def depth(self, depth):
        self.attach_depth(depth)

    @depth.deleter
    def depth(self):
        self.attach_depth(None)

    def attach_depth(self, texture=None, layer=None, level=0):
        """Attach a texture to the depth attachment.

        C{texture} may be a (texture, layer) tuple generated by
        L{Texture}C{.__getitem__()}.  Otherwise, C{layer} specifies which
        texture layer is to be bound. All layers are bound when C{layer} is
        C{None}.

        C{level} specifies which resolution level of the texture is to be
        bound.

        If C{texture} is C{None}, the attachment will be unbound.
        """

        self._attach(_gl.GL_DEPTH_ATTACHMENT, texture, layer, level)
        self._depth = texture

    @property
    def stencil(self):
        if not hasattr(self, "_stencil"):
            return None
        return self._stencil

    @stencil.setter
    def stencil(self, stencil):
        self.attach_stencil(stencil)

    @stencil.deleter
    def stencil(self):
        self.attach_stencil(None)

    def attach_stencil(self, texture=None, layer=None, level=0):
        """Attach a texture to the stencil attachment.

        C{texture} may be a (texture, layer) tuple generated by
        L{Texture}C{.__getitem__()}.  Otherwise, C{layer} specifies which
        texture layer is to be bound. All layers are bound when C{layer} is
        C{None}.

        C{level} specifies which resolution level of the texture is to be
        bound.

        If C{texture} is C{None}, the attachment will be unbound.
        """

        self._attach(_gl.GL_STENCIL_ATTACHMENT, texture, layer, level)
        self._stencil = texture

    @property
    def status(self):
        """The framebuffer completeness status.

        @rtype: L{Framebuffer.framebuffer_status} enum
        """

        with self:
            return self.framebuffer_status[_gl.glCheckFramebufferStatus(self._target)]

    @property
    def shape(self):
        shape = None
        for i, attachment in sorted(self._attachments.items()):
            if attachment is not None:
                if type(attachment) is tuple:
                    texture, layer = attachment
                    shape = (min(shape[0], texture.shape[1]), min(shape[1], texture.shape[2])) if shape else texture.shape[1:3]
                else:
                    shape = (min(shape[0], attachment.shape[0]), min(shape[1], attachment.shape[1])) if shape else attachment.shape[:2]
        if self.depth is not None:
            shape = (min(shape[0], self.depth.shape[0]), min(shape[1], self.depth.shape[1])) if shape else self.depth.shape[:2]
        if self.stencil is not None:
            shape = (min(shape[0], self.stencil.shape[0]), min(shape[1], self.stencil.shape[1])) if shape else self.stencil.shape[:2]
        return shape

    def clear(self, color=None, depth=None, stencil=None):
        """Clear the framebuffer.

        @param color: Whether to clear the color buffer, and optionally, to which value.
        @type color: C{bool} or C{numpy.ndarray}.
        @param depth: Whether to clear the depth buffer, and optionally, to which value.
        @type depth: C{bool} or C{numpy.ndarray}.
        @param stencil: Whether to clear the stencil buffer, and optionally, to which value.
        @type stencil: C{bool} or C{numpy.ndarray}.

        If no parameters are given, color, depth and stencil are cleared with
        the current clear values.

        @todo: Use C{glClearBuffer} to clear selected attachments only.
        """

        with self:
            self._context._perform_gl_clear(color, depth, stencil)

__all__ = ["Framebuffer"]

