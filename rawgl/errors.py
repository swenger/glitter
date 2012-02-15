import gl

class GLError(Exception):
    def __init__(self, error, result, func, arguments):
        self.error = error
        self.result = result
        self.func = func
        self.arguments = arguments

    def __str__(self):
        return "OpenGL error #%d (%s) in %s(%s)" % (self.error, errname(self.error), self.func.__name__, ", ".join(map(repr, self.arguments)))

def errcheck(result, func, arguments):
    error = gl.glGetError()
    if error != gl.GL_NO_ERROR:
        raise GLError(error, result, func, arguments)

def errname(error):
    try:
        import glu
        return gl.string_at(glu.gluErrorString(error))
    except ImportError:
        candidates = [key for key, value in gl.__dict__.items() if key.startswith("GL_") and value == error]
        return "/".join(candidates)

