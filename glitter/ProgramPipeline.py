from rawgl import gl

class ProgramPipeline(object):
    def __init__(self, id=None):
        if id is None:
            id = gl.glGenProgramPipelines()
        if not gl.IsProgramPipeline(id):
            raise ValueError("not a program pipeline")
        self.id = id

    def __del__(self):
        try:
            gl.glDeleteProgramPipelines(self.id)
        except:
            pass

    def bind(self):
        old_binding = gl.glGet(gl.GL_PROGRAM_PIPELINE_BINDING)
        gl.glBindProgramPipeline(self.id)
        return old_binding

