from rawgl import gl as _gl

from glitter.util import BindableObject, ManagedObject

class ProgramPipeline(BindableObject, ManagedObject): # TODO
    _generate_id = _gl.glGenProgramPipelines
    _delete_id = _gl.glDeleteProgramPipelines
    _db = "program_pipelines"
    _binding = "program_pipeline_binding"

    def __init__(self):
        super(ProgramPipeline, self).__init__()

__all__ = ["ProgramPipeline"]

