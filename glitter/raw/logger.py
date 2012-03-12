"""Logging of OpenGL calls.
"""

import re

class LoggingWrapper(object):
    """Wrap a ctypes function so that function calls are logged.
    """

    def __init__(self, func, logger_func):
        self._func = func
        self._logger_func = logger_func
        self.__name__ = func.__name__
        self.__doc__ = func.__doc__

        for key in dir(func):
            if not key.startswith("_"):
                setattr(self, key, getattr(func, key))

    def _format_arg(self, x):
        if hasattr(x, "_type_") and hasattr(x, "__len__") and hasattr(x, "__getitem__"):
            return "%s[%s]" % (x._type_.__name__, ", ".join(self._format_arg(a) for a in x))
        elif hasattr(x, "value"):
            return "%s(%r)" % (x.__class__.__name__, x.value)
        elif hasattr(x, "contents"):
            return "&%s" % self._format_arg(x.contents)
        elif hasattr(x, "_name"):
            return x._name
        else:
            return repr(x)

    def _format_args(self, args, kwargs):
        return ", ".join([self._format_arg(x) for x in args] + ["%s=%s" % (k, self._format_arg(v)) for (k, v) in kwargs.items()])

    def __call__(self, *args, **kwargs):
        self._logger_func("%s(%s)", self.__name__, self._format_args(args, kwargs))
        return self._func(*args, **kwargs)

    def __str__(self):
        return self.__name__

def add_logger(logger="root", name_re="^(gl|glu|glut|glX)[A-Z].*$", d=None):
    """Add a logger to OpenGL functions.

    All values in C{d} that match C{name_re} have an C{errcheck} attribute will
    be replaced by corresponding L{LoggingWrapper}s that call C{logger} before
    each invocation. By default, C{d} is C{glitter.raw.__dict__}.

    C{logger} may be either a callable, a C{logging.logger} object, the name of
    a registered C{logging.Logger} object, or C{None} to remove the logger.

    @attention: If you add multiple loggers to a function, you will not only
    incur a double performance penalty, but also have to remove them in the
    reverse order; there is no way to remove a specific logger.
    """

    if d is None:
        from glitter import raw
        d = raw.__dict__

    if logger is None:
        for key, value in d.items():
            if re.match(name_re, key) and isinstance(value, LoggingWrapper):
                d[key] = value._func
    else:
        if not callable(logger):
            import logging
            if isinstance(logger, logging.Logger):
                logger = logger.debug
            else:
                logger = logging.getLogger(logger).debug

        for key, value in d.items():
            if re.match(name_re, key) and hasattr(value, "errcheck"):
                d[key] = LoggingWrapper(value, logger)

__all__ = ["LoggingWrapper", "add_logger"]

