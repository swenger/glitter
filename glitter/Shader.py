from rawgl import gl as _gl

from util import GLObject

# TODO

class Shader(GLObject):
    _generate_id = _gl.glCreateShader
    _delete_id = _gl.glDeleteShader

    # TODO glShaderSource, glCompileShader, glGetShaderInfoLog etc.

