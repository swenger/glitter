"""Tools for managing render contexts.

@author: Stephan Wenger
@date: 2012-03-08
"""

class ContextBindingProxy(object):
    _bound_context = None

    def __get__(self, obj, cls=None):
        return self._bound_context

    def __set__(self, obj, context=None):
        with obj:
            old_value, self._bound_context = self._bound_context, context
            context._bind()

    def __repr__(self):
        return "proxy for context binding"

class ContextManager(object):
    _stack = []

    current_context = ContextBindingProxy()
    """The currently active context."""

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

__all__ = ["ContextManager"]

