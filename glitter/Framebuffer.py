from rawgl import gl as _gl

import constants
from util import BindableObject, EnumConstant

# TODO binding to different targets

class Framebuffer(BindableObject):
    _generate_id = _gl.glGenFramebuffers
    _delete_id = _gl.glDeleteBuffers
    _bind = _gl.glBindFramebuffer
    _target = _gl.GL_FRAMEBUFFER
    _binding = constants.framebuffer_target_to_binding[_target]

    attachment_names = constants.framebuffer_attachment_names

    def __init__(self):
        super(Framebuffer, self).__init__()

    def attach(self, attachment, texture=None, level=0):
        _texture = texture._id if texture is not None else 0
        _attachment = attachment._value if isinstance(attachment, EnumConstant) else _gl.GL_COLOR_ATTACHMENT0 + attachment
        with self:
            _gl.glFramebufferTexture(self._target, _attachment, _texture, level)

    # TODO get and set attachments using a proxy and __getitem__/__setitem__ and Texture._db

