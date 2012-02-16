from rawgl import gl

from util import InstanceDescriptorMixin, Binding

BINDINGS = {
        gl.GL_FRAMEBUFFER: gl.GL_FRAMEBUFFER_BINDING,
        gl.GL_DRAW_FRAMEBUFFER: gl.GL_DRAW_FRAMEBUFFER_BINDING,
        gl.GL_READ_FRAMEBUFFER: gl.GL_READ_FRAMEBUFFER_BINDING,
        }

class Framebuffer(InstanceDescriptorMixin):
    def __init__(self, id=None):
        if id is None:
            id = gl.glGenFramebuffers()
        if not gl.IsFramebuffer(id):
            raise ValueError("not a framebuffer")
        self.id = id

        for i in range(gl.glGet(gl.GL_MAX_COLOR_ATTACHMENTS)):
            setattr(self, "color_attachment%d" % i, Attachment(gl.GL_COLOR_ATTACHMENT0 + i))

    def __del__(self):
        try:
            gl.glDeleteFramebuffers(self.id)
        except:
            pass

    def __call__(self, target=gl.GL_FRAMEBUFFER):
        return FramebufferBinding(target, self.id)

class Attachment(object):
    def __init__(self, target):
        self.target = target

    def __get__(self, instance, owner):
        with instance():
            pass # TODO

    def __set__(self, instance, value):
        with instance():
            pass # TODO call gl.glFramebufferTexture

class FramebufferBinding(Binding):
    def __init__(self, target, id=0):
        self.target = target
        self.id = id

    def get(self):
        return gl.glGet(BINDINGS[self.target])

    def set(self, id):
        gl.glBindFramebuffer(self.target, id)

