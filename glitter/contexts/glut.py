"""GLUT context creation and management.

@bug: Closing a GLUT window via the window system (not the API) causes bogus error messages and even the occasional segfault.
@todo: Implement subwindows using C{glutCreateSubWindow} and C{glutGet(GLUT_WINDOW_PARENT)}.
@todo: Implement menus, font rendering, and geometric object rendering,
@todo: Fail gracefully (better error message) when context cannot be created, e.g. when opengl 4.0 not available

@author: Stephan Wenger
@date: 2012-02-29
"""

import random as _random

import glitter.raw as _gl
from glitter.utils import Enum
from glitter.contexts.context import Context
from glitter.contexts.contextmanager import ContextManager

_cursors = Enum(
    right_arrow=_gl.GLUT_CURSOR_RIGHT_ARROW,
    left_arrow=_gl.GLUT_CURSOR_LEFT_ARROW,
    info=_gl.GLUT_CURSOR_INFO,
    destroy=_gl.GLUT_CURSOR_DESTROY,
    help=_gl.GLUT_CURSOR_HELP,
    cycle=_gl.GLUT_CURSOR_CYCLE,
    spray=_gl.GLUT_CURSOR_SPRAY,
    wait=_gl.GLUT_CURSOR_WAIT,
    text=_gl.GLUT_CURSOR_TEXT,
    crosshair=_gl.GLUT_CURSOR_CROSSHAIR,
    up_down=_gl.GLUT_CURSOR_UP_DOWN,
    left_right=_gl.GLUT_CURSOR_LEFT_RIGHT,
    top_side=_gl.GLUT_CURSOR_TOP_SIDE,
    bottom_side=_gl.GLUT_CURSOR_BOTTOM_SIDE,
    left_side=_gl.GLUT_CURSOR_LEFT_SIDE,
    right_side=_gl.GLUT_CURSOR_RIGHT_SIDE,
    top_left_corner=_gl.GLUT_CURSOR_TOP_LEFT_CORNER,
    top_right_corner=_gl.GLUT_CURSOR_TOP_RIGHT_CORNER,
    bottom_right_corner=_gl.GLUT_CURSOR_BOTTOM_RIGHT_CORNER,
    bottom_left_corner=_gl.GLUT_CURSOR_BOTTOM_LEFT_CORNER,
    full_crosshair=_gl.GLUT_CURSOR_FULL_CROSSHAIR,
    none=_gl.GLUT_CURSOR_NONE,
    inherit=_gl.GLUT_CURSOR_INHERIT,
)

def _func_property(glut_func):
    import re
    name = re.match("^glut(.*)Func$", glut_func.__name__).groups()[0]
    name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)).lower()
    private_name = "_%s_func" % name
    private_c_name = "_%s_func_c" % name

    def getter(self):
        if not hasattr(self, private_name):
            setattr(self, private_name, None)
        return getattr(self, private_name)

    def setter(self, func):
        ftype = glut_func.argtypes[0]
        setattr(self, private_c_name, ftype(func) if func is not None else ftype())
        setattr(self, private_name, func)
        with self:
            glut_func(getattr(self, private_c_name))

    return property(getter, setter)

def initialize(argv=None):
    """Initialize GLUT. Called automatically on import."""
    if argv is None:
        import sys
        argv = sys.argv
    _argc = _gl.c_int(len(argv))
    _argv = (_gl.c_char_p * _argc.value)()
    for i, a in enumerate(argv):
        _argv[i] = a
    _gl.glutInit(_gl.pointer(_argc), _argv)
    argv[:] = [_argv[i] for i in range(_argc.value)]

def main_loop():
    """Enter the GLUT main loop.
    
    @todo: Avoid destroying a window in C{__del__} that has already been destroyed by closing it; can C{glutCloseFunc} help?
    """
    _gl.glutMainLoop()
    initialize()

def main_loop_event():
    """Allow GLUT to process events."""
    _gl.glutMainLoopEvent()

def leave_main_loop():
    """Leave the GLUT main loop."""
    _gl.glutLeaveMainLoop()

def get_screen_shape():
    """Screen height and width in pixels."""
    return _gl.glutGet(_gl.GLUT_SCREEN_HEIGHT, _gl.GLUT_SCREEN_WIDTH)

def get_screen_shape_mm():
    """Screen height and width in millimeters."""
    return _gl.glutGet(_gl.GLUT_SCREEN_HEIGHT_MM, _gl.GLUT_SCREEN_WIDTH_MM)

def get_elapsed_time():
    """Time in seconds since GLUT was initialized."""
    return _gl.glutGet(_gl.GLUT_ELAPSED_TIME) / 1000.0

def get_shift_state():
    """Only available in keyboard, special, and mouse callbacks."""
    return _gl.glutGetModifiers(_gl.GLUT_ACTIVE_SHIFT)

def get_ctrl_state():
    """Only available in keyboard, special, and mouse callbacks."""
    return _gl.glutGetModifiers(_gl.GLUT_ACTIVE_CTRL)

def get_alt_state():
    """Only available in keyboard, special, and mouse callbacks."""
    return _gl.glutGetModifiers(_gl.GLUT_ACTIVE_ALT)

class GlutWindow(Context):
    cursors = _cursors

    def __init__(self, version=(3, 2), compatibility_profile=False,
            debug=False, forward_compatible=True, shape=(300, 300),
            position=(-1, -1), index=False, double=False, accum=False,
            alpha=False, depth=False, stencil=False, multisample=False,
            stereo=False, luminance=False, name="", hide=False):
        """Create a new GLUT window.

        `version` is the OpenGL version to use. It can be either an integer or a (major, minor) tuple.
        If `compatibility_profile` is `True`, the compatibility profile will be used instead of the core profile.
        `debug` enables OpenGL debug mode, `forward_compatible` the forward compatibility mode.
        `shape` and `position` control the initial (height, width) shape and (y, x) position of the window.
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
        
        self._timer_funcs = {}
        def timer_func(value):
            self._timer_funcs.pop(value)()
        self._timer_func = _gl.glutTimerFunc.argtypes[1](timer_func)

        self._name = self._window_title = self._icon_title = name

        if hasattr(version, "__iter__"):
            _gl.glutInitContextVersion(*version)
        else:
            _gl.glutInitContextVersion(version, 0)

        _gl.glutInitContextProfile(_gl.GLUT_COMPATIBILITY_PROFILE if compatibility_profile else _gl.GLUT_CORE_PROFILE)

        _gl.glutInitContextFlags(
                (_gl.GLUT_DEBUG if debug else 0) |
                (_gl.GLUT_FORWARD_COMPATIBLE if forward_compatible else 0)
                )

        height, width = shape
        _gl.glutInitWindowSize(width, height)

        y, x = position
        _gl.glutInitWindowPosition(x, y)

        _gl.glutInitDisplayMode(
                (_gl.GLUT_INDEX if index else _gl.GLUT_RGBA) |
                (_gl.GLUT_DOUBLE if double else _gl.GLUT_SINGLE) |
                (_gl.GLUT_ACCUM if accum else 0) |
                (_gl.GLUT_ALPHA if alpha else 0) |
                (_gl.GLUT_DEPTH if depth else 0) |
                (_gl.GLUT_STENCIL if stencil else 0) |
                (_gl.GLUT_MULTISAMPLE if multisample else 0) |
                (_gl.GLUT_STEREO if stereo else 0) |
                (_gl.GLUT_LUMINANCE if luminance else 0)
                )

        _gl.glutSetOption(_gl.GLUT_ACTION_ON_WINDOW_CLOSE, _gl.GLUT_ACTION_CONTINUE_EXECUTION)

        if not _gl.glutGet(_gl.GLUT_DISPLAY_MODE_POSSIBLE):
            raise RuntimeError("display mode not possible")

        old_binding = ContextManager.current_context
        self._id = _gl.glutCreateWindow(self._name) # creating a window changes the current context without the context manager's knowledge
        if old_binding:
            old_binding._bind() # rebind the previous context circumventing any caching performed by the context
        else:
            ContextManager.current_context = self # tell the context manager about the changed binding

        super(GlutWindow, self).__init__()

        if hide:
            self.hide()
        else:
            self.show()

    def destroy(self):
        _gl.glutDestroyWindow(self._id)
        self._id = 0

    def _bind(self):
        if self._id == 0:
            raise RuntimeError("window has already been destroyed")
        _gl.glutSetWindow(self._id)

    def swap_buffers(self):
        with self:
            _gl.glutSwapBuffers()

    def post_redisplay(self):
        with self:
            _gl.glutPostRedisplay()

    def full_screen(self):
        with self:
            _gl.glutFullScreen()

    def leave_full_screen(self):
        with self:
            _gl.glutLeaveFullScreen()

    def toggle_full_screen(self):
        with self:
            _gl.glutFullScreenToggle()

    def push(self):
        with self:
            _gl.glutPushWindow()

    def pop(self):
        with self:
            _gl.glutPopWindow()

    def show(self):
        with self:
            _gl.glutShowWindow()

    def hide(self):
        with self:
            _gl.glutHideWindow()

    def iconify(self):
        with self:
            _gl.glutIconifyWindow()

    @property
    def cursor(self):
        with self:
            return GlutWindow.cursors[_gl.glutGet(_gl.GLUT_WINDOW_CURSOR)]

    @cursor.setter
    def cursor(self, cursor):
        with self:
            _gl.glutSetCursor(cursor._value)

    @property
    def num_children(self):
        with self:
            return _gl.glutGet(_gl.GLUT_WINDOW_NUM_CHILDREN)

    @property
    def shape(self):
        with self:
            return _gl.glutGet(_gl.GLUT_WINDOW_HEIGHT), _gl.glutGet(_gl.GLUT_WINDOW_WIDTH)

    @shape.setter
    def shape(self, shape):
        height, width = shape
        with self:
            _gl.glutReshapeWindow(width, height)

    @property
    def position(self):
        with self:
            return _gl.glutGet(_gl.GLUT_WINDOW_Y), _gl.glutGet(_gl.GLUT_WINDOW_X)

    @position.setter
    def position(self, position):
        y, x = position
        with self:
            _gl.glutPositionWindow(x, y)

    @property
    def name(self):
        return self._name

    @property
    def window_title(self):
        return self._window_title

    @window_title.setter
    def window_title(self, window_title):
        self._window_title = window_title
        with self:
            _gl.glutSetWindowTitle(window_title)

    @property
    def icon_title(self):
        return self._icon_title

    @icon_title.setter
    def icon_title(self, icon_title):
        self._icon_title = icon_title
        with self:
            _gl.glutSetIconTitle(icon_title)

    def add_timer(self, msecs, func):
        timer_id = _random.randint(0, 1 << 30)
        while timer_id in self._timer_funcs:
            timer_id = _random.randint(0, 1 << 30)
        self._timer_funcs[timer_id] = func
        _gl.glutTimerFunc(msecs, self._timer_func, timer_id)

    close_callback = _func_property(_gl.glutCloseFunc)
    display_callback = _func_property(_gl.glutDisplayFunc)
    entry_callback = _func_property(_gl.glutEntryFunc)
    idle_callback = _func_property(_gl.glutIdleFunc) # within the callback, current window is not necessarily this window
    joystick_callback = _func_property(_gl.glutJoystickFunc)
    keyboard_callback = _func_property(_gl.glutKeyboardFunc)
    keyboard_up_callback = _func_property(_gl.glutKeyboardUpFunc)
    menu_destroy_callback = _func_property(_gl.glutMenuDestroyFunc)
    menu_state_callback = _func_property(_gl.glutMenuStateFunc)
    menu_status_callback = _func_property(_gl.glutMenuStatusFunc)
    motion_callback = _func_property(_gl.glutMotionFunc)
    mouse_callback = _func_property(_gl.glutMouseFunc)
    mouse_wheel_callback = _func_property(_gl.glutMouseWheelFunc)
    passive_motion_callback = _func_property(_gl.glutPassiveMotionFunc)
    reshape_callback = _func_property(_gl.glutReshapeFunc)
    special_callback = _func_property(_gl.glutSpecialFunc)
    special_up_callback = _func_property(_gl.glutSpecialUpFunc)
    visibility_callback = _func_property(_gl.glutVisibilityFunc)
    window_status_callback = _func_property(_gl.glutWindowStatusFunc)
    wm_close_callback = _func_property(_gl.glutWMCloseFunc)

initialize()

__all__ = [
    "main_loop",
    "main_loop_event",
    "leave_main_loop",
    "get_screen_shape",
    "get_screen_shape_mm",
    "get_elapsed_time",
    "get_shift_state",
    "get_ctrl_state",
    "get_alt_state",
    "GlutWindow",
]

