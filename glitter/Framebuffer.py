from rawgl import gl as _gl

from util import BindableObject, Enum, EnumConstant

# TODO binding to different targets

_framebuffer_targets = [
        (_gl.GL_FRAMEBUFFER,      _gl.GL_FRAMEBUFFER_BINDING),
        (_gl.GL_DRAW_FRAMEBUFFER, None                      ), # XXX why is there no GL_DRAW_FRAMEBUFFER_BINDING?
        (_gl.GL_READ_FRAMEBUFFER, None                      ), # XXX why is there no GL_READ_FRAMEBUFFER_BINDING?
]
_framebuffer_target_to_binding = dict((x[0], x[1]) for x in _framebuffer_targets)

class Framebuffer(BindableObject):
    _generate_id = _gl.glGenFramebuffers
    _delete_id = _gl.glDeleteBuffers
    _bind = _gl.glBindFramebuffer
    _target = _gl.GL_FRAMEBUFFER
    _binding = _framebuffer_target_to_binding[_target]

    attachment_names = Enum(
            DEPTH=_gl.GL_DEPTH_ATTACHMENT,
            STENCIL=_gl.GL_STENCIL_ATTACHMENT,
            DEPTH_STENCIL=_gl.GL_DEPTH_STENCIL_ATTACHMENT,
    )

    def __init__(self):
        super(Framebuffer, self).__init__()

    def attach(self, attachment, texture=None, level=0):
        _texture = texture._id if texture is not None else 0
        _attachment = attachment._value if isinstance(attachment, EnumConstant) else _gl.GL_COLOR_ATTACHMENT0 + attachment
        with self:
            _gl.glFramebufferTexture(self._target, _attachment, _texture, level)

    # TODO get and set attachments using a proxy and __getitem__/__setitem__; needs a texture database

