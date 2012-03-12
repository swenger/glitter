"""Automatic error checking for GL calls.
"""

import re

class GLError(Exception):
    """Exception representing an error within OpenGL.
    """

    def __init__(self, error, result, func, arguments):
        self.error = error
        self.result = result
        self.func = func
        self.arguments = arguments

    @staticmethod
    def string_from_id(error):
        """Lookup the error message for the given error number.
        """

        try:
            from glitter.raw import glu
            return glu.string_at(glu.gluErrorString(error))
        except (ImportError, AttributeError):
            return "error #%d" % error

    def __str__(self):
        return "GLError: %s in %s(%s)" % (GLError.string_from_id(self.error), self.func.__name__, ", ".join(repr(x) for x in self.arguments))

    def __repr__(self):
        return str(self)

def set_error_check(errcheck_func=Ellipsis, errcheck_ok=Ellipsis, name_re="^gl[A-Z].*$", d=None):
    """Add error handlers to OpenGL functions.

    The C{errcheck} attribute of all items in a dictionary C{d} having such an
    attribute and matching C{name_re} will be set to a function that calls
    C{errcheck_func} and raises L{GLError} if the return value is unequal to
    C{errcheck_ok}. By default, C{d} is C{glitter.raw.__dict__}.

    Defaults for C{errcheck_func} and C{errcheck_ok} are C{glGetError} and
    C{GL_NO_ERROR}, respectively. If C{errcheck_func} is C{None}, error
    checking will be disabled.
    """

    if d is None:
        from glitter import raw
        d = raw.__dict__

    if errcheck_func is Ellipsis:
        from glitter.raw import gl
        errcheck_func = gl.glGetError

    if errcheck_func is not None and errcheck_ok is Ellipsis:
        from glitter.raw import gl
        errcheck_ok = gl.GL_NO_ERROR

    def errcheck(result, func, arguments):
        error = errcheck_func()
        if error == errcheck_ok:
            return result
        else:
            raise GLError(error, result, func, arguments)

    for key, value in d.items():
        if re.match(name_re, key) and value is not errcheck_func and hasattr(value, "errcheck"):
            value.errcheck = errcheck

__all__ = ["GLError", "set_error_check"]

