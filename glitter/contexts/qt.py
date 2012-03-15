"""Qt context creation and management.

@author: Stephan Wenger
@date: 2012-02-29
"""

try:
    from PySide import QtOpenGL
except ImportError:
    from PyQt4 import QtOpenGL

from glitter.contexts.context import Context

class QtContextWrapper(Context):
    def __init__(self, context):
        super(QtContextWrapper, self).__init__(self)
        if isinstance(context, QtOpenGL.QGLContext):
            self._qt_context = context
        else:
            self._qt_context = context.context()

    def _bind(self):
        self._qt_context.makeCurrent()

class QtWidget(QtOpenGL.QGLWidget, Context):
    def __init__(self, *args, **kwargs):
        QtOpenGL.QGLWidget.__init__(self, *args, **kwargs)
        with self:
            Context.__init__(self)

    def _bind(self):
        self.makeCurrent()

