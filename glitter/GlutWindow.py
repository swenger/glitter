from rawgl import glut as _glut

# TODO implement complete API as in http://www.opengl.org/resources/libraries/glut/glut-3.spec.pdf from p. 9

def initialize(argv=None):
    if argv is None:
        import sys
        argv = sys.argv
    _argc = _glut.c_int(len(argv))
    _argv = (_glut.c_char_p * _argc.value)()
    for i, a in enumerate(argv):
        _argv[i] = a
    _glut.glutInit(_glut.pointer(_argc), _argv)
    argv[:] = [_argv[i] for i in range(_argc.value)]

def main_loop():
    _glut.glutMainLoop()
    initialize()

def main_loop_event():
    _glut.glutMainLoopEvent()

def leave_main_loop():
    _glut.glutLeaveMainLoop()

class GlutWindow(object):
    def __init__(self, version=(4, 0), compatibility_profile=False,
            debug=False, forward_compatible=True, width=300, height=300, x=-1,
            y=-1, index=False, double=False, accum=False, alpha=False,
            depth=False, stencil=False, multisample=False, stereo=False,
            luminance=False, name="", hide=False):
        """Create a new GLUT window.

        `version` is the OpenGL version to use. It can be either an integer or a (major, minor) tuple.
        If `compatibility_profile` is `True`, the compatibility profile will be used instead of the core profile.
        `debug` enables OpenGL debug mode, `forward_compatible` the forward compatibility mode.
        `width`, `height`, `x`, and `y` control the initial size and position of the window.
        `index` enables color index mode instead of RGBA.
        `double` enables double buffering.
        `accum`, `alpha`, `depth`, and `stencil` enable the corresponding buffers.
        `multisample` enables multisampling.
        `stereo` enables stereo buffers.
        `luminance` enables luminance rendering instead of true RGBA.
        `name` is the name of the window and its initial title.
        If `hide` is `True`, the window will initially be hidden.
        """

        self._stack = []

        self._idle_func = None
        self._display_func = None
        self._reshape_func = None
        self._mouse_func = None
        self._motion_func = None
        self._keyboard_func = None

        self._name = self._title = name

        if hasattr(version, "__iter__"):
            _glut.glutInitContextVersion(*version)
        else:
            _glut.glutInitContextVersion(version, 0)

        _glut.glutInitContextProfile(_glut.GLUT_COMPATIBILITY_PROFILE if compatibility_profile else _glut.GLUT_CORE_PROFILE)

        _glut.glutInitContextFlags(
                (_glut.GLUT_DEBUG if debug else 0) |
                (_glut.GLUT_FORWARD_COMPATIBLE if forward_compatible else 0)
                )

        _glut.glutInitWindowSize(width, height)
        _glut.glutInitWindowPosition(x, y)

        _glut.glutInitDisplayMode(
                (_glut.GLUT_INDEX if index else _glut.GLUT_RGBA) |
                (_glut.GLUT_DOUBLE if double else _glut.GLUT_SINGLE) |
                (_glut.GLUT_ACCUM if accum else 0) |
                (_glut.GLUT_ALPHA if alpha else 0) |
                (_glut.GLUT_DEPTH if depth else 0) |
                (_glut.GLUT_STENCIL if stencil else 0) |
                (_glut.GLUT_MULTISAMPLE if multisample else 0) |
                (_glut.GLUT_STEREO if stereo else 0) |
                (_glut.GLUT_LUMINANCE if luminance else 0)
                )

        _glut.glutSetOption(_glut.GLUT_ACTION_ON_WINDOW_CLOSE, _glut.GLUT_ACTION_CONTINUE_EXECUTION)

        old_binding = _glut.glutGetWindow()
        self._id = _glut.glutCreateWindow(self._title)
        if old_binding:
            _glut.glutSetWindow(old_binding)

        if hide:
            self.hide()
        else:
            self.show()

    def destroy(self):
        _glut.glutDestroyWindow(self._id)
        self._id = 0

    def bind(self):
        old_binding = _glut.glutGetWindow()
        _glut.glutSetWindow(self._id)
        return old_binding

    def __enter__(self):
        self._stack.append(self.bind())

    def __exit__(self, type, value, traceback):
        _glut.glutSetWindow(self._stack.pop())

    def swap_buffers(self):
        with self:
            _glut.glutSwapBuffers()

    def post_redisplay(self):
        with self:
            _glut.glutPostRedisplay()

    def show(self):
        with self:
            _glut.glutShowWindow()

    def hide(self):
        with self:
            _glut.glutHideWindow()


    @property
    def shape(self):
        with self:
            return _glut.glutGet(_glut.GLUT_WINDOW_WIDTH), _glut.glutGet(_glut.GLUT_WINDOW_HEIGHT)

    @shape.setter
    def shape(self, shape):
        width, height = shape
        with self:
            _glut.glutReshapeWindow(width, height)

    @property
    def idle_func(self):
        return self._idle_func

    @idle_func.setter
    def idle_func(self, idle_func):
        self._idle_func = idle_func
        ftype = _glut.glutIdleFunc.argtypes[0]
        self._idle_func_c = ftype(idle_func) if idle_func is not None else ftype()
        with self:
            _glut.glutIdleFunc(self._idle_func_c)

    @property
    def display_func(self):
        return self._display_func

    @display_func.setter
    def display_func(self, display_func):
        self._display_func = display_func
        ftype = _glut.glutDisplayFunc.argtypes[0]
        self._display_func_c = ftype(display_func) if display_func is not None else ftype()
        with self:
            _glut.glutDisplayFunc(self._display_func_c)

    @property
    def reshape_func(self):
        return self._reshape_func

    @reshape_func.setter
    def reshape_func(self, reshape_func):
        self._reshape_func = reshape_func
        ftype = _glut.glutReshapeFunc.argtypes[0]
        self._reshape_func_c = ftype(reshape_func) if reshape_func is not None else ftype()
        with self:
            _glut.glutReshapeFunc(self._reshape_func_c)

    @property
    def mouse_func(self):
        return self._mouse_func

    @mouse_func.setter
    def mouse_func(self, mouse_func):
        self._mouse_func = mouse_func
        ftype = _glut.glutMouseFunc.argtypes[0]
        self._mouse_func_c = ftype(mouse_func) if mouse_func is not None else ftype()
        with self:
            _glut.glutMouseFunc(self._mouse_func_c)

    @property
    def motion_func(self):
        return self._motion_func

    @motion_func.setter
    def motion_func(self, motion_func):
        self._motion_func = motion_func
        ftype = _glut.glutMotionFunc.argtypes[0]
        self._motion_func_c = ftype(motion_func) if motion_func is not None else ftype()
        with self:
            _glut.glutMotionFunc(self._motion_func_c)

    @property
    def keyboard_func(self):
        return self._keyboard_func

    @keyboard_func.setter
    def keyboard_func(self, keyboard_func):
        self._keyboard_func = keyboard_func
        ftype = _glut.glutKeyboardFunc.argtypes[0]
        self._keyboard_func_c = ftype(keyboard_func) if keyboard_func is not None else ftype()
        with self:
            _glut.glutKeyboardFunc(self._keyboard_func_c)

    @property
    def name(self):
        return self._name

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title
        with self:
            _glut.glutSetWindowTitle(title)

initialize()

