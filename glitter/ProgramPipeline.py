from rawgl import gl as _gl

from GLObject import BindableObject

class ProgramPipeline(BindableObject): # TODO
    _generate_id = _gl.glGenProgramPipelines
    _delete_id = _gl.glDeleteProgramPipelines
    _binding = "program_pipeline_binding"

    def __init__(self):
        super(ProgramPipeline, self).__init__()

