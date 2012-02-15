import gllib

BINDINGS = {
        gllib.GL_ARRAY_BUFFER: gllib.GL_ARRAY_BUFFER_BINDING,
        gllib.GL_ATOMIC_COUNTER_BUFFER: gllib.GL_ATOMIC_COUNTER_BUFFER_BINDING,
        gllib.GL_COPY_READ_BUFFER: gllib.GL_COPY_READ_BUFFER_BINDING,
        gllib.GL_COPY_WRITE_BUFFER: gllib.GL_COPY_WRITE_BUFFER_BINDING,
        gllib.GL_DRAW_INDIRECT_BUFFER: gllib.GL_DRAW_INDIRECT_BUFFER_BINDING,
        gllib.GL_ELEMENT_ARRAY_BUFFER: gllib.GL_ELEMENT_ARRAY_BUFFER_BINDING,
        gllib.GL_PIXEL_PACK_BUFFER: gllib.GL_PIXEL_PACK_BUFFER_BINDING,
        gllib.GL_PIXEL_UNPACK_BUFFER: gllib.GL_PIXEL_UNPACK_BUFFER_BINDING,
        gllib.GL_TEXTURE_BUFFER: None, # ???
        gllib.GL_TRANSFORM_FEEDBACK_BUFFER: gllib.GL_TRANSFORM_FEEDBACK_BUFFER_BINDING,
        gllib.GL_UNIFORM_BUFFER: gllib.GL_UNIFORM_BUFFER_BINDING,
        }

class Buffer(object):
    def __init__(self, id=None):
        if id is None:
            id = gllib.glGenBuffers()
        if not gllib.glIsBuffer(id):
            raise ValueError("not a buffer")
        self.id = id
    
    def __del__(self):
        try:
            gllib.glDeleteBuffers(self.id)
        except:
            pass

    def bind(self, target):
        old_binding = gllib.glGet(BINDINGS[target])
        gllib.glBindBuffers(target, self.id)
        return old_binding

