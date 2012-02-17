from rawgl import gl as _gl

from util import BindableObject

# TODO

class ShaderProgram(BindableObject):
    _generate_id = _gl.glCreateProgram
    _delete_id = _gl.glDeleteProgram
    _bind = _gl.glUseProgram
    _binding = _gl.GL_CURRENT_PROGRAM

    def __init__(self):
        super(ShaderProgram, self).__init__()

    # TODO glAttachShader, glLinkProgram, glGetProgramInfoLog etc.

