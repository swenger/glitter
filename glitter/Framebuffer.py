from rawgl import gl as _gl

from util import BindableObject

# TODO binding to different targets
# TODO color and depth attachments

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

    def __init__(self):
        super(Framebuffer, self).__init__()

