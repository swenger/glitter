import gllib

class ProgramPipeline(object):
    def __init__(self, id=None):
        if id is None:
            id = gllib.glGenProgramPipelines()
        if not gllib.IsProgramPipeline(id):
            raise ValueError("not a program pipeline")
        self.id = id

    def __del__(self):
        try:
            gllib.glDeleteProgramPipelines(self.id)
        except:
            pass

    def bind(self):
        old_binding = gllib.glGet(gllib.GL_PROGRAM_PIPELINE_BINDING)
        gllib.glBindProgramPipeline(self.id)
        return old_binding

