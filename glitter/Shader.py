from rawgl import gl as _gl

from util import GLObject

# TODO

class Shader(GLObject):
    _generate_id = _gl.glCreateShader # TODO only one parameter!
    _delete_id = _gl.glDeleteShader # TODO only one parameter!
    # TODO no _bind, but glAttachShader / glDetachShader (with different semantics!)

    # TODO glShaderSource, glCompileShader, glGetShaderInfoLog etc.

