``glitter`` is an intuitive wrapper around OpenGL 3 and up.

Code example
============

The following code creates a window displaying a rotating quad::

    from math import cos, sin
    from glitter import VertexArray, get_default_program
    from glitter.contexts.glut import GlutWindow, main_loop, get_elapsed_time

    vertices = ((0, 0, 0), (-1, 1, 0), (1, 1, 0), (1, -1, 0), (-1, -1, 0))
    colors = ((1, 1, 1), (0, 1, 0), (0, 0, 1), (0, 1, 1), (1, 0, 0))
    indices = ((0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 1))

    def display():
        window.clear()
        vao.draw()
        window.swap_buffers()

    def timer():
        phi = get_elapsed_time()
        shader.modelview_matrix = (
			( cos(phi), sin(phi), 0, 0),
			(-sin(phi), cos(phi), 0, 0),
			(        0,        0, 1, 0),
			(        0,        0, 0, 2)
		)
        window.add_timer(10, timer)
        window.post_redisplay()

    if __name__ == "__main__":
        window = GlutWindow(double=True, multisample=True)
        window.display_callback = display
        shader = get_default_program()
        vao = VertexArray([vertices, colors], elements=indices)
        timer()
        with shader:
            main_loop()

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

- installing: ``sudo python setup.py install``

- docs: ``cd docs; ./build.sh``

- tests: ``nosetests tests``

- installing with Python 3: run ``python setup.py build`` with Python 2, then
  ``2to3 -w build`` and manually install the files from the build folder

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

Changelog
=========

The following versions introduced noteworthy features, bug fixes, or API changes:

version 0.1.7
-----------
- Fix GLUT modifier key functions.
- Add rudimentary support for ``glReadPixels`` on ``Context`` objects.
- Fix glActiveTexture call when calling bind() on already bound ``Texture``.

version 0.1.6
-------------
- Add support for depth and stencil textures.
- Additional examples.
- Python 3 compatibility (built distribution only, not build script).
- Add GLX and dummy contexts (GLX context via separate glxcontext package), GLX is now the default if available.
- Fix ``Framebuffer`` viewport.
- Rename and add parameters to copy pipeline.
- Add convenience matrix functions.
- Fix setattr bug in ``Pipeline``.

version 0.1.5
-------------
- Add support for integer sampler types in ``glitter.convenience``.

version 0.1.4
-------------
- ``Framebuffer``\s expect attributes as separate ``__init__()`` parameters instead of a list.
- Implement mesh loading from HDF5.
- Fix context bugs in ``VertexArray``, ``Pipeline``, and ``ShaderProgram``.
- Fix shader proxies in ``Pipeline``.
- ``Pipeline`` now uses the currently bound framebuffer instead of the default framebuffer.
- Add context properties to ``Pipeline``.

version 0.1.3
-------------

- Introduce literate example programs.
- ``ArrayBuffer``\s determine the primitive type and check the buffer dimensions separately.
- ``GLObject``\s accept a ``context`` parameter to ``__init__()``.
- ``VertexArray``\s expect attributes as separate ``__init__()`` parameters instead of a list.
- Fix bug in ``ContextManger`` (did not call ``_bind()``) and add caching.
- Cast parameters that should be ``EnumConstant``\s into the appropriate types and accept constant names in addition to constant objects.
- Add Qt support via PySide or PyQt4.
- Add plausibility checks to avoid huge memory allocation when a ``Context`` object was created without a valid OpenGL context.
- Make color and modelview matrix optional in ``defaultpipeline``.

