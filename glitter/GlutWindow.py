from OpenGL import GL, GLUT
from math import sqrt, exp
import sys

# TODO rewrite using rawgl
# TODO cleanup
# TODO Texture, Shader etc. are attached to a context; make sure they use this context (in __enter__ / __exit__ / __del__)
class GlutWindow(object):
    def __init__(self,
            title="",
            width=512,
            height=512,
            argv=[],
            mode=GLUT.GLUT_DOUBLE|GLUT.GLUT_RGB,
            idle=lambda: None,
            display=lambda: None,
            reshape=lambda width, height: None,
            mouse=lambda button, state, x, y: None,
            motion=lambda x, y: None,
            keyboard=lambda key, x, y: None,
            hide=False):
        self._stack = []

        self._window_width = width
        self._window_height = height
        self._idle_hook = idle
        self._display_hook = display
        self._reshape_hook = reshape
        self._mouse_hook = mouse
        self._motion_hook = motion
        self._keyboard_hook = keyboard

        # initialize OpenGL
        GLUT.glutInit(argv)
        # TODO GLUT.freeglut.glutInitContextVersion(4, 0)
        # TODO GLUT.freeglut.glutInitContextFlags(GLUT.freeglut.GLUT_FORWARD_COMPATIBLE)
        # TODO GLUT.freeglut.glutInitContextProfile(GLUT.freeglut.GLUT_CORE_PROFILE)
        GLUT.glutInitDisplayMode(mode)
        GLUT.glutInitWindowPosition(0, 0)
        GLUT.glutInitWindowSize(self._window_width, self._window_height)
        self._id = GLUT.glutCreateWindow(title)
        if hide:
            GLUT.glutHideWindow()
        GLUT.glutIdleFunc(self._idle)
        GLUT.glutDisplayFunc(self._display)
        GLUT.glutReshapeFunc(self._reshape)
        GLUT.glutMouseFunc(self._mouse)
        GLUT.glutMotionFunc(self._motion)
        GLUT.glutKeyboardFunc(self._keyboard)
        GLUT.freeglut.glutSetOption(GLUT.freeglut.GLUT_ACTION_ON_WINDOW_CLOSE, GLUT.freeglut.GLUT_ACTION_GLUTMAINLOOP_RETURNS)
        
        # create initial modelview matrix
        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glLoadIdentity()
        self._modelview_matrix = GL.glGetFloatv(GL.GL_MODELVIEW_MATRIX)
    
    def __del__(self):
        try:
            GLUT.glutDestroyWindow(self._id)
        except TypeError:
            pass
        except AttributeError:
            pass

    def __enter__(self):
        self._stack.append(GLUT.glutGetWindow())
        GLUT.glutSetWindow(self._id)

    def __exit__(self, type, value, traceback):
        GLUT.glutSetWindow(self._stack.pop())

    def _idle(self):
        self._idle_hook()
        GLUT.glutPostRedisplay()

    def _display(self):
        # set up viewport
        GL.glViewport(0, 0, self._window_width, self._window_height)

        # set up projection
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GL.glOrtho(-1, 1, -1, 1, -1, 1)

        # set up camera
        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glLoadIdentity()
        GL.glMultMatrixf(self._modelview_matrix)

        # clear
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        
        # execute drawing
        self._display_hook()

        # display
        GLUT.glutSwapBuffers()

    def _reshape(self, width, height):
        self._window_width = width
        self._window_height = height
        self._reshape_hook(width, height)

    def _mouse(self, button, state, x, y):
        self._old_button = button
        self._old_state = state
        self._old_x = x
        self._old_y = y
        self._mouse_hook(button, state, x, y)

    def _motion(self, x, y):
        dx = x - self._old_x
        dy = y - self._old_y

        if self._old_button == GLUT.GLUT_LEFT_BUTTON:
            GL.glMatrixMode(GL.GL_MODELVIEW)
            GL.glLoadIdentity()
            GL.glRotatef(sqrt(dx ** 2 + dy ** 2), dy, dx, 0.0)
            GL.glMultMatrixf(self._modelview_matrix)
            self._modelview_matrix = GL.glGetFloatv(GL.GL_MODELVIEW_MATRIX)
            GLUT.glutPostRedisplay()
        elif self._old_button == GLUT.GLUT_RIGHT_BUTTON:
            GL.glMatrixMode(GL.GL_MODELVIEW)
            GL.glLoadIdentity()
            GL.glScalef(exp(-0.01 * dy), exp(-0.01 * dy), exp(-0.01 * dy))
            GL.glMultMatrixf(self._modelview_matrix)
            self._modelview_matrix = GL.glGetFloatv(GL.GL_MODELVIEW_MATRIX)
            GLUT.glutPostRedisplay()

        self._old_x = x
        self._old_y = y

        self._motion_hook(x, y)

    def _keyboard(self, key, x, y):
        if key == "r":
            GL.glMatrixMode(GL.GL_MODELVIEW)
            GL.glLoadIdentity()
            self._modelview_matrix = GL.glGetFloatv(GL.GL_MODELVIEW_MATRIX)
            GLUT.glutPostRedisplay()
        elif key == chr(27):
            sys.exit(0)
        else:
            self._keyboard_hook(key, x, y)

    @property
    def id(self):
        return self._id

    def __call__(self, loop=True):
        GLUT.glutSetWindow(self._id)
        if loop:
            GLUT.glutMainLoop()
        else:
            GLUT.glutMainLoopEvent()

