"""Renderbuffer object class.

@bug: Renderbuffers are currently unimplemented.

@author: Stephan Wenger
@date: 2012-02-29
"""

import glitter.raw as _gl
from glitter.utils import ManagedObject, BindableObject

class Renderbuffer(ManagedObject, BindableObject):
    """Renderbuffer class.
    
    @todo: Use C{glFramebufferRenderbuffer} instead of L{_binding}; returns C{GLsync}!
    @todo: Wrap C{glRenderbufferStorage} and C{glRenderbufferStorageMultisample}.
    """

    _generate_id = _gl.glGenRenderbuffers
    _delete_id = _gl.glDeleteRenderbuffers
    _db = "renderbuffers"

    def __init__(self, context=None):
        super(Renderbuffer, self).__init__(context=context)

__all__ = ["Renderbuffer"]

