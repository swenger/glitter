"""Sync classes.

@author: Stephan Wenger
@date: 2012-02-29
"""

import glitter.raw as _gl
from glitter.utils import ManagedObject, client_wait_sync_returns

class Sync(ManagedObject):
    """@todo: Implement properties using C{glGetSynciv}."""
    _delete_id = _gl.glDeleteSync

    def __init__(self, context=None):
        super(Sync, self).__init__(context=context)

class FenceSync(Sync):
    _generate_id = lambda: _gl.glFenceSync(_gl.GL_SYNC_GPU_COMMANDS_COMPLETE, 0)

    client_wait_sync_returns = client_wait_sync_returns

    def wait(self):
        _gl.glWaitSync(self._id, 0, _gl.GL_TIMEOUT_IGNORED)

    def client_wait(self):
        return self.client_wait_sync_returns[_gl.glClientWaitSync(self._id, _gl.GL_SYNC_FLUSH_COMMANDS_BIT, _gl.GL_TIMEOUT_IGNORED)]

__all__ = ["Sync", "FenceSync"]

