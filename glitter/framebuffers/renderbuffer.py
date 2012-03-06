"""Renderbuffer object class.

@bug: Renderbuffers are currently unimplemented.

@author: Stephan Wenger
@date: 2012-02-29
"""

from rawgl import gl as _gl

from glitter.utils import BindableObject, ManagedObject

class Renderbuffer(BindableObject, ManagedObject):
    """Renderbuffer class.
    
    @todo: Use C{glFramebufferRenderbuffer} instead of L{_binding}; returns C{GLsync}!
    @todo: Wrap C{glRenderbufferStorage} and C{glRenderbufferStorageMultisample}.
    """

    _generate_id = _gl.glGenRenderbuffers
    _delete_id = _gl.glDeleteRenderbuffers
    _db = "renderbuffers"

__all__ = ["Renderbuffer"]

