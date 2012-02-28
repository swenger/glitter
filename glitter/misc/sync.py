from rawgl import gl as _gl

from glitter.utils.objects import ManagedObject
from glitter.utils import constants

class Sync(ManagedObject):
    _delete_id = _gl.glDeleteSync

    # TODO properties via glGetSynciv

class FenceSync(Sync):
    _generate_id = lambda: _gl.glFenceSync(_gl.GL_SYNC_GPU_COMMANDS_COMPLETE, 0)

    client_wait_sync_returns = constants.client_wait_sync_returns

    def wait(self):
        _gl.glWaitSync(self._id, 0, _gl.GL_TIMEOUT_IGNORED)

    def client_wait(self):
        return self.client_wait_sync_returns[_gl.glClientWaitSync(self._id, _gl.GL_SYNC_FLUSH_COMMANDS_BIT, _gl.GL_TIMEOUT_IGNORED)]

__all__ = ["Sync", "FenceSync"]

