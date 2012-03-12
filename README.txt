Intuitive OpenGL 3 wrappers.

Design principles
=================

- Glitter wraps the OpenGL 3 core profile only. This allows for a pythonic
  representation of (eventually) the complete OpenGL API, while any nuts and
  bolts are readily supplied by Python and numpy.

- Inituitive use is chosen over performance (no premature optimization; make it
  run, then make it fast). Users do not need to (nor should they) use raw GL
  functions at any time.

- OpenGL objects (e.g., textures, buffers, or shader programs) are represented
  by Python objects.

- All GL state changes go through either a context object or a responsible
  object, for example:

	- Vertex attribute pointer bindings are performed by vertex array objects.

	- Settings for draw buffers other than the screen are performed by
	  framebuffer objects.

	- Texture bindings are performed by shader programs. An available texture
	  unit is chosen automatically.

- Array data (e.g. texture images or vertex buffer data) is represented in
  numpy.

- Glitter has a focus on GPGPU computing, but typical use for rendering
  should be as easy.

- Platform independence is be sought for, although Linux/GLX is currently the
  primary target. Any experiences with other platforms are very welcome.

Dependencies
============

- gccxml: http://www.gccxml.org

- ctypeslib: http://pypi.python.org/pypi/ctypeslib

Build instructions
==================

- installing: `sudo python setup.py install`

- docs: `epydoc --html -v -o docs glitter examples tests`

- tests: `nosetests tests`

OpenGL 3 notes
==============

The distribution includes the official OpenGL 3 header file from
http://www.opengl.org/registry/api/gl3.h, with the following bugfixes applied:

The following functions are not part of the core profile and have been
removed::

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

The following constants are missing and have been defined::

    #define GL_POLYGON_MODE                   0x0B40

