from rawgl import gl as _gl

from util import GLObject

# TODO

class ShaderProgram(GLObject):
    _generate_id = _gl.glCreateProgram # TODO only one parameter!
    _delete_id = _gl.glDeleteProgram # TODO only one parameter!
    _bind = _gl.glUseProgram
    _binding = _gl.GL_CURRENT_PROGRAM

    def __init__(self):
        super(ShaderProgram, self).__init__()

    # TODO glAttachShader, glLinkProgram, glGetProgramInfoLog etc.

