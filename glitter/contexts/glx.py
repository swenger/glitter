"""GLX context creation and management.

@author: Stephan Wenger
@date: 2012-08-28
"""

try:
    from glxcontext import GLXContext as _GLXContext

    from glitter.contexts.context import Context

    class GLXContext(_GLXContext, Context):
        """Offscreen GLX context."""

        def __init__(self, **kwargs):
            _GLXContext.__init__(self, **kwargs)
            Context.__init__(self)

        def _bind(self):
            return _GLXContext.bind(self)

        def bind(self):
            return Context.bind(self)

    __all__ = ["GLXContext"]
except ImportError:
    pass

