from rawgl import gl as _gl

class ProgramPipeline(object): # TODO
    def __init__(self, id=None):
        if id is None:
            id = _gl.glGenProgramPipelines()
        if not _gl.IsProgramPipeline(id):
            raise ValueError("not a program pipeline")
        self.id = id

    def __del__(self):
        try:
            _gl.glDeleteProgramPipelines(self.id)
        except:
            pass

    def bind(self):
        old_binding = _gl.glGet(_gl.GL_PROGRAM_PIPELINE_BINDING)
        _gl.glBindProgramPipeline(self.id)
        return old_binding

