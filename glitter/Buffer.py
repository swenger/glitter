from rawgl import gl

BINDINGS = {
        gl.GL_ARRAY_BUFFER: gl.GL_ARRAY_BUFFER_BINDING,
        gl.GL_ATOMIC_COUNTER_BUFFER: gl.GL_ATOMIC_COUNTER_BUFFER_BINDING,
        gl.GL_COPY_READ_BUFFER: gl.GL_COPY_READ_BUFFER_BINDING,
        gl.GL_COPY_WRITE_BUFFER: gl.GL_COPY_WRITE_BUFFER_BINDING,
        gl.GL_DRAW_INDIRECT_BUFFER: gl.GL_DRAW_INDIRECT_BUFFER_BINDING,
        gl.GL_ELEMENT_ARRAY_BUFFER: gl.GL_ELEMENT_ARRAY_BUFFER_BINDING,
        gl.GL_PIXEL_PACK_BUFFER: gl.GL_PIXEL_PACK_BUFFER_BINDING,
        gl.GL_PIXEL_UNPACK_BUFFER: gl.GL_PIXEL_UNPACK_BUFFER_BINDING,
        gl.GL_TEXTURE_BUFFER: None, # ???
        gl.GL_TRANSFORM_FEEDBACK_BUFFER: gl.GL_TRANSFORM_FEEDBACK_BUFFER_BINDING,
        gl.GL_UNIFORM_BUFFER: gl.GL_UNIFORM_BUFFER_BINDING,
        }

class Buffer(object):
    def __init__(self, id=None):
        if id is None:
            id = gl.glGenBuffers()
        if not gl.glIsBuffer(id):
            raise ValueError("not a buffer")
        self.id = id
    
    def __del__(self):
        try:
            gl.glDeleteBuffers(self.id)
        except:
            pass

    def bind(self, target):
        old_binding = gl.glGet(BINDINGS[target])
        gl.glBindBuffers(target, self.id)
        return old_binding

