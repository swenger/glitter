from rawgl import gl as _gl

import constants
from GLObject import ManagedObject, BindableObject
from util import EnumConstant

class Framebuffer(ManagedObject, BindableObject):
    _generate_id = _gl.glGenFramebuffers
    _delete_id = _gl.glDeleteBuffers
    _db = "framebuffers"
    _target = _gl.GL_FRAMEBUFFER
    _binding = "framebuffer_binding"

    attachment_names = constants.framebuffer_attachment_names

    def __init__(self, other=None):
        super(Framebuffer, self).__init__(other)

    def _clone_into(self, other):
        super(Framebuffer, self)._clone_into(self, other)

    def attach(self, attachment, texture=None, level=0):
        _texture = texture._id if texture is not None else 0
        _attachment = attachment._value if isinstance(attachment, EnumConstant) else _gl.GL_COLOR_ATTACHMENT0 + attachment
        with self:
            _gl.glFramebufferTexture(self._target, _attachment, _texture, level)

    # TODO get and set attachments using __getitem__/__setitem__

class DrawFramebuffer(Framebuffer): pass # TODO

class ReadFramebuffer(Framebuffer): pass # TODO

