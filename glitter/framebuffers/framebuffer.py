from itertools import izip_longest as _zip
from rawgl import gl as _gl

from glitter.utils import BindableObject, ManagedObject, constants

# TODO binding as read_framebuffer_binding, glBlitFramebuffer, glCopyTexSubImage
class Framebuffer(BindableObject, ManagedObject):
    _generate_id = _gl.glGenFramebuffers
    _delete_id = _gl.glDeleteBuffers
    _db = "framebuffers"
    _binding = "draw_framebuffer_binding"
    _target = _gl.GL_DRAW_FRAMEBUFFER

    framebuffer_status = constants.framebuffer_status

    def __init__(self, attachments=[], depth=None, stencil=None):
        super(Framebuffer, self).__init__()
        self._attachments = {}
        for i, attachment in _zip(range(self._context.max_color_attachments), attachments, fillvalue=None):
            self[i] = attachment
        self.depth = depth
        self.stencil = stencil

    def __getitem__(self, index):
        return self._attachments[index]

    def __setitem__(self, index, value):
        self.attach(index, value)

    def __delitem__(self, index):
        self.attach(index, None)

    def _on_bind(self):
        self._stack.append(self._context.draw_buffers)
        self._context.draw_buffers = [i if self[i] is not None else None for i in range(len(self._attachments))]
        # TODO does this work correctly during __init__?
        # TODO set viewport, color_writemask, depth_writemask, blend_func, blend_equation, depth_range

    def _on_release(self):
        # TODO reset viewport, color_writemask, depth_writemask, blend_func, blend_equation, depth_range
        self._context.draw_buffers = self._stack.pop()

    def attach(self, index, texture=None, level=0):
        with self:
            if texture is None:
                _gl.glFramebufferTextureLayer(self._target, _gl.GL_COLOR_ATTACHMENT0 + index, 0, level, 0)
            else:
                _gl.glFramebufferTexture(self._target, _gl.GL_COLOR_ATTACHMENT0 + index, 0 if texture is None else texture._id, level)
        self._attachments[index] = texture

    # TODO properties for viewport, color_writemask, depth_writemask, blend_func, blend_equation, depth_range (glDepthRangeArray, glDepthRangeIndexed)

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, depth):
        self.attach_depth(depth)

    @depth.deleter
    def depth(self):
        self.attach_depth(None)

    def attach_depth(self, texture=None, level=0):
        with self:
            if texture is None:
                _gl.glFramebufferTextureLayer(self._target, _gl.GL_DEPTH_ATTACHMENT, 0, level, 0)
            else:
                _gl.glFramebufferTexture(self._target, _gl.GL_DEPTH_ATTACHMENT, 0 if texture is None else texture._id, level)
        self._depth = texture

    @property
    def stencil(self):
        return self._stencil

    @stencil.setter
    def stencil(self, stencil):
        self.attach_stencil(stencil)

    @stencil.deleter
    def stencil(self):
        self.attach_stencil(None)

    def attach_stencil(self, texture=None, level=0):
        with self:
            if texture is None:
                _gl.glFramebufferTextureLayer(self._target, _gl.GL_STENCIL_ATTACHMENT, 0, level, 0)
            else:
                _gl.glFramebufferTexture(self._target, _gl.GL_STENCIL_ATTACHMENT, 0 if texture is None else texture._id, level)
        self._stencil = texture

    def check(self):
        with self:
            return self.framebuffer_status[_gl.glCheckFramebufferStatus(self._target)]

    def clear(self, color=None, depth=None, stencil=None): # TODO glClearBuffer for clearing selected attachments
        with self:
            self._context._clear(color, depth, stencil)

__all__ = ["Framebuffer"]

