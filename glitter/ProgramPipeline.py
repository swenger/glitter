from rawgl import gl as _gl

from util import GLObject

# TODO

class ProgramPipeline(GLObject):
    _generate_id = _gl.glGenProgramPipelines
    _delete_id = _gl.glDeleteProgramPipelines
    _bind = _gl.glBindProgramPipeline
    _binding = _gl.GL_PROGRAM_PIPELINE_BINDING

    def __init__(self):
        super(ProgramPipeline, self).__init__()

