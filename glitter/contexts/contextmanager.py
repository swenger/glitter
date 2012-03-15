"""Tools for managing render contexts.

@author: Stephan Wenger
@date: 2012-03-08
"""

class ContextBindingProxy(object):
    _bound_context = None

    def __get__(self, obj, cls=None):
        return self._bound_context

    def __set__(self, obj, context=None):
        if context is None:
            self._bound_context = None
        elif context != self._bound_context:
            self._bound_context = context
            context._bind()

    def __repr__(self):
        return "proxy for context binding"

class ContextManager(object):
    current_context = ContextBindingProxy()
    """The currently active context."""

    def __init__(self):
        self._stack = []

    def push(self, context):
        self._stack.append(self.current_context)
        self.current_context = context

    def pop(self):
        self.current_context = self._stack.pop()

    @staticmethod
    def create_default_context():
        """Create a default offscreen rendering context.

        @todo: This is window system dependent; create an appropriate context
        dynamically.
        @todo: When no context exists, create a raw offscreen context instead of a
        hidden GLUT window so that rendering is possible without an X connection.
        """

        from glitter.contexts.glut import GlutWindow
        return GlutWindow(shape=(1, 1), hide=True)

context_manager = ContextManager()

__all__ = ["context_manager"]

