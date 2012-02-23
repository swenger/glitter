Design principles:
- The user should not need to use the raw GL/GLUT wrappers at any time.
- If possible, changes in the GL should be reflected in the wrapper, but unchecked caching is okay if it cannot easily be avoided (e.g. to keep references to bound shader objects).
- When choosing between inituitive use and performance, choose intuitive use (no premature optimization; make it run, then make it fast).
- Array data is represented in numpy, but objects should convert as appropriate.
- Objects should accept convenience constructor parameters (e.g. VertexArray, ShaderProgram).
- Binding and unbinding should be possible manually via bind(), or automatically via with statements.
- All GL state changes that are independent of objects should go through a Context object.
- Platform independence should be sought for, although Linux/GLX is the primary target.

TODO move tests to separate package
TODO use context's getters and setters in library, make sure to use "with self._context" where necessary
TODO create raw offscreen GLX context
TODO replace relative imports by absolute imports
TODO make rawgl replaceable



TODO:

# vertex attrib pointer bindings have to go through a vertex array object
# texture bindings have to go through a texture unit object or are automatically attached to one
# ids and bindings are only unique per context

ab0 = ArrayBuffer(random((32, 3)))
ab1 = ArrayBuffer(random((32, 3)))
eab = ElementArrayBuffer((random((16, 3)) * 32).astype(uint8))
vao = VertexArray([ab0, ab1], elements=eab)

shader = ShaderProgram(vertex=vertex_shader, fragment=fragment_shader)
shader.texture1 = Texture2D(random((32, 32, 3)).astype(float32))
shader.texture2 = Texture2D(random((32, 32, 3)).astype(float32))

fbo = FBO()
fbo.color_attachments[0] = shader.texture1
fbo.color_attachments[1] = shader.texture2

with shader:
	fbo.clear()
	vao.draw()



context.buffers[0] = Buffer(random((32, 3)))
context.array_buffer_binding = context.buffers[0]
context.element_array_buffer_binding = context.buffers[2]
context.vertex_arrays[0] = VertexArray(...)

context.shaders[0] = vertex_shader
context.shaders[1] = fragment_shader
context.shader_programs[0] = ShaderProgram(...)

context.textures[0] = Texture2D(...)




class Texture(object):
	_db = "textures"

class Texture2D(Texture):
	_binding = "texture_binding_2d"


class Buffer(object):
	_db = "buffers"

class ArrayBuffer(Buffer):
	_binding = "array_buffer_binding"


class BufferBindingProperty(property):
	# TODO

class Context(object):
	def __init__(self):
		self._buffers = WeakValueDictionary()
		self._array_buffer_binding = None

	@property
	def array_buffer_binding(self):
		return self._array_buffer_binding
	
	@array_buffer_binding.setter
	def array_buffer_binding(self, value):
		_gl.glBindBuffer(_gl.GL_ARRAY_BUFFER, value._id)
		self._array_buffer_binding = value
	
	@array_buffer_binding.deleter
	def array_buffer_binding(self):
		_gl.glBindBuffer(_gl.GL_ARRAY_BUFFER, 0)
		self._array_buffer_binding = None
	
	array_buffer_binding = BufferProperty(_gl.GL_ARRAY_BUFFER)

