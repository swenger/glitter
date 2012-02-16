import gl

class GLError(Exception):
    def __init__(self, error, result, func, arguments):
        self.error = error
        self.result = result
        self.func = func
        self.arguments = arguments

    def format_arguments(self):
        return ", ".join([resolve_constant(x) if self.func.argtypes[i] == gl.GLenum else repr(x) for i, x in enumerate(self.arguments)])

    def __str__(self):
        return "OpenGL error #%d (%s) in %s(%s)" % (self.error, errname(self.error), self.func.__name__, self.format_arguments())

    def __repr__(self):
        return str(self)

def errcheck(result, func, arguments):
    error = gl.glGetError()
    if error != gl.GL_NO_ERROR:
        raise GLError(error, result, func, arguments)

def resolve_constant(constant):
    candidates = [key for key, value in gl.__dict__.items() if key.startswith("GL_") and value == constant]
    return "/".join(candidates) if candidates else constant

def errname(error):
    try:
        import glu
        return gl.string_at(glu.gluErrorString(error))
    except (ImportError, AttributeError):
        return resolve_constant(error)

