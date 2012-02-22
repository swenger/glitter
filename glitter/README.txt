Design principles:
- The user should not need to use the raw GL/GLUT wrappers at any time.
- If possible, changes in the GL should be reflected in the wrapper, but unchecked caching is okay if it cannot easily be avoided (e.g. to keep references to bound shader objects).
- When choosing between inituitive use and performance, choose intuitive use (no premature optimization; make it run, then make it fast).
- Array data is represented in numpy, but objects should convert as appropriate.
- Objects should accept convenience constructor parameters (e.g. VertexArray, ShaderProgram).
- Binding and unbinding should be possible manually via bind(), or via with statements.
- All GL state changes that are independent of objects should go through a Context object.
- Platform independence should be sought for, although Linux/GLX is the primary target.

TODO use own dtypes
TODO automatic casts into numpy arrays, cast float64 to float32
TODO move tests to separate package
TODO move constant tables to separate package
TODO use context's getters and setters in library
TODO create raw offscreen GLX context
TODO for each bind()able object, have a context function to return the current binding only
TODO replace relative imports by absolute imports
TODO make rawgl replaceable

