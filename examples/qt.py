#!/usr/bin/env python

#! This file is a literate Python program. You can compile the documentation
#! using mylit (http://pypi.python.org/pypi/mylit/).
## title = "glitter Example: Qt"
## stylesheet = "pygments_style.css"

# <h1><i>glitter</i> Example: Qt</h1>

# <h2>Summary</h2>

# This program will show a Qt application to display meshes.

# <img src="qt.png">

# <h2>Front matter</h2>

# <h3>Module docstring</h3>

# The module docstring is used as a description of this example in the
# generated documentation:
"""Example for Qt (PySide) interaction.

@author: Stephan Wenger
@date: 2012-03-16
"""

# <h3>Imports</h3>

# Some math functions are required for mouse interaction:
from math import sqrt, exp

# We use <a href="http://www.pyside.org/">PySide</a> for <a
# href="http://qt.nokia.com/">Qt</a> interaction:
from PySide import QtCore, QtGui

# Note that we did not import the <code>QtOpenGL</code> package. Instead, we
# will use a Qt OpenGL widget that doubles as a <i>glitter</i>
# <code>Context</code>:
from glitter.contexts.qt import QtWidget
# If you'd rather use an existing Qt OpenGL context,
# <code>QtContextWrapper</code> provides an alternative solution.

# Since there are no more build-in matrices in the OpenGL core profile, we use
# <i>glitter</i>'s matrix constructors. <i>glitter</i> also provides a method
# for loading meshes from files that we will use:
from glitter import rotation_matrix, scale_matrix, identity_matrix, load_mesh

# <h2>Qt GUI</h2>

# <h3>Qt OpenGL Widget</h3>

# OpenGL rendering in Qt is through an OpenGL widget. Instead of subclassing
# <code>QGLWidget</code> directly, we inherit from <i>glitter</i>'s
# <code>QtWidget</code> which acts as a <i>glitter</i> <code>Context</code>.
# This not only provides us with a convenient interface for changing OpenGL
# state, it also ensures that the correct context is made active whenever
# OpenGL commands are issued.
class Canvas(QtWidget):
    # <h4>Initialization</h4>
    # The canvas will store a mesh to display, a modelview matrix that can be
    # changed by moving the mouse, and a helper variable for the mouse
    # interaction:
    def __init__(self, parent=None):
        super(Canvas, self).__init__(parent)
        self.mesh = None
        self.modelview_matrix = identity_matrix()
        self.lastPos = QtCore.QPoint()

    # The size of the canvas is specified by overriding <code>sizeHint()</code>:
    def sizeHint(self):
        return QtCore.QSize(512, 512)

    # When the user requests loading a mesh via the menu system, we create a
    # <code>Pipeline</code> containing the mesh vertices and an appropriate
    # shader, all with a single call to <code>load_mesh()</code> from the
    # <code>glitter.convenience</code> module. Also, we can pass additional
    # parameters to the <code>Pipeline</code> constructor. In this case, we
    # want depth testing to be enabled whenever the pipeline is executed, so we
    # pass <code>depth_text=True</code>:
    def loadMesh(self, filename):
        self.mesh = load_mesh(filename, context=self, depth_test=True)
        # Note that we pass the canvas as the <code>context</code> parameter to
        # make sure the pipeline is created in the correct context. This is
        # necessary because in a real-world application, we cannot be sure that
        # the canvas context is currently active.

        # When the mesh is loaded, we ask Qt to redraw the OpenGL screen:
        self.updateGL()

    # <h4>Mouse interaction</h4>
    # The viewpoint can be changed by moving the mouse with a button pressed:
    # left button rotates, right button zooms.

    # When a mouse button is pressed, we store the position where it was
    # pressed:
    def mousePressEvent(self, event):
        self.lastPos = QtCore.QPoint(event.pos())

    # When the mouse is moved, we take action according to the type of the
    # pressed button:
    def mouseMoveEvent(self, event):
        # First, we compute the mouse movement since the last time we processed
        # a mouse event. If there was no movement (which does happen from time
        # to time), we exit early to avoid division by zero later on:
        dx, dy = event.x() - self.lastPos.x(), event.y() - self.lastPos.y()
        if dx == dy == 0:
            return

        # If the left mouse button is down, we rotate the modelview matrix
        # about an axis within the image plane that is perpendicular to the
        # direction of mouse movement. The amount of rotation is proportional
        # to the distance travelled. Then we cause a screen redraw by calling
        # <code>updateGL()</code>.
        elif event.buttons() & QtCore.Qt.LeftButton:
            self.modelview_matrix *= rotation_matrix(-sqrt(dx ** 2 + dy ** 2), (dy, dx, 0.0), degrees=True)
            self.updateGL()

        # If the right mouse button is down, we scale the modelview matrix
        # dependent on the vertical mouse movement.  Again, a screen redraw is
        # triggered by calling <code>updateGL()</code>.
        elif event.buttons() & QtCore.Qt.RightButton:
            self.modelview_matrix *= scale_matrix(exp(-0.01 * dy))
            self.updateGL()

        # Finally, the mouse position is stored for processing of the following
        # mouse event.
        self.lastPos = QtCore.QPoint(event.pos())

    # <h4>OpenGL interaction</h4>

    # Whenever the canvas is resized (also on creation), we set the viewport
    # (which is actually a <i>glitter</i> <code>Context</code> property) to the
    # full window and change the projection matrix such that it encompasses the
    # whole range from -1 to +1:
    def resizeGL(self, w, h):
        self.viewport = (0, 0, w, h)
        self.projection_matrix = scale_matrix(h / float(w) if w > h else 1.0, w / float(h) if h > w else 1.0, 0.4)

    # The <code>paintGL()</code> method is called by Qt whenever the canvas
    # needs to be redrawn:
    def paintGL(self):
        # First, we clear the canvas using <code>Context.clear()</code>.
        self.clear()

        # Then, if a mesh pipeline has been loaded, we draw it with the
        # <code>modelview_matrix</code> uniform set. The pipeline binds the
        # vertex array and the shader, sets the depth test we requested
        # earlier, draws the vertex array, and resets all modified state:
        if self.mesh is not None:
            self.mesh.draw_with(modelview_matrix=self.projection_matrix * self.modelview_matrix)

    # Finally, when the user requests resetting the view via the menu system,
    # we create a clean modelview matrix and update the screen:
    def resetView(self):
        self.modelview_matrix = identity_matrix()
        self.updateGL()

# <h3>Qt Main Window</h3>

# The OpenGL widget will be displayed within a <code>QMainWindow</code> that
# provides menus, keyboard shortcuts, and many other amenities:
class MainWindow(QtGui.QMainWindow):
    # <h4>Initialization</h4>
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # First, we create an instance of the <code>Canvas</code> class we
        # defined previously and make it the main widget in the window:
        self.canvas = Canvas()
        self.setCentralWidget(self.canvas)

        # Then, we create menus and keyboard shortcuts for opening meshes,
        # resetting the view, and exiting the program:
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileOpenMeshAction = QtGui.QAction(u"&Open Mesh\u2026", self)
        self.fileOpenMeshAction.setShortcut(QtGui.QKeySequence(QtCore.Qt.Key_O))
        self.fileOpenMeshAction.triggered.connect(self.fileOpenMesh)
        self.fileMenu.addAction(self.fileOpenMeshAction)
        self.fileMenu.addSeparator()
        self.fileQuitAction = QtGui.QAction("&Quit", self)
        self.fileQuitAction.setShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Escape))
        self.fileQuitAction.triggered.connect(self.close)
        self.fileMenu.addAction(self.fileQuitAction)

        self.viewMenu = self.menuBar().addMenu("&View")
        self.viewResetAction = QtGui.QAction("&Reset", self)
        self.viewResetAction.setShortcut(QtGui.QKeySequence(QtCore.Qt.Key_R))
        self.viewResetAction.triggered.connect(self.canvas.resetView)
        self.viewMenu.addAction(self.viewResetAction)

    # <h4>File loading</h4>
    # When the file open action is triggered via the menu or a keyboard
    # shortcut, we display a dialog for selecting a file. If a file is
    # selected, we tell the canvas to load a mesh from it.
    def fileOpenMesh(self, filename=None):
        if filename is None:
            dialog = QtGui.QFileDialog(self, "Open Mesh")
            dialog.setNameFilters(["%s files (*.%s)" % (x.upper(), x) for x in load_mesh.supported_formats])
            dialog.setViewMode(QtGui.QFileDialog.Detail)
            dialog.setAcceptMode(QtGui.QFileDialog.AcceptOpen)
            dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
            if dialog.exec_():
                filename = dialog.selectedFiles()[0]
        if filename is not None:
            self.canvas.loadMesh(filename)

# <h2>Main section</h2>
# Finally, if this program is being run from the command line, we create a
# <code>QApplication</code>, show a <code>MainWindow</code> instance and run
# the Qt main loop.
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

# When the main window is closed, the application will exit cleanly.

