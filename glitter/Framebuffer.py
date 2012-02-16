from rawgl import gl as _gl

from util import InstanceDescriptorMixin, Binding # TODO factor commons of Buffer and Texture into util

BINDINGS = { # TODO
        _gl.GL_FRAMEBUFFER: _gl.GL_FRAMEBUFFER_BINDING,
        _gl.GL_DRAW_FRAMEBUFFER: _gl.GL_DRAW_FRAMEBUFFER_BINDING,
        _gl.GL_READ_FRAMEBUFFER: _gl.GL_READ_FRAMEBUFFER_BINDING,
        }

class Framebuffer(InstanceDescriptorMixin): # TODO
    def __init__(self, id=None):
        if id is None:
            id = _gl.glGenFramebuffers()
        if not _gl.IsFramebuffer(id):
            raise ValueError("not a framebuffer")
        self.id = id

        for i in range(_gl.glGet(_gl.GL_MAX_COLOR_ATTACHMENTS)):
            setattr(self, "color_attachment%d" % i, Attachment(_gl.GL_COLOR_ATTACHMENT0 + i))

    def __del__(self):
        try:
            _gl.glDeleteFramebuffers(self.id)
        except:
            pass

    def __call__(self, target=_gl.GL_FRAMEBUFFER):
        return FramebufferBinding(target, self.id)

class Attachment(object):
    def __init__(self, target):
        self.target = target

    def __get__(self, instance, owner):
        with instance():
            pass # TODO

    def __set__(self, instance, value):
        with instance():
            pass # TODO call _gl.glFramebufferTexture

class FramebufferBinding(Binding):
    def __init__(self, target, id=0):
        self.target = target
        self.id = id

    def get(self):
        return _gl.glGet(BINDINGS[self.target])

    def set(self, id):
        _gl.glBindFramebuffer(self.target, id)

