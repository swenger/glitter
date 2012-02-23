from rawgl import gl as _gl

from GLObject import BindableObject

class Renderbuffer(BindableObject): # TODO
    _generate_id = _gl.glGenRenderbuffers
    _delete_id = _gl.glDeleteRenderbuffers
    _db = "renderbuffers"
    # TODO glFramebufferRenderbuffer instead of _bind; returns GLsync

