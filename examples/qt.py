#!/usr/bin/env python

import sys
import numpy
from PySide import QtCore, QtGui

from glitter.contexts.qt import QtWidget
from glitter import rotation_matrix, scale_matrix, load_mesh

class Canvas(QtWidget):
    modelview_matrix = ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
    projection_matrix = ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))

    def __init__(self, parent=None):
        super(Canvas, self).__init__(parent)
        self.mesh = None
        self.lastButton = None
        self.lastPos = QtCore.QPoint()

    def mousePressEvent(self, event):
        self.lastButton = event.button()
        self.lastPos = QtCore.QPoint(event.pos())

    def mouseMoveEvent(self, event):
        dx, dy = event.x() - self.lastPos.x(), event.y() - self.lastPos.y()
        if dx == dy == 0:
            return
        elif event.buttons() & QtCore.Qt.LeftButton:
            self.modelview_matrix = numpy.dot(self.modelview_matrix,
                    rotation_matrix(-numpy.sqrt(dx ** 2 + dy ** 2), (dy, dx, 0.0), degrees=True))
            self.updateGL()
        elif event.buttons() & QtCore.Qt.RightButton:
            self.modelview_matrix = numpy.dot(self.modelview_matrix,
                    scale_matrix(numpy.exp(-0.01 * dy)))
            self.updateGL()
        self.lastPos = QtCore.QPoint(event.pos())

    def sizeHint(self):
        return QtCore.QSize(512, 512)

    def resizeGL(self, w, h):
        self.viewport = (0, 0, w, h)
        self.projection_matrix = scale_matrix(h / float(w) if w > h else 1.0,
                                              w / float(h) if h > w else 1.0, 0.4)

    def paintGL(self):
        self.clear()
        if self.mesh is not None:
            self.mesh.modelview_matrix = numpy.dot(self.projection_matrix, self.modelview_matrix)
            self.mesh.draw()

    def resetView(self):
        self.modelview_matrix = self.__class__.modelview_matrix
        self.updateGL()

    def loadMesh(self, filename):
        self.mesh = load_mesh(filename, context=self, depth_test=True)
        self.updateGL()

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.canvas = Canvas()
        self.setCentralWidget(self.canvas)

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

    def fileOpenMesh(self, filename=None):
        if filename is None:
            dialog = QtGui.QFileDialog(self, "Open Mesh")
            dialog.setNameFilter("HDF5 Files (*.hdf5)")
            dialog.setViewMode(QtGui.QFileDialog.Detail)
            dialog.setAcceptMode(QtGui.QFileDialog.AcceptOpen)
            dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
            if dialog.exec_():
                filename = dialog.selectedFiles()[0]
        if filename is not None:
            self.canvas.loadMesh(filename)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

