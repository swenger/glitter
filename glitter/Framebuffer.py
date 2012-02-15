import gllib

from util import InstanceDescriptorMixin, Binding

BINDINGS = {
        gllib.GL_FRAMEBUFFER: gllib.GL_FRAMEBUFFER_BINDING,
        gllib.GL_DRAW_FRAMEBUFFER: gllib.GL_DRAW_FRAMEBUFFER_BINDING,
        gllib.GL_READ_FRAMEBUFFER: gllib.GL_READ_FRAMEBUFFER_BINDING,
        }

class Framebuffer(InstanceDescriptorMixin):
    def __init__(self, id=None):
        if id is None:
            id = gllib.glGenFramebuffers()
        if not gllib.IsFramebuffer(id):
            raise ValueError("not a framebuffer")
        self.id = id

        for i in range(gllib.glGet(gllib.GL_MAX_COLOR_ATTACHMENTS)):
            setattr(self, "color_attachment%d" % i, Attachment(gllib.GL_COLOR_ATTACHMENT0 + i))

    def __del__(self):
        try:
            gllib.glDeleteFramebuffers(self.id)
        except:
            pass

    def __call__(self, target=gllib.GL_FRAMEBUFFER):
        return FramebufferBinding(target, self.id)

class Attachment(object):
    def __init__(self, target):
        self.target = target

    def __get__(self, instance, owner):
        with instance():
            pass # TODO

    def __set__(self, instance, value):
        with instance():
            pass # TODO call gllib.glFramebufferTexture

class FramebufferBinding(Binding):
    def __init__(self, target, id=0):
        self.target = target
        self.id = id

    def get(self):
        return gllib.glGet(BINDINGS[self.target])

    def set(self, id):
        gllib.glBindFramebuffer(self.target, id)

