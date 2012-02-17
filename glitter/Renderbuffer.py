from rawgl import gl as _gl

from util import BindableObject

# TODO

class Renderbuffer(BindableObject):
    _generate_id = _gl.glGenRenderbuffers
    _delete_id = _gl.glDeleteRenderbuffers
    # TODO glFramebufferRenderbuffer instead of _bind; returns GLsync

