from rawgl import gl as _gl

from GLObject import ManagedObject, BindableObject

class ProgramPipeline(ManagedObject, BindableObject): # TODO
    _generate_id = _gl.glGenProgramPipelines
    _delete_id = _gl.glDeleteProgramPipelines
    _db = "program_pipelines"
    _binding = "program_pipeline_binding"

    def __init__(self):
        super(ProgramPipeline, self).__init__()

