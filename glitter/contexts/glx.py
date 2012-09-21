"""GLX context creation and management.

Depends on the binary glxcontext module.

@todo: Include glxcontext in distribution as an optional module.

@author: Stephan Wenger
@date: 2012-08-28
"""

try:
    from glxcontext import GLXContext as _GLXContext

    from glitter.contexts.context import Context
    from glitter.contexts.contextmanager import context_manager

    class GLXContext(_GLXContext, Context):
        """Offscreen GLX context."""

        def __init__(self, **kwargs):
            _GLXContext.__init__(self, **kwargs)
            Context.__init__(self)

            # TODO the lines below should not be necessary, or should at least be performed automatically by context_manager
            # XXX I would have expected it worked without these lines because of "with self._context" around GLObject functions; is this a problem with multiple Contexts?
            old_binding = context_manager.current_context
            if old_binding:
                old_binding._bind()
            else:
                context_manager.current_context = self

        def _bind(self):
            return _GLXContext.bind(self)

        def bind(self):
            return Context.bind(self)

    __all__ = ["GLXContext"]
except ImportError:
    pass

