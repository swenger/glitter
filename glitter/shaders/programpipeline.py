"""Program pipeline class.

@author: Stephan Wenger
@date: 2012-02-29
"""

from rawgl import gl as _gl

from glitter.utils import BindableObject, ManagedObject

class ProgramPipeline(BindableObject, ManagedObject): # TODO glUseProgramStages, glValidateProgramPipeline etc.
    _generate_id = _gl.glGenProgramPipelines
    _delete_id = _gl.glDeleteProgramPipelines
    _db = "program_pipelines"
    _binding = "program_pipeline_binding"

    def __init__(self):
        super(ProgramPipeline, self).__init__()

__all__ = ["ProgramPipeline"]

