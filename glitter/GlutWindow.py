from rawgl import glut as _glut

# TODO manage viewport, swap_buffers() / post_redisplay()

class GlutWindow(object):
    def __init__(self, title="", width=512, height=512, argv=[], mode=_glut.GLUT_DOUBLE|_glut.GLUT_RGB, hide=False):
        self._called = False
        self._stack = []

        self._idle_func = None
        self._display_func = None
        self._reshape_func = None
        self._mouse_func = None
        self._motion_func = None
        self._keyboard_func = None
        self._title = title

        argc = _glut.c_int(len(argv))
        argv_c = (_glut.c_char_p * argc.value)()
        for i, a in enumerate(argv):
            argv_c[i] = a
        _glut.glutInit(_glut.pointer(argc), argv_c)
        # TODO modify argv

        _glut.glutInitContextVersion(4, 0)
        _glut.glutInitContextFlags(_glut.GLUT_FORWARD_COMPATIBLE)
        _glut.glutInitContextProfile(_glut.GLUT_CORE_PROFILE)
        _glut.glutSetOption(_glut.GLUT_ACTION_ON_WINDOW_CLOSE, _glut.GLUT_ACTION_GLUTMAINLOOP_RETURNS)
        _glut.glutInitDisplayMode(mode) # TODO boolean flags
        _glut.glutInitWindowSize(width, height)
        self._id = _glut.glutCreateWindow(self._title)

        if hide:
            _glut.glutHideWindow()

    def __del__(self):
        try:
            if not self._called:
                _glut.glutDestroyWindow(self._id)
            self._id = 0
        except AttributeError:
            pass # avoid error when GLUT module has already been unloaded

    def bind(self):
        old_binding = _glut.glutGetWindow()
        self._bind(self._id)
        return old_binding

    def __enter__(self):
        self._stack.append(self.bind())

    def __exit__(self, type, value, traceback):
        self._bind(self._stack.pop())

    def _bind(self, _id):
        _glut.glutSetWindow(_id)

    def __call__(self, loop=True):
        if self._called:
            raise RuntimeError("glutMainLoop() has already been called")
        self.bind()
        if loop:
            self._called = True
            _glut.glutMainLoop()
        else:
            _glut.glutMainLoopEvent()


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
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title
        with self:
            _glut.glutSetWindowTitle(title)

