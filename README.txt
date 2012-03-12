Intuitive OpenGL wrappers.

Design principles:
  - Choose inituitive use over performance (no premature optimization; make it
	run, then make it fast). Users should not (need to) use the raw GL/GLUT
	wrappers at any time.
  - All GL state changes that are independent of objects should go through a
	Context object. Other changes go through the corresponding objects:
	  - Vertex attribute pointer bindings are performed by vertex array objects
		only.
	  - Settings for draw buffers other than the screen are performed by
		framebuffer objects only.
	  - Texture bindings are performed by shader programs only.
	  - If possible, changes in the GL should be reflected in the wrapper, but
		unchecked caching is okay to keep references to bound objects.
  - Array data is represented in numpy, but objects should convert as
	appropriate.
	  - No loss of precision should occur when copying data to and from the
		GPU. Exceptions are made where iterables are accepted; numpy
		converts these to 64 bit datatypes, which are silently converted to 32
		bit in some places.
  - Binding and unbinding of objects should be possible automatically (via with
	statements) as well as manually (through properties of the context).
  - The library has a focus on GPGPU computing, but typical use for rendering
	should be as easy.
  - Platform independence should be sought for, although Linux/GLX is the
	primary target.

Dependencies:
  - gccxml: www.gccxml.org
  - ctypeslib: pypi.python.org/pypi/ctypeslib/

Build instructions:
  - installing: sudo python setup.py install
  - docs: epydoc --html -v -o docs glitter examples tests
  - tests: nosetests tests

The distribution includes the official OpenGL 3 header file from
http://www.opengl.org/registry/api/gl3.h, with the following bugfixes applied:

The following functions are not part of the core profile and have been removed:
GLAPI void APIENTRY glVertexP2ui (GLenum type, GLuint value);
GLAPI void APIENTRY glVertexP2uiv (GLenum type, const GLuint *value);
GLAPI void APIENTRY glVertexP3ui (GLenum type, GLuint value);
GLAPI void APIENTRY glVertexP3uiv (GLenum type, const GLuint *value);
GLAPI void APIENTRY glVertexP4ui (GLenum type, GLuint value);
GLAPI void APIENTRY glVertexP4uiv (GLenum type, const GLuint *value);
GLAPI void APIENTRY glTexCoordP1ui (GLenum type, GLuint coords);
GLAPI void APIENTRY glTexCoordP1uiv (GLenum type, const GLuint *coords);
GLAPI void APIENTRY glTexCoordP2ui (GLenum type, GLuint coords);
GLAPI void APIENTRY glTexCoordP2uiv (GLenum type, const GLuint *coords);
GLAPI void APIENTRY glTexCoordP3ui (GLenum type, GLuint coords);
GLAPI void APIENTRY glTexCoordP3uiv (GLenum type, const GLuint *coords);
GLAPI void APIENTRY glTexCoordP4ui (GLenum type, GLuint coords);
GLAPI void APIENTRY glTexCoordP4uiv (GLenum type, const GLuint *coords);
GLAPI void APIENTRY glMultiTexCoordP1ui (GLenum texture, GLenum type, GLuint coords);
GLAPI void APIENTRY glMultiTexCoordP1uiv (GLenum texture, GLenum type, const GLuint *coords);
GLAPI void APIENTRY glMultiTexCoordP2ui (GLenum texture, GLenum type, GLuint coords);
GLAPI void APIENTRY glMultiTexCoordP2uiv (GLenum texture, GLenum type, const GLuint *coords);
GLAPI void APIENTRY glMultiTexCoordP3ui (GLenum texture, GLenum type, GLuint coords);
GLAPI void APIENTRY glMultiTexCoordP3uiv (GLenum texture, GLenum type, const GLuint *coords);
GLAPI void APIENTRY glMultiTexCoordP4ui (GLenum texture, GLenum type, GLuint coords);
GLAPI void APIENTRY glMultiTexCoordP4uiv (GLenum texture, GLenum type, const GLuint *coords);
GLAPI void APIENTRY glNormalP3ui (GLenum type, GLuint coords);
GLAPI void APIENTRY glNormalP3uiv (GLenum type, const GLuint *coords);
GLAPI void APIENTRY glColorP3ui (GLenum type, GLuint color);
GLAPI void APIENTRY glColorP3uiv (GLenum type, const GLuint *color);
GLAPI void APIENTRY glColorP4ui (GLenum type, GLuint color);
GLAPI void APIENTRY glColorP4uiv (GLenum type, const GLuint *color);
GLAPI void APIENTRY glSecondaryColorP3ui (GLenum type, GLuint color);
GLAPI void APIENTRY glSecondaryColorP3uiv (GLenum type, const GLuint *color);

The following constants are missing and have been defined:
#define GL_POLYGON_MODE                   0x0B40

