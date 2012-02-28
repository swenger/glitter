Design principles:
- The user should not (need to) use the raw GL/GLUT wrappers at any time.
- The library has a focus on GPGPU computing, but standard usage should also be possible.
- No loss of precision should occur when copying data to and from the GPU.
- If possible, changes in the GL should be reflected in the wrapper, but unchecked caching is okay to keep references to bound objects.
- Choose inituitive use over performance (no premature optimization; make it run, then make it fast).
- Array data is represented in numpy, but objects should convert as appropriate.
- Objects should accept convenience constructor parameters (e.g. VertexArray, ShaderProgram).
- Binding and unbinding should be possible automatically (via with statements) as well as manually.
- All GL state changes that are independent of objects should go through a Context object. Other changes go through the corresponding objects:
  - Vertex attribute pointer bindings are performed by vertex array objects only.
  - Settings for draw buffers other than the screen are performed by framebuffer objects only.
  - Texture bindings are performed by shader programs only.
- Platform independence should be sought for, although Linux/GLX is the primary target.

Remember:
- IDs and bindings are only unique per context!
- glBindBuffer and glBindBufferRange/glBindBufferBase interfer with each other!
- when using enums, import them into the corresponding class
- docs: epydoc --html glitter
- tests: nosetests tests

TODO:
- contexts:
  - add a generic mechanism for setting and resetting state and use it (instead of maintaining stacks in objects)
  - use context's getters and setters in library, make sure to use "with self._context" where necessary
  - create a raw offscreen GLX context class with context generation and switching and a GLUT context class (or make GlutWindow a Context subclass)
- make rawgl replaceable
- transparent CUDA and OpenCL interoperability
- write documentation and tests

