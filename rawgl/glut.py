from ctypes import *

_libraries = {}
_libraries['/usr/lib/libglut.so'] = CDLL('/usr/lib/libglut.so')
STRING = c_char_p


glutMainLoopEvent = _libraries['/usr/lib/libglut.so'].glutMainLoopEvent
glutMainLoopEvent.restype = None
glutMainLoopEvent.argtypes = []
glutMainLoopEvent.__doc__ = \
"""void glutMainLoopEvent()
/usr/include/GL/freeglut_ext.h:116"""
glutLeaveMainLoop = _libraries['/usr/lib/libglut.so'].glutLeaveMainLoop
glutLeaveMainLoop.restype = None
glutLeaveMainLoop.argtypes = []
glutLeaveMainLoop.__doc__ = \
"""void glutLeaveMainLoop()
/usr/include/GL/freeglut_ext.h:117"""
glutExit = _libraries['/usr/lib/libglut.so'].glutExit
glutExit.restype = None
glutExit.argtypes = []
glutExit.__doc__ = \
"""void glutExit()
/usr/include/GL/freeglut_ext.h:118"""
glutFullScreenToggle = _libraries['/usr/lib/libglut.so'].glutFullScreenToggle
glutFullScreenToggle.restype = None
glutFullScreenToggle.argtypes = []
glutFullScreenToggle.__doc__ = \
"""void glutFullScreenToggle()
/usr/include/GL/freeglut_ext.h:123"""
glutMouseWheelFunc = _libraries['/usr/lib/libglut.so'].glutMouseWheelFunc
glutMouseWheelFunc.restype = None
glutMouseWheelFunc.argtypes = [CFUNCTYPE(None, c_int, c_int, c_int, c_int)]
glutMouseWheelFunc.__doc__ = \
"""void glutMouseWheelFunc(unknown * callback)
/usr/include/GL/freeglut_ext.h:128"""
glutCloseFunc = _libraries['/usr/lib/libglut.so'].glutCloseFunc
glutCloseFunc.restype = None
glutCloseFunc.argtypes = [CFUNCTYPE(None)]
glutCloseFunc.__doc__ = \
"""void glutCloseFunc(unknown * callback)
/usr/include/GL/freeglut_ext.h:129"""
glutWMCloseFunc = _libraries['/usr/lib/libglut.so'].glutWMCloseFunc
glutWMCloseFunc.restype = None
glutWMCloseFunc.argtypes = [CFUNCTYPE(None)]
glutWMCloseFunc.__doc__ = \
"""void glutWMCloseFunc(unknown * callback)
/usr/include/GL/freeglut_ext.h:130"""
glutMenuDestroyFunc = _libraries['/usr/lib/libglut.so'].glutMenuDestroyFunc
glutMenuDestroyFunc.restype = None
glutMenuDestroyFunc.argtypes = [CFUNCTYPE(None)]
glutMenuDestroyFunc.__doc__ = \
"""void glutMenuDestroyFunc(unknown * callback)
/usr/include/GL/freeglut_ext.h:132"""
GLenum = c_uint
glutSetOption = _libraries['/usr/lib/libglut.so'].glutSetOption
glutSetOption.restype = None
glutSetOption.argtypes = [GLenum, c_int]
glutSetOption.__doc__ = \
"""void glutSetOption(GLenum option_flag, int value)
/usr/include/GL/freeglut_ext.h:137"""
glutGetModeValues = _libraries['/usr/lib/libglut.so'].glutGetModeValues
glutGetModeValues.restype = POINTER(c_int)
glutGetModeValues.argtypes = [GLenum, POINTER(c_int)]
glutGetModeValues.__doc__ = \
"""int * glutGetModeValues(GLenum mode, int * size)
/usr/include/GL/freeglut_ext.h:138"""
glutGetWindowData = _libraries['/usr/lib/libglut.so'].glutGetWindowData
glutGetWindowData.restype = c_void_p
glutGetWindowData.argtypes = []
glutGetWindowData.__doc__ = \
"""void * glutGetWindowData()
/usr/include/GL/freeglut_ext.h:140"""
glutSetWindowData = _libraries['/usr/lib/libglut.so'].glutSetWindowData
glutSetWindowData.restype = None
glutSetWindowData.argtypes = [c_void_p]
glutSetWindowData.__doc__ = \
"""void glutSetWindowData(void * data)
/usr/include/GL/freeglut_ext.h:141"""
glutGetMenuData = _libraries['/usr/lib/libglut.so'].glutGetMenuData
glutGetMenuData.restype = c_void_p
glutGetMenuData.argtypes = []
glutGetMenuData.__doc__ = \
"""void * glutGetMenuData()
/usr/include/GL/freeglut_ext.h:142"""
glutSetMenuData = _libraries['/usr/lib/libglut.so'].glutSetMenuData
glutSetMenuData.restype = None
glutSetMenuData.argtypes = [c_void_p]
glutSetMenuData.__doc__ = \
"""void glutSetMenuData(void * data)
/usr/include/GL/freeglut_ext.h:143"""
glutBitmapHeight = _libraries['/usr/lib/libglut.so'].glutBitmapHeight
glutBitmapHeight.restype = c_int
glutBitmapHeight.argtypes = [c_void_p]
glutBitmapHeight.__doc__ = \
"""int glutBitmapHeight(void * font)
/usr/include/GL/freeglut_ext.h:148"""
GLfloat = c_float
glutStrokeHeight = _libraries['/usr/lib/libglut.so'].glutStrokeHeight
glutStrokeHeight.restype = GLfloat
glutStrokeHeight.argtypes = [c_void_p]
glutStrokeHeight.__doc__ = \
"""GLfloat glutStrokeHeight(void * font)
/usr/include/GL/freeglut_ext.h:149"""
glutBitmapString = _libraries['/usr/lib/libglut.so'].glutBitmapString
glutBitmapString.restype = None
glutBitmapString.argtypes = [c_void_p, POINTER(c_ubyte)]
glutBitmapString.__doc__ = \
"""void glutBitmapString(void * font, unknown * string)
/usr/include/GL/freeglut_ext.h:150"""
glutStrokeString = _libraries['/usr/lib/libglut.so'].glutStrokeString
glutStrokeString.restype = None
glutStrokeString.argtypes = [c_void_p, POINTER(c_ubyte)]
glutStrokeString.__doc__ = \
"""void glutStrokeString(void * font, unknown * string)
/usr/include/GL/freeglut_ext.h:151"""
glutWireRhombicDodecahedron = _libraries['/usr/lib/libglut.so'].glutWireRhombicDodecahedron
glutWireRhombicDodecahedron.restype = None
glutWireRhombicDodecahedron.argtypes = []
glutWireRhombicDodecahedron.__doc__ = \
"""void glutWireRhombicDodecahedron()
/usr/include/GL/freeglut_ext.h:156"""
glutSolidRhombicDodecahedron = _libraries['/usr/lib/libglut.so'].glutSolidRhombicDodecahedron
glutSolidRhombicDodecahedron.restype = None
glutSolidRhombicDodecahedron.argtypes = []
glutSolidRhombicDodecahedron.__doc__ = \
"""void glutSolidRhombicDodecahedron()
/usr/include/GL/freeglut_ext.h:157"""
GLdouble = c_double
glutWireSierpinskiSponge = _libraries['/usr/lib/libglut.so'].glutWireSierpinskiSponge
glutWireSierpinskiSponge.restype = None
glutWireSierpinskiSponge.argtypes = [c_int, POINTER(GLdouble), GLdouble]
glutWireSierpinskiSponge.__doc__ = \
"""void glutWireSierpinskiSponge(int num_levels, GLdouble * offset, GLdouble scale)
/usr/include/GL/freeglut_ext.h:158"""
glutSolidSierpinskiSponge = _libraries['/usr/lib/libglut.so'].glutSolidSierpinskiSponge
glutSolidSierpinskiSponge.restype = None
glutSolidSierpinskiSponge.argtypes = [c_int, POINTER(GLdouble), GLdouble]
glutSolidSierpinskiSponge.__doc__ = \
"""void glutSolidSierpinskiSponge(int num_levels, GLdouble * offset, GLdouble scale)
/usr/include/GL/freeglut_ext.h:159"""
GLint = c_int
glutWireCylinder = _libraries['/usr/lib/libglut.so'].glutWireCylinder
glutWireCylinder.restype = None
glutWireCylinder.argtypes = [GLdouble, GLdouble, GLint, GLint]
glutWireCylinder.__doc__ = \
"""void glutWireCylinder(GLdouble radius, GLdouble height, GLint slices, GLint stacks)
/usr/include/GL/freeglut_ext.h:160"""
glutSolidCylinder = _libraries['/usr/lib/libglut.so'].glutSolidCylinder
glutSolidCylinder.restype = None
glutSolidCylinder.argtypes = [GLdouble, GLdouble, GLint, GLint]
glutSolidCylinder.__doc__ = \
"""void glutSolidCylinder(GLdouble radius, GLdouble height, GLint slices, GLint stacks)
/usr/include/GL/freeglut_ext.h:161"""
GLUTproc = CFUNCTYPE(None)
glutGetProcAddress = _libraries['/usr/lib/libglut.so'].glutGetProcAddress
glutGetProcAddress.restype = GLUTproc
glutGetProcAddress.argtypes = [STRING]
glutGetProcAddress.__doc__ = \
"""GLUTproc glutGetProcAddress(unknown * procName)
/usr/include/GL/freeglut_ext.h:167"""
glutJoystickGetNumAxes = _libraries['/usr/lib/libglut.so'].glutJoystickGetNumAxes
glutJoystickGetNumAxes.restype = c_int
glutJoystickGetNumAxes.argtypes = [c_int]
glutJoystickGetNumAxes.__doc__ = \
"""int glutJoystickGetNumAxes(int ident)
/usr/include/GL/freeglut_ext.h:178"""
glutJoystickGetNumButtons = _libraries['/usr/lib/libglut.so'].glutJoystickGetNumButtons
glutJoystickGetNumButtons.restype = c_int
glutJoystickGetNumButtons.argtypes = [c_int]
glutJoystickGetNumButtons.__doc__ = \
"""int glutJoystickGetNumButtons(int ident)
/usr/include/GL/freeglut_ext.h:179"""
glutJoystickNotWorking = _libraries['/usr/lib/libglut.so'].glutJoystickNotWorking
glutJoystickNotWorking.restype = c_int
glutJoystickNotWorking.argtypes = [c_int]
glutJoystickNotWorking.__doc__ = \
"""int glutJoystickNotWorking(int ident)
/usr/include/GL/freeglut_ext.h:180"""
glutJoystickGetDeadBand = _libraries['/usr/lib/libglut.so'].glutJoystickGetDeadBand
glutJoystickGetDeadBand.restype = c_float
glutJoystickGetDeadBand.argtypes = [c_int, c_int]
glutJoystickGetDeadBand.__doc__ = \
"""float glutJoystickGetDeadBand(int ident, int axis)
/usr/include/GL/freeglut_ext.h:181"""
glutJoystickSetDeadBand = _libraries['/usr/lib/libglut.so'].glutJoystickSetDeadBand
glutJoystickSetDeadBand.restype = None
glutJoystickSetDeadBand.argtypes = [c_int, c_int, c_float]
glutJoystickSetDeadBand.__doc__ = \
"""void glutJoystickSetDeadBand(int ident, int axis, float db)
/usr/include/GL/freeglut_ext.h:182"""
glutJoystickGetSaturation = _libraries['/usr/lib/libglut.so'].glutJoystickGetSaturation
glutJoystickGetSaturation.restype = c_float
glutJoystickGetSaturation.argtypes = [c_int, c_int]
glutJoystickGetSaturation.__doc__ = \
"""float glutJoystickGetSaturation(int ident, int axis)
/usr/include/GL/freeglut_ext.h:183"""
glutJoystickSetSaturation = _libraries['/usr/lib/libglut.so'].glutJoystickSetSaturation
glutJoystickSetSaturation.restype = None
glutJoystickSetSaturation.argtypes = [c_int, c_int, c_float]
glutJoystickSetSaturation.__doc__ = \
"""void glutJoystickSetSaturation(int ident, int axis, float st)
/usr/include/GL/freeglut_ext.h:184"""
glutJoystickSetMinRange = _libraries['/usr/lib/libglut.so'].glutJoystickSetMinRange
glutJoystickSetMinRange.restype = None
glutJoystickSetMinRange.argtypes = [c_int, POINTER(c_float)]
glutJoystickSetMinRange.__doc__ = \
"""void glutJoystickSetMinRange(int ident, float * axes)
/usr/include/GL/freeglut_ext.h:185"""
glutJoystickSetMaxRange = _libraries['/usr/lib/libglut.so'].glutJoystickSetMaxRange
glutJoystickSetMaxRange.restype = None
glutJoystickSetMaxRange.argtypes = [c_int, POINTER(c_float)]
glutJoystickSetMaxRange.__doc__ = \
"""void glutJoystickSetMaxRange(int ident, float * axes)
/usr/include/GL/freeglut_ext.h:186"""
glutJoystickSetCenter = _libraries['/usr/lib/libglut.so'].glutJoystickSetCenter
glutJoystickSetCenter.restype = None
glutJoystickSetCenter.argtypes = [c_int, POINTER(c_float)]
glutJoystickSetCenter.__doc__ = \
"""void glutJoystickSetCenter(int ident, float * axes)
/usr/include/GL/freeglut_ext.h:187"""
glutJoystickGetMinRange = _libraries['/usr/lib/libglut.so'].glutJoystickGetMinRange
glutJoystickGetMinRange.restype = None
glutJoystickGetMinRange.argtypes = [c_int, POINTER(c_float)]
glutJoystickGetMinRange.__doc__ = \
"""void glutJoystickGetMinRange(int ident, float * axes)
/usr/include/GL/freeglut_ext.h:188"""
glutJoystickGetMaxRange = _libraries['/usr/lib/libglut.so'].glutJoystickGetMaxRange
glutJoystickGetMaxRange.restype = None
glutJoystickGetMaxRange.argtypes = [c_int, POINTER(c_float)]
glutJoystickGetMaxRange.__doc__ = \
"""void glutJoystickGetMaxRange(int ident, float * axes)
/usr/include/GL/freeglut_ext.h:189"""
glutJoystickGetCenter = _libraries['/usr/lib/libglut.so'].glutJoystickGetCenter
glutJoystickGetCenter.restype = None
glutJoystickGetCenter.argtypes = [c_int, POINTER(c_float)]
glutJoystickGetCenter.__doc__ = \
"""void glutJoystickGetCenter(int ident, float * axes)
/usr/include/GL/freeglut_ext.h:190"""
glutInitContextVersion = _libraries['/usr/lib/libglut.so'].glutInitContextVersion
glutInitContextVersion.restype = None
glutInitContextVersion.argtypes = [c_int, c_int]
glutInitContextVersion.__doc__ = \
"""void glutInitContextVersion(int majorVersion, int minorVersion)
/usr/include/GL/freeglut_ext.h:195"""
glutInitContextFlags = _libraries['/usr/lib/libglut.so'].glutInitContextFlags
glutInitContextFlags.restype = None
glutInitContextFlags.argtypes = [c_int]
glutInitContextFlags.__doc__ = \
"""void glutInitContextFlags(int flags)
/usr/include/GL/freeglut_ext.h:196"""
glutInitContextProfile = _libraries['/usr/lib/libglut.so'].glutInitContextProfile
glutInitContextProfile.restype = None
glutInitContextProfile.argtypes = [c_int]
glutInitContextProfile.__doc__ = \
"""void glutInitContextProfile(int profile)
/usr/include/GL/freeglut_ext.h:197"""
glutStrokeRoman = (c_void_p).in_dll(_libraries['/usr/lib/libglut.so'], 'glutStrokeRoman')
glutStrokeMonoRoman = (c_void_p).in_dll(_libraries['/usr/lib/libglut.so'], 'glutStrokeMonoRoman')
glutBitmap9By15 = (c_void_p).in_dll(_libraries['/usr/lib/libglut.so'], 'glutBitmap9By15')
glutBitmap8By13 = (c_void_p).in_dll(_libraries['/usr/lib/libglut.so'], 'glutBitmap8By13')
glutBitmapTimesRoman10 = (c_void_p).in_dll(_libraries['/usr/lib/libglut.so'], 'glutBitmapTimesRoman10')
glutBitmapTimesRoman24 = (c_void_p).in_dll(_libraries['/usr/lib/libglut.so'], 'glutBitmapTimesRoman24')
glutBitmapHelvetica10 = (c_void_p).in_dll(_libraries['/usr/lib/libglut.so'], 'glutBitmapHelvetica10')
glutBitmapHelvetica12 = (c_void_p).in_dll(_libraries['/usr/lib/libglut.so'], 'glutBitmapHelvetica12')
glutBitmapHelvetica18 = (c_void_p).in_dll(_libraries['/usr/lib/libglut.so'], 'glutBitmapHelvetica18')
glutInit = _libraries['/usr/lib/libglut.so'].glutInit
glutInit.restype = None
glutInit.argtypes = [POINTER(c_int), POINTER(STRING)]
glutInit.__doc__ = \
"""void glutInit(int * pargc, char * * argv)
/usr/include/GL/freeglut_std.h:389"""
glutInitWindowPosition = _libraries['/usr/lib/libglut.so'].glutInitWindowPosition
glutInitWindowPosition.restype = None
glutInitWindowPosition.argtypes = [c_int, c_int]
glutInitWindowPosition.__doc__ = \
"""void glutInitWindowPosition(int x, int y)
/usr/include/GL/freeglut_std.h:390"""
glutInitWindowSize = _libraries['/usr/lib/libglut.so'].glutInitWindowSize
glutInitWindowSize.restype = None
glutInitWindowSize.argtypes = [c_int, c_int]
glutInitWindowSize.__doc__ = \
"""void glutInitWindowSize(int width, int height)
/usr/include/GL/freeglut_std.h:391"""
glutInitDisplayMode = _libraries['/usr/lib/libglut.so'].glutInitDisplayMode
glutInitDisplayMode.restype = None
glutInitDisplayMode.argtypes = [c_uint]
glutInitDisplayMode.__doc__ = \
"""void glutInitDisplayMode(unsigned int displayMode)
/usr/include/GL/freeglut_std.h:392"""
glutInitDisplayString = _libraries['/usr/lib/libglut.so'].glutInitDisplayString
glutInitDisplayString.restype = None
glutInitDisplayString.argtypes = [STRING]
glutInitDisplayString.__doc__ = \
"""void glutInitDisplayString(unknown * displayMode)
/usr/include/GL/freeglut_std.h:393"""
glutMainLoop = _libraries['/usr/lib/libglut.so'].glutMainLoop
glutMainLoop.restype = None
glutMainLoop.argtypes = []
glutMainLoop.__doc__ = \
"""void glutMainLoop()
/usr/include/GL/freeglut_std.h:398"""
glutCreateWindow = _libraries['/usr/lib/libglut.so'].glutCreateWindow
glutCreateWindow.restype = c_int
glutCreateWindow.argtypes = [STRING]
glutCreateWindow.__doc__ = \
"""int glutCreateWindow(unknown * title)
/usr/include/GL/freeglut_std.h:403"""
glutCreateSubWindow = _libraries['/usr/lib/libglut.so'].glutCreateSubWindow
glutCreateSubWindow.restype = c_int
glutCreateSubWindow.argtypes = [c_int, c_int, c_int, c_int, c_int]
glutCreateSubWindow.__doc__ = \
"""int glutCreateSubWindow(int window, int x, int y, int width, int height)
/usr/include/GL/freeglut_std.h:404"""
glutDestroyWindow = _libraries['/usr/lib/libglut.so'].glutDestroyWindow
glutDestroyWindow.restype = None
glutDestroyWindow.argtypes = [c_int]
glutDestroyWindow.__doc__ = \
"""void glutDestroyWindow(int window)
/usr/include/GL/freeglut_std.h:405"""
glutSetWindow = _libraries['/usr/lib/libglut.so'].glutSetWindow
glutSetWindow.restype = None
glutSetWindow.argtypes = [c_int]
glutSetWindow.__doc__ = \
"""void glutSetWindow(int window)
/usr/include/GL/freeglut_std.h:406"""
glutGetWindow = _libraries['/usr/lib/libglut.so'].glutGetWindow
glutGetWindow.restype = c_int
glutGetWindow.argtypes = []
glutGetWindow.__doc__ = \
"""int glutGetWindow()
/usr/include/GL/freeglut_std.h:407"""
glutSetWindowTitle = _libraries['/usr/lib/libglut.so'].glutSetWindowTitle
glutSetWindowTitle.restype = None
glutSetWindowTitle.argtypes = [STRING]
glutSetWindowTitle.__doc__ = \
"""void glutSetWindowTitle(unknown * title)
/usr/include/GL/freeglut_std.h:408"""
glutSetIconTitle = _libraries['/usr/lib/libglut.so'].glutSetIconTitle
glutSetIconTitle.restype = None
glutSetIconTitle.argtypes = [STRING]
glutSetIconTitle.__doc__ = \
"""void glutSetIconTitle(unknown * title)
/usr/include/GL/freeglut_std.h:409"""
glutReshapeWindow = _libraries['/usr/lib/libglut.so'].glutReshapeWindow
glutReshapeWindow.restype = None
glutReshapeWindow.argtypes = [c_int, c_int]
glutReshapeWindow.__doc__ = \
"""void glutReshapeWindow(int width, int height)
/usr/include/GL/freeglut_std.h:410"""
glutPositionWindow = _libraries['/usr/lib/libglut.so'].glutPositionWindow
glutPositionWindow.restype = None
glutPositionWindow.argtypes = [c_int, c_int]
glutPositionWindow.__doc__ = \
"""void glutPositionWindow(int x, int y)
/usr/include/GL/freeglut_std.h:411"""
glutShowWindow = _libraries['/usr/lib/libglut.so'].glutShowWindow
glutShowWindow.restype = None
glutShowWindow.argtypes = []
glutShowWindow.__doc__ = \
"""void glutShowWindow()
/usr/include/GL/freeglut_std.h:412"""
glutHideWindow = _libraries['/usr/lib/libglut.so'].glutHideWindow
glutHideWindow.restype = None
glutHideWindow.argtypes = []
glutHideWindow.__doc__ = \
"""void glutHideWindow()
/usr/include/GL/freeglut_std.h:413"""
glutIconifyWindow = _libraries['/usr/lib/libglut.so'].glutIconifyWindow
glutIconifyWindow.restype = None
glutIconifyWindow.argtypes = []
glutIconifyWindow.__doc__ = \
"""void glutIconifyWindow()
/usr/include/GL/freeglut_std.h:414"""
glutPushWindow = _libraries['/usr/lib/libglut.so'].glutPushWindow
glutPushWindow.restype = None
glutPushWindow.argtypes = []
glutPushWindow.__doc__ = \
"""void glutPushWindow()
/usr/include/GL/freeglut_std.h:415"""
glutPopWindow = _libraries['/usr/lib/libglut.so'].glutPopWindow
glutPopWindow.restype = None
glutPopWindow.argtypes = []
glutPopWindow.__doc__ = \
"""void glutPopWindow()
/usr/include/GL/freeglut_std.h:416"""
glutFullScreen = _libraries['/usr/lib/libglut.so'].glutFullScreen
glutFullScreen.restype = None
glutFullScreen.argtypes = []
glutFullScreen.__doc__ = \
"""void glutFullScreen()
/usr/include/GL/freeglut_std.h:417"""
glutPostWindowRedisplay = _libraries['/usr/lib/libglut.so'].glutPostWindowRedisplay
glutPostWindowRedisplay.restype = None
glutPostWindowRedisplay.argtypes = [c_int]
glutPostWindowRedisplay.__doc__ = \
"""void glutPostWindowRedisplay(int window)
/usr/include/GL/freeglut_std.h:422"""
glutPostRedisplay = _libraries['/usr/lib/libglut.so'].glutPostRedisplay
glutPostRedisplay.restype = None
glutPostRedisplay.argtypes = []
glutPostRedisplay.__doc__ = \
"""void glutPostRedisplay()
/usr/include/GL/freeglut_std.h:423"""
glutSwapBuffers = _libraries['/usr/lib/libglut.so'].glutSwapBuffers
glutSwapBuffers.restype = None
glutSwapBuffers.argtypes = []
glutSwapBuffers.__doc__ = \
"""void glutSwapBuffers()
/usr/include/GL/freeglut_std.h:424"""
glutWarpPointer = _libraries['/usr/lib/libglut.so'].glutWarpPointer
glutWarpPointer.restype = None
glutWarpPointer.argtypes = [c_int, c_int]
glutWarpPointer.__doc__ = \
"""void glutWarpPointer(int x, int y)
/usr/include/GL/freeglut_std.h:429"""
glutSetCursor = _libraries['/usr/lib/libglut.so'].glutSetCursor
glutSetCursor.restype = None
glutSetCursor.argtypes = [c_int]
glutSetCursor.__doc__ = \
"""void glutSetCursor(int cursor)
/usr/include/GL/freeglut_std.h:430"""
glutEstablishOverlay = _libraries['/usr/lib/libglut.so'].glutEstablishOverlay
glutEstablishOverlay.restype = None
glutEstablishOverlay.argtypes = []
glutEstablishOverlay.__doc__ = \
"""void glutEstablishOverlay()
/usr/include/GL/freeglut_std.h:435"""
glutRemoveOverlay = _libraries['/usr/lib/libglut.so'].glutRemoveOverlay
glutRemoveOverlay.restype = None
glutRemoveOverlay.argtypes = []
glutRemoveOverlay.__doc__ = \
"""void glutRemoveOverlay()
/usr/include/GL/freeglut_std.h:436"""
glutUseLayer = _libraries['/usr/lib/libglut.so'].glutUseLayer
glutUseLayer.restype = None
glutUseLayer.argtypes = [GLenum]
glutUseLayer.__doc__ = \
"""void glutUseLayer(GLenum layer)
/usr/include/GL/freeglut_std.h:437"""
glutPostOverlayRedisplay = _libraries['/usr/lib/libglut.so'].glutPostOverlayRedisplay
glutPostOverlayRedisplay.restype = None
glutPostOverlayRedisplay.argtypes = []
glutPostOverlayRedisplay.__doc__ = \
"""void glutPostOverlayRedisplay()
/usr/include/GL/freeglut_std.h:438"""
glutPostWindowOverlayRedisplay = _libraries['/usr/lib/libglut.so'].glutPostWindowOverlayRedisplay
glutPostWindowOverlayRedisplay.restype = None
glutPostWindowOverlayRedisplay.argtypes = [c_int]
glutPostWindowOverlayRedisplay.__doc__ = \
"""void glutPostWindowOverlayRedisplay(int window)
/usr/include/GL/freeglut_std.h:439"""
glutShowOverlay = _libraries['/usr/lib/libglut.so'].glutShowOverlay
glutShowOverlay.restype = None
glutShowOverlay.argtypes = []
glutShowOverlay.__doc__ = \
"""void glutShowOverlay()
/usr/include/GL/freeglut_std.h:440"""
glutHideOverlay = _libraries['/usr/lib/libglut.so'].glutHideOverlay
glutHideOverlay.restype = None
glutHideOverlay.argtypes = []
glutHideOverlay.__doc__ = \
"""void glutHideOverlay()
/usr/include/GL/freeglut_std.h:441"""
glutCreateMenu = _libraries['/usr/lib/libglut.so'].glutCreateMenu
glutCreateMenu.restype = c_int
glutCreateMenu.argtypes = [CFUNCTYPE(None, c_int)]
glutCreateMenu.__doc__ = \
"""int glutCreateMenu(unknown * callback)
/usr/include/GL/freeglut_std.h:446"""
glutDestroyMenu = _libraries['/usr/lib/libglut.so'].glutDestroyMenu
glutDestroyMenu.restype = None
glutDestroyMenu.argtypes = [c_int]
glutDestroyMenu.__doc__ = \
"""void glutDestroyMenu(int menu)
/usr/include/GL/freeglut_std.h:447"""
glutGetMenu = _libraries['/usr/lib/libglut.so'].glutGetMenu
glutGetMenu.restype = c_int
glutGetMenu.argtypes = []
glutGetMenu.__doc__ = \
"""int glutGetMenu()
/usr/include/GL/freeglut_std.h:448"""
glutSetMenu = _libraries['/usr/lib/libglut.so'].glutSetMenu
glutSetMenu.restype = None
glutSetMenu.argtypes = [c_int]
glutSetMenu.__doc__ = \
"""void glutSetMenu(int menu)
/usr/include/GL/freeglut_std.h:449"""
glutAddMenuEntry = _libraries['/usr/lib/libglut.so'].glutAddMenuEntry
glutAddMenuEntry.restype = None
glutAddMenuEntry.argtypes = [STRING, c_int]
glutAddMenuEntry.__doc__ = \
"""void glutAddMenuEntry(unknown * label, int value)
/usr/include/GL/freeglut_std.h:450"""
glutAddSubMenu = _libraries['/usr/lib/libglut.so'].glutAddSubMenu
glutAddSubMenu.restype = None
glutAddSubMenu.argtypes = [STRING, c_int]
glutAddSubMenu.__doc__ = \
"""void glutAddSubMenu(unknown * label, int subMenu)
/usr/include/GL/freeglut_std.h:451"""
glutChangeToMenuEntry = _libraries['/usr/lib/libglut.so'].glutChangeToMenuEntry
glutChangeToMenuEntry.restype = None
glutChangeToMenuEntry.argtypes = [c_int, STRING, c_int]
glutChangeToMenuEntry.__doc__ = \
"""void glutChangeToMenuEntry(int item, unknown * label, int value)
/usr/include/GL/freeglut_std.h:452"""
glutChangeToSubMenu = _libraries['/usr/lib/libglut.so'].glutChangeToSubMenu
glutChangeToSubMenu.restype = None
glutChangeToSubMenu.argtypes = [c_int, STRING, c_int]
glutChangeToSubMenu.__doc__ = \
"""void glutChangeToSubMenu(int item, unknown * label, int value)
/usr/include/GL/freeglut_std.h:453"""
glutRemoveMenuItem = _libraries['/usr/lib/libglut.so'].glutRemoveMenuItem
glutRemoveMenuItem.restype = None
glutRemoveMenuItem.argtypes = [c_int]
glutRemoveMenuItem.__doc__ = \
"""void glutRemoveMenuItem(int item)
/usr/include/GL/freeglut_std.h:454"""
glutAttachMenu = _libraries['/usr/lib/libglut.so'].glutAttachMenu
glutAttachMenu.restype = None
glutAttachMenu.argtypes = [c_int]
glutAttachMenu.__doc__ = \
"""void glutAttachMenu(int button)
/usr/include/GL/freeglut_std.h:455"""
glutDetachMenu = _libraries['/usr/lib/libglut.so'].glutDetachMenu
glutDetachMenu.restype = None
glutDetachMenu.argtypes = [c_int]
glutDetachMenu.__doc__ = \
"""void glutDetachMenu(int button)
/usr/include/GL/freeglut_std.h:456"""
glutTimerFunc = _libraries['/usr/lib/libglut.so'].glutTimerFunc
glutTimerFunc.restype = None
glutTimerFunc.argtypes = [c_uint, CFUNCTYPE(None, c_int), c_int]
glutTimerFunc.__doc__ = \
"""void glutTimerFunc(unsigned int time, unknown * callback, int value)
/usr/include/GL/freeglut_std.h:461"""
glutIdleFunc = _libraries['/usr/lib/libglut.so'].glutIdleFunc
glutIdleFunc.restype = None
glutIdleFunc.argtypes = [CFUNCTYPE(None)]
glutIdleFunc.__doc__ = \
"""void glutIdleFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:462"""
glutKeyboardFunc = _libraries['/usr/lib/libglut.so'].glutKeyboardFunc
glutKeyboardFunc.restype = None
glutKeyboardFunc.argtypes = [CFUNCTYPE(None, c_ubyte, c_int, c_int)]
glutKeyboardFunc.__doc__ = \
"""void glutKeyboardFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:467"""
glutSpecialFunc = _libraries['/usr/lib/libglut.so'].glutSpecialFunc
glutSpecialFunc.restype = None
glutSpecialFunc.argtypes = [CFUNCTYPE(None, c_int, c_int, c_int)]
glutSpecialFunc.__doc__ = \
"""void glutSpecialFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:468"""
glutReshapeFunc = _libraries['/usr/lib/libglut.so'].glutReshapeFunc
glutReshapeFunc.restype = None
glutReshapeFunc.argtypes = [CFUNCTYPE(None, c_int, c_int)]
glutReshapeFunc.__doc__ = \
"""void glutReshapeFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:469"""
glutVisibilityFunc = _libraries['/usr/lib/libglut.so'].glutVisibilityFunc
glutVisibilityFunc.restype = None
glutVisibilityFunc.argtypes = [CFUNCTYPE(None, c_int)]
glutVisibilityFunc.__doc__ = \
"""void glutVisibilityFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:470"""
glutDisplayFunc = _libraries['/usr/lib/libglut.so'].glutDisplayFunc
glutDisplayFunc.restype = None
glutDisplayFunc.argtypes = [CFUNCTYPE(None)]
glutDisplayFunc.__doc__ = \
"""void glutDisplayFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:471"""
glutMouseFunc = _libraries['/usr/lib/libglut.so'].glutMouseFunc
glutMouseFunc.restype = None
glutMouseFunc.argtypes = [CFUNCTYPE(None, c_int, c_int, c_int, c_int)]
glutMouseFunc.__doc__ = \
"""void glutMouseFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:472"""
glutMotionFunc = _libraries['/usr/lib/libglut.so'].glutMotionFunc
glutMotionFunc.restype = None
glutMotionFunc.argtypes = [CFUNCTYPE(None, c_int, c_int)]
glutMotionFunc.__doc__ = \
"""void glutMotionFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:473"""
glutPassiveMotionFunc = _libraries['/usr/lib/libglut.so'].glutPassiveMotionFunc
glutPassiveMotionFunc.restype = None
glutPassiveMotionFunc.argtypes = [CFUNCTYPE(None, c_int, c_int)]
glutPassiveMotionFunc.__doc__ = \
"""void glutPassiveMotionFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:474"""
glutEntryFunc = _libraries['/usr/lib/libglut.so'].glutEntryFunc
glutEntryFunc.restype = None
glutEntryFunc.argtypes = [CFUNCTYPE(None, c_int)]
glutEntryFunc.__doc__ = \
"""void glutEntryFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:475"""
glutKeyboardUpFunc = _libraries['/usr/lib/libglut.so'].glutKeyboardUpFunc
glutKeyboardUpFunc.restype = None
glutKeyboardUpFunc.argtypes = [CFUNCTYPE(None, c_ubyte, c_int, c_int)]
glutKeyboardUpFunc.__doc__ = \
"""void glutKeyboardUpFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:477"""
glutSpecialUpFunc = _libraries['/usr/lib/libglut.so'].glutSpecialUpFunc
glutSpecialUpFunc.restype = None
glutSpecialUpFunc.argtypes = [CFUNCTYPE(None, c_int, c_int, c_int)]
glutSpecialUpFunc.__doc__ = \
"""void glutSpecialUpFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:478"""
glutJoystickFunc = _libraries['/usr/lib/libglut.so'].glutJoystickFunc
glutJoystickFunc.restype = None
glutJoystickFunc.argtypes = [CFUNCTYPE(None, c_uint, c_int, c_int, c_int), c_int]
glutJoystickFunc.__doc__ = \
"""void glutJoystickFunc(unknown * callback, int pollInterval)
/usr/include/GL/freeglut_std.h:479"""
glutMenuStateFunc = _libraries['/usr/lib/libglut.so'].glutMenuStateFunc
glutMenuStateFunc.restype = None
glutMenuStateFunc.argtypes = [CFUNCTYPE(None, c_int)]
glutMenuStateFunc.__doc__ = \
"""void glutMenuStateFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:480"""
glutMenuStatusFunc = _libraries['/usr/lib/libglut.so'].glutMenuStatusFunc
glutMenuStatusFunc.restype = None
glutMenuStatusFunc.argtypes = [CFUNCTYPE(None, c_int, c_int, c_int)]
glutMenuStatusFunc.__doc__ = \
"""void glutMenuStatusFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:481"""
glutOverlayDisplayFunc = _libraries['/usr/lib/libglut.so'].glutOverlayDisplayFunc
glutOverlayDisplayFunc.restype = None
glutOverlayDisplayFunc.argtypes = [CFUNCTYPE(None)]
glutOverlayDisplayFunc.__doc__ = \
"""void glutOverlayDisplayFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:482"""
glutWindowStatusFunc = _libraries['/usr/lib/libglut.so'].glutWindowStatusFunc
glutWindowStatusFunc.restype = None
glutWindowStatusFunc.argtypes = [CFUNCTYPE(None, c_int)]
glutWindowStatusFunc.__doc__ = \
"""void glutWindowStatusFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:483"""
glutSpaceballMotionFunc = _libraries['/usr/lib/libglut.so'].glutSpaceballMotionFunc
glutSpaceballMotionFunc.restype = None
glutSpaceballMotionFunc.argtypes = [CFUNCTYPE(None, c_int, c_int, c_int)]
glutSpaceballMotionFunc.__doc__ = \
"""void glutSpaceballMotionFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:485"""
glutSpaceballRotateFunc = _libraries['/usr/lib/libglut.so'].glutSpaceballRotateFunc
glutSpaceballRotateFunc.restype = None
glutSpaceballRotateFunc.argtypes = [CFUNCTYPE(None, c_int, c_int, c_int)]
glutSpaceballRotateFunc.__doc__ = \
"""void glutSpaceballRotateFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:486"""
glutSpaceballButtonFunc = _libraries['/usr/lib/libglut.so'].glutSpaceballButtonFunc
glutSpaceballButtonFunc.restype = None
glutSpaceballButtonFunc.argtypes = [CFUNCTYPE(None, c_int, c_int)]
glutSpaceballButtonFunc.__doc__ = \
"""void glutSpaceballButtonFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:487"""
glutButtonBoxFunc = _libraries['/usr/lib/libglut.so'].glutButtonBoxFunc
glutButtonBoxFunc.restype = None
glutButtonBoxFunc.argtypes = [CFUNCTYPE(None, c_int, c_int)]
glutButtonBoxFunc.__doc__ = \
"""void glutButtonBoxFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:488"""
glutDialsFunc = _libraries['/usr/lib/libglut.so'].glutDialsFunc
glutDialsFunc.restype = None
glutDialsFunc.argtypes = [CFUNCTYPE(None, c_int, c_int)]
glutDialsFunc.__doc__ = \
"""void glutDialsFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:489"""
glutTabletMotionFunc = _libraries['/usr/lib/libglut.so'].glutTabletMotionFunc
glutTabletMotionFunc.restype = None
glutTabletMotionFunc.argtypes = [CFUNCTYPE(None, c_int, c_int)]
glutTabletMotionFunc.__doc__ = \
"""void glutTabletMotionFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:490"""
glutTabletButtonFunc = _libraries['/usr/lib/libglut.so'].glutTabletButtonFunc
glutTabletButtonFunc.restype = None
glutTabletButtonFunc.argtypes = [CFUNCTYPE(None, c_int, c_int, c_int, c_int)]
glutTabletButtonFunc.__doc__ = \
"""void glutTabletButtonFunc(unknown * callback)
/usr/include/GL/freeglut_std.h:491"""
glutGet = _libraries['/usr/lib/libglut.so'].glutGet
glutGet.restype = c_int
glutGet.argtypes = [GLenum]
glutGet.__doc__ = \
"""int glutGet(GLenum query)
/usr/include/GL/freeglut_std.h:496"""
glutDeviceGet = _libraries['/usr/lib/libglut.so'].glutDeviceGet
glutDeviceGet.restype = c_int
glutDeviceGet.argtypes = [GLenum]
glutDeviceGet.__doc__ = \
"""int glutDeviceGet(GLenum query)
/usr/include/GL/freeglut_std.h:497"""
glutGetModifiers = _libraries['/usr/lib/libglut.so'].glutGetModifiers
glutGetModifiers.restype = c_int
glutGetModifiers.argtypes = []
glutGetModifiers.__doc__ = \
"""int glutGetModifiers()
/usr/include/GL/freeglut_std.h:498"""
glutLayerGet = _libraries['/usr/lib/libglut.so'].glutLayerGet
glutLayerGet.restype = c_int
glutLayerGet.argtypes = [GLenum]
glutLayerGet.__doc__ = \
"""int glutLayerGet(GLenum query)
/usr/include/GL/freeglut_std.h:499"""
glutBitmapCharacter = _libraries['/usr/lib/libglut.so'].glutBitmapCharacter
glutBitmapCharacter.restype = None
glutBitmapCharacter.argtypes = [c_void_p, c_int]
glutBitmapCharacter.__doc__ = \
"""void glutBitmapCharacter(void * font, int character)
/usr/include/GL/freeglut_std.h:504"""
glutBitmapWidth = _libraries['/usr/lib/libglut.so'].glutBitmapWidth
glutBitmapWidth.restype = c_int
glutBitmapWidth.argtypes = [c_void_p, c_int]
glutBitmapWidth.__doc__ = \
"""int glutBitmapWidth(void * font, int character)
/usr/include/GL/freeglut_std.h:505"""
glutStrokeCharacter = _libraries['/usr/lib/libglut.so'].glutStrokeCharacter
glutStrokeCharacter.restype = None
glutStrokeCharacter.argtypes = [c_void_p, c_int]
glutStrokeCharacter.__doc__ = \
"""void glutStrokeCharacter(void * font, int character)
/usr/include/GL/freeglut_std.h:506"""
glutStrokeWidth = _libraries['/usr/lib/libglut.so'].glutStrokeWidth
glutStrokeWidth.restype = c_int
glutStrokeWidth.argtypes = [c_void_p, c_int]
glutStrokeWidth.__doc__ = \
"""int glutStrokeWidth(void * font, int character)
/usr/include/GL/freeglut_std.h:507"""
glutBitmapLength = _libraries['/usr/lib/libglut.so'].glutBitmapLength
glutBitmapLength.restype = c_int
glutBitmapLength.argtypes = [c_void_p, POINTER(c_ubyte)]
glutBitmapLength.__doc__ = \
"""int glutBitmapLength(void * font, unknown * string)
/usr/include/GL/freeglut_std.h:508"""
glutStrokeLength = _libraries['/usr/lib/libglut.so'].glutStrokeLength
glutStrokeLength.restype = c_int
glutStrokeLength.argtypes = [c_void_p, POINTER(c_ubyte)]
glutStrokeLength.__doc__ = \
"""int glutStrokeLength(void * font, unknown * string)
/usr/include/GL/freeglut_std.h:509"""
glutWireCube = _libraries['/usr/lib/libglut.so'].glutWireCube
glutWireCube.restype = None
glutWireCube.argtypes = [GLdouble]
glutWireCube.__doc__ = \
"""void glutWireCube(GLdouble size)
/usr/include/GL/freeglut_std.h:514"""
glutSolidCube = _libraries['/usr/lib/libglut.so'].glutSolidCube
glutSolidCube.restype = None
glutSolidCube.argtypes = [GLdouble]
glutSolidCube.__doc__ = \
"""void glutSolidCube(GLdouble size)
/usr/include/GL/freeglut_std.h:515"""
glutWireSphere = _libraries['/usr/lib/libglut.so'].glutWireSphere
glutWireSphere.restype = None
glutWireSphere.argtypes = [GLdouble, GLint, GLint]
glutWireSphere.__doc__ = \
"""void glutWireSphere(GLdouble radius, GLint slices, GLint stacks)
/usr/include/GL/freeglut_std.h:516"""
glutSolidSphere = _libraries['/usr/lib/libglut.so'].glutSolidSphere
glutSolidSphere.restype = None
glutSolidSphere.argtypes = [GLdouble, GLint, GLint]
glutSolidSphere.__doc__ = \
"""void glutSolidSphere(GLdouble radius, GLint slices, GLint stacks)
/usr/include/GL/freeglut_std.h:517"""
glutWireCone = _libraries['/usr/lib/libglut.so'].glutWireCone
glutWireCone.restype = None
glutWireCone.argtypes = [GLdouble, GLdouble, GLint, GLint]
glutWireCone.__doc__ = \
"""void glutWireCone(GLdouble base, GLdouble height, GLint slices, GLint stacks)
/usr/include/GL/freeglut_std.h:518"""
glutSolidCone = _libraries['/usr/lib/libglut.so'].glutSolidCone
glutSolidCone.restype = None
glutSolidCone.argtypes = [GLdouble, GLdouble, GLint, GLint]
glutSolidCone.__doc__ = \
"""void glutSolidCone(GLdouble base, GLdouble height, GLint slices, GLint stacks)
/usr/include/GL/freeglut_std.h:519"""
glutWireTorus = _libraries['/usr/lib/libglut.so'].glutWireTorus
glutWireTorus.restype = None
glutWireTorus.argtypes = [GLdouble, GLdouble, GLint, GLint]
glutWireTorus.__doc__ = \
"""void glutWireTorus(GLdouble innerRadius, GLdouble outerRadius, GLint sides, GLint rings)
/usr/include/GL/freeglut_std.h:521"""
glutSolidTorus = _libraries['/usr/lib/libglut.so'].glutSolidTorus
glutSolidTorus.restype = None
glutSolidTorus.argtypes = [GLdouble, GLdouble, GLint, GLint]
glutSolidTorus.__doc__ = \
"""void glutSolidTorus(GLdouble innerRadius, GLdouble outerRadius, GLint sides, GLint rings)
/usr/include/GL/freeglut_std.h:522"""
glutWireDodecahedron = _libraries['/usr/lib/libglut.so'].glutWireDodecahedron
glutWireDodecahedron.restype = None
glutWireDodecahedron.argtypes = []
glutWireDodecahedron.__doc__ = \
"""void glutWireDodecahedron()
/usr/include/GL/freeglut_std.h:523"""
glutSolidDodecahedron = _libraries['/usr/lib/libglut.so'].glutSolidDodecahedron
glutSolidDodecahedron.restype = None
glutSolidDodecahedron.argtypes = []
glutSolidDodecahedron.__doc__ = \
"""void glutSolidDodecahedron()
/usr/include/GL/freeglut_std.h:524"""
glutWireOctahedron = _libraries['/usr/lib/libglut.so'].glutWireOctahedron
glutWireOctahedron.restype = None
glutWireOctahedron.argtypes = []
glutWireOctahedron.__doc__ = \
"""void glutWireOctahedron()
/usr/include/GL/freeglut_std.h:525"""
glutSolidOctahedron = _libraries['/usr/lib/libglut.so'].glutSolidOctahedron
glutSolidOctahedron.restype = None
glutSolidOctahedron.argtypes = []
glutSolidOctahedron.__doc__ = \
"""void glutSolidOctahedron()
/usr/include/GL/freeglut_std.h:526"""
glutWireTetrahedron = _libraries['/usr/lib/libglut.so'].glutWireTetrahedron
glutWireTetrahedron.restype = None
glutWireTetrahedron.argtypes = []
glutWireTetrahedron.__doc__ = \
"""void glutWireTetrahedron()
/usr/include/GL/freeglut_std.h:527"""
glutSolidTetrahedron = _libraries['/usr/lib/libglut.so'].glutSolidTetrahedron
glutSolidTetrahedron.restype = None
glutSolidTetrahedron.argtypes = []
glutSolidTetrahedron.__doc__ = \
"""void glutSolidTetrahedron()
/usr/include/GL/freeglut_std.h:528"""
glutWireIcosahedron = _libraries['/usr/lib/libglut.so'].glutWireIcosahedron
glutWireIcosahedron.restype = None
glutWireIcosahedron.argtypes = []
glutWireIcosahedron.__doc__ = \
"""void glutWireIcosahedron()
/usr/include/GL/freeglut_std.h:529"""
glutSolidIcosahedron = _libraries['/usr/lib/libglut.so'].glutSolidIcosahedron
glutSolidIcosahedron.restype = None
glutSolidIcosahedron.argtypes = []
glutSolidIcosahedron.__doc__ = \
"""void glutSolidIcosahedron()
/usr/include/GL/freeglut_std.h:530"""
glutWireTeapot = _libraries['/usr/lib/libglut.so'].glutWireTeapot
glutWireTeapot.restype = None
glutWireTeapot.argtypes = [GLdouble]
glutWireTeapot.__doc__ = \
"""void glutWireTeapot(GLdouble size)
/usr/include/GL/freeglut_std.h:535"""
glutSolidTeapot = _libraries['/usr/lib/libglut.so'].glutSolidTeapot
glutSolidTeapot.restype = None
glutSolidTeapot.argtypes = [GLdouble]
glutSolidTeapot.__doc__ = \
"""void glutSolidTeapot(GLdouble size)
/usr/include/GL/freeglut_std.h:536"""
glutGameModeString = _libraries['/usr/lib/libglut.so'].glutGameModeString
glutGameModeString.restype = None
glutGameModeString.argtypes = [STRING]
glutGameModeString.__doc__ = \
"""void glutGameModeString(unknown * string)
/usr/include/GL/freeglut_std.h:541"""
glutEnterGameMode = _libraries['/usr/lib/libglut.so'].glutEnterGameMode
glutEnterGameMode.restype = c_int
glutEnterGameMode.argtypes = []
glutEnterGameMode.__doc__ = \
"""int glutEnterGameMode()
/usr/include/GL/freeglut_std.h:542"""
glutLeaveGameMode = _libraries['/usr/lib/libglut.so'].glutLeaveGameMode
glutLeaveGameMode.restype = None
glutLeaveGameMode.argtypes = []
glutLeaveGameMode.__doc__ = \
"""void glutLeaveGameMode()
/usr/include/GL/freeglut_std.h:543"""
glutGameModeGet = _libraries['/usr/lib/libglut.so'].glutGameModeGet
glutGameModeGet.restype = c_int
glutGameModeGet.argtypes = [GLenum]
glutGameModeGet.__doc__ = \
"""int glutGameModeGet(GLenum query)
/usr/include/GL/freeglut_std.h:544"""
glutVideoResizeGet = _libraries['/usr/lib/libglut.so'].glutVideoResizeGet
glutVideoResizeGet.restype = c_int
glutVideoResizeGet.argtypes = [GLenum]
glutVideoResizeGet.__doc__ = \
"""int glutVideoResizeGet(GLenum query)
/usr/include/GL/freeglut_std.h:549"""
glutSetupVideoResizing = _libraries['/usr/lib/libglut.so'].glutSetupVideoResizing
glutSetupVideoResizing.restype = None
glutSetupVideoResizing.argtypes = []
glutSetupVideoResizing.__doc__ = \
"""void glutSetupVideoResizing()
/usr/include/GL/freeglut_std.h:550"""
glutStopVideoResizing = _libraries['/usr/lib/libglut.so'].glutStopVideoResizing
glutStopVideoResizing.restype = None
glutStopVideoResizing.argtypes = []
glutStopVideoResizing.__doc__ = \
"""void glutStopVideoResizing()
/usr/include/GL/freeglut_std.h:551"""
glutVideoResize = _libraries['/usr/lib/libglut.so'].glutVideoResize
glutVideoResize.restype = None
glutVideoResize.argtypes = [c_int, c_int, c_int, c_int]
glutVideoResize.__doc__ = \
"""void glutVideoResize(int x, int y, int width, int height)
/usr/include/GL/freeglut_std.h:552"""
glutVideoPan = _libraries['/usr/lib/libglut.so'].glutVideoPan
glutVideoPan.restype = None
glutVideoPan.argtypes = [c_int, c_int, c_int, c_int]
glutVideoPan.__doc__ = \
"""void glutVideoPan(int x, int y, int width, int height)
/usr/include/GL/freeglut_std.h:553"""
glutSetColor = _libraries['/usr/lib/libglut.so'].glutSetColor
glutSetColor.restype = None
glutSetColor.argtypes = [c_int, GLfloat, GLfloat, GLfloat]
glutSetColor.__doc__ = \
"""void glutSetColor(int color, GLfloat red, GLfloat green, GLfloat blue)
/usr/include/GL/freeglut_std.h:558"""
glutGetColor = _libraries['/usr/lib/libglut.so'].glutGetColor
glutGetColor.restype = GLfloat
glutGetColor.argtypes = [c_int, c_int]
glutGetColor.__doc__ = \
"""GLfloat glutGetColor(int color, int component)
/usr/include/GL/freeglut_std.h:559"""
glutCopyColormap = _libraries['/usr/lib/libglut.so'].glutCopyColormap
glutCopyColormap.restype = None
glutCopyColormap.argtypes = [c_int]
glutCopyColormap.__doc__ = \
"""void glutCopyColormap(int window)
/usr/include/GL/freeglut_std.h:560"""
glutIgnoreKeyRepeat = _libraries['/usr/lib/libglut.so'].glutIgnoreKeyRepeat
glutIgnoreKeyRepeat.restype = None
glutIgnoreKeyRepeat.argtypes = [c_int]
glutIgnoreKeyRepeat.__doc__ = \
"""void glutIgnoreKeyRepeat(int ignore)
/usr/include/GL/freeglut_std.h:565"""
glutSetKeyRepeat = _libraries['/usr/lib/libglut.so'].glutSetKeyRepeat
glutSetKeyRepeat.restype = None
glutSetKeyRepeat.argtypes = [c_int]
glutSetKeyRepeat.__doc__ = \
"""void glutSetKeyRepeat(int repeatMode)
/usr/include/GL/freeglut_std.h:566"""
glutForceJoystickFunc = _libraries['/usr/lib/libglut.so'].glutForceJoystickFunc
glutForceJoystickFunc.restype = None
glutForceJoystickFunc.argtypes = []
glutForceJoystickFunc.__doc__ = \
"""void glutForceJoystickFunc()
/usr/include/GL/freeglut_std.h:567"""
glutExtensionSupported = _libraries['/usr/lib/libglut.so'].glutExtensionSupported
glutExtensionSupported.restype = c_int
glutExtensionSupported.argtypes = [STRING]
glutExtensionSupported.__doc__ = \
"""int glutExtensionSupported(unknown * extension)
/usr/include/GL/freeglut_std.h:572"""
glutReportErrors = _libraries['/usr/lib/libglut.so'].glutReportErrors
glutReportErrors.restype = None
glutReportErrors.argtypes = []
glutReportErrors.__doc__ = \
"""void glutReportErrors()
/usr/include/GL/freeglut_std.h:573"""
GLboolean = c_ubyte
GLbitfield = c_uint
GLvoid = None
GLbyte = c_byte
GLshort = c_short
GLubyte = c_ubyte
GLushort = c_ushort
GLuint = c_uint
GLsizei = c_int
GLclampf = c_float
GLclampd = c_double
glClearIndex = _libraries['/usr/lib/libglut.so'].glClearIndex
glClearIndex.restype = None
glClearIndex.argtypes = [GLfloat]
glClearIndex.__doc__ = \
"""void glClearIndex(GLfloat c)
/usr/include/GL/gl.h:782"""
glClearColor = _libraries['/usr/lib/libglut.so'].glClearColor
glClearColor.restype = None
glClearColor.argtypes = [GLclampf, GLclampf, GLclampf, GLclampf]
glClearColor.__doc__ = \
"""void glClearColor(GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha)
/usr/include/GL/gl.h:784"""
glClear = _libraries['/usr/lib/libglut.so'].glClear
glClear.restype = None
glClear.argtypes = [GLbitfield]
glClear.__doc__ = \
"""void glClear(GLbitfield mask)
/usr/include/GL/gl.h:786"""
glIndexMask = _libraries['/usr/lib/libglut.so'].glIndexMask
glIndexMask.restype = None
glIndexMask.argtypes = [GLuint]
glIndexMask.__doc__ = \
"""void glIndexMask(GLuint mask)
/usr/include/GL/gl.h:788"""
glColorMask = _libraries['/usr/lib/libglut.so'].glColorMask
glColorMask.restype = None
glColorMask.argtypes = [GLboolean, GLboolean, GLboolean, GLboolean]
glColorMask.__doc__ = \
"""void glColorMask(GLboolean red, GLboolean green, GLboolean blue, GLboolean alpha)
/usr/include/GL/gl.h:790"""
glAlphaFunc = _libraries['/usr/lib/libglut.so'].glAlphaFunc
glAlphaFunc.restype = None
glAlphaFunc.argtypes = [GLenum, GLclampf]
glAlphaFunc.__doc__ = \
"""void glAlphaFunc(GLenum func, GLclampf ref)
/usr/include/GL/gl.h:792"""
glBlendFunc = _libraries['/usr/lib/libglut.so'].glBlendFunc
glBlendFunc.restype = None
glBlendFunc.argtypes = [GLenum, GLenum]
glBlendFunc.__doc__ = \
"""void glBlendFunc(GLenum sfactor, GLenum dfactor)
/usr/include/GL/gl.h:794"""
glLogicOp = _libraries['/usr/lib/libglut.so'].glLogicOp
glLogicOp.restype = None
glLogicOp.argtypes = [GLenum]
glLogicOp.__doc__ = \
"""void glLogicOp(GLenum opcode)
/usr/include/GL/gl.h:796"""
glCullFace = _libraries['/usr/lib/libglut.so'].glCullFace
glCullFace.restype = None
glCullFace.argtypes = [GLenum]
glCullFace.__doc__ = \
"""void glCullFace(GLenum mode)
/usr/include/GL/gl.h:798"""
glFrontFace = _libraries['/usr/lib/libglut.so'].glFrontFace
glFrontFace.restype = None
glFrontFace.argtypes = [GLenum]
glFrontFace.__doc__ = \
"""void glFrontFace(GLenum mode)
/usr/include/GL/gl.h:800"""
glPointSize = _libraries['/usr/lib/libglut.so'].glPointSize
glPointSize.restype = None
glPointSize.argtypes = [GLfloat]
glPointSize.__doc__ = \
"""void glPointSize(GLfloat size)
/usr/include/GL/gl.h:802"""
glLineWidth = _libraries['/usr/lib/libglut.so'].glLineWidth
glLineWidth.restype = None
glLineWidth.argtypes = [GLfloat]
glLineWidth.__doc__ = \
"""void glLineWidth(GLfloat width)
/usr/include/GL/gl.h:804"""
glLineStipple = _libraries['/usr/lib/libglut.so'].glLineStipple
glLineStipple.restype = None
glLineStipple.argtypes = [GLint, GLushort]
glLineStipple.__doc__ = \
"""void glLineStipple(GLint factor, GLushort pattern)
/usr/include/GL/gl.h:806"""
glPolygonMode = _libraries['/usr/lib/libglut.so'].glPolygonMode
glPolygonMode.restype = None
glPolygonMode.argtypes = [GLenum, GLenum]
glPolygonMode.__doc__ = \
"""void glPolygonMode(GLenum face, GLenum mode)
/usr/include/GL/gl.h:808"""
glPolygonOffset = _libraries['/usr/lib/libglut.so'].glPolygonOffset
glPolygonOffset.restype = None
glPolygonOffset.argtypes = [GLfloat, GLfloat]
glPolygonOffset.__doc__ = \
"""void glPolygonOffset(GLfloat factor, GLfloat units)
/usr/include/GL/gl.h:810"""
glPolygonStipple = _libraries['/usr/lib/libglut.so'].glPolygonStipple
glPolygonStipple.restype = None
glPolygonStipple.argtypes = [POINTER(GLubyte)]
glPolygonStipple.__doc__ = \
"""void glPolygonStipple(unknown * mask)
/usr/include/GL/gl.h:812"""
glGetPolygonStipple = _libraries['/usr/lib/libglut.so'].glGetPolygonStipple
glGetPolygonStipple.restype = None
glGetPolygonStipple.argtypes = [POINTER(GLubyte)]
glGetPolygonStipple.__doc__ = \
"""void glGetPolygonStipple(GLubyte * mask)
/usr/include/GL/gl.h:814"""
glEdgeFlag = _libraries['/usr/lib/libglut.so'].glEdgeFlag
glEdgeFlag.restype = None
glEdgeFlag.argtypes = [GLboolean]
glEdgeFlag.__doc__ = \
"""void glEdgeFlag(GLboolean flag)
/usr/include/GL/gl.h:816"""
glEdgeFlagv = _libraries['/usr/lib/libglut.so'].glEdgeFlagv
glEdgeFlagv.restype = None
glEdgeFlagv.argtypes = [POINTER(GLboolean)]
glEdgeFlagv.__doc__ = \
"""void glEdgeFlagv(unknown * flag)
/usr/include/GL/gl.h:818"""
glScissor = _libraries['/usr/lib/libglut.so'].glScissor
glScissor.restype = None
glScissor.argtypes = [GLint, GLint, GLsizei, GLsizei]
glScissor.__doc__ = \
"""void glScissor(GLint x, GLint y, GLsizei width, GLsizei height)
/usr/include/GL/gl.h:820"""
glClipPlane = _libraries['/usr/lib/libglut.so'].glClipPlane
glClipPlane.restype = None
glClipPlane.argtypes = [GLenum, POINTER(GLdouble)]
glClipPlane.__doc__ = \
"""void glClipPlane(GLenum plane, unknown * equation)
/usr/include/GL/gl.h:822"""
glGetClipPlane = _libraries['/usr/lib/libglut.so'].glGetClipPlane
glGetClipPlane.restype = None
glGetClipPlane.argtypes = [GLenum, POINTER(GLdouble)]
glGetClipPlane.__doc__ = \
"""void glGetClipPlane(GLenum plane, GLdouble * equation)
/usr/include/GL/gl.h:824"""
glDrawBuffer = _libraries['/usr/lib/libglut.so'].glDrawBuffer
glDrawBuffer.restype = None
glDrawBuffer.argtypes = [GLenum]
glDrawBuffer.__doc__ = \
"""void glDrawBuffer(GLenum mode)
/usr/include/GL/gl.h:826"""
glReadBuffer = _libraries['/usr/lib/libglut.so'].glReadBuffer
glReadBuffer.restype = None
glReadBuffer.argtypes = [GLenum]
glReadBuffer.__doc__ = \
"""void glReadBuffer(GLenum mode)
/usr/include/GL/gl.h:828"""
glEnable = _libraries['/usr/lib/libglut.so'].glEnable
glEnable.restype = None
glEnable.argtypes = [GLenum]
glEnable.__doc__ = \
"""void glEnable(GLenum cap)
/usr/include/GL/gl.h:830"""
glDisable = _libraries['/usr/lib/libglut.so'].glDisable
glDisable.restype = None
glDisable.argtypes = [GLenum]
glDisable.__doc__ = \
"""void glDisable(GLenum cap)
/usr/include/GL/gl.h:832"""
glIsEnabled = _libraries['/usr/lib/libglut.so'].glIsEnabled
glIsEnabled.restype = GLboolean
glIsEnabled.argtypes = [GLenum]
glIsEnabled.__doc__ = \
"""GLboolean glIsEnabled(GLenum cap)
/usr/include/GL/gl.h:834"""
glEnableClientState = _libraries['/usr/lib/libglut.so'].glEnableClientState
glEnableClientState.restype = None
glEnableClientState.argtypes = [GLenum]
glEnableClientState.__doc__ = \
"""void glEnableClientState(GLenum cap)
/usr/include/GL/gl.h:837"""
glDisableClientState = _libraries['/usr/lib/libglut.so'].glDisableClientState
glDisableClientState.restype = None
glDisableClientState.argtypes = [GLenum]
glDisableClientState.__doc__ = \
"""void glDisableClientState(GLenum cap)
/usr/include/GL/gl.h:839"""
glGetBooleanv = _libraries['/usr/lib/libglut.so'].glGetBooleanv
glGetBooleanv.restype = None
glGetBooleanv.argtypes = [GLenum, POINTER(GLboolean)]
glGetBooleanv.__doc__ = \
"""void glGetBooleanv(GLenum pname, GLboolean * params)
/usr/include/GL/gl.h:842"""
glGetDoublev = _libraries['/usr/lib/libglut.so'].glGetDoublev
glGetDoublev.restype = None
glGetDoublev.argtypes = [GLenum, POINTER(GLdouble)]
glGetDoublev.__doc__ = \
"""void glGetDoublev(GLenum pname, GLdouble * params)
/usr/include/GL/gl.h:844"""
glGetFloatv = _libraries['/usr/lib/libglut.so'].glGetFloatv
glGetFloatv.restype = None
glGetFloatv.argtypes = [GLenum, POINTER(GLfloat)]
glGetFloatv.__doc__ = \
"""void glGetFloatv(GLenum pname, GLfloat * params)
/usr/include/GL/gl.h:846"""
glGetIntegerv = _libraries['/usr/lib/libglut.so'].glGetIntegerv
glGetIntegerv.restype = None
glGetIntegerv.argtypes = [GLenum, POINTER(GLint)]
glGetIntegerv.__doc__ = \
"""void glGetIntegerv(GLenum pname, GLint * params)
/usr/include/GL/gl.h:848"""
glPushAttrib = _libraries['/usr/lib/libglut.so'].glPushAttrib
glPushAttrib.restype = None
glPushAttrib.argtypes = [GLbitfield]
glPushAttrib.__doc__ = \
"""void glPushAttrib(GLbitfield mask)
/usr/include/GL/gl.h:851"""
glPopAttrib = _libraries['/usr/lib/libglut.so'].glPopAttrib
glPopAttrib.restype = None
glPopAttrib.argtypes = []
glPopAttrib.__doc__ = \
"""void glPopAttrib()
/usr/include/GL/gl.h:853"""
glPushClientAttrib = _libraries['/usr/lib/libglut.so'].glPushClientAttrib
glPushClientAttrib.restype = None
glPushClientAttrib.argtypes = [GLbitfield]
glPushClientAttrib.__doc__ = \
"""void glPushClientAttrib(GLbitfield mask)
/usr/include/GL/gl.h:856"""
glPopClientAttrib = _libraries['/usr/lib/libglut.so'].glPopClientAttrib
glPopClientAttrib.restype = None
glPopClientAttrib.argtypes = []
glPopClientAttrib.__doc__ = \
"""void glPopClientAttrib()
/usr/include/GL/gl.h:858"""
glRenderMode = _libraries['/usr/lib/libglut.so'].glRenderMode
glRenderMode.restype = GLint
glRenderMode.argtypes = [GLenum]
glRenderMode.__doc__ = \
"""GLint glRenderMode(GLenum mode)
/usr/include/GL/gl.h:861"""
glGetError = _libraries['/usr/lib/libglut.so'].glGetError
glGetError.restype = GLenum
glGetError.argtypes = []
glGetError.__doc__ = \
"""GLenum glGetError()
/usr/include/GL/gl.h:863"""
glGetString = _libraries['/usr/lib/libglut.so'].glGetString
glGetString.restype = POINTER(GLubyte)
glGetString.argtypes = [GLenum]
glGetString.__doc__ = \
"""unknown * glGetString(GLenum name)
/usr/include/GL/gl.h:865"""
glFinish = _libraries['/usr/lib/libglut.so'].glFinish
glFinish.restype = None
glFinish.argtypes = []
glFinish.__doc__ = \
"""void glFinish()
/usr/include/GL/gl.h:867"""
glFlush = _libraries['/usr/lib/libglut.so'].glFlush
glFlush.restype = None
glFlush.argtypes = []
glFlush.__doc__ = \
"""void glFlush()
/usr/include/GL/gl.h:869"""
glHint = _libraries['/usr/lib/libglut.so'].glHint
glHint.restype = None
glHint.argtypes = [GLenum, GLenum]
glHint.__doc__ = \
"""void glHint(GLenum target, GLenum mode)
/usr/include/GL/gl.h:871"""
glClearDepth = _libraries['/usr/lib/libglut.so'].glClearDepth
glClearDepth.restype = None
glClearDepth.argtypes = [GLclampd]
glClearDepth.__doc__ = \
"""void glClearDepth(GLclampd depth)
/usr/include/GL/gl.h:878"""
glDepthFunc = _libraries['/usr/lib/libglut.so'].glDepthFunc
glDepthFunc.restype = None
glDepthFunc.argtypes = [GLenum]
glDepthFunc.__doc__ = \
"""void glDepthFunc(GLenum func)
/usr/include/GL/gl.h:880"""
glDepthMask = _libraries['/usr/lib/libglut.so'].glDepthMask
glDepthMask.restype = None
glDepthMask.argtypes = [GLboolean]
glDepthMask.__doc__ = \
"""void glDepthMask(GLboolean flag)
/usr/include/GL/gl.h:882"""
glDepthRange = _libraries['/usr/lib/libglut.so'].glDepthRange
glDepthRange.restype = None
glDepthRange.argtypes = [GLclampd, GLclampd]
glDepthRange.__doc__ = \
"""void glDepthRange(GLclampd near_val, GLclampd far_val)
/usr/include/GL/gl.h:884"""
glClearAccum = _libraries['/usr/lib/libglut.so'].glClearAccum
glClearAccum.restype = None
glClearAccum.argtypes = [GLfloat, GLfloat, GLfloat, GLfloat]
glClearAccum.__doc__ = \
"""void glClearAccum(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha)
/usr/include/GL/gl.h:891"""
glAccum = _libraries['/usr/lib/libglut.so'].glAccum
glAccum.restype = None
glAccum.argtypes = [GLenum, GLfloat]
glAccum.__doc__ = \
"""void glAccum(GLenum op, GLfloat value)
/usr/include/GL/gl.h:893"""
glMatrixMode = _libraries['/usr/lib/libglut.so'].glMatrixMode
glMatrixMode.restype = None
glMatrixMode.argtypes = [GLenum]
glMatrixMode.__doc__ = \
"""void glMatrixMode(GLenum mode)
/usr/include/GL/gl.h:900"""
glOrtho = _libraries['/usr/lib/libglut.so'].glOrtho
glOrtho.restype = None
glOrtho.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble]
glOrtho.__doc__ = \
"""void glOrtho(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble near_val, GLdouble far_val)
/usr/include/GL/gl.h:904"""
glFrustum = _libraries['/usr/lib/libglut.so'].glFrustum
glFrustum.restype = None
glFrustum.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble]
glFrustum.__doc__ = \
"""void glFrustum(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble near_val, GLdouble far_val)
/usr/include/GL/gl.h:908"""
glViewport = _libraries['/usr/lib/libglut.so'].glViewport
glViewport.restype = None
glViewport.argtypes = [GLint, GLint, GLsizei, GLsizei]
glViewport.__doc__ = \
"""void glViewport(GLint x, GLint y, GLsizei width, GLsizei height)
/usr/include/GL/gl.h:911"""
glPushMatrix = _libraries['/usr/lib/libglut.so'].glPushMatrix
glPushMatrix.restype = None
glPushMatrix.argtypes = []
glPushMatrix.__doc__ = \
"""void glPushMatrix()
/usr/include/GL/gl.h:913"""
glPopMatrix = _libraries['/usr/lib/libglut.so'].glPopMatrix
glPopMatrix.restype = None
glPopMatrix.argtypes = []
glPopMatrix.__doc__ = \
"""void glPopMatrix()
/usr/include/GL/gl.h:915"""
glLoadIdentity = _libraries['/usr/lib/libglut.so'].glLoadIdentity
glLoadIdentity.restype = None
glLoadIdentity.argtypes = []
glLoadIdentity.__doc__ = \
"""void glLoadIdentity()
/usr/include/GL/gl.h:917"""
glLoadMatrixd = _libraries['/usr/lib/libglut.so'].glLoadMatrixd
glLoadMatrixd.restype = None
glLoadMatrixd.argtypes = [POINTER(GLdouble)]
glLoadMatrixd.__doc__ = \
"""void glLoadMatrixd(unknown * m)
/usr/include/GL/gl.h:919"""
glLoadMatrixf = _libraries['/usr/lib/libglut.so'].glLoadMatrixf
glLoadMatrixf.restype = None
glLoadMatrixf.argtypes = [POINTER(GLfloat)]
glLoadMatrixf.__doc__ = \
"""void glLoadMatrixf(unknown * m)
/usr/include/GL/gl.h:920"""
glMultMatrixd = _libraries['/usr/lib/libglut.so'].glMultMatrixd
glMultMatrixd.restype = None
glMultMatrixd.argtypes = [POINTER(GLdouble)]
glMultMatrixd.__doc__ = \
"""void glMultMatrixd(unknown * m)
/usr/include/GL/gl.h:922"""
glMultMatrixf = _libraries['/usr/lib/libglut.so'].glMultMatrixf
glMultMatrixf.restype = None
glMultMatrixf.argtypes = [POINTER(GLfloat)]
glMultMatrixf.__doc__ = \
"""void glMultMatrixf(unknown * m)
/usr/include/GL/gl.h:923"""
glRotated = _libraries['/usr/lib/libglut.so'].glRotated
glRotated.restype = None
glRotated.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble]
glRotated.__doc__ = \
"""void glRotated(GLdouble angle, GLdouble x, GLdouble y, GLdouble z)
/usr/include/GL/gl.h:926"""
glRotatef = _libraries['/usr/lib/libglut.so'].glRotatef
glRotatef.restype = None
glRotatef.argtypes = [GLfloat, GLfloat, GLfloat, GLfloat]
glRotatef.__doc__ = \
"""void glRotatef(GLfloat angle, GLfloat x, GLfloat y, GLfloat z)
/usr/include/GL/gl.h:928"""
glScaled = _libraries['/usr/lib/libglut.so'].glScaled
glScaled.restype = None
glScaled.argtypes = [GLdouble, GLdouble, GLdouble]
glScaled.__doc__ = \
"""void glScaled(GLdouble x, GLdouble y, GLdouble z)
/usr/include/GL/gl.h:930"""
glScalef = _libraries['/usr/lib/libglut.so'].glScalef
glScalef.restype = None
glScalef.argtypes = [GLfloat, GLfloat, GLfloat]
glScalef.__doc__ = \
"""void glScalef(GLfloat x, GLfloat y, GLfloat z)
/usr/include/GL/gl.h:931"""
glTranslated = _libraries['/usr/lib/libglut.so'].glTranslated
glTranslated.restype = None
glTranslated.argtypes = [GLdouble, GLdouble, GLdouble]
glTranslated.__doc__ = \
"""void glTranslated(GLdouble x, GLdouble y, GLdouble z)
/usr/include/GL/gl.h:933"""
glTranslatef = _libraries['/usr/lib/libglut.so'].glTranslatef
glTranslatef.restype = None
glTranslatef.argtypes = [GLfloat, GLfloat, GLfloat]
glTranslatef.__doc__ = \
"""void glTranslatef(GLfloat x, GLfloat y, GLfloat z)
/usr/include/GL/gl.h:934"""
glIsList = _libraries['/usr/lib/libglut.so'].glIsList
glIsList.restype = GLboolean
glIsList.argtypes = [GLuint]
glIsList.__doc__ = \
"""GLboolean glIsList(GLuint list)
/usr/include/GL/gl.h:941"""
glDeleteLists = _libraries['/usr/lib/libglut.so'].glDeleteLists
glDeleteLists.restype = None
glDeleteLists.argtypes = [GLuint, GLsizei]
glDeleteLists.__doc__ = \
"""void glDeleteLists(GLuint list, GLsizei range)
/usr/include/GL/gl.h:943"""
glGenLists = _libraries['/usr/lib/libglut.so'].glGenLists
glGenLists.restype = GLuint
glGenLists.argtypes = [GLsizei]
glGenLists.__doc__ = \
"""GLuint glGenLists(GLsizei range)
/usr/include/GL/gl.h:945"""
glNewList = _libraries['/usr/lib/libglut.so'].glNewList
glNewList.restype = None
glNewList.argtypes = [GLuint, GLenum]
glNewList.__doc__ = \
"""void glNewList(GLuint list, GLenum mode)
/usr/include/GL/gl.h:947"""
glEndList = _libraries['/usr/lib/libglut.so'].glEndList
glEndList.restype = None
glEndList.argtypes = []
glEndList.__doc__ = \
"""void glEndList()
/usr/include/GL/gl.h:949"""
glCallList = _libraries['/usr/lib/libglut.so'].glCallList
glCallList.restype = None
glCallList.argtypes = [GLuint]
glCallList.__doc__ = \
"""void glCallList(GLuint list)
/usr/include/GL/gl.h:951"""
glCallLists = _libraries['/usr/lib/libglut.so'].glCallLists
glCallLists.restype = None
glCallLists.argtypes = [GLsizei, GLenum, POINTER(GLvoid)]
glCallLists.__doc__ = \
"""void glCallLists(GLsizei n, GLenum type, unknown * lists)
/usr/include/GL/gl.h:954"""
glListBase = _libraries['/usr/lib/libglut.so'].glListBase
glListBase.restype = None
glListBase.argtypes = [GLuint]
glListBase.__doc__ = \
"""void glListBase(GLuint base)
/usr/include/GL/gl.h:956"""
glBegin = _libraries['/usr/lib/libglut.so'].glBegin
glBegin.restype = None
glBegin.argtypes = [GLenum]
glBegin.__doc__ = \
"""void glBegin(GLenum mode)
/usr/include/GL/gl.h:963"""
glEnd = _libraries['/usr/lib/libglut.so'].glEnd
glEnd.restype = None
glEnd.argtypes = []
glEnd.__doc__ = \
"""void glEnd()
/usr/include/GL/gl.h:965"""
glVertex2d = _libraries['/usr/lib/libglut.so'].glVertex2d
glVertex2d.restype = None
glVertex2d.argtypes = [GLdouble, GLdouble]
glVertex2d.__doc__ = \
"""void glVertex2d(GLdouble x, GLdouble y)
/usr/include/GL/gl.h:968"""
glVertex2f = _libraries['/usr/lib/libglut.so'].glVertex2f
glVertex2f.restype = None
glVertex2f.argtypes = [GLfloat, GLfloat]
glVertex2f.__doc__ = \
"""void glVertex2f(GLfloat x, GLfloat y)
/usr/include/GL/gl.h:969"""
glVertex2i = _libraries['/usr/lib/libglut.so'].glVertex2i
glVertex2i.restype = None
glVertex2i.argtypes = [GLint, GLint]
glVertex2i.__doc__ = \
"""void glVertex2i(GLint x, GLint y)
/usr/include/GL/gl.h:970"""
glVertex2s = _libraries['/usr/lib/libglut.so'].glVertex2s
glVertex2s.restype = None
glVertex2s.argtypes = [GLshort, GLshort]
glVertex2s.__doc__ = \
"""void glVertex2s(GLshort x, GLshort y)
/usr/include/GL/gl.h:971"""
glVertex3d = _libraries['/usr/lib/libglut.so'].glVertex3d
glVertex3d.restype = None
glVertex3d.argtypes = [GLdouble, GLdouble, GLdouble]
glVertex3d.__doc__ = \
"""void glVertex3d(GLdouble x, GLdouble y, GLdouble z)
/usr/include/GL/gl.h:973"""
glVertex3f = _libraries['/usr/lib/libglut.so'].glVertex3f
glVertex3f.restype = None
glVertex3f.argtypes = [GLfloat, GLfloat, GLfloat]
glVertex3f.__doc__ = \
"""void glVertex3f(GLfloat x, GLfloat y, GLfloat z)
/usr/include/GL/gl.h:974"""
glVertex3i = _libraries['/usr/lib/libglut.so'].glVertex3i
glVertex3i.restype = None
glVertex3i.argtypes = [GLint, GLint, GLint]
glVertex3i.__doc__ = \
"""void glVertex3i(GLint x, GLint y, GLint z)
/usr/include/GL/gl.h:975"""
glVertex3s = _libraries['/usr/lib/libglut.so'].glVertex3s
glVertex3s.restype = None
glVertex3s.argtypes = [GLshort, GLshort, GLshort]
glVertex3s.__doc__ = \
"""void glVertex3s(GLshort x, GLshort y, GLshort z)
/usr/include/GL/gl.h:976"""
glVertex4d = _libraries['/usr/lib/libglut.so'].glVertex4d
glVertex4d.restype = None
glVertex4d.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble]
glVertex4d.__doc__ = \
"""void glVertex4d(GLdouble x, GLdouble y, GLdouble z, GLdouble w)
/usr/include/GL/gl.h:978"""
glVertex4f = _libraries['/usr/lib/libglut.so'].glVertex4f
glVertex4f.restype = None
glVertex4f.argtypes = [GLfloat, GLfloat, GLfloat, GLfloat]
glVertex4f.__doc__ = \
"""void glVertex4f(GLfloat x, GLfloat y, GLfloat z, GLfloat w)
/usr/include/GL/gl.h:979"""
glVertex4i = _libraries['/usr/lib/libglut.so'].glVertex4i
glVertex4i.restype = None
glVertex4i.argtypes = [GLint, GLint, GLint, GLint]
glVertex4i.__doc__ = \
"""void glVertex4i(GLint x, GLint y, GLint z, GLint w)
/usr/include/GL/gl.h:980"""
glVertex4s = _libraries['/usr/lib/libglut.so'].glVertex4s
glVertex4s.restype = None
glVertex4s.argtypes = [GLshort, GLshort, GLshort, GLshort]
glVertex4s.__doc__ = \
"""void glVertex4s(GLshort x, GLshort y, GLshort z, GLshort w)
/usr/include/GL/gl.h:981"""
glVertex2dv = _libraries['/usr/lib/libglut.so'].glVertex2dv
glVertex2dv.restype = None
glVertex2dv.argtypes = [POINTER(GLdouble)]
glVertex2dv.__doc__ = \
"""void glVertex2dv(unknown * v)
/usr/include/GL/gl.h:983"""
glVertex2fv = _libraries['/usr/lib/libglut.so'].glVertex2fv
glVertex2fv.restype = None
glVertex2fv.argtypes = [POINTER(GLfloat)]
glVertex2fv.__doc__ = \
"""void glVertex2fv(unknown * v)
/usr/include/GL/gl.h:984"""
glVertex2iv = _libraries['/usr/lib/libglut.so'].glVertex2iv
glVertex2iv.restype = None
glVertex2iv.argtypes = [POINTER(GLint)]
glVertex2iv.__doc__ = \
"""void glVertex2iv(unknown * v)
/usr/include/GL/gl.h:985"""
glVertex2sv = _libraries['/usr/lib/libglut.so'].glVertex2sv
glVertex2sv.restype = None
glVertex2sv.argtypes = [POINTER(GLshort)]
glVertex2sv.__doc__ = \
"""void glVertex2sv(unknown * v)
/usr/include/GL/gl.h:986"""
glVertex3dv = _libraries['/usr/lib/libglut.so'].glVertex3dv
glVertex3dv.restype = None
glVertex3dv.argtypes = [POINTER(GLdouble)]
glVertex3dv.__doc__ = \
"""void glVertex3dv(unknown * v)
/usr/include/GL/gl.h:988"""
glVertex3fv = _libraries['/usr/lib/libglut.so'].glVertex3fv
glVertex3fv.restype = None
glVertex3fv.argtypes = [POINTER(GLfloat)]
glVertex3fv.__doc__ = \
"""void glVertex3fv(unknown * v)
/usr/include/GL/gl.h:989"""
glVertex3iv = _libraries['/usr/lib/libglut.so'].glVertex3iv
glVertex3iv.restype = None
glVertex3iv.argtypes = [POINTER(GLint)]
glVertex3iv.__doc__ = \
"""void glVertex3iv(unknown * v)
/usr/include/GL/gl.h:990"""
glVertex3sv = _libraries['/usr/lib/libglut.so'].glVertex3sv
glVertex3sv.restype = None
glVertex3sv.argtypes = [POINTER(GLshort)]
glVertex3sv.__doc__ = \
"""void glVertex3sv(unknown * v)
/usr/include/GL/gl.h:991"""
glVertex4dv = _libraries['/usr/lib/libglut.so'].glVertex4dv
glVertex4dv.restype = None
glVertex4dv.argtypes = [POINTER(GLdouble)]
glVertex4dv.__doc__ = \
"""void glVertex4dv(unknown * v)
/usr/include/GL/gl.h:993"""
glVertex4fv = _libraries['/usr/lib/libglut.so'].glVertex4fv
glVertex4fv.restype = None
glVertex4fv.argtypes = [POINTER(GLfloat)]
glVertex4fv.__doc__ = \
"""void glVertex4fv(unknown * v)
/usr/include/GL/gl.h:994"""
glVertex4iv = _libraries['/usr/lib/libglut.so'].glVertex4iv
glVertex4iv.restype = None
glVertex4iv.argtypes = [POINTER(GLint)]
glVertex4iv.__doc__ = \
"""void glVertex4iv(unknown * v)
/usr/include/GL/gl.h:995"""
glVertex4sv = _libraries['/usr/lib/libglut.so'].glVertex4sv
glVertex4sv.restype = None
glVertex4sv.argtypes = [POINTER(GLshort)]
glVertex4sv.__doc__ = \
"""void glVertex4sv(unknown * v)
/usr/include/GL/gl.h:996"""
glNormal3b = _libraries['/usr/lib/libglut.so'].glNormal3b
glNormal3b.restype = None
glNormal3b.argtypes = [GLbyte, GLbyte, GLbyte]
glNormal3b.__doc__ = \
"""void glNormal3b(GLbyte nx, GLbyte ny, GLbyte nz)
/usr/include/GL/gl.h:999"""
glNormal3d = _libraries['/usr/lib/libglut.so'].glNormal3d
glNormal3d.restype = None
glNormal3d.argtypes = [GLdouble, GLdouble, GLdouble]
glNormal3d.__doc__ = \
"""void glNormal3d(GLdouble nx, GLdouble ny, GLdouble nz)
/usr/include/GL/gl.h:1000"""
glNormal3f = _libraries['/usr/lib/libglut.so'].glNormal3f
glNormal3f.restype = None
glNormal3f.argtypes = [GLfloat, GLfloat, GLfloat]
glNormal3f.__doc__ = \
"""void glNormal3f(GLfloat nx, GLfloat ny, GLfloat nz)
/usr/include/GL/gl.h:1001"""
glNormal3i = _libraries['/usr/lib/libglut.so'].glNormal3i
glNormal3i.restype = None
glNormal3i.argtypes = [GLint, GLint, GLint]
glNormal3i.__doc__ = \
"""void glNormal3i(GLint nx, GLint ny, GLint nz)
/usr/include/GL/gl.h:1002"""
glNormal3s = _libraries['/usr/lib/libglut.so'].glNormal3s
glNormal3s.restype = None
glNormal3s.argtypes = [GLshort, GLshort, GLshort]
glNormal3s.__doc__ = \
"""void glNormal3s(GLshort nx, GLshort ny, GLshort nz)
/usr/include/GL/gl.h:1003"""
glNormal3bv = _libraries['/usr/lib/libglut.so'].glNormal3bv
glNormal3bv.restype = None
glNormal3bv.argtypes = [POINTER(GLbyte)]
glNormal3bv.__doc__ = \
"""void glNormal3bv(unknown * v)
/usr/include/GL/gl.h:1005"""
glNormal3dv = _libraries['/usr/lib/libglut.so'].glNormal3dv
glNormal3dv.restype = None
glNormal3dv.argtypes = [POINTER(GLdouble)]
glNormal3dv.__doc__ = \
"""void glNormal3dv(unknown * v)
/usr/include/GL/gl.h:1006"""
glNormal3fv = _libraries['/usr/lib/libglut.so'].glNormal3fv
glNormal3fv.restype = None
glNormal3fv.argtypes = [POINTER(GLfloat)]
glNormal3fv.__doc__ = \
"""void glNormal3fv(unknown * v)
/usr/include/GL/gl.h:1007"""
glNormal3iv = _libraries['/usr/lib/libglut.so'].glNormal3iv
glNormal3iv.restype = None
glNormal3iv.argtypes = [POINTER(GLint)]
glNormal3iv.__doc__ = \
"""void glNormal3iv(unknown * v)
/usr/include/GL/gl.h:1008"""
glNormal3sv = _libraries['/usr/lib/libglut.so'].glNormal3sv
glNormal3sv.restype = None
glNormal3sv.argtypes = [POINTER(GLshort)]
glNormal3sv.__doc__ = \
"""void glNormal3sv(unknown * v)
/usr/include/GL/gl.h:1009"""
glIndexd = _libraries['/usr/lib/libglut.so'].glIndexd
glIndexd.restype = None
glIndexd.argtypes = [GLdouble]
glIndexd.__doc__ = \
"""void glIndexd(GLdouble c)
/usr/include/GL/gl.h:1012"""
glIndexf = _libraries['/usr/lib/libglut.so'].glIndexf
glIndexf.restype = None
glIndexf.argtypes = [GLfloat]
glIndexf.__doc__ = \
"""void glIndexf(GLfloat c)
/usr/include/GL/gl.h:1013"""
glIndexi = _libraries['/usr/lib/libglut.so'].glIndexi
glIndexi.restype = None
glIndexi.argtypes = [GLint]
glIndexi.__doc__ = \
"""void glIndexi(GLint c)
/usr/include/GL/gl.h:1014"""
glIndexs = _libraries['/usr/lib/libglut.so'].glIndexs
glIndexs.restype = None
glIndexs.argtypes = [GLshort]
glIndexs.__doc__ = \
"""void glIndexs(GLshort c)
/usr/include/GL/gl.h:1015"""
glIndexub = _libraries['/usr/lib/libglut.so'].glIndexub
glIndexub.restype = None
glIndexub.argtypes = [GLubyte]
glIndexub.__doc__ = \
"""void glIndexub(GLubyte c)
/usr/include/GL/gl.h:1016"""
glIndexdv = _libraries['/usr/lib/libglut.so'].glIndexdv
glIndexdv.restype = None
glIndexdv.argtypes = [POINTER(GLdouble)]
glIndexdv.__doc__ = \
"""void glIndexdv(unknown * c)
/usr/include/GL/gl.h:1018"""
glIndexfv = _libraries['/usr/lib/libglut.so'].glIndexfv
glIndexfv.restype = None
glIndexfv.argtypes = [POINTER(GLfloat)]
glIndexfv.__doc__ = \
"""void glIndexfv(unknown * c)
/usr/include/GL/gl.h:1019"""
glIndexiv = _libraries['/usr/lib/libglut.so'].glIndexiv
glIndexiv.restype = None
glIndexiv.argtypes = [POINTER(GLint)]
glIndexiv.__doc__ = \
"""void glIndexiv(unknown * c)
/usr/include/GL/gl.h:1020"""
glIndexsv = _libraries['/usr/lib/libglut.so'].glIndexsv
glIndexsv.restype = None
glIndexsv.argtypes = [POINTER(GLshort)]
glIndexsv.__doc__ = \
"""void glIndexsv(unknown * c)
/usr/include/GL/gl.h:1021"""
glIndexubv = _libraries['/usr/lib/libglut.so'].glIndexubv
glIndexubv.restype = None
glIndexubv.argtypes = [POINTER(GLubyte)]
glIndexubv.__doc__ = \
"""void glIndexubv(unknown * c)
/usr/include/GL/gl.h:1022"""
glColor3b = _libraries['/usr/lib/libglut.so'].glColor3b
glColor3b.restype = None
glColor3b.argtypes = [GLbyte, GLbyte, GLbyte]
glColor3b.__doc__ = \
"""void glColor3b(GLbyte red, GLbyte green, GLbyte blue)
/usr/include/GL/gl.h:1024"""
glColor3d = _libraries['/usr/lib/libglut.so'].glColor3d
glColor3d.restype = None
glColor3d.argtypes = [GLdouble, GLdouble, GLdouble]
glColor3d.__doc__ = \
"""void glColor3d(GLdouble red, GLdouble green, GLdouble blue)
/usr/include/GL/gl.h:1025"""
glColor3f = _libraries['/usr/lib/libglut.so'].glColor3f
glColor3f.restype = None
glColor3f.argtypes = [GLfloat, GLfloat, GLfloat]
glColor3f.__doc__ = \
"""void glColor3f(GLfloat red, GLfloat green, GLfloat blue)
/usr/include/GL/gl.h:1026"""
glColor3i = _libraries['/usr/lib/libglut.so'].glColor3i
glColor3i.restype = None
glColor3i.argtypes = [GLint, GLint, GLint]
glColor3i.__doc__ = \
"""void glColor3i(GLint red, GLint green, GLint blue)
/usr/include/GL/gl.h:1027"""
glColor3s = _libraries['/usr/lib/libglut.so'].glColor3s
glColor3s.restype = None
glColor3s.argtypes = [GLshort, GLshort, GLshort]
glColor3s.__doc__ = \
"""void glColor3s(GLshort red, GLshort green, GLshort blue)
/usr/include/GL/gl.h:1028"""
glColor3ub = _libraries['/usr/lib/libglut.so'].glColor3ub
glColor3ub.restype = None
glColor3ub.argtypes = [GLubyte, GLubyte, GLubyte]
glColor3ub.__doc__ = \
"""void glColor3ub(GLubyte red, GLubyte green, GLubyte blue)
/usr/include/GL/gl.h:1029"""
glColor3ui = _libraries['/usr/lib/libglut.so'].glColor3ui
glColor3ui.restype = None
glColor3ui.argtypes = [GLuint, GLuint, GLuint]
glColor3ui.__doc__ = \
"""void glColor3ui(GLuint red, GLuint green, GLuint blue)
/usr/include/GL/gl.h:1030"""
glColor3us = _libraries['/usr/lib/libglut.so'].glColor3us
glColor3us.restype = None
glColor3us.argtypes = [GLushort, GLushort, GLushort]
glColor3us.__doc__ = \
"""void glColor3us(GLushort red, GLushort green, GLushort blue)
/usr/include/GL/gl.h:1031"""
glColor4b = _libraries['/usr/lib/libglut.so'].glColor4b
glColor4b.restype = None
glColor4b.argtypes = [GLbyte, GLbyte, GLbyte, GLbyte]
glColor4b.__doc__ = \
"""void glColor4b(GLbyte red, GLbyte green, GLbyte blue, GLbyte alpha)
/usr/include/GL/gl.h:1034"""
glColor4d = _libraries['/usr/lib/libglut.so'].glColor4d
glColor4d.restype = None
glColor4d.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble]
glColor4d.__doc__ = \
"""void glColor4d(GLdouble red, GLdouble green, GLdouble blue, GLdouble alpha)
/usr/include/GL/gl.h:1036"""
glColor4f = _libraries['/usr/lib/libglut.so'].glColor4f
glColor4f.restype = None
glColor4f.argtypes = [GLfloat, GLfloat, GLfloat, GLfloat]
glColor4f.__doc__ = \
"""void glColor4f(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha)
/usr/include/GL/gl.h:1038"""
glColor4i = _libraries['/usr/lib/libglut.so'].glColor4i
glColor4i.restype = None
glColor4i.argtypes = [GLint, GLint, GLint, GLint]
glColor4i.__doc__ = \
"""void glColor4i(GLint red, GLint green, GLint blue, GLint alpha)
/usr/include/GL/gl.h:1040"""
glColor4s = _libraries['/usr/lib/libglut.so'].glColor4s
glColor4s.restype = None
glColor4s.argtypes = [GLshort, GLshort, GLshort, GLshort]
glColor4s.__doc__ = \
"""void glColor4s(GLshort red, GLshort green, GLshort blue, GLshort alpha)
/usr/include/GL/gl.h:1042"""
glColor4ub = _libraries['/usr/lib/libglut.so'].glColor4ub
glColor4ub.restype = None
glColor4ub.argtypes = [GLubyte, GLubyte, GLubyte, GLubyte]
glColor4ub.__doc__ = \
"""void glColor4ub(GLubyte red, GLubyte green, GLubyte blue, GLubyte alpha)
/usr/include/GL/gl.h:1044"""
glColor4ui = _libraries['/usr/lib/libglut.so'].glColor4ui
glColor4ui.restype = None
glColor4ui.argtypes = [GLuint, GLuint, GLuint, GLuint]
glColor4ui.__doc__ = \
"""void glColor4ui(GLuint red, GLuint green, GLuint blue, GLuint alpha)
/usr/include/GL/gl.h:1046"""
glColor4us = _libraries['/usr/lib/libglut.so'].glColor4us
glColor4us.restype = None
glColor4us.argtypes = [GLushort, GLushort, GLushort, GLushort]
glColor4us.__doc__ = \
"""void glColor4us(GLushort red, GLushort green, GLushort blue, GLushort alpha)
/usr/include/GL/gl.h:1048"""
glColor3bv = _libraries['/usr/lib/libglut.so'].glColor3bv
glColor3bv.restype = None
glColor3bv.argtypes = [POINTER(GLbyte)]
glColor3bv.__doc__ = \
"""void glColor3bv(unknown * v)
/usr/include/GL/gl.h:1051"""
glColor3dv = _libraries['/usr/lib/libglut.so'].glColor3dv
glColor3dv.restype = None
glColor3dv.argtypes = [POINTER(GLdouble)]
glColor3dv.__doc__ = \
"""void glColor3dv(unknown * v)
/usr/include/GL/gl.h:1052"""
glColor3fv = _libraries['/usr/lib/libglut.so'].glColor3fv
glColor3fv.restype = None
glColor3fv.argtypes = [POINTER(GLfloat)]
glColor3fv.__doc__ = \
"""void glColor3fv(unknown * v)
/usr/include/GL/gl.h:1053"""
glColor3iv = _libraries['/usr/lib/libglut.so'].glColor3iv
glColor3iv.restype = None
glColor3iv.argtypes = [POINTER(GLint)]
glColor3iv.__doc__ = \
"""void glColor3iv(unknown * v)
/usr/include/GL/gl.h:1054"""
glColor3sv = _libraries['/usr/lib/libglut.so'].glColor3sv
glColor3sv.restype = None
glColor3sv.argtypes = [POINTER(GLshort)]
glColor3sv.__doc__ = \
"""void glColor3sv(unknown * v)
/usr/include/GL/gl.h:1055"""
glColor3ubv = _libraries['/usr/lib/libglut.so'].glColor3ubv
glColor3ubv.restype = None
glColor3ubv.argtypes = [POINTER(GLubyte)]
glColor3ubv.__doc__ = \
"""void glColor3ubv(unknown * v)
/usr/include/GL/gl.h:1056"""
glColor3uiv = _libraries['/usr/lib/libglut.so'].glColor3uiv
glColor3uiv.restype = None
glColor3uiv.argtypes = [POINTER(GLuint)]
glColor3uiv.__doc__ = \
"""void glColor3uiv(unknown * v)
/usr/include/GL/gl.h:1057"""
glColor3usv = _libraries['/usr/lib/libglut.so'].glColor3usv
glColor3usv.restype = None
glColor3usv.argtypes = [POINTER(GLushort)]
glColor3usv.__doc__ = \
"""void glColor3usv(unknown * v)
/usr/include/GL/gl.h:1058"""
glColor4bv = _libraries['/usr/lib/libglut.so'].glColor4bv
glColor4bv.restype = None
glColor4bv.argtypes = [POINTER(GLbyte)]
glColor4bv.__doc__ = \
"""void glColor4bv(unknown * v)
/usr/include/GL/gl.h:1060"""
glColor4dv = _libraries['/usr/lib/libglut.so'].glColor4dv
glColor4dv.restype = None
glColor4dv.argtypes = [POINTER(GLdouble)]
glColor4dv.__doc__ = \
"""void glColor4dv(unknown * v)
/usr/include/GL/gl.h:1061"""
glColor4fv = _libraries['/usr/lib/libglut.so'].glColor4fv
glColor4fv.restype = None
glColor4fv.argtypes = [POINTER(GLfloat)]
glColor4fv.__doc__ = \
"""void glColor4fv(unknown * v)
/usr/include/GL/gl.h:1062"""
glColor4iv = _libraries['/usr/lib/libglut.so'].glColor4iv
glColor4iv.restype = None
glColor4iv.argtypes = [POINTER(GLint)]
glColor4iv.__doc__ = \
"""void glColor4iv(unknown * v)
/usr/include/GL/gl.h:1063"""
glColor4sv = _libraries['/usr/lib/libglut.so'].glColor4sv
glColor4sv.restype = None
glColor4sv.argtypes = [POINTER(GLshort)]
glColor4sv.__doc__ = \
"""void glColor4sv(unknown * v)
/usr/include/GL/gl.h:1064"""
glColor4ubv = _libraries['/usr/lib/libglut.so'].glColor4ubv
glColor4ubv.restype = None
glColor4ubv.argtypes = [POINTER(GLubyte)]
glColor4ubv.__doc__ = \
"""void glColor4ubv(unknown * v)
/usr/include/GL/gl.h:1065"""
glColor4uiv = _libraries['/usr/lib/libglut.so'].glColor4uiv
glColor4uiv.restype = None
glColor4uiv.argtypes = [POINTER(GLuint)]
glColor4uiv.__doc__ = \
"""void glColor4uiv(unknown * v)
/usr/include/GL/gl.h:1066"""
glColor4usv = _libraries['/usr/lib/libglut.so'].glColor4usv
glColor4usv.restype = None
glColor4usv.argtypes = [POINTER(GLushort)]
glColor4usv.__doc__ = \
"""void glColor4usv(unknown * v)
/usr/include/GL/gl.h:1067"""
glTexCoord1d = _libraries['/usr/lib/libglut.so'].glTexCoord1d
glTexCoord1d.restype = None
glTexCoord1d.argtypes = [GLdouble]
glTexCoord1d.__doc__ = \
"""void glTexCoord1d(GLdouble s)
/usr/include/GL/gl.h:1070"""
glTexCoord1f = _libraries['/usr/lib/libglut.so'].glTexCoord1f
glTexCoord1f.restype = None
glTexCoord1f.argtypes = [GLfloat]
glTexCoord1f.__doc__ = \
"""void glTexCoord1f(GLfloat s)
/usr/include/GL/gl.h:1071"""
glTexCoord1i = _libraries['/usr/lib/libglut.so'].glTexCoord1i
glTexCoord1i.restype = None
glTexCoord1i.argtypes = [GLint]
glTexCoord1i.__doc__ = \
"""void glTexCoord1i(GLint s)
/usr/include/GL/gl.h:1072"""
glTexCoord1s = _libraries['/usr/lib/libglut.so'].glTexCoord1s
glTexCoord1s.restype = None
glTexCoord1s.argtypes = [GLshort]
glTexCoord1s.__doc__ = \
"""void glTexCoord1s(GLshort s)
/usr/include/GL/gl.h:1073"""
glTexCoord2d = _libraries['/usr/lib/libglut.so'].glTexCoord2d
glTexCoord2d.restype = None
glTexCoord2d.argtypes = [GLdouble, GLdouble]
glTexCoord2d.__doc__ = \
"""void glTexCoord2d(GLdouble s, GLdouble t)
/usr/include/GL/gl.h:1075"""
glTexCoord2f = _libraries['/usr/lib/libglut.so'].glTexCoord2f
glTexCoord2f.restype = None
glTexCoord2f.argtypes = [GLfloat, GLfloat]
glTexCoord2f.__doc__ = \
"""void glTexCoord2f(GLfloat s, GLfloat t)
/usr/include/GL/gl.h:1076"""
glTexCoord2i = _libraries['/usr/lib/libglut.so'].glTexCoord2i
glTexCoord2i.restype = None
glTexCoord2i.argtypes = [GLint, GLint]
glTexCoord2i.__doc__ = \
"""void glTexCoord2i(GLint s, GLint t)
/usr/include/GL/gl.h:1077"""
glTexCoord2s = _libraries['/usr/lib/libglut.so'].glTexCoord2s
glTexCoord2s.restype = None
glTexCoord2s.argtypes = [GLshort, GLshort]
glTexCoord2s.__doc__ = \
"""void glTexCoord2s(GLshort s, GLshort t)
/usr/include/GL/gl.h:1078"""
glTexCoord3d = _libraries['/usr/lib/libglut.so'].glTexCoord3d
glTexCoord3d.restype = None
glTexCoord3d.argtypes = [GLdouble, GLdouble, GLdouble]
glTexCoord3d.__doc__ = \
"""void glTexCoord3d(GLdouble s, GLdouble t, GLdouble r)
/usr/include/GL/gl.h:1080"""
glTexCoord3f = _libraries['/usr/lib/libglut.so'].glTexCoord3f
glTexCoord3f.restype = None
glTexCoord3f.argtypes = [GLfloat, GLfloat, GLfloat]
glTexCoord3f.__doc__ = \
"""void glTexCoord3f(GLfloat s, GLfloat t, GLfloat r)
/usr/include/GL/gl.h:1081"""
glTexCoord3i = _libraries['/usr/lib/libglut.so'].glTexCoord3i
glTexCoord3i.restype = None
glTexCoord3i.argtypes = [GLint, GLint, GLint]
glTexCoord3i.__doc__ = \
"""void glTexCoord3i(GLint s, GLint t, GLint r)
/usr/include/GL/gl.h:1082"""
glTexCoord3s = _libraries['/usr/lib/libglut.so'].glTexCoord3s
glTexCoord3s.restype = None
glTexCoord3s.argtypes = [GLshort, GLshort, GLshort]
glTexCoord3s.__doc__ = \
"""void glTexCoord3s(GLshort s, GLshort t, GLshort r)
/usr/include/GL/gl.h:1083"""
glTexCoord4d = _libraries['/usr/lib/libglut.so'].glTexCoord4d
glTexCoord4d.restype = None
glTexCoord4d.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble]
glTexCoord4d.__doc__ = \
"""void glTexCoord4d(GLdouble s, GLdouble t, GLdouble r, GLdouble q)
/usr/include/GL/gl.h:1085"""
glTexCoord4f = _libraries['/usr/lib/libglut.so'].glTexCoord4f
glTexCoord4f.restype = None
glTexCoord4f.argtypes = [GLfloat, GLfloat, GLfloat, GLfloat]
glTexCoord4f.__doc__ = \
"""void glTexCoord4f(GLfloat s, GLfloat t, GLfloat r, GLfloat q)
/usr/include/GL/gl.h:1086"""
glTexCoord4i = _libraries['/usr/lib/libglut.so'].glTexCoord4i
glTexCoord4i.restype = None
glTexCoord4i.argtypes = [GLint, GLint, GLint, GLint]
glTexCoord4i.__doc__ = \
"""void glTexCoord4i(GLint s, GLint t, GLint r, GLint q)
/usr/include/GL/gl.h:1087"""
glTexCoord4s = _libraries['/usr/lib/libglut.so'].glTexCoord4s
glTexCoord4s.restype = None
glTexCoord4s.argtypes = [GLshort, GLshort, GLshort, GLshort]
glTexCoord4s.__doc__ = \
"""void glTexCoord4s(GLshort s, GLshort t, GLshort r, GLshort q)
/usr/include/GL/gl.h:1088"""
glTexCoord1dv = _libraries['/usr/lib/libglut.so'].glTexCoord1dv
glTexCoord1dv.restype = None
glTexCoord1dv.argtypes = [POINTER(GLdouble)]
glTexCoord1dv.__doc__ = \
"""void glTexCoord1dv(unknown * v)
/usr/include/GL/gl.h:1090"""
glTexCoord1fv = _libraries['/usr/lib/libglut.so'].glTexCoord1fv
glTexCoord1fv.restype = None
glTexCoord1fv.argtypes = [POINTER(GLfloat)]
glTexCoord1fv.__doc__ = \
"""void glTexCoord1fv(unknown * v)
/usr/include/GL/gl.h:1091"""
glTexCoord1iv = _libraries['/usr/lib/libglut.so'].glTexCoord1iv
glTexCoord1iv.restype = None
glTexCoord1iv.argtypes = [POINTER(GLint)]
glTexCoord1iv.__doc__ = \
"""void glTexCoord1iv(unknown * v)
/usr/include/GL/gl.h:1092"""
glTexCoord1sv = _libraries['/usr/lib/libglut.so'].glTexCoord1sv
glTexCoord1sv.restype = None
glTexCoord1sv.argtypes = [POINTER(GLshort)]
glTexCoord1sv.__doc__ = \
"""void glTexCoord1sv(unknown * v)
/usr/include/GL/gl.h:1093"""
glTexCoord2dv = _libraries['/usr/lib/libglut.so'].glTexCoord2dv
glTexCoord2dv.restype = None
glTexCoord2dv.argtypes = [POINTER(GLdouble)]
glTexCoord2dv.__doc__ = \
"""void glTexCoord2dv(unknown * v)
/usr/include/GL/gl.h:1095"""
glTexCoord2fv = _libraries['/usr/lib/libglut.so'].glTexCoord2fv
glTexCoord2fv.restype = None
glTexCoord2fv.argtypes = [POINTER(GLfloat)]
glTexCoord2fv.__doc__ = \
"""void glTexCoord2fv(unknown * v)
/usr/include/GL/gl.h:1096"""
glTexCoord2iv = _libraries['/usr/lib/libglut.so'].glTexCoord2iv
glTexCoord2iv.restype = None
glTexCoord2iv.argtypes = [POINTER(GLint)]
glTexCoord2iv.__doc__ = \
"""void glTexCoord2iv(unknown * v)
/usr/include/GL/gl.h:1097"""
glTexCoord2sv = _libraries['/usr/lib/libglut.so'].glTexCoord2sv
glTexCoord2sv.restype = None
glTexCoord2sv.argtypes = [POINTER(GLshort)]
glTexCoord2sv.__doc__ = \
"""void glTexCoord2sv(unknown * v)
/usr/include/GL/gl.h:1098"""
glTexCoord3dv = _libraries['/usr/lib/libglut.so'].glTexCoord3dv
glTexCoord3dv.restype = None
glTexCoord3dv.argtypes = [POINTER(GLdouble)]
glTexCoord3dv.__doc__ = \
"""void glTexCoord3dv(unknown * v)
/usr/include/GL/gl.h:1100"""
glTexCoord3fv = _libraries['/usr/lib/libglut.so'].glTexCoord3fv
glTexCoord3fv.restype = None
glTexCoord3fv.argtypes = [POINTER(GLfloat)]
glTexCoord3fv.__doc__ = \
"""void glTexCoord3fv(unknown * v)
/usr/include/GL/gl.h:1101"""
glTexCoord3iv = _libraries['/usr/lib/libglut.so'].glTexCoord3iv
glTexCoord3iv.restype = None
glTexCoord3iv.argtypes = [POINTER(GLint)]
glTexCoord3iv.__doc__ = \
"""void glTexCoord3iv(unknown * v)
/usr/include/GL/gl.h:1102"""
glTexCoord3sv = _libraries['/usr/lib/libglut.so'].glTexCoord3sv
glTexCoord3sv.restype = None
glTexCoord3sv.argtypes = [POINTER(GLshort)]
glTexCoord3sv.__doc__ = \
"""void glTexCoord3sv(unknown * v)
/usr/include/GL/gl.h:1103"""
glTexCoord4dv = _libraries['/usr/lib/libglut.so'].glTexCoord4dv
glTexCoord4dv.restype = None
glTexCoord4dv.argtypes = [POINTER(GLdouble)]
glTexCoord4dv.__doc__ = \
"""void glTexCoord4dv(unknown * v)
/usr/include/GL/gl.h:1105"""
glTexCoord4fv = _libraries['/usr/lib/libglut.so'].glTexCoord4fv
glTexCoord4fv.restype = None
glTexCoord4fv.argtypes = [POINTER(GLfloat)]
glTexCoord4fv.__doc__ = \
"""void glTexCoord4fv(unknown * v)
/usr/include/GL/gl.h:1106"""
glTexCoord4iv = _libraries['/usr/lib/libglut.so'].glTexCoord4iv
glTexCoord4iv.restype = None
glTexCoord4iv.argtypes = [POINTER(GLint)]
glTexCoord4iv.__doc__ = \
"""void glTexCoord4iv(unknown * v)
/usr/include/GL/gl.h:1107"""
glTexCoord4sv = _libraries['/usr/lib/libglut.so'].glTexCoord4sv
glTexCoord4sv.restype = None
glTexCoord4sv.argtypes = [POINTER(GLshort)]
glTexCoord4sv.__doc__ = \
"""void glTexCoord4sv(unknown * v)
/usr/include/GL/gl.h:1108"""
glRasterPos2d = _libraries['/usr/lib/libglut.so'].glRasterPos2d
glRasterPos2d.restype = None
glRasterPos2d.argtypes = [GLdouble, GLdouble]
glRasterPos2d.__doc__ = \
"""void glRasterPos2d(GLdouble x, GLdouble y)
/usr/include/GL/gl.h:1111"""
glRasterPos2f = _libraries['/usr/lib/libglut.so'].glRasterPos2f
glRasterPos2f.restype = None
glRasterPos2f.argtypes = [GLfloat, GLfloat]
glRasterPos2f.__doc__ = \
"""void glRasterPos2f(GLfloat x, GLfloat y)
/usr/include/GL/gl.h:1112"""
glRasterPos2i = _libraries['/usr/lib/libglut.so'].glRasterPos2i
glRasterPos2i.restype = None
glRasterPos2i.argtypes = [GLint, GLint]
glRasterPos2i.__doc__ = \
"""void glRasterPos2i(GLint x, GLint y)
/usr/include/GL/gl.h:1113"""
glRasterPos2s = _libraries['/usr/lib/libglut.so'].glRasterPos2s
glRasterPos2s.restype = None
glRasterPos2s.argtypes = [GLshort, GLshort]
glRasterPos2s.__doc__ = \
"""void glRasterPos2s(GLshort x, GLshort y)
/usr/include/GL/gl.h:1114"""
glRasterPos3d = _libraries['/usr/lib/libglut.so'].glRasterPos3d
glRasterPos3d.restype = None
glRasterPos3d.argtypes = [GLdouble, GLdouble, GLdouble]
glRasterPos3d.__doc__ = \
"""void glRasterPos3d(GLdouble x, GLdouble y, GLdouble z)
/usr/include/GL/gl.h:1116"""
glRasterPos3f = _libraries['/usr/lib/libglut.so'].glRasterPos3f
glRasterPos3f.restype = None
glRasterPos3f.argtypes = [GLfloat, GLfloat, GLfloat]
glRasterPos3f.__doc__ = \
"""void glRasterPos3f(GLfloat x, GLfloat y, GLfloat z)
/usr/include/GL/gl.h:1117"""
glRasterPos3i = _libraries['/usr/lib/libglut.so'].glRasterPos3i
glRasterPos3i.restype = None
glRasterPos3i.argtypes = [GLint, GLint, GLint]
glRasterPos3i.__doc__ = \
"""void glRasterPos3i(GLint x, GLint y, GLint z)
/usr/include/GL/gl.h:1118"""
glRasterPos3s = _libraries['/usr/lib/libglut.so'].glRasterPos3s
glRasterPos3s.restype = None
glRasterPos3s.argtypes = [GLshort, GLshort, GLshort]
glRasterPos3s.__doc__ = \
"""void glRasterPos3s(GLshort x, GLshort y, GLshort z)
/usr/include/GL/gl.h:1119"""
glRasterPos4d = _libraries['/usr/lib/libglut.so'].glRasterPos4d
glRasterPos4d.restype = None
glRasterPos4d.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble]
glRasterPos4d.__doc__ = \
"""void glRasterPos4d(GLdouble x, GLdouble y, GLdouble z, GLdouble w)
/usr/include/GL/gl.h:1121"""
glRasterPos4f = _libraries['/usr/lib/libglut.so'].glRasterPos4f
glRasterPos4f.restype = None
glRasterPos4f.argtypes = [GLfloat, GLfloat, GLfloat, GLfloat]
glRasterPos4f.__doc__ = \
"""void glRasterPos4f(GLfloat x, GLfloat y, GLfloat z, GLfloat w)
/usr/include/GL/gl.h:1122"""
glRasterPos4i = _libraries['/usr/lib/libglut.so'].glRasterPos4i
glRasterPos4i.restype = None
glRasterPos4i.argtypes = [GLint, GLint, GLint, GLint]
glRasterPos4i.__doc__ = \
"""void glRasterPos4i(GLint x, GLint y, GLint z, GLint w)
/usr/include/GL/gl.h:1123"""
glRasterPos4s = _libraries['/usr/lib/libglut.so'].glRasterPos4s
glRasterPos4s.restype = None
glRasterPos4s.argtypes = [GLshort, GLshort, GLshort, GLshort]
glRasterPos4s.__doc__ = \
"""void glRasterPos4s(GLshort x, GLshort y, GLshort z, GLshort w)
/usr/include/GL/gl.h:1124"""
glRasterPos2dv = _libraries['/usr/lib/libglut.so'].glRasterPos2dv
glRasterPos2dv.restype = None
glRasterPos2dv.argtypes = [POINTER(GLdouble)]
glRasterPos2dv.__doc__ = \
"""void glRasterPos2dv(unknown * v)
/usr/include/GL/gl.h:1126"""
glRasterPos2fv = _libraries['/usr/lib/libglut.so'].glRasterPos2fv
glRasterPos2fv.restype = None
glRasterPos2fv.argtypes = [POINTER(GLfloat)]
glRasterPos2fv.__doc__ = \
"""void glRasterPos2fv(unknown * v)
/usr/include/GL/gl.h:1127"""
glRasterPos2iv = _libraries['/usr/lib/libglut.so'].glRasterPos2iv
glRasterPos2iv.restype = None
glRasterPos2iv.argtypes = [POINTER(GLint)]
glRasterPos2iv.__doc__ = \
"""void glRasterPos2iv(unknown * v)
/usr/include/GL/gl.h:1128"""
glRasterPos2sv = _libraries['/usr/lib/libglut.so'].glRasterPos2sv
glRasterPos2sv.restype = None
glRasterPos2sv.argtypes = [POINTER(GLshort)]
glRasterPos2sv.__doc__ = \
"""void glRasterPos2sv(unknown * v)
/usr/include/GL/gl.h:1129"""
glRasterPos3dv = _libraries['/usr/lib/libglut.so'].glRasterPos3dv
glRasterPos3dv.restype = None
glRasterPos3dv.argtypes = [POINTER(GLdouble)]
glRasterPos3dv.__doc__ = \
"""void glRasterPos3dv(unknown * v)
/usr/include/GL/gl.h:1131"""
glRasterPos3fv = _libraries['/usr/lib/libglut.so'].glRasterPos3fv
glRasterPos3fv.restype = None
glRasterPos3fv.argtypes = [POINTER(GLfloat)]
glRasterPos3fv.__doc__ = \
"""void glRasterPos3fv(unknown * v)
/usr/include/GL/gl.h:1132"""
glRasterPos3iv = _libraries['/usr/lib/libglut.so'].glRasterPos3iv
glRasterPos3iv.restype = None
glRasterPos3iv.argtypes = [POINTER(GLint)]
glRasterPos3iv.__doc__ = \
"""void glRasterPos3iv(unknown * v)
/usr/include/GL/gl.h:1133"""
glRasterPos3sv = _libraries['/usr/lib/libglut.so'].glRasterPos3sv
glRasterPos3sv.restype = None
glRasterPos3sv.argtypes = [POINTER(GLshort)]
glRasterPos3sv.__doc__ = \
"""void glRasterPos3sv(unknown * v)
/usr/include/GL/gl.h:1134"""
glRasterPos4dv = _libraries['/usr/lib/libglut.so'].glRasterPos4dv
glRasterPos4dv.restype = None
glRasterPos4dv.argtypes = [POINTER(GLdouble)]
glRasterPos4dv.__doc__ = \
"""void glRasterPos4dv(unknown * v)
/usr/include/GL/gl.h:1136"""
glRasterPos4fv = _libraries['/usr/lib/libglut.so'].glRasterPos4fv
glRasterPos4fv.restype = None
glRasterPos4fv.argtypes = [POINTER(GLfloat)]
glRasterPos4fv.__doc__ = \
"""void glRasterPos4fv(unknown * v)
/usr/include/GL/gl.h:1137"""
glRasterPos4iv = _libraries['/usr/lib/libglut.so'].glRasterPos4iv
glRasterPos4iv.restype = None
glRasterPos4iv.argtypes = [POINTER(GLint)]
glRasterPos4iv.__doc__ = \
"""void glRasterPos4iv(unknown * v)
/usr/include/GL/gl.h:1138"""
glRasterPos4sv = _libraries['/usr/lib/libglut.so'].glRasterPos4sv
glRasterPos4sv.restype = None
glRasterPos4sv.argtypes = [POINTER(GLshort)]
glRasterPos4sv.__doc__ = \
"""void glRasterPos4sv(unknown * v)
/usr/include/GL/gl.h:1139"""
glRectd = _libraries['/usr/lib/libglut.so'].glRectd
glRectd.restype = None
glRectd.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble]
glRectd.__doc__ = \
"""void glRectd(GLdouble x1, GLdouble y1, GLdouble x2, GLdouble y2)
/usr/include/GL/gl.h:1142"""
glRectf = _libraries['/usr/lib/libglut.so'].glRectf
glRectf.restype = None
glRectf.argtypes = [GLfloat, GLfloat, GLfloat, GLfloat]
glRectf.__doc__ = \
"""void glRectf(GLfloat x1, GLfloat y1, GLfloat x2, GLfloat y2)
/usr/include/GL/gl.h:1143"""
glRecti = _libraries['/usr/lib/libglut.so'].glRecti
glRecti.restype = None
glRecti.argtypes = [GLint, GLint, GLint, GLint]
glRecti.__doc__ = \
"""void glRecti(GLint x1, GLint y1, GLint x2, GLint y2)
/usr/include/GL/gl.h:1144"""
glRects = _libraries['/usr/lib/libglut.so'].glRects
glRects.restype = None
glRects.argtypes = [GLshort, GLshort, GLshort, GLshort]
glRects.__doc__ = \
"""void glRects(GLshort x1, GLshort y1, GLshort x2, GLshort y2)
/usr/include/GL/gl.h:1145"""
glRectdv = _libraries['/usr/lib/libglut.so'].glRectdv
glRectdv.restype = None
glRectdv.argtypes = [POINTER(GLdouble), POINTER(GLdouble)]
glRectdv.__doc__ = \
"""void glRectdv(unknown * v1, unknown * v2)
/usr/include/GL/gl.h:1148"""
glRectfv = _libraries['/usr/lib/libglut.so'].glRectfv
glRectfv.restype = None
glRectfv.argtypes = [POINTER(GLfloat), POINTER(GLfloat)]
glRectfv.__doc__ = \
"""void glRectfv(unknown * v1, unknown * v2)
/usr/include/GL/gl.h:1149"""
glRectiv = _libraries['/usr/lib/libglut.so'].glRectiv
glRectiv.restype = None
glRectiv.argtypes = [POINTER(GLint), POINTER(GLint)]
glRectiv.__doc__ = \
"""void glRectiv(unknown * v1, unknown * v2)
/usr/include/GL/gl.h:1150"""
glRectsv = _libraries['/usr/lib/libglut.so'].glRectsv
glRectsv.restype = None
glRectsv.argtypes = [POINTER(GLshort), POINTER(GLshort)]
glRectsv.__doc__ = \
"""void glRectsv(unknown * v1, unknown * v2)
/usr/include/GL/gl.h:1151"""
glVertexPointer = _libraries['/usr/lib/libglut.so'].glVertexPointer
glVertexPointer.restype = None
glVertexPointer.argtypes = [GLint, GLenum, GLsizei, POINTER(GLvoid)]
glVertexPointer.__doc__ = \
"""void glVertexPointer(GLint size, GLenum type, GLsizei stride, unknown * ptr)
/usr/include/GL/gl.h:1159"""
glNormalPointer = _libraries['/usr/lib/libglut.so'].glNormalPointer
glNormalPointer.restype = None
glNormalPointer.argtypes = [GLenum, GLsizei, POINTER(GLvoid)]
glNormalPointer.__doc__ = \
"""void glNormalPointer(GLenum type, GLsizei stride, unknown * ptr)
/usr/include/GL/gl.h:1162"""
glColorPointer = _libraries['/usr/lib/libglut.so'].glColorPointer
glColorPointer.restype = None
glColorPointer.argtypes = [GLint, GLenum, GLsizei, POINTER(GLvoid)]
glColorPointer.__doc__ = \
"""void glColorPointer(GLint size, GLenum type, GLsizei stride, unknown * ptr)
/usr/include/GL/gl.h:1165"""
glIndexPointer = _libraries['/usr/lib/libglut.so'].glIndexPointer
glIndexPointer.restype = None
glIndexPointer.argtypes = [GLenum, GLsizei, POINTER(GLvoid)]
glIndexPointer.__doc__ = \
"""void glIndexPointer(GLenum type, GLsizei stride, unknown * ptr)
/usr/include/GL/gl.h:1168"""
glTexCoordPointer = _libraries['/usr/lib/libglut.so'].glTexCoordPointer
glTexCoordPointer.restype = None
glTexCoordPointer.argtypes = [GLint, GLenum, GLsizei, POINTER(GLvoid)]
glTexCoordPointer.__doc__ = \
"""void glTexCoordPointer(GLint size, GLenum type, GLsizei stride, unknown * ptr)
/usr/include/GL/gl.h:1171"""
glEdgeFlagPointer = _libraries['/usr/lib/libglut.so'].glEdgeFlagPointer
glEdgeFlagPointer.restype = None
glEdgeFlagPointer.argtypes = [GLsizei, POINTER(GLvoid)]
glEdgeFlagPointer.__doc__ = \
"""void glEdgeFlagPointer(GLsizei stride, unknown * ptr)
/usr/include/GL/gl.h:1173"""
glGetPointerv = _libraries['/usr/lib/libglut.so'].glGetPointerv
glGetPointerv.restype = None
glGetPointerv.argtypes = [GLenum, POINTER(POINTER(GLvoid))]
glGetPointerv.__doc__ = \
"""void glGetPointerv(GLenum pname, GLvoid * * params)
/usr/include/GL/gl.h:1175"""
glArrayElement = _libraries['/usr/lib/libglut.so'].glArrayElement
glArrayElement.restype = None
glArrayElement.argtypes = [GLint]
glArrayElement.__doc__ = \
"""void glArrayElement(GLint i)
/usr/include/GL/gl.h:1177"""
glDrawArrays = _libraries['/usr/lib/libglut.so'].glDrawArrays
glDrawArrays.restype = None
glDrawArrays.argtypes = [GLenum, GLint, GLsizei]
glDrawArrays.__doc__ = \
"""void glDrawArrays(GLenum mode, GLint first, GLsizei count)
/usr/include/GL/gl.h:1179"""
glDrawElements = _libraries['/usr/lib/libglut.so'].glDrawElements
glDrawElements.restype = None
glDrawElements.argtypes = [GLenum, GLsizei, GLenum, POINTER(GLvoid)]
glDrawElements.__doc__ = \
"""void glDrawElements(GLenum mode, GLsizei count, GLenum type, unknown * indices)
/usr/include/GL/gl.h:1182"""
glInterleavedArrays = _libraries['/usr/lib/libglut.so'].glInterleavedArrays
glInterleavedArrays.restype = None
glInterleavedArrays.argtypes = [GLenum, GLsizei, POINTER(GLvoid)]
glInterleavedArrays.__doc__ = \
"""void glInterleavedArrays(GLenum format, GLsizei stride, unknown * pointer)
/usr/include/GL/gl.h:1185"""
glShadeModel = _libraries['/usr/lib/libglut.so'].glShadeModel
glShadeModel.restype = None
glShadeModel.argtypes = [GLenum]
glShadeModel.__doc__ = \
"""void glShadeModel(GLenum mode)
/usr/include/GL/gl.h:1191"""
glLightf = _libraries['/usr/lib/libglut.so'].glLightf
glLightf.restype = None
glLightf.argtypes = [GLenum, GLenum, GLfloat]
glLightf.__doc__ = \
"""void glLightf(GLenum light, GLenum pname, GLfloat param)
/usr/include/GL/gl.h:1193"""
glLighti = _libraries['/usr/lib/libglut.so'].glLighti
glLighti.restype = None
glLighti.argtypes = [GLenum, GLenum, GLint]
glLighti.__doc__ = \
"""void glLighti(GLenum light, GLenum pname, GLint param)
/usr/include/GL/gl.h:1194"""
glLightfv = _libraries['/usr/lib/libglut.so'].glLightfv
glLightfv.restype = None
glLightfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
glLightfv.__doc__ = \
"""void glLightfv(GLenum light, GLenum pname, unknown * params)
/usr/include/GL/gl.h:1196"""
glLightiv = _libraries['/usr/lib/libglut.so'].glLightiv
glLightiv.restype = None
glLightiv.argtypes = [GLenum, GLenum, POINTER(GLint)]
glLightiv.__doc__ = \
"""void glLightiv(GLenum light, GLenum pname, unknown * params)
/usr/include/GL/gl.h:1198"""
glGetLightfv = _libraries['/usr/lib/libglut.so'].glGetLightfv
glGetLightfv.restype = None
glGetLightfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
glGetLightfv.__doc__ = \
"""void glGetLightfv(GLenum light, GLenum pname, GLfloat * params)
/usr/include/GL/gl.h:1201"""
glGetLightiv = _libraries['/usr/lib/libglut.so'].glGetLightiv
glGetLightiv.restype = None
glGetLightiv.argtypes = [GLenum, GLenum, POINTER(GLint)]
glGetLightiv.__doc__ = \
"""void glGetLightiv(GLenum light, GLenum pname, GLint * params)
/usr/include/GL/gl.h:1203"""
glLightModelf = _libraries['/usr/lib/libglut.so'].glLightModelf
glLightModelf.restype = None
glLightModelf.argtypes = [GLenum, GLfloat]
glLightModelf.__doc__ = \
"""void glLightModelf(GLenum pname, GLfloat param)
/usr/include/GL/gl.h:1205"""
glLightModeli = _libraries['/usr/lib/libglut.so'].glLightModeli
glLightModeli.restype = None
glLightModeli.argtypes = [GLenum, GLint]
glLightModeli.__doc__ = \
"""void glLightModeli(GLenum pname, GLint param)
/usr/include/GL/gl.h:1206"""
glLightModelfv = _libraries['/usr/lib/libglut.so'].glLightModelfv
glLightModelfv.restype = None
glLightModelfv.argtypes = [GLenum, POINTER(GLfloat)]
glLightModelfv.__doc__ = \
"""void glLightModelfv(GLenum pname, unknown * params)
/usr/include/GL/gl.h:1207"""
glLightModeliv = _libraries['/usr/lib/libglut.so'].glLightModeliv
glLightModeliv.restype = None
glLightModeliv.argtypes = [GLenum, POINTER(GLint)]
glLightModeliv.__doc__ = \
"""void glLightModeliv(GLenum pname, unknown * params)
/usr/include/GL/gl.h:1208"""
glMaterialf = _libraries['/usr/lib/libglut.so'].glMaterialf
glMaterialf.restype = None
glMaterialf.argtypes = [GLenum, GLenum, GLfloat]
glMaterialf.__doc__ = \
"""void glMaterialf(GLenum face, GLenum pname, GLfloat param)
/usr/include/GL/gl.h:1210"""
glMateriali = _libraries['/usr/lib/libglut.so'].glMateriali
glMateriali.restype = None
glMateriali.argtypes = [GLenum, GLenum, GLint]
glMateriali.__doc__ = \
"""void glMateriali(GLenum face, GLenum pname, GLint param)
/usr/include/GL/gl.h:1211"""
glMaterialfv = _libraries['/usr/lib/libglut.so'].glMaterialfv
glMaterialfv.restype = None
glMaterialfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
glMaterialfv.__doc__ = \
"""void glMaterialfv(GLenum face, GLenum pname, unknown * params)
/usr/include/GL/gl.h:1212"""
glMaterialiv = _libraries['/usr/lib/libglut.so'].glMaterialiv
glMaterialiv.restype = None
glMaterialiv.argtypes = [GLenum, GLenum, POINTER(GLint)]
glMaterialiv.__doc__ = \
"""void glMaterialiv(GLenum face, GLenum pname, unknown * params)
/usr/include/GL/gl.h:1213"""
glGetMaterialfv = _libraries['/usr/lib/libglut.so'].glGetMaterialfv
glGetMaterialfv.restype = None
glGetMaterialfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
glGetMaterialfv.__doc__ = \
"""void glGetMaterialfv(GLenum face, GLenum pname, GLfloat * params)
/usr/include/GL/gl.h:1215"""
glGetMaterialiv = _libraries['/usr/lib/libglut.so'].glGetMaterialiv
glGetMaterialiv.restype = None
glGetMaterialiv.argtypes = [GLenum, GLenum, POINTER(GLint)]
glGetMaterialiv.__doc__ = \
"""void glGetMaterialiv(GLenum face, GLenum pname, GLint * params)
/usr/include/GL/gl.h:1216"""
glColorMaterial = _libraries['/usr/lib/libglut.so'].glColorMaterial
glColorMaterial.restype = None
glColorMaterial.argtypes = [GLenum, GLenum]
glColorMaterial.__doc__ = \
"""void glColorMaterial(GLenum face, GLenum mode)
/usr/include/GL/gl.h:1218"""
glPixelZoom = _libraries['/usr/lib/libglut.so'].glPixelZoom
glPixelZoom.restype = None
glPixelZoom.argtypes = [GLfloat, GLfloat]
glPixelZoom.__doc__ = \
"""void glPixelZoom(GLfloat xfactor, GLfloat yfactor)
/usr/include/GL/gl.h:1225"""
glPixelStoref = _libraries['/usr/lib/libglut.so'].glPixelStoref
glPixelStoref.restype = None
glPixelStoref.argtypes = [GLenum, GLfloat]
glPixelStoref.__doc__ = \
"""void glPixelStoref(GLenum pname, GLfloat param)
/usr/include/GL/gl.h:1227"""
glPixelStorei = _libraries['/usr/lib/libglut.so'].glPixelStorei
glPixelStorei.restype = None
glPixelStorei.argtypes = [GLenum, GLint]
glPixelStorei.__doc__ = \
"""void glPixelStorei(GLenum pname, GLint param)
/usr/include/GL/gl.h:1228"""
glPixelTransferf = _libraries['/usr/lib/libglut.so'].glPixelTransferf
glPixelTransferf.restype = None
glPixelTransferf.argtypes = [GLenum, GLfloat]
glPixelTransferf.__doc__ = \
"""void glPixelTransferf(GLenum pname, GLfloat param)
/usr/include/GL/gl.h:1230"""
glPixelTransferi = _libraries['/usr/lib/libglut.so'].glPixelTransferi
glPixelTransferi.restype = None
glPixelTransferi.argtypes = [GLenum, GLint]
glPixelTransferi.__doc__ = \
"""void glPixelTransferi(GLenum pname, GLint param)
/usr/include/GL/gl.h:1231"""
glPixelMapfv = _libraries['/usr/lib/libglut.so'].glPixelMapfv
glPixelMapfv.restype = None
glPixelMapfv.argtypes = [GLenum, GLsizei, POINTER(GLfloat)]
glPixelMapfv.__doc__ = \
"""void glPixelMapfv(GLenum map, GLsizei mapsize, unknown * values)
/usr/include/GL/gl.h:1234"""
glPixelMapuiv = _libraries['/usr/lib/libglut.so'].glPixelMapuiv
glPixelMapuiv.restype = None
glPixelMapuiv.argtypes = [GLenum, GLsizei, POINTER(GLuint)]
glPixelMapuiv.__doc__ = \
"""void glPixelMapuiv(GLenum map, GLsizei mapsize, unknown * values)
/usr/include/GL/gl.h:1236"""
glPixelMapusv = _libraries['/usr/lib/libglut.so'].glPixelMapusv
glPixelMapusv.restype = None
glPixelMapusv.argtypes = [GLenum, GLsizei, POINTER(GLushort)]
glPixelMapusv.__doc__ = \
"""void glPixelMapusv(GLenum map, GLsizei mapsize, unknown * values)
/usr/include/GL/gl.h:1238"""
glGetPixelMapfv = _libraries['/usr/lib/libglut.so'].glGetPixelMapfv
glGetPixelMapfv.restype = None
glGetPixelMapfv.argtypes = [GLenum, POINTER(GLfloat)]
glGetPixelMapfv.__doc__ = \
"""void glGetPixelMapfv(GLenum map, GLfloat * values)
/usr/include/GL/gl.h:1240"""
glGetPixelMapuiv = _libraries['/usr/lib/libglut.so'].glGetPixelMapuiv
glGetPixelMapuiv.restype = None
glGetPixelMapuiv.argtypes = [GLenum, POINTER(GLuint)]
glGetPixelMapuiv.__doc__ = \
"""void glGetPixelMapuiv(GLenum map, GLuint * values)
/usr/include/GL/gl.h:1241"""
glGetPixelMapusv = _libraries['/usr/lib/libglut.so'].glGetPixelMapusv
glGetPixelMapusv.restype = None
glGetPixelMapusv.argtypes = [GLenum, POINTER(GLushort)]
glGetPixelMapusv.__doc__ = \
"""void glGetPixelMapusv(GLenum map, GLushort * values)
/usr/include/GL/gl.h:1242"""
glBitmap = _libraries['/usr/lib/libglut.so'].glBitmap
glBitmap.restype = None
glBitmap.argtypes = [GLsizei, GLsizei, GLfloat, GLfloat, GLfloat, GLfloat, POINTER(GLubyte)]
glBitmap.__doc__ = \
"""void glBitmap(GLsizei width, GLsizei height, GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat ymove, unknown * bitmap)
/usr/include/GL/gl.h:1247"""
glReadPixels = _libraries['/usr/lib/libglut.so'].glReadPixels
glReadPixels.restype = None
glReadPixels.argtypes = [GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid)]
glReadPixels.__doc__ = \
"""void glReadPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLvoid * pixels)
/usr/include/GL/gl.h:1252"""
glDrawPixels = _libraries['/usr/lib/libglut.so'].glDrawPixels
glDrawPixels.restype = None
glDrawPixels.argtypes = [GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid)]
glDrawPixels.__doc__ = \
"""void glDrawPixels(GLsizei width, GLsizei height, GLenum format, GLenum type, unknown * pixels)
/usr/include/GL/gl.h:1256"""
glCopyPixels = _libraries['/usr/lib/libglut.so'].glCopyPixels
glCopyPixels.restype = None
glCopyPixels.argtypes = [GLint, GLint, GLsizei, GLsizei, GLenum]
glCopyPixels.__doc__ = \
"""void glCopyPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum type)
/usr/include/GL/gl.h:1260"""
glStencilFunc = _libraries['/usr/lib/libglut.so'].glStencilFunc
glStencilFunc.restype = None
glStencilFunc.argtypes = [GLenum, GLint, GLuint]
glStencilFunc.__doc__ = \
"""void glStencilFunc(GLenum func, GLint ref, GLuint mask)
/usr/include/GL/gl.h:1266"""
glStencilMask = _libraries['/usr/lib/libglut.so'].glStencilMask
glStencilMask.restype = None
glStencilMask.argtypes = [GLuint]
glStencilMask.__doc__ = \
"""void glStencilMask(GLuint mask)
/usr/include/GL/gl.h:1268"""
glStencilOp = _libraries['/usr/lib/libglut.so'].glStencilOp
glStencilOp.restype = None
glStencilOp.argtypes = [GLenum, GLenum, GLenum]
glStencilOp.__doc__ = \
"""void glStencilOp(GLenum fail, GLenum zfail, GLenum zpass)
/usr/include/GL/gl.h:1270"""
glClearStencil = _libraries['/usr/lib/libglut.so'].glClearStencil
glClearStencil.restype = None
glClearStencil.argtypes = [GLint]
glClearStencil.__doc__ = \
"""void glClearStencil(GLint s)
/usr/include/GL/gl.h:1272"""
glTexGend = _libraries['/usr/lib/libglut.so'].glTexGend
glTexGend.restype = None
glTexGend.argtypes = [GLenum, GLenum, GLdouble]
glTexGend.__doc__ = \
"""void glTexGend(GLenum coord, GLenum pname, GLdouble param)
/usr/include/GL/gl.h:1280"""
glTexGenf = _libraries['/usr/lib/libglut.so'].glTexGenf
glTexGenf.restype = None
glTexGenf.argtypes = [GLenum, GLenum, GLfloat]
glTexGenf.__doc__ = \
"""void glTexGenf(GLenum coord, GLenum pname, GLfloat param)
/usr/include/GL/gl.h:1281"""
glTexGeni = _libraries['/usr/lib/libglut.so'].glTexGeni
glTexGeni.restype = None
glTexGeni.argtypes = [GLenum, GLenum, GLint]
glTexGeni.__doc__ = \
"""void glTexGeni(GLenum coord, GLenum pname, GLint param)
/usr/include/GL/gl.h:1282"""
glTexGendv = _libraries['/usr/lib/libglut.so'].glTexGendv
glTexGendv.restype = None
glTexGendv.argtypes = [GLenum, GLenum, POINTER(GLdouble)]
glTexGendv.__doc__ = \
"""void glTexGendv(GLenum coord, GLenum pname, unknown * params)
/usr/include/GL/gl.h:1284"""
glTexGenfv = _libraries['/usr/lib/libglut.so'].glTexGenfv
glTexGenfv.restype = None
glTexGenfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
glTexGenfv.__doc__ = \
"""void glTexGenfv(GLenum coord, GLenum pname, unknown * params)
/usr/include/GL/gl.h:1285"""
glTexGeniv = _libraries['/usr/lib/libglut.so'].glTexGeniv
glTexGeniv.restype = None
glTexGeniv.argtypes = [GLenum, GLenum, POINTER(GLint)]
glTexGeniv.__doc__ = \
"""void glTexGeniv(GLenum coord, GLenum pname, unknown * params)
/usr/include/GL/gl.h:1286"""
glGetTexGendv = _libraries['/usr/lib/libglut.so'].glGetTexGendv
glGetTexGendv.restype = None
glGetTexGendv.argtypes = [GLenum, GLenum, POINTER(GLdouble)]
glGetTexGendv.__doc__ = \
"""void glGetTexGendv(GLenum coord, GLenum pname, GLdouble * params)
/usr/include/GL/gl.h:1288"""
glGetTexGenfv = _libraries['/usr/lib/libglut.so'].glGetTexGenfv
glGetTexGenfv.restype = None
glGetTexGenfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
glGetTexGenfv.__doc__ = \
"""void glGetTexGenfv(GLenum coord, GLenum pname, GLfloat * params)
/usr/include/GL/gl.h:1289"""
glGetTexGeniv = _libraries['/usr/lib/libglut.so'].glGetTexGeniv
glGetTexGeniv.restype = None
glGetTexGeniv.argtypes = [GLenum, GLenum, POINTER(GLint)]
glGetTexGeniv.__doc__ = \
"""void glGetTexGeniv(GLenum coord, GLenum pname, GLint * params)
/usr/include/GL/gl.h:1290"""
glTexEnvf = _libraries['/usr/lib/libglut.so'].glTexEnvf
glTexEnvf.restype = None
glTexEnvf.argtypes = [GLenum, GLenum, GLfloat]
glTexEnvf.__doc__ = \
"""void glTexEnvf(GLenum target, GLenum pname, GLfloat param)
/usr/include/GL/gl.h:1293"""
glTexEnvi = _libraries['/usr/lib/libglut.so'].glTexEnvi
glTexEnvi.restype = None
glTexEnvi.argtypes = [GLenum, GLenum, GLint]
glTexEnvi.__doc__ = \
"""void glTexEnvi(GLenum target, GLenum pname, GLint param)
/usr/include/GL/gl.h:1294"""
glTexEnvfv = _libraries['/usr/lib/libglut.so'].glTexEnvfv
glTexEnvfv.restype = None
glTexEnvfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
glTexEnvfv.__doc__ = \
"""void glTexEnvfv(GLenum target, GLenum pname, unknown * params)
/usr/include/GL/gl.h:1296"""
glTexEnviv = _libraries['/usr/lib/libglut.so'].glTexEnviv
glTexEnviv.restype = None
glTexEnviv.argtypes = [GLenum, GLenum, POINTER(GLint)]
glTexEnviv.__doc__ = \
"""void glTexEnviv(GLenum target, GLenum pname, unknown * params)
/usr/include/GL/gl.h:1297"""
glGetTexEnvfv = _libraries['/usr/lib/libglut.so'].glGetTexEnvfv
glGetTexEnvfv.restype = None
glGetTexEnvfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
glGetTexEnvfv.__doc__ = \
"""void glGetTexEnvfv(GLenum target, GLenum pname, GLfloat * params)
/usr/include/GL/gl.h:1299"""
glGetTexEnviv = _libraries['/usr/lib/libglut.so'].glGetTexEnviv
glGetTexEnviv.restype = None
glGetTexEnviv.argtypes = [GLenum, GLenum, POINTER(GLint)]
glGetTexEnviv.__doc__ = \
"""void glGetTexEnviv(GLenum target, GLenum pname, GLint * params)
/usr/include/GL/gl.h:1300"""
glTexParameterf = _libraries['/usr/lib/libglut.so'].glTexParameterf
glTexParameterf.restype = None
glTexParameterf.argtypes = [GLenum, GLenum, GLfloat]
glTexParameterf.__doc__ = \
"""void glTexParameterf(GLenum target, GLenum pname, GLfloat param)
/usr/include/GL/gl.h:1303"""
glTexParameteri = _libraries['/usr/lib/libglut.so'].glTexParameteri
glTexParameteri.restype = None
glTexParameteri.argtypes = [GLenum, GLenum, GLint]
glTexParameteri.__doc__ = \
"""void glTexParameteri(GLenum target, GLenum pname, GLint param)
/usr/include/GL/gl.h:1304"""
glTexParameterfv = _libraries['/usr/lib/libglut.so'].glTexParameterfv
glTexParameterfv.restype = None
glTexParameterfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
glTexParameterfv.__doc__ = \
"""void glTexParameterfv(GLenum target, GLenum pname, unknown * params)
/usr/include/GL/gl.h:1307"""
glTexParameteriv = _libraries['/usr/lib/libglut.so'].glTexParameteriv
glTexParameteriv.restype = None
glTexParameteriv.argtypes = [GLenum, GLenum, POINTER(GLint)]
glTexParameteriv.__doc__ = \
"""void glTexParameteriv(GLenum target, GLenum pname, unknown * params)
/usr/include/GL/gl.h:1309"""
glGetTexParameterfv = _libraries['/usr/lib/libglut.so'].glGetTexParameterfv
glGetTexParameterfv.restype = None
glGetTexParameterfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
glGetTexParameterfv.__doc__ = \
"""void glGetTexParameterfv(GLenum target, GLenum pname, GLfloat * params)
/usr/include/GL/gl.h:1312"""
glGetTexParameteriv = _libraries['/usr/lib/libglut.so'].glGetTexParameteriv
glGetTexParameteriv.restype = None
glGetTexParameteriv.argtypes = [GLenum, GLenum, POINTER(GLint)]
glGetTexParameteriv.__doc__ = \
"""void glGetTexParameteriv(GLenum target, GLenum pname, GLint * params)
/usr/include/GL/gl.h:1314"""
glGetTexLevelParameterfv = _libraries['/usr/lib/libglut.so'].glGetTexLevelParameterfv
glGetTexLevelParameterfv.restype = None
glGetTexLevelParameterfv.argtypes = [GLenum, GLint, GLenum, POINTER(GLfloat)]
glGetTexLevelParameterfv.__doc__ = \
"""void glGetTexLevelParameterfv(GLenum target, GLint level, GLenum pname, GLfloat * params)
/usr/include/GL/gl.h:1317"""
glGetTexLevelParameteriv = _libraries['/usr/lib/libglut.so'].glGetTexLevelParameteriv
glGetTexLevelParameteriv.restype = None
glGetTexLevelParameteriv.argtypes = [GLenum, GLint, GLenum, POINTER(GLint)]
glGetTexLevelParameteriv.__doc__ = \
"""void glGetTexLevelParameteriv(GLenum target, GLint level, GLenum pname, GLint * params)
/usr/include/GL/gl.h:1319"""
glTexImage1D = _libraries['/usr/lib/libglut.so'].glTexImage1D
glTexImage1D.restype = None
glTexImage1D.argtypes = [GLenum, GLint, GLint, GLsizei, GLint, GLenum, GLenum, POINTER(GLvoid)]
glTexImage1D.__doc__ = \
"""void glTexImage1D(GLenum target, GLint level, GLint internalFormat, GLsizei width, GLint border, GLenum format, GLenum type, unknown * pixels)
/usr/include/GL/gl.h:1326"""
glTexImage2D = _libraries['/usr/lib/libglut.so'].glTexImage2D
glTexImage2D.restype = None
glTexImage2D.argtypes = [GLenum, GLint, GLint, GLsizei, GLsizei, GLint, GLenum, GLenum, POINTER(GLvoid)]
glTexImage2D.__doc__ = \
"""void glTexImage2D(GLenum target, GLint level, GLint internalFormat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, unknown * pixels)
/usr/include/GL/gl.h:1332"""
glGetTexImage = _libraries['/usr/lib/libglut.so'].glGetTexImage
glGetTexImage.restype = None
glGetTexImage.argtypes = [GLenum, GLint, GLenum, GLenum, POINTER(GLvoid)]
glGetTexImage.__doc__ = \
"""void glGetTexImage(GLenum target, GLint level, GLenum format, GLenum type, GLvoid * pixels)
/usr/include/GL/gl.h:1336"""
glGenTextures = _libraries['/usr/lib/libglut.so'].glGenTextures
glGenTextures.restype = None
glGenTextures.argtypes = [GLsizei, POINTER(GLuint)]
glGenTextures.__doc__ = \
"""void glGenTextures(GLsizei n, GLuint * textures)
/usr/include/GL/gl.h:1341"""
glDeleteTextures = _libraries['/usr/lib/libglut.so'].glDeleteTextures
glDeleteTextures.restype = None
glDeleteTextures.argtypes = [GLsizei, POINTER(GLuint)]
glDeleteTextures.__doc__ = \
"""void glDeleteTextures(GLsizei n, unknown * textures)
/usr/include/GL/gl.h:1343"""
glBindTexture = _libraries['/usr/lib/libglut.so'].glBindTexture
glBindTexture.restype = None
glBindTexture.argtypes = [GLenum, GLuint]
glBindTexture.__doc__ = \
"""void glBindTexture(GLenum target, GLuint texture)
/usr/include/GL/gl.h:1345"""
glPrioritizeTextures = _libraries['/usr/lib/libglut.so'].glPrioritizeTextures
glPrioritizeTextures.restype = None
glPrioritizeTextures.argtypes = [GLsizei, POINTER(GLuint), POINTER(GLclampf)]
glPrioritizeTextures.__doc__ = \
"""void glPrioritizeTextures(GLsizei n, unknown * textures, unknown * priorities)
/usr/include/GL/gl.h:1349"""
glAreTexturesResident = _libraries['/usr/lib/libglut.so'].glAreTexturesResident
glAreTexturesResident.restype = GLboolean
glAreTexturesResident.argtypes = [GLsizei, POINTER(GLuint), POINTER(GLboolean)]
glAreTexturesResident.__doc__ = \
"""GLboolean glAreTexturesResident(GLsizei n, unknown * textures, GLboolean * residences)
/usr/include/GL/gl.h:1353"""
glIsTexture = _libraries['/usr/lib/libglut.so'].glIsTexture
glIsTexture.restype = GLboolean
glIsTexture.argtypes = [GLuint]
glIsTexture.__doc__ = \
"""GLboolean glIsTexture(GLuint texture)
/usr/include/GL/gl.h:1355"""
glTexSubImage1D = _libraries['/usr/lib/libglut.so'].glTexSubImage1D
glTexSubImage1D.restype = None
glTexSubImage1D.argtypes = [GLenum, GLint, GLint, GLsizei, GLenum, GLenum, POINTER(GLvoid)]
glTexSubImage1D.__doc__ = \
"""void glTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, unknown * pixels)
/usr/include/GL/gl.h:1361"""
glTexSubImage2D = _libraries['/usr/lib/libglut.so'].glTexSubImage2D
glTexSubImage2D.restype = None
glTexSubImage2D.argtypes = [GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid)]
glTexSubImage2D.__doc__ = \
"""void glTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, unknown * pixels)
/usr/include/GL/gl.h:1368"""
glCopyTexImage1D = _libraries['/usr/lib/libglut.so'].glCopyTexImage1D
glCopyTexImage1D.restype = None
glCopyTexImage1D.argtypes = [GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLint]
glCopyTexImage1D.__doc__ = \
"""void glCopyTexImage1D(GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLint border)
/usr/include/GL/gl.h:1374"""
glCopyTexImage2D = _libraries['/usr/lib/libglut.so'].glCopyTexImage2D
glCopyTexImage2D.restype = None
glCopyTexImage2D.argtypes = [GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLsizei, GLint]
glCopyTexImage2D.__doc__ = \
"""void glCopyTexImage2D(GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border)
/usr/include/GL/gl.h:1381"""
glCopyTexSubImage1D = _libraries['/usr/lib/libglut.so'].glCopyTexSubImage1D
glCopyTexSubImage1D.restype = None
glCopyTexSubImage1D.argtypes = [GLenum, GLint, GLint, GLint, GLint, GLsizei]
glCopyTexSubImage1D.__doc__ = \
"""void glCopyTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width)
/usr/include/GL/gl.h:1386"""
glCopyTexSubImage2D = _libraries['/usr/lib/libglut.so'].glCopyTexSubImage2D
glCopyTexSubImage2D.restype = None
glCopyTexSubImage2D.argtypes = [GLenum, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei]
glCopyTexSubImage2D.__doc__ = \
"""void glCopyTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height)
/usr/include/GL/gl.h:1392"""
glMap1d = _libraries['/usr/lib/libglut.so'].glMap1d
glMap1d.restype = None
glMap1d.argtypes = [GLenum, GLdouble, GLdouble, GLint, GLint, POINTER(GLdouble)]
glMap1d.__doc__ = \
"""void glMap1d(GLenum target, GLdouble u1, GLdouble u2, GLint stride, GLint order, unknown * points)
/usr/include/GL/gl.h:1401"""
glMap1f = _libraries['/usr/lib/libglut.so'].glMap1f
glMap1f.restype = None
glMap1f.argtypes = [GLenum, GLfloat, GLfloat, GLint, GLint, POINTER(GLfloat)]
glMap1f.__doc__ = \
"""void glMap1f(GLenum target, GLfloat u1, GLfloat u2, GLint stride, GLint order, unknown * points)
/usr/include/GL/gl.h:1404"""
glMap2d = _libraries['/usr/lib/libglut.so'].glMap2d
glMap2d.restype = None
glMap2d.argtypes = [GLenum, GLdouble, GLdouble, GLint, GLint, GLdouble, GLdouble, GLint, GLint, POINTER(GLdouble)]
glMap2d.__doc__ = \
"""void glMap2d(GLenum target, GLdouble u1, GLdouble u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble v2, GLint vstride, GLint vorder, unknown * points)
/usr/include/GL/gl.h:1409"""
glMap2f = _libraries['/usr/lib/libglut.so'].glMap2f
glMap2f.restype = None
glMap2f.argtypes = [GLenum, GLfloat, GLfloat, GLint, GLint, GLfloat, GLfloat, GLint, GLint, POINTER(GLfloat)]
glMap2f.__doc__ = \
"""void glMap2f(GLenum target, GLfloat u1, GLfloat u2, GLint ustride, GLint uorder, GLfloat v1, GLfloat v2, GLint vstride, GLint vorder, unknown * points)
/usr/include/GL/gl.h:1413"""
glGetMapdv = _libraries['/usr/lib/libglut.so'].glGetMapdv
glGetMapdv.restype = None
glGetMapdv.argtypes = [GLenum, GLenum, POINTER(GLdouble)]
glGetMapdv.__doc__ = \
"""void glGetMapdv(GLenum target, GLenum query, GLdouble * v)
/usr/include/GL/gl.h:1415"""
glGetMapfv = _libraries['/usr/lib/libglut.so'].glGetMapfv
glGetMapfv.restype = None
glGetMapfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
glGetMapfv.__doc__ = \
"""void glGetMapfv(GLenum target, GLenum query, GLfloat * v)
/usr/include/GL/gl.h:1416"""
glGetMapiv = _libraries['/usr/lib/libglut.so'].glGetMapiv
glGetMapiv.restype = None
glGetMapiv.argtypes = [GLenum, GLenum, POINTER(GLint)]
glGetMapiv.__doc__ = \
"""void glGetMapiv(GLenum target, GLenum query, GLint * v)
/usr/include/GL/gl.h:1417"""
glEvalCoord1d = _libraries['/usr/lib/libglut.so'].glEvalCoord1d
glEvalCoord1d.restype = None
glEvalCoord1d.argtypes = [GLdouble]
glEvalCoord1d.__doc__ = \
"""void glEvalCoord1d(GLdouble u)
/usr/include/GL/gl.h:1419"""
glEvalCoord1f = _libraries['/usr/lib/libglut.so'].glEvalCoord1f
glEvalCoord1f.restype = None
glEvalCoord1f.argtypes = [GLfloat]
glEvalCoord1f.__doc__ = \
"""void glEvalCoord1f(GLfloat u)
/usr/include/GL/gl.h:1420"""
glEvalCoord1dv = _libraries['/usr/lib/libglut.so'].glEvalCoord1dv
glEvalCoord1dv.restype = None
glEvalCoord1dv.argtypes = [POINTER(GLdouble)]
glEvalCoord1dv.__doc__ = \
"""void glEvalCoord1dv(unknown * u)
/usr/include/GL/gl.h:1422"""
glEvalCoord1fv = _libraries['/usr/lib/libglut.so'].glEvalCoord1fv
glEvalCoord1fv.restype = None
glEvalCoord1fv.argtypes = [POINTER(GLfloat)]
glEvalCoord1fv.__doc__ = \
"""void glEvalCoord1fv(unknown * u)
/usr/include/GL/gl.h:1423"""
glEvalCoord2d = _libraries['/usr/lib/libglut.so'].glEvalCoord2d
glEvalCoord2d.restype = None
glEvalCoord2d.argtypes = [GLdouble, GLdouble]
glEvalCoord2d.__doc__ = \
"""void glEvalCoord2d(GLdouble u, GLdouble v)
/usr/include/GL/gl.h:1425"""
glEvalCoord2f = _libraries['/usr/lib/libglut.so'].glEvalCoord2f
glEvalCoord2f.restype = None
glEvalCoord2f.argtypes = [GLfloat, GLfloat]
glEvalCoord2f.__doc__ = \
"""void glEvalCoord2f(GLfloat u, GLfloat v)
/usr/include/GL/gl.h:1426"""
glEvalCoord2dv = _libraries['/usr/lib/libglut.so'].glEvalCoord2dv
glEvalCoord2dv.restype = None
glEvalCoord2dv.argtypes = [POINTER(GLdouble)]
glEvalCoord2dv.__doc__ = \
"""void glEvalCoord2dv(unknown * u)
/usr/include/GL/gl.h:1428"""
glEvalCoord2fv = _libraries['/usr/lib/libglut.so'].glEvalCoord2fv
glEvalCoord2fv.restype = None
glEvalCoord2fv.argtypes = [POINTER(GLfloat)]
glEvalCoord2fv.__doc__ = \
"""void glEvalCoord2fv(unknown * u)
/usr/include/GL/gl.h:1429"""
glMapGrid1d = _libraries['/usr/lib/libglut.so'].glMapGrid1d
glMapGrid1d.restype = None
glMapGrid1d.argtypes = [GLint, GLdouble, GLdouble]
glMapGrid1d.__doc__ = \
"""void glMapGrid1d(GLint un, GLdouble u1, GLdouble u2)
/usr/include/GL/gl.h:1431"""
glMapGrid1f = _libraries['/usr/lib/libglut.so'].glMapGrid1f
glMapGrid1f.restype = None
glMapGrid1f.argtypes = [GLint, GLfloat, GLfloat]
glMapGrid1f.__doc__ = \
"""void glMapGrid1f(GLint un, GLfloat u1, GLfloat u2)
/usr/include/GL/gl.h:1432"""
glMapGrid2d = _libraries['/usr/lib/libglut.so'].glMapGrid2d
glMapGrid2d.restype = None
glMapGrid2d.argtypes = [GLint, GLdouble, GLdouble, GLint, GLdouble, GLdouble]
glMapGrid2d.__doc__ = \
"""void glMapGrid2d(GLint un, GLdouble u1, GLdouble u2, GLint vn, GLdouble v1, GLdouble v2)
/usr/include/GL/gl.h:1435"""
glMapGrid2f = _libraries['/usr/lib/libglut.so'].glMapGrid2f
glMapGrid2f.restype = None
glMapGrid2f.argtypes = [GLint, GLfloat, GLfloat, GLint, GLfloat, GLfloat]
glMapGrid2f.__doc__ = \
"""void glMapGrid2f(GLint un, GLfloat u1, GLfloat u2, GLint vn, GLfloat v1, GLfloat v2)
/usr/include/GL/gl.h:1437"""
glEvalPoint1 = _libraries['/usr/lib/libglut.so'].glEvalPoint1
glEvalPoint1.restype = None
glEvalPoint1.argtypes = [GLint]
glEvalPoint1.__doc__ = \
"""void glEvalPoint1(GLint i)
/usr/include/GL/gl.h:1439"""
glEvalPoint2 = _libraries['/usr/lib/libglut.so'].glEvalPoint2
glEvalPoint2.restype = None
glEvalPoint2.argtypes = [GLint, GLint]
glEvalPoint2.__doc__ = \
"""void glEvalPoint2(GLint i, GLint j)
/usr/include/GL/gl.h:1441"""
glEvalMesh1 = _libraries['/usr/lib/libglut.so'].glEvalMesh1
glEvalMesh1.restype = None
glEvalMesh1.argtypes = [GLenum, GLint, GLint]
glEvalMesh1.__doc__ = \
"""void glEvalMesh1(GLenum mode, GLint i1, GLint i2)
/usr/include/GL/gl.h:1443"""
glEvalMesh2 = _libraries['/usr/lib/libglut.so'].glEvalMesh2
glEvalMesh2.restype = None
glEvalMesh2.argtypes = [GLenum, GLint, GLint, GLint, GLint]
glEvalMesh2.__doc__ = \
"""void glEvalMesh2(GLenum mode, GLint i1, GLint i2, GLint j1, GLint j2)
/usr/include/GL/gl.h:1445"""
glFogf = _libraries['/usr/lib/libglut.so'].glFogf
glFogf.restype = None
glFogf.argtypes = [GLenum, GLfloat]
glFogf.__doc__ = \
"""void glFogf(GLenum pname, GLfloat param)
/usr/include/GL/gl.h:1452"""
glFogi = _libraries['/usr/lib/libglut.so'].glFogi
glFogi.restype = None
glFogi.argtypes = [GLenum, GLint]
glFogi.__doc__ = \
"""void glFogi(GLenum pname, GLint param)
/usr/include/GL/gl.h:1454"""
glFogfv = _libraries['/usr/lib/libglut.so'].glFogfv
glFogfv.restype = None
glFogfv.argtypes = [GLenum, POINTER(GLfloat)]
glFogfv.__doc__ = \
"""void glFogfv(GLenum pname, unknown * params)
/usr/include/GL/gl.h:1456"""
glFogiv = _libraries['/usr/lib/libglut.so'].glFogiv
glFogiv.restype = None
glFogiv.argtypes = [GLenum, POINTER(GLint)]
glFogiv.__doc__ = \
"""void glFogiv(GLenum pname, unknown * params)
/usr/include/GL/gl.h:1458"""
glFeedbackBuffer = _libraries['/usr/lib/libglut.so'].glFeedbackBuffer
glFeedbackBuffer.restype = None
glFeedbackBuffer.argtypes = [GLsizei, GLenum, POINTER(GLfloat)]
glFeedbackBuffer.__doc__ = \
"""void glFeedbackBuffer(GLsizei size, GLenum type, GLfloat * buffer)
/usr/include/GL/gl.h:1465"""
glPassThrough = _libraries['/usr/lib/libglut.so'].glPassThrough
glPassThrough.restype = None
glPassThrough.argtypes = [GLfloat]
glPassThrough.__doc__ = \
"""void glPassThrough(GLfloat token)
/usr/include/GL/gl.h:1467"""
glSelectBuffer = _libraries['/usr/lib/libglut.so'].glSelectBuffer
glSelectBuffer.restype = None
glSelectBuffer.argtypes = [GLsizei, POINTER(GLuint)]
glSelectBuffer.__doc__ = \
"""void glSelectBuffer(GLsizei size, GLuint * buffer)
/usr/include/GL/gl.h:1469"""
glInitNames = _libraries['/usr/lib/libglut.so'].glInitNames
glInitNames.restype = None
glInitNames.argtypes = []
glInitNames.__doc__ = \
"""void glInitNames()
/usr/include/GL/gl.h:1471"""
glLoadName = _libraries['/usr/lib/libglut.so'].glLoadName
glLoadName.restype = None
glLoadName.argtypes = [GLuint]
glLoadName.__doc__ = \
"""void glLoadName(GLuint name)
/usr/include/GL/gl.h:1473"""
glPushName = _libraries['/usr/lib/libglut.so'].glPushName
glPushName.restype = None
glPushName.argtypes = [GLuint]
glPushName.__doc__ = \
"""void glPushName(GLuint name)
/usr/include/GL/gl.h:1475"""
glPopName = _libraries['/usr/lib/libglut.so'].glPopName
glPopName.restype = None
glPopName.argtypes = []
glPopName.__doc__ = \
"""void glPopName()
/usr/include/GL/gl.h:1477"""
glDrawRangeElements = _libraries['/usr/lib/libglut.so'].glDrawRangeElements
glDrawRangeElements.restype = None
glDrawRangeElements.argtypes = [GLenum, GLuint, GLuint, GLsizei, GLenum, POINTER(GLvoid)]
glDrawRangeElements.__doc__ = \
"""void glDrawRangeElements(GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, unknown * indices)
/usr/include/GL/gl.h:1528"""
glTexImage3D = _libraries['/usr/lib/libglut.so'].glTexImage3D
glTexImage3D.restype = None
glTexImage3D.argtypes = [GLenum, GLint, GLint, GLsizei, GLsizei, GLsizei, GLint, GLenum, GLenum, POINTER(GLvoid)]
glTexImage3D.__doc__ = \
"""void glTexImage3D(GLenum target, GLint level, GLint internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum type, unknown * pixels)
/usr/include/GL/gl.h:1535"""
glTexSubImage3D = _libraries['/usr/lib/libglut.so'].glTexSubImage3D
glTexSubImage3D.restype = None
glTexSubImage3D.argtypes = [GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid)]
glTexSubImage3D.__doc__ = \
"""void glTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, unknown * pixels)
/usr/include/GL/gl.h:1542"""
glCopyTexSubImage3D = _libraries['/usr/lib/libglut.so'].glCopyTexSubImage3D
glCopyTexSubImage3D.restype = None
glCopyTexSubImage3D.argtypes = [GLenum, GLint, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei]
glCopyTexSubImage3D.__doc__ = \
"""void glCopyTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y, GLsizei width, GLsizei height)
/usr/include/GL/gl.h:1548"""
glColorTable = _libraries['/usr/lib/libglut.so'].glColorTable
glColorTable.restype = None
glColorTable.argtypes = [GLenum, GLenum, GLsizei, GLenum, GLenum, POINTER(GLvoid)]
glColorTable.__doc__ = \
"""void glColorTable(GLenum target, GLenum internalformat, GLsizei width, GLenum format, GLenum type, unknown * table)
/usr/include/GL/gl.h:1639"""
glColorSubTable = _libraries['/usr/lib/libglut.so'].glColorSubTable
glColorSubTable.restype = None
glColorSubTable.argtypes = [GLenum, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid)]
glColorSubTable.__doc__ = \
"""void glColorSubTable(GLenum target, GLsizei start, GLsizei count, GLenum format, GLenum type, unknown * data)
/usr/include/GL/gl.h:1644"""
glColorTableParameteriv = _libraries['/usr/lib/libglut.so'].glColorTableParameteriv
glColorTableParameteriv.restype = None
glColorTableParameteriv.argtypes = [GLenum, GLenum, POINTER(GLint)]
glColorTableParameteriv.__doc__ = \
"""void glColorTableParameteriv(GLenum target, GLenum pname, unknown * params)
/usr/include/GL/gl.h:1647"""
glColorTableParameterfv = _libraries['/usr/lib/libglut.so'].glColorTableParameterfv
glColorTableParameterfv.restype = None
glColorTableParameterfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
glColorTableParameterfv.__doc__ = \
"""void glColorTableParameterfv(GLenum target, GLenum pname, unknown * params)
/usr/include/GL/gl.h:1650"""
glCopyColorSubTable = _libraries['/usr/lib/libglut.so'].glCopyColorSubTable
glCopyColorSubTable.restype = None
glCopyColorSubTable.argtypes = [GLenum, GLsizei, GLint, GLint, GLsizei]
glCopyColorSubTable.__doc__ = \
"""void glCopyColorSubTable(GLenum target, GLsizei start, GLint x, GLint y, GLsizei width)
/usr/include/GL/gl.h:1653"""
glCopyColorTable = _libraries['/usr/lib/libglut.so'].glCopyColorTable
glCopyColorTable.restype = None
glCopyColorTable.argtypes = [GLenum, GLenum, GLint, GLint, GLsizei]
glCopyColorTable.__doc__ = \
"""void glCopyColorTable(GLenum target, GLenum internalformat, GLint x, GLint y, GLsizei width)
/usr/include/GL/gl.h:1656"""
glGetColorTable = _libraries['/usr/lib/libglut.so'].glGetColorTable
glGetColorTable.restype = None
glGetColorTable.argtypes = [GLenum, GLenum, GLenum, POINTER(GLvoid)]
glGetColorTable.__doc__ = \
"""void glGetColorTable(GLenum target, GLenum format, GLenum type, GLvoid * table)
/usr/include/GL/gl.h:1659"""
glGetColorTableParameterfv = _libraries['/usr/lib/libglut.so'].glGetColorTableParameterfv
glGetColorTableParameterfv.restype = None
glGetColorTableParameterfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
glGetColorTableParameterfv.__doc__ = \
"""void glGetColorTableParameterfv(GLenum target, GLenum pname, GLfloat * params)
/usr/include/GL/gl.h:1662"""
glGetColorTableParameteriv = _libraries['/usr/lib/libglut.so'].glGetColorTableParameteriv
glGetColorTableParameteriv.restype = None
glGetColorTableParameteriv.argtypes = [GLenum, GLenum, POINTER(GLint)]
glGetColorTableParameteriv.__doc__ = \
"""void glGetColorTableParameteriv(GLenum target, GLenum pname, GLint * params)
/usr/include/GL/gl.h:1665"""
glBlendEquation = _libraries['/usr/lib/libglut.so'].glBlendEquation
glBlendEquation.restype = None
glBlendEquation.argtypes = [GLenum]
glBlendEquation.__doc__ = \
"""void glBlendEquation(GLenum mode)
/usr/include/GL/gl.h:1667"""
glBlendColor = _libraries['/usr/lib/libglut.so'].glBlendColor
glBlendColor.restype = None
glBlendColor.argtypes = [GLclampf, GLclampf, GLclampf, GLclampf]
glBlendColor.__doc__ = \
"""void glBlendColor(GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha)
/usr/include/GL/gl.h:1670"""
glHistogram = _libraries['/usr/lib/libglut.so'].glHistogram
glHistogram.restype = None
glHistogram.argtypes = [GLenum, GLsizei, GLenum, GLboolean]
glHistogram.__doc__ = \
"""void glHistogram(GLenum target, GLsizei width, GLenum internalformat, GLboolean sink)
/usr/include/GL/gl.h:1673"""
glResetHistogram = _libraries['/usr/lib/libglut.so'].glResetHistogram
glResetHistogram.restype = None
glResetHistogram.argtypes = [GLenum]
glResetHistogram.__doc__ = \
"""void glResetHistogram(GLenum target)
/usr/include/GL/gl.h:1675"""
glGetHistogram = _libraries['/usr/lib/libglut.so'].glGetHistogram
glGetHistogram.restype = None
glGetHistogram.argtypes = [GLenum, GLboolean, GLenum, GLenum, POINTER(GLvoid)]
glGetHistogram.__doc__ = \
"""void glGetHistogram(GLenum target, GLboolean reset, GLenum format, GLenum type, GLvoid * values)
/usr/include/GL/gl.h:1679"""
glGetHistogramParameterfv = _libraries['/usr/lib/libglut.so'].glGetHistogramParameterfv
glGetHistogramParameterfv.restype = None
glGetHistogramParameterfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
glGetHistogramParameterfv.__doc__ = \
"""void glGetHistogramParameterfv(GLenum target, GLenum pname, GLfloat * params)
/usr/include/GL/gl.h:1682"""
glGetHistogramParameteriv = _libraries['/usr/lib/libglut.so'].glGetHistogramParameteriv
glGetHistogramParameteriv.restype = None
glGetHistogramParameteriv.argtypes = [GLenum, GLenum, POINTER(GLint)]
glGetHistogramParameteriv.__doc__ = \
"""void glGetHistogramParameteriv(GLenum target, GLenum pname, GLint * params)
/usr/include/GL/gl.h:1685"""
glMinmax = _libraries['/usr/lib/libglut.so'].glMinmax
glMinmax.restype = None
glMinmax.argtypes = [GLenum, GLenum, GLboolean]
glMinmax.__doc__ = \
"""void glMinmax(GLenum target, GLenum internalformat, GLboolean sink)
/usr/include/GL/gl.h:1688"""
glResetMinmax = _libraries['/usr/lib/libglut.so'].glResetMinmax
glResetMinmax.restype = None
glResetMinmax.argtypes = [GLenum]
glResetMinmax.__doc__ = \
"""void glResetMinmax(GLenum target)
/usr/include/GL/gl.h:1690"""
glGetMinmax = _libraries['/usr/lib/libglut.so'].glGetMinmax
glGetMinmax.restype = None
glGetMinmax.argtypes = [GLenum, GLboolean, GLenum, GLenum, POINTER(GLvoid)]
glGetMinmax.__doc__ = \
"""void glGetMinmax(GLenum target, GLboolean reset, GLenum format, GLenum types, GLvoid * values)
/usr/include/GL/gl.h:1694"""
glGetMinmaxParameterfv = _libraries['/usr/lib/libglut.so'].glGetMinmaxParameterfv
glGetMinmaxParameterfv.restype = None
glGetMinmaxParameterfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
glGetMinmaxParameterfv.__doc__ = \
"""void glGetMinmaxParameterfv(GLenum target, GLenum pname, GLfloat * params)
/usr/include/GL/gl.h:1697"""
glGetMinmaxParameteriv = _libraries['/usr/lib/libglut.so'].glGetMinmaxParameteriv
glGetMinmaxParameteriv.restype = None
glGetMinmaxParameteriv.argtypes = [GLenum, GLenum, POINTER(GLint)]
glGetMinmaxParameteriv.__doc__ = \
"""void glGetMinmaxParameteriv(GLenum target, GLenum pname, GLint * params)
/usr/include/GL/gl.h:1700"""
glConvolutionFilter1D = _libraries['/usr/lib/libglut.so'].glConvolutionFilter1D
glConvolutionFilter1D.restype = None
glConvolutionFilter1D.argtypes = [GLenum, GLenum, GLsizei, GLenum, GLenum, POINTER(GLvoid)]
glConvolutionFilter1D.__doc__ = \
"""void glConvolutionFilter1D(GLenum target, GLenum internalformat, GLsizei width, GLenum format, GLenum type, unknown * image)
/usr/include/GL/gl.h:1704"""
glConvolutionFilter2D = _libraries['/usr/lib/libglut.so'].glConvolutionFilter2D
glConvolutionFilter2D.restype = None
glConvolutionFilter2D.argtypes = [GLenum, GLenum, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid)]
glConvolutionFilter2D.__doc__ = \
"""void glConvolutionFilter2D(GLenum target, GLenum internalformat, GLsizei width, GLsizei height, GLenum format, GLenum type, unknown * image)
/usr/include/GL/gl.h:1708"""
glConvolutionParameterf = _libraries['/usr/lib/libglut.so'].glConvolutionParameterf
glConvolutionParameterf.restype = None
glConvolutionParameterf.argtypes = [GLenum, GLenum, GLfloat]
glConvolutionParameterf.__doc__ = \
"""void glConvolutionParameterf(GLenum target, GLenum pname, GLfloat params)
/usr/include/GL/gl.h:1711"""
glConvolutionParameterfv = _libraries['/usr/lib/libglut.so'].glConvolutionParameterfv
glConvolutionParameterfv.restype = None
glConvolutionParameterfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
glConvolutionParameterfv.__doc__ = \
"""void glConvolutionParameterfv(GLenum target, GLenum pname, unknown * params)
/usr/include/GL/gl.h:1714"""
glConvolutionParameteri = _libraries['/usr/lib/libglut.so'].glConvolutionParameteri
glConvolutionParameteri.restype = None
glConvolutionParameteri.argtypes = [GLenum, GLenum, GLint]
glConvolutionParameteri.__doc__ = \
"""void glConvolutionParameteri(GLenum target, GLenum pname, GLint params)
/usr/include/GL/gl.h:1717"""
glConvolutionParameteriv = _libraries['/usr/lib/libglut.so'].glConvolutionParameteriv
glConvolutionParameteriv.restype = None
glConvolutionParameteriv.argtypes = [GLenum, GLenum, POINTER(GLint)]
glConvolutionParameteriv.__doc__ = \
"""void glConvolutionParameteriv(GLenum target, GLenum pname, unknown * params)
/usr/include/GL/gl.h:1720"""
glCopyConvolutionFilter1D = _libraries['/usr/lib/libglut.so'].glCopyConvolutionFilter1D
glCopyConvolutionFilter1D.restype = None
glCopyConvolutionFilter1D.argtypes = [GLenum, GLenum, GLint, GLint, GLsizei]
glCopyConvolutionFilter1D.__doc__ = \
"""void glCopyConvolutionFilter1D(GLenum target, GLenum internalformat, GLint x, GLint y, GLsizei width)
/usr/include/GL/gl.h:1723"""
glCopyConvolutionFilter2D = _libraries['/usr/lib/libglut.so'].glCopyConvolutionFilter2D
glCopyConvolutionFilter2D.restype = None
glCopyConvolutionFilter2D.argtypes = [GLenum, GLenum, GLint, GLint, GLsizei, GLsizei]
glCopyConvolutionFilter2D.__doc__ = \
"""void glCopyConvolutionFilter2D(GLenum target, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei height)
/usr/include/GL/gl.h:1727"""
glGetConvolutionFilter = _libraries['/usr/lib/libglut.so'].glGetConvolutionFilter
glGetConvolutionFilter.restype = None
glGetConvolutionFilter.argtypes = [GLenum, GLenum, GLenum, POINTER(GLvoid)]
glGetConvolutionFilter.__doc__ = \
"""void glGetConvolutionFilter(GLenum target, GLenum format, GLenum type, GLvoid * image)
/usr/include/GL/gl.h:1730"""
glGetConvolutionParameterfv = _libraries['/usr/lib/libglut.so'].glGetConvolutionParameterfv
glGetConvolutionParameterfv.restype = None
glGetConvolutionParameterfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
glGetConvolutionParameterfv.__doc__ = \
"""void glGetConvolutionParameterfv(GLenum target, GLenum pname, GLfloat * params)
/usr/include/GL/gl.h:1733"""
glGetConvolutionParameteriv = _libraries['/usr/lib/libglut.so'].glGetConvolutionParameteriv
glGetConvolutionParameteriv.restype = None
glGetConvolutionParameteriv.argtypes = [GLenum, GLenum, POINTER(GLint)]
glGetConvolutionParameteriv.__doc__ = \
"""void glGetConvolutionParameteriv(GLenum target, GLenum pname, GLint * params)
/usr/include/GL/gl.h:1736"""
glSeparableFilter2D = _libraries['/usr/lib/libglut.so'].glSeparableFilter2D
glSeparableFilter2D.restype = None
glSeparableFilter2D.argtypes = [GLenum, GLenum, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid), POINTER(GLvoid)]
glSeparableFilter2D.__doc__ = \
"""void glSeparableFilter2D(GLenum target, GLenum internalformat, GLsizei width, GLsizei height, GLenum format, GLenum type, unknown * row, unknown * column)
/usr/include/GL/gl.h:1740"""
glGetSeparableFilter = _libraries['/usr/lib/libglut.so'].glGetSeparableFilter
glGetSeparableFilter.restype = None
glGetSeparableFilter.argtypes = [GLenum, GLenum, GLenum, POINTER(GLvoid), POINTER(GLvoid), POINTER(GLvoid)]
glGetSeparableFilter.__doc__ = \
"""void glGetSeparableFilter(GLenum target, GLenum format, GLenum type, GLvoid * row, GLvoid * column, GLvoid * span)
/usr/include/GL/gl.h:1743"""
glActiveTexture = _libraries['/usr/lib/libglut.so'].glActiveTexture
glActiveTexture.restype = None
glActiveTexture.argtypes = [GLenum]
glActiveTexture.__doc__ = \
"""void glActiveTexture(GLenum texture)
/usr/include/GL/gl.h:1859"""
glClientActiveTexture = _libraries['/usr/lib/libglut.so'].glClientActiveTexture
glClientActiveTexture.restype = None
glClientActiveTexture.argtypes = [GLenum]
glClientActiveTexture.__doc__ = \
"""void glClientActiveTexture(GLenum texture)
/usr/include/GL/gl.h:1861"""
glCompressedTexImage1D = _libraries['/usr/lib/libglut.so'].glCompressedTexImage1D
glCompressedTexImage1D.restype = None
glCompressedTexImage1D.argtypes = [GLenum, GLint, GLenum, GLsizei, GLint, GLsizei, POINTER(GLvoid)]
glCompressedTexImage1D.__doc__ = \
"""void glCompressedTexImage1D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLint border, GLsizei imageSize, unknown * data)
/usr/include/GL/gl.h:1863"""
glCompressedTexImage2D = _libraries['/usr/lib/libglut.so'].glCompressedTexImage2D
glCompressedTexImage2D.restype = None
glCompressedTexImage2D.argtypes = [GLenum, GLint, GLenum, GLsizei, GLsizei, GLint, GLsizei, POINTER(GLvoid)]
glCompressedTexImage2D.__doc__ = \
"""void glCompressedTexImage2D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint border, GLsizei imageSize, unknown * data)
/usr/include/GL/gl.h:1865"""
glCompressedTexImage3D = _libraries['/usr/lib/libglut.so'].glCompressedTexImage3D
glCompressedTexImage3D.restype = None
glCompressedTexImage3D.argtypes = [GLenum, GLint, GLenum, GLsizei, GLsizei, GLsizei, GLint, GLsizei, POINTER(GLvoid)]
glCompressedTexImage3D.__doc__ = \
"""void glCompressedTexImage3D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLsizei imageSize, unknown * data)
/usr/include/GL/gl.h:1867"""
glCompressedTexSubImage1D = _libraries['/usr/lib/libglut.so'].glCompressedTexSubImage1D
glCompressedTexSubImage1D.restype = None
glCompressedTexSubImage1D.argtypes = [GLenum, GLint, GLint, GLsizei, GLenum, GLsizei, POINTER(GLvoid)]
glCompressedTexSubImage1D.__doc__ = \
"""void glCompressedTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei imageSize, unknown * data)
/usr/include/GL/gl.h:1869"""
glCompressedTexSubImage2D = _libraries['/usr/lib/libglut.so'].glCompressedTexSubImage2D
glCompressedTexSubImage2D.restype = None
glCompressedTexSubImage2D.argtypes = [GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLsizei, POINTER(GLvoid)]
glCompressedTexSubImage2D.__doc__ = \
"""void glCompressedTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, unknown * data)
/usr/include/GL/gl.h:1871"""
glCompressedTexSubImage3D = _libraries['/usr/lib/libglut.so'].glCompressedTexSubImage3D
glCompressedTexSubImage3D.restype = None
glCompressedTexSubImage3D.argtypes = [GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLsizei, POINTER(GLvoid)]
glCompressedTexSubImage3D.__doc__ = \
"""void glCompressedTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, unknown * data)
/usr/include/GL/gl.h:1873"""
glGetCompressedTexImage = _libraries['/usr/lib/libglut.so'].glGetCompressedTexImage
glGetCompressedTexImage.restype = None
glGetCompressedTexImage.argtypes = [GLenum, GLint, POINTER(GLvoid)]
glGetCompressedTexImage.__doc__ = \
"""void glGetCompressedTexImage(GLenum target, GLint lod, GLvoid * img)
/usr/include/GL/gl.h:1875"""
glMultiTexCoord1d = _libraries['/usr/lib/libglut.so'].glMultiTexCoord1d
glMultiTexCoord1d.restype = None
glMultiTexCoord1d.argtypes = [GLenum, GLdouble]
glMultiTexCoord1d.__doc__ = \
"""void glMultiTexCoord1d(GLenum target, GLdouble s)
/usr/include/GL/gl.h:1877"""
glMultiTexCoord1dv = _libraries['/usr/lib/libglut.so'].glMultiTexCoord1dv
glMultiTexCoord1dv.restype = None
glMultiTexCoord1dv.argtypes = [GLenum, POINTER(GLdouble)]
glMultiTexCoord1dv.__doc__ = \
"""void glMultiTexCoord1dv(GLenum target, unknown * v)
/usr/include/GL/gl.h:1879"""
glMultiTexCoord1f = _libraries['/usr/lib/libglut.so'].glMultiTexCoord1f
glMultiTexCoord1f.restype = None
glMultiTexCoord1f.argtypes = [GLenum, GLfloat]
glMultiTexCoord1f.__doc__ = \
"""void glMultiTexCoord1f(GLenum target, GLfloat s)
/usr/include/GL/gl.h:1881"""
glMultiTexCoord1fv = _libraries['/usr/lib/libglut.so'].glMultiTexCoord1fv
glMultiTexCoord1fv.restype = None
glMultiTexCoord1fv.argtypes = [GLenum, POINTER(GLfloat)]
glMultiTexCoord1fv.__doc__ = \
"""void glMultiTexCoord1fv(GLenum target, unknown * v)
/usr/include/GL/gl.h:1883"""
glMultiTexCoord1i = _libraries['/usr/lib/libglut.so'].glMultiTexCoord1i
glMultiTexCoord1i.restype = None
glMultiTexCoord1i.argtypes = [GLenum, GLint]
glMultiTexCoord1i.__doc__ = \
"""void glMultiTexCoord1i(GLenum target, GLint s)
/usr/include/GL/gl.h:1885"""
glMultiTexCoord1iv = _libraries['/usr/lib/libglut.so'].glMultiTexCoord1iv
glMultiTexCoord1iv.restype = None
glMultiTexCoord1iv.argtypes = [GLenum, POINTER(GLint)]
glMultiTexCoord1iv.__doc__ = \
"""void glMultiTexCoord1iv(GLenum target, unknown * v)
/usr/include/GL/gl.h:1887"""
glMultiTexCoord1s = _libraries['/usr/lib/libglut.so'].glMultiTexCoord1s
glMultiTexCoord1s.restype = None
glMultiTexCoord1s.argtypes = [GLenum, GLshort]
glMultiTexCoord1s.__doc__ = \
"""void glMultiTexCoord1s(GLenum target, GLshort s)
/usr/include/GL/gl.h:1889"""
glMultiTexCoord1sv = _libraries['/usr/lib/libglut.so'].glMultiTexCoord1sv
glMultiTexCoord1sv.restype = None
glMultiTexCoord1sv.argtypes = [GLenum, POINTER(GLshort)]
glMultiTexCoord1sv.__doc__ = \
"""void glMultiTexCoord1sv(GLenum target, unknown * v)
/usr/include/GL/gl.h:1891"""
glMultiTexCoord2d = _libraries['/usr/lib/libglut.so'].glMultiTexCoord2d
glMultiTexCoord2d.restype = None
glMultiTexCoord2d.argtypes = [GLenum, GLdouble, GLdouble]
glMultiTexCoord2d.__doc__ = \
"""void glMultiTexCoord2d(GLenum target, GLdouble s, GLdouble t)
/usr/include/GL/gl.h:1893"""
glMultiTexCoord2dv = _libraries['/usr/lib/libglut.so'].glMultiTexCoord2dv
glMultiTexCoord2dv.restype = None
glMultiTexCoord2dv.argtypes = [GLenum, POINTER(GLdouble)]
glMultiTexCoord2dv.__doc__ = \
"""void glMultiTexCoord2dv(GLenum target, unknown * v)
/usr/include/GL/gl.h:1895"""
glMultiTexCoord2f = _libraries['/usr/lib/libglut.so'].glMultiTexCoord2f
glMultiTexCoord2f.restype = None
glMultiTexCoord2f.argtypes = [GLenum, GLfloat, GLfloat]
glMultiTexCoord2f.__doc__ = \
"""void glMultiTexCoord2f(GLenum target, GLfloat s, GLfloat t)
/usr/include/GL/gl.h:1897"""
glMultiTexCoord2fv = _libraries['/usr/lib/libglut.so'].glMultiTexCoord2fv
glMultiTexCoord2fv.restype = None
glMultiTexCoord2fv.argtypes = [GLenum, POINTER(GLfloat)]
glMultiTexCoord2fv.__doc__ = \
"""void glMultiTexCoord2fv(GLenum target, unknown * v)
/usr/include/GL/gl.h:1899"""
glMultiTexCoord2i = _libraries['/usr/lib/libglut.so'].glMultiTexCoord2i
glMultiTexCoord2i.restype = None
glMultiTexCoord2i.argtypes = [GLenum, GLint, GLint]
glMultiTexCoord2i.__doc__ = \
"""void glMultiTexCoord2i(GLenum target, GLint s, GLint t)
/usr/include/GL/gl.h:1901"""
glMultiTexCoord2iv = _libraries['/usr/lib/libglut.so'].glMultiTexCoord2iv
glMultiTexCoord2iv.restype = None
glMultiTexCoord2iv.argtypes = [GLenum, POINTER(GLint)]
glMultiTexCoord2iv.__doc__ = \
"""void glMultiTexCoord2iv(GLenum target, unknown * v)
/usr/include/GL/gl.h:1903"""
glMultiTexCoord2s = _libraries['/usr/lib/libglut.so'].glMultiTexCoord2s
glMultiTexCoord2s.restype = None
glMultiTexCoord2s.argtypes = [GLenum, GLshort, GLshort]
glMultiTexCoord2s.__doc__ = \
"""void glMultiTexCoord2s(GLenum target, GLshort s, GLshort t)
/usr/include/GL/gl.h:1905"""
glMultiTexCoord2sv = _libraries['/usr/lib/libglut.so'].glMultiTexCoord2sv
glMultiTexCoord2sv.restype = None
glMultiTexCoord2sv.argtypes = [GLenum, POINTER(GLshort)]
glMultiTexCoord2sv.__doc__ = \
"""void glMultiTexCoord2sv(GLenum target, unknown * v)
/usr/include/GL/gl.h:1907"""
glMultiTexCoord3d = _libraries['/usr/lib/libglut.so'].glMultiTexCoord3d
glMultiTexCoord3d.restype = None
glMultiTexCoord3d.argtypes = [GLenum, GLdouble, GLdouble, GLdouble]
glMultiTexCoord3d.__doc__ = \
"""void glMultiTexCoord3d(GLenum target, GLdouble s, GLdouble t, GLdouble r)
/usr/include/GL/gl.h:1909"""
glMultiTexCoord3dv = _libraries['/usr/lib/libglut.so'].glMultiTexCoord3dv
glMultiTexCoord3dv.restype = None
glMultiTexCoord3dv.argtypes = [GLenum, POINTER(GLdouble)]
glMultiTexCoord3dv.__doc__ = \
"""void glMultiTexCoord3dv(GLenum target, unknown * v)
/usr/include/GL/gl.h:1911"""
glMultiTexCoord3f = _libraries['/usr/lib/libglut.so'].glMultiTexCoord3f
glMultiTexCoord3f.restype = None
glMultiTexCoord3f.argtypes = [GLenum, GLfloat, GLfloat, GLfloat]
glMultiTexCoord3f.__doc__ = \
"""void glMultiTexCoord3f(GLenum target, GLfloat s, GLfloat t, GLfloat r)
/usr/include/GL/gl.h:1913"""
glMultiTexCoord3fv = _libraries['/usr/lib/libglut.so'].glMultiTexCoord3fv
glMultiTexCoord3fv.restype = None
glMultiTexCoord3fv.argtypes = [GLenum, POINTER(GLfloat)]
glMultiTexCoord3fv.__doc__ = \
"""void glMultiTexCoord3fv(GLenum target, unknown * v)
/usr/include/GL/gl.h:1915"""
glMultiTexCoord3i = _libraries['/usr/lib/libglut.so'].glMultiTexCoord3i
glMultiTexCoord3i.restype = None
glMultiTexCoord3i.argtypes = [GLenum, GLint, GLint, GLint]
glMultiTexCoord3i.__doc__ = \
"""void glMultiTexCoord3i(GLenum target, GLint s, GLint t, GLint r)
/usr/include/GL/gl.h:1917"""
glMultiTexCoord3iv = _libraries['/usr/lib/libglut.so'].glMultiTexCoord3iv
glMultiTexCoord3iv.restype = None
glMultiTexCoord3iv.argtypes = [GLenum, POINTER(GLint)]
glMultiTexCoord3iv.__doc__ = \
"""void glMultiTexCoord3iv(GLenum target, unknown * v)
/usr/include/GL/gl.h:1919"""
glMultiTexCoord3s = _libraries['/usr/lib/libglut.so'].glMultiTexCoord3s
glMultiTexCoord3s.restype = None
glMultiTexCoord3s.argtypes = [GLenum, GLshort, GLshort, GLshort]
glMultiTexCoord3s.__doc__ = \
"""void glMultiTexCoord3s(GLenum target, GLshort s, GLshort t, GLshort r)
/usr/include/GL/gl.h:1921"""
glMultiTexCoord3sv = _libraries['/usr/lib/libglut.so'].glMultiTexCoord3sv
glMultiTexCoord3sv.restype = None
glMultiTexCoord3sv.argtypes = [GLenum, POINTER(GLshort)]
glMultiTexCoord3sv.__doc__ = \
"""void glMultiTexCoord3sv(GLenum target, unknown * v)
/usr/include/GL/gl.h:1923"""
glMultiTexCoord4d = _libraries['/usr/lib/libglut.so'].glMultiTexCoord4d
glMultiTexCoord4d.restype = None
glMultiTexCoord4d.argtypes = [GLenum, GLdouble, GLdouble, GLdouble, GLdouble]
glMultiTexCoord4d.__doc__ = \
"""void glMultiTexCoord4d(GLenum target, GLdouble s, GLdouble t, GLdouble r, GLdouble q)
/usr/include/GL/gl.h:1925"""
glMultiTexCoord4dv = _libraries['/usr/lib/libglut.so'].glMultiTexCoord4dv
glMultiTexCoord4dv.restype = None
glMultiTexCoord4dv.argtypes = [GLenum, POINTER(GLdouble)]
glMultiTexCoord4dv.__doc__ = \
"""void glMultiTexCoord4dv(GLenum target, unknown * v)
/usr/include/GL/gl.h:1927"""
glMultiTexCoord4f = _libraries['/usr/lib/libglut.so'].glMultiTexCoord4f
glMultiTexCoord4f.restype = None
glMultiTexCoord4f.argtypes = [GLenum, GLfloat, GLfloat, GLfloat, GLfloat]
glMultiTexCoord4f.__doc__ = \
"""void glMultiTexCoord4f(GLenum target, GLfloat s, GLfloat t, GLfloat r, GLfloat q)
/usr/include/GL/gl.h:1929"""
glMultiTexCoord4fv = _libraries['/usr/lib/libglut.so'].glMultiTexCoord4fv
glMultiTexCoord4fv.restype = None
glMultiTexCoord4fv.argtypes = [GLenum, POINTER(GLfloat)]
glMultiTexCoord4fv.__doc__ = \
"""void glMultiTexCoord4fv(GLenum target, unknown * v)
/usr/include/GL/gl.h:1931"""
glMultiTexCoord4i = _libraries['/usr/lib/libglut.so'].glMultiTexCoord4i
glMultiTexCoord4i.restype = None
glMultiTexCoord4i.argtypes = [GLenum, GLint, GLint, GLint, GLint]
glMultiTexCoord4i.__doc__ = \
"""void glMultiTexCoord4i(GLenum target, GLint s, GLint t, GLint r, GLint q)
/usr/include/GL/gl.h:1933"""
glMultiTexCoord4iv = _libraries['/usr/lib/libglut.so'].glMultiTexCoord4iv
glMultiTexCoord4iv.restype = None
glMultiTexCoord4iv.argtypes = [GLenum, POINTER(GLint)]
glMultiTexCoord4iv.__doc__ = \
"""void glMultiTexCoord4iv(GLenum target, unknown * v)
/usr/include/GL/gl.h:1935"""
glMultiTexCoord4s = _libraries['/usr/lib/libglut.so'].glMultiTexCoord4s
glMultiTexCoord4s.restype = None
glMultiTexCoord4s.argtypes = [GLenum, GLshort, GLshort, GLshort, GLshort]
glMultiTexCoord4s.__doc__ = \
"""void glMultiTexCoord4s(GLenum target, GLshort s, GLshort t, GLshort r, GLshort q)
/usr/include/GL/gl.h:1937"""
glMultiTexCoord4sv = _libraries['/usr/lib/libglut.so'].glMultiTexCoord4sv
glMultiTexCoord4sv.restype = None
glMultiTexCoord4sv.argtypes = [GLenum, POINTER(GLshort)]
glMultiTexCoord4sv.__doc__ = \
"""void glMultiTexCoord4sv(GLenum target, unknown * v)
/usr/include/GL/gl.h:1939"""
glLoadTransposeMatrixd = _libraries['/usr/lib/libglut.so'].glLoadTransposeMatrixd
glLoadTransposeMatrixd.restype = None
glLoadTransposeMatrixd.argtypes = [POINTER(GLdouble)]
glLoadTransposeMatrixd.__doc__ = \
"""void glLoadTransposeMatrixd(unknown * m)
/usr/include/GL/gl.h:1942"""
glLoadTransposeMatrixf = _libraries['/usr/lib/libglut.so'].glLoadTransposeMatrixf
glLoadTransposeMatrixf.restype = None
glLoadTransposeMatrixf.argtypes = [POINTER(GLfloat)]
glLoadTransposeMatrixf.__doc__ = \
"""void glLoadTransposeMatrixf(unknown * m)
/usr/include/GL/gl.h:1944"""
glMultTransposeMatrixd = _libraries['/usr/lib/libglut.so'].glMultTransposeMatrixd
glMultTransposeMatrixd.restype = None
glMultTransposeMatrixd.argtypes = [POINTER(GLdouble)]
glMultTransposeMatrixd.__doc__ = \
"""void glMultTransposeMatrixd(unknown * m)
/usr/include/GL/gl.h:1946"""
glMultTransposeMatrixf = _libraries['/usr/lib/libglut.so'].glMultTransposeMatrixf
glMultTransposeMatrixf.restype = None
glMultTransposeMatrixf.argtypes = [POINTER(GLfloat)]
glMultTransposeMatrixf.__doc__ = \
"""void glMultTransposeMatrixf(unknown * m)
/usr/include/GL/gl.h:1948"""
glSampleCoverage = _libraries['/usr/lib/libglut.so'].glSampleCoverage
glSampleCoverage.restype = None
glSampleCoverage.argtypes = [GLclampf, GLboolean]
glSampleCoverage.__doc__ = \
"""void glSampleCoverage(GLclampf value, GLboolean invert)
/usr/include/GL/gl.h:1950"""
glActiveTextureARB = _libraries['/usr/lib/libglut.so'].glActiveTextureARB
glActiveTextureARB.restype = None
glActiveTextureARB.argtypes = [GLenum]
glActiveTextureARB.__doc__ = \
"""void glActiveTextureARB(GLenum texture)
/usr/include/GL/gl.h:2007"""
glClientActiveTextureARB = _libraries['/usr/lib/libglut.so'].glClientActiveTextureARB
glClientActiveTextureARB.restype = None
glClientActiveTextureARB.argtypes = [GLenum]
glClientActiveTextureARB.__doc__ = \
"""void glClientActiveTextureARB(GLenum texture)
/usr/include/GL/gl.h:2008"""
glMultiTexCoord1dARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord1dARB
glMultiTexCoord1dARB.restype = None
glMultiTexCoord1dARB.argtypes = [GLenum, GLdouble]
glMultiTexCoord1dARB.__doc__ = \
"""void glMultiTexCoord1dARB(GLenum target, GLdouble s)
/usr/include/GL/gl.h:2009"""
glMultiTexCoord1dvARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord1dvARB
glMultiTexCoord1dvARB.restype = None
glMultiTexCoord1dvARB.argtypes = [GLenum, POINTER(GLdouble)]
glMultiTexCoord1dvARB.__doc__ = \
"""void glMultiTexCoord1dvARB(GLenum target, unknown * v)
/usr/include/GL/gl.h:2010"""
glMultiTexCoord1fARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord1fARB
glMultiTexCoord1fARB.restype = None
glMultiTexCoord1fARB.argtypes = [GLenum, GLfloat]
glMultiTexCoord1fARB.__doc__ = \
"""void glMultiTexCoord1fARB(GLenum target, GLfloat s)
/usr/include/GL/gl.h:2011"""
glMultiTexCoord1fvARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord1fvARB
glMultiTexCoord1fvARB.restype = None
glMultiTexCoord1fvARB.argtypes = [GLenum, POINTER(GLfloat)]
glMultiTexCoord1fvARB.__doc__ = \
"""void glMultiTexCoord1fvARB(GLenum target, unknown * v)
/usr/include/GL/gl.h:2012"""
glMultiTexCoord1iARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord1iARB
glMultiTexCoord1iARB.restype = None
glMultiTexCoord1iARB.argtypes = [GLenum, GLint]
glMultiTexCoord1iARB.__doc__ = \
"""void glMultiTexCoord1iARB(GLenum target, GLint s)
/usr/include/GL/gl.h:2013"""
glMultiTexCoord1ivARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord1ivARB
glMultiTexCoord1ivARB.restype = None
glMultiTexCoord1ivARB.argtypes = [GLenum, POINTER(GLint)]
glMultiTexCoord1ivARB.__doc__ = \
"""void glMultiTexCoord1ivARB(GLenum target, unknown * v)
/usr/include/GL/gl.h:2014"""
glMultiTexCoord1sARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord1sARB
glMultiTexCoord1sARB.restype = None
glMultiTexCoord1sARB.argtypes = [GLenum, GLshort]
glMultiTexCoord1sARB.__doc__ = \
"""void glMultiTexCoord1sARB(GLenum target, GLshort s)
/usr/include/GL/gl.h:2015"""
glMultiTexCoord1svARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord1svARB
glMultiTexCoord1svARB.restype = None
glMultiTexCoord1svARB.argtypes = [GLenum, POINTER(GLshort)]
glMultiTexCoord1svARB.__doc__ = \
"""void glMultiTexCoord1svARB(GLenum target, unknown * v)
/usr/include/GL/gl.h:2016"""
glMultiTexCoord2dARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord2dARB
glMultiTexCoord2dARB.restype = None
glMultiTexCoord2dARB.argtypes = [GLenum, GLdouble, GLdouble]
glMultiTexCoord2dARB.__doc__ = \
"""void glMultiTexCoord2dARB(GLenum target, GLdouble s, GLdouble t)
/usr/include/GL/gl.h:2017"""
glMultiTexCoord2dvARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord2dvARB
glMultiTexCoord2dvARB.restype = None
glMultiTexCoord2dvARB.argtypes = [GLenum, POINTER(GLdouble)]
glMultiTexCoord2dvARB.__doc__ = \
"""void glMultiTexCoord2dvARB(GLenum target, unknown * v)
/usr/include/GL/gl.h:2018"""
glMultiTexCoord2fARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord2fARB
glMultiTexCoord2fARB.restype = None
glMultiTexCoord2fARB.argtypes = [GLenum, GLfloat, GLfloat]
glMultiTexCoord2fARB.__doc__ = \
"""void glMultiTexCoord2fARB(GLenum target, GLfloat s, GLfloat t)
/usr/include/GL/gl.h:2019"""
glMultiTexCoord2fvARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord2fvARB
glMultiTexCoord2fvARB.restype = None
glMultiTexCoord2fvARB.argtypes = [GLenum, POINTER(GLfloat)]
glMultiTexCoord2fvARB.__doc__ = \
"""void glMultiTexCoord2fvARB(GLenum target, unknown * v)
/usr/include/GL/gl.h:2020"""
glMultiTexCoord2iARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord2iARB
glMultiTexCoord2iARB.restype = None
glMultiTexCoord2iARB.argtypes = [GLenum, GLint, GLint]
glMultiTexCoord2iARB.__doc__ = \
"""void glMultiTexCoord2iARB(GLenum target, GLint s, GLint t)
/usr/include/GL/gl.h:2021"""
glMultiTexCoord2ivARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord2ivARB
glMultiTexCoord2ivARB.restype = None
glMultiTexCoord2ivARB.argtypes = [GLenum, POINTER(GLint)]
glMultiTexCoord2ivARB.__doc__ = \
"""void glMultiTexCoord2ivARB(GLenum target, unknown * v)
/usr/include/GL/gl.h:2022"""
glMultiTexCoord2sARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord2sARB
glMultiTexCoord2sARB.restype = None
glMultiTexCoord2sARB.argtypes = [GLenum, GLshort, GLshort]
glMultiTexCoord2sARB.__doc__ = \
"""void glMultiTexCoord2sARB(GLenum target, GLshort s, GLshort t)
/usr/include/GL/gl.h:2023"""
glMultiTexCoord2svARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord2svARB
glMultiTexCoord2svARB.restype = None
glMultiTexCoord2svARB.argtypes = [GLenum, POINTER(GLshort)]
glMultiTexCoord2svARB.__doc__ = \
"""void glMultiTexCoord2svARB(GLenum target, unknown * v)
/usr/include/GL/gl.h:2024"""
glMultiTexCoord3dARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord3dARB
glMultiTexCoord3dARB.restype = None
glMultiTexCoord3dARB.argtypes = [GLenum, GLdouble, GLdouble, GLdouble]
glMultiTexCoord3dARB.__doc__ = \
"""void glMultiTexCoord3dARB(GLenum target, GLdouble s, GLdouble t, GLdouble r)
/usr/include/GL/gl.h:2025"""
glMultiTexCoord3dvARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord3dvARB
glMultiTexCoord3dvARB.restype = None
glMultiTexCoord3dvARB.argtypes = [GLenum, POINTER(GLdouble)]
glMultiTexCoord3dvARB.__doc__ = \
"""void glMultiTexCoord3dvARB(GLenum target, unknown * v)
/usr/include/GL/gl.h:2026"""
glMultiTexCoord3fARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord3fARB
glMultiTexCoord3fARB.restype = None
glMultiTexCoord3fARB.argtypes = [GLenum, GLfloat, GLfloat, GLfloat]
glMultiTexCoord3fARB.__doc__ = \
"""void glMultiTexCoord3fARB(GLenum target, GLfloat s, GLfloat t, GLfloat r)
/usr/include/GL/gl.h:2027"""
glMultiTexCoord3fvARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord3fvARB
glMultiTexCoord3fvARB.restype = None
glMultiTexCoord3fvARB.argtypes = [GLenum, POINTER(GLfloat)]
glMultiTexCoord3fvARB.__doc__ = \
"""void glMultiTexCoord3fvARB(GLenum target, unknown * v)
/usr/include/GL/gl.h:2028"""
glMultiTexCoord3iARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord3iARB
glMultiTexCoord3iARB.restype = None
glMultiTexCoord3iARB.argtypes = [GLenum, GLint, GLint, GLint]
glMultiTexCoord3iARB.__doc__ = \
"""void glMultiTexCoord3iARB(GLenum target, GLint s, GLint t, GLint r)
/usr/include/GL/gl.h:2029"""
glMultiTexCoord3ivARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord3ivARB
glMultiTexCoord3ivARB.restype = None
glMultiTexCoord3ivARB.argtypes = [GLenum, POINTER(GLint)]
glMultiTexCoord3ivARB.__doc__ = \
"""void glMultiTexCoord3ivARB(GLenum target, unknown * v)
/usr/include/GL/gl.h:2030"""
glMultiTexCoord3sARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord3sARB
glMultiTexCoord3sARB.restype = None
glMultiTexCoord3sARB.argtypes = [GLenum, GLshort, GLshort, GLshort]
glMultiTexCoord3sARB.__doc__ = \
"""void glMultiTexCoord3sARB(GLenum target, GLshort s, GLshort t, GLshort r)
/usr/include/GL/gl.h:2031"""
glMultiTexCoord3svARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord3svARB
glMultiTexCoord3svARB.restype = None
glMultiTexCoord3svARB.argtypes = [GLenum, POINTER(GLshort)]
glMultiTexCoord3svARB.__doc__ = \
"""void glMultiTexCoord3svARB(GLenum target, unknown * v)
/usr/include/GL/gl.h:2032"""
glMultiTexCoord4dARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord4dARB
glMultiTexCoord4dARB.restype = None
glMultiTexCoord4dARB.argtypes = [GLenum, GLdouble, GLdouble, GLdouble, GLdouble]
glMultiTexCoord4dARB.__doc__ = \
"""void glMultiTexCoord4dARB(GLenum target, GLdouble s, GLdouble t, GLdouble r, GLdouble q)
/usr/include/GL/gl.h:2033"""
glMultiTexCoord4dvARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord4dvARB
glMultiTexCoord4dvARB.restype = None
glMultiTexCoord4dvARB.argtypes = [GLenum, POINTER(GLdouble)]
glMultiTexCoord4dvARB.__doc__ = \
"""void glMultiTexCoord4dvARB(GLenum target, unknown * v)
/usr/include/GL/gl.h:2034"""
glMultiTexCoord4fARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord4fARB
glMultiTexCoord4fARB.restype = None
glMultiTexCoord4fARB.argtypes = [GLenum, GLfloat, GLfloat, GLfloat, GLfloat]
glMultiTexCoord4fARB.__doc__ = \
"""void glMultiTexCoord4fARB(GLenum target, GLfloat s, GLfloat t, GLfloat r, GLfloat q)
/usr/include/GL/gl.h:2035"""
glMultiTexCoord4fvARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord4fvARB
glMultiTexCoord4fvARB.restype = None
glMultiTexCoord4fvARB.argtypes = [GLenum, POINTER(GLfloat)]
glMultiTexCoord4fvARB.__doc__ = \
"""void glMultiTexCoord4fvARB(GLenum target, unknown * v)
/usr/include/GL/gl.h:2036"""
glMultiTexCoord4iARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord4iARB
glMultiTexCoord4iARB.restype = None
glMultiTexCoord4iARB.argtypes = [GLenum, GLint, GLint, GLint, GLint]
glMultiTexCoord4iARB.__doc__ = \
"""void glMultiTexCoord4iARB(GLenum target, GLint s, GLint t, GLint r, GLint q)
/usr/include/GL/gl.h:2037"""
glMultiTexCoord4ivARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord4ivARB
glMultiTexCoord4ivARB.restype = None
glMultiTexCoord4ivARB.argtypes = [GLenum, POINTER(GLint)]
glMultiTexCoord4ivARB.__doc__ = \
"""void glMultiTexCoord4ivARB(GLenum target, unknown * v)
/usr/include/GL/gl.h:2038"""
glMultiTexCoord4sARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord4sARB
glMultiTexCoord4sARB.restype = None
glMultiTexCoord4sARB.argtypes = [GLenum, GLshort, GLshort, GLshort, GLshort]
glMultiTexCoord4sARB.__doc__ = \
"""void glMultiTexCoord4sARB(GLenum target, GLshort s, GLshort t, GLshort r, GLshort q)
/usr/include/GL/gl.h:2039"""
glMultiTexCoord4svARB = _libraries['/usr/lib/libglut.so'].glMultiTexCoord4svARB
glMultiTexCoord4svARB.restype = None
glMultiTexCoord4svARB.argtypes = [GLenum, POINTER(GLshort)]
glMultiTexCoord4svARB.__doc__ = \
"""void glMultiTexCoord4svARB(GLenum target, unknown * v)
/usr/include/GL/gl.h:2040"""
GLprogramcallbackMESA = CFUNCTYPE(None, GLenum, POINTER(GLvoid))
GLeglImageOES = c_void_p
GLchar = c_char
ptrdiff_t = c_long
GLintptr = ptrdiff_t
GLsizeiptr = ptrdiff_t
GLintptrARB = ptrdiff_t
GLsizeiptrARB = ptrdiff_t
GLcharARB = c_char
GLhandleARB = c_uint
GLhalfARB = c_ushort
GLhalfNV = c_ushort
int64_t = c_int64
GLint64EXT = int64_t
uint64_t = c_uint64
GLuint64EXT = uint64_t
GLint64 = int64_t
GLuint64 = uint64_t
class __GLsync(Structure):
    pass
GLsync = POINTER(__GLsync)
GLvdpauSurfaceNV = GLintptr
class GLUnurbs(Structure):
    pass
GLUnurbs._fields_ = [
]
class GLUquadric(Structure):
    pass
GLUquadric._fields_ = [
]
class GLUtesselator(Structure):
    pass
GLUtesselator._fields_ = [
]
GLUnurbsObj = GLUnurbs
GLUquadricObj = GLUquadric
GLUtesselatorObj = GLUtesselator
GLUtriangulatorObj = GLUtesselator
GL_ABGR_EXT = 32768L # Variable c_uint '32768u'
GL_ACCUM = 256L # Variable c_uint '256u'
GL_ACCUM_ALPHA_BITS = 3419L # Variable c_uint '3419u'
GL_ACCUM_BLUE_BITS = 3418L # Variable c_uint '3418u'
GL_ACCUM_BUFFER_BIT = 512L # Variable c_uint '512u'
GL_ACCUM_CLEAR_VALUE = 2944L # Variable c_uint '2944u'
GL_ACCUM_GREEN_BITS = 3417L # Variable c_uint '3417u'
GL_ACCUM_RED_BITS = 3416L # Variable c_uint '3416u'
GL_ACTIVE_ATTRIBUTE_MAX_LENGTH = 35722L # Variable c_uint '35722u'
GL_ACTIVE_ATTRIBUTES = 35721L # Variable c_uint '35721u'
GL_ACTIVE_PROGRAM = 33369L # Variable c_uint '33369u'
GL_ACTIVE_PROGRAM_EXT = 35725L # Variable c_uint '35725u'
GL_ACTIVE_STENCIL_FACE_EXT = 35089L # Variable c_uint '35089u'
GL_ACTIVE_SUBROUTINE_MAX_LENGTH = 36424L # Variable c_uint '36424u'
GL_ACTIVE_SUBROUTINES = 36325L # Variable c_uint '36325u'
GL_ACTIVE_SUBROUTINE_UNIFORM_LOCATIONS = 36423L # Variable c_uint '36423u'
GL_ACTIVE_SUBROUTINE_UNIFORM_MAX_LENGTH = 36425L # Variable c_uint '36425u'
GL_ACTIVE_SUBROUTINE_UNIFORMS = 36326L # Variable c_uint '36326u'
GL_ACTIVE_TEXTURE = 34016L # Variable c_uint '34016u'
GL_ACTIVE_TEXTURE_ARB = 34016L # Variable c_uint '34016u'
GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH = 35381L # Variable c_uint '35381u'
GL_ACTIVE_UNIFORM_BLOCKS = 35382L # Variable c_uint '35382u'
GL_ACTIVE_UNIFORM_MAX_LENGTH = 35719L # Variable c_uint '35719u'
GL_ACTIVE_UNIFORMS = 35718L # Variable c_uint '35718u'
GL_ACTIVE_VARYING_MAX_LENGTH_NV = 35970L # Variable c_uint '35970u'
GL_ACTIVE_VARYINGS_NV = 35969L # Variable c_uint '35969u'
GL_ACTIVE_VERTEX_UNITS_ARB = 34469L # Variable c_uint '34469u'
GL_ADD = 260L # Variable c_uint '260u'
GL_ADD_ATI = 35171L # Variable c_uint '35171u'
GL_ADD_SIGNED = 34164L # Variable c_uint '34164u'
GL_ADD_SIGNED_ARB = 34164L # Variable c_uint '34164u'
GL_ADD_SIGNED_EXT = 34164L # Variable c_uint '34164u'
GL_ALIASED_LINE_WIDTH_RANGE = 33902L # Variable c_uint '33902u'
GL_ALIASED_POINT_SIZE_RANGE = 33901L # Variable c_uint '33901u'
GL_ALL_ATTRIB_BITS = 1048575L # Variable c_uint '1048575u'
GL_ALL_BARRIER_BITS_EXT = 4294967295L # Variable c_uint '4294967295u'
GL_ALL_CLIENT_ATTRIB_BITS = 4294967295L # Variable c_uint '4294967295u'
GL_ALL_COMPLETED_NV = 34034L # Variable c_uint '34034u'
GL_ALLOW_DRAW_FRG_HINT_PGI = 107024L # Variable c_uint '107024u'
GL_ALLOW_DRAW_MEM_HINT_PGI = 107025L # Variable c_uint '107025u'
GL_ALLOW_DRAW_OBJ_HINT_PGI = 107022L # Variable c_uint '107022u'
GL_ALLOW_DRAW_WIN_HINT_PGI = 107023L # Variable c_uint '107023u'
GL_ALL_SHADER_BITS = 4294967295L # Variable c_uint '4294967295u'
GL_ALPHA = 6406L # Variable c_uint '6406u'
GL_ALPHA12 = 32829L # Variable c_uint '32829u'
GL_ALPHA12_EXT = 32829L # Variable c_uint '32829u'
GL_ALPHA16 = 32830L # Variable c_uint '32830u'
GL_ALPHA16_EXT = 32830L # Variable c_uint '32830u'
GL_ALPHA16F_ARB = 34844L # Variable c_uint '34844u'
GL_ALPHA16I_EXT = 36234L # Variable c_uint '36234u'
GL_ALPHA16_SNORM = 36888L # Variable c_uint '36888u'
GL_ALPHA16UI_EXT = 36216L # Variable c_uint '36216u'
GL_ALPHA32F_ARB = 34838L # Variable c_uint '34838u'
GL_ALPHA32I_EXT = 36228L # Variable c_uint '36228u'
GL_ALPHA32UI_EXT = 36210L # Variable c_uint '36210u'
GL_ALPHA4 = 32827L # Variable c_uint '32827u'
GL_ALPHA4_EXT = 32827L # Variable c_uint '32827u'
GL_ALPHA8 = 32828L # Variable c_uint '32828u'
GL_ALPHA8_EXT = 32828L # Variable c_uint '32828u'
GL_ALPHA8I_EXT = 36240L # Variable c_uint '36240u'
GL_ALPHA8_SNORM = 36884L # Variable c_uint '36884u'
GL_ALPHA8UI_EXT = 36222L # Variable c_uint '36222u'
GL_ALPHA_BIAS = 3357L # Variable c_uint '3357u'
GL_ALPHA_BITS = 3413L # Variable c_uint '3413u'
GL_ALPHA_BLEND_EQUATION_ATI = 34877L # Variable c_uint '34877u'
GL_ALPHA_FLOAT16_APPLE = 34844L # Variable c_uint '34844u'
GL_ALPHA_FLOAT16_ATI = 34844L # Variable c_uint '34844u'
GL_ALPHA_FLOAT32_APPLE = 34838L # Variable c_uint '34838u'
GL_ALPHA_FLOAT32_ATI = 34838L # Variable c_uint '34838u'
GL_ALPHA_INTEGER = 36247L # Variable c_uint '36247u'
GL_ALPHA_INTEGER_EXT = 36247L # Variable c_uint '36247u'
GL_ALPHA_MAX_CLAMP_INGR = 34151L # Variable c_uint '34151u'
GL_ALPHA_MAX_SGIX = 33569L # Variable c_uint '33569u'
GL_ALPHA_MIN_CLAMP_INGR = 34147L # Variable c_uint '34147u'
GL_ALPHA_MIN_SGIX = 33568L # Variable c_uint '33568u'
GL_ALPHA_SCALE = 3356L # Variable c_uint '3356u'
GL_ALPHA_SNORM = 36880L # Variable c_uint '36880u'
GL_ALPHA_TEST = 3008L # Variable c_uint '3008u'
GL_ALPHA_TEST_FUNC = 3009L # Variable c_uint '3009u'
GL_ALPHA_TEST_REF = 3010L # Variable c_uint '3010u'
GL_ALREADY_SIGNALED = 37146L # Variable c_uint '37146u'
GL_ALWAYS = 519L # Variable c_uint '519u'
GL_ALWAYS_FAST_HINT_PGI = 107020L # Variable c_uint '107020u'
GL_ALWAYS_SOFT_HINT_PGI = 107021L # Variable c_uint '107021u'
GL_AMBIENT = 4608L # Variable c_uint '4608u'
GL_AMBIENT_AND_DIFFUSE = 5634L # Variable c_uint '5634u'
GL_AND = 5377L # Variable c_uint '5377u'
GL_AND_INVERTED = 5380L # Variable c_uint '5380u'
GL_AND_REVERSE = 5378L # Variable c_uint '5378u'
GL_ANY_SAMPLES_PASSED = 35887L # Variable c_uint '35887u'
GL_ARRAY_BUFFER = 34962L # Variable c_uint '34962u'
GL_ARRAY_BUFFER_ARB = 34962L # Variable c_uint '34962u'
GL_ARRAY_BUFFER_BINDING = 34964L # Variable c_uint '34964u'
GL_ARRAY_BUFFER_BINDING_ARB = 34964L # Variable c_uint '34964u'
GL_ARRAY_ELEMENT_LOCK_COUNT_EXT = 33193L # Variable c_uint '33193u'
GL_ARRAY_ELEMENT_LOCK_FIRST_EXT = 33192L # Variable c_uint '33192u'
GL_ARRAY_OBJECT_BUFFER_ATI = 34662L # Variable c_uint '34662u'
GL_ARRAY_OBJECT_OFFSET_ATI = 34663L # Variable c_uint '34663u'
GL_ASYNC_DRAW_PIXELS_SGIX = 33629L # Variable c_uint '33629u'
GL_ASYNC_HISTOGRAM_SGIX = 33580L # Variable c_uint '33580u'
GL_ASYNC_MARKER_SGIX = 33577L # Variable c_uint '33577u'
GL_ASYNC_READ_PIXELS_SGIX = 33630L # Variable c_uint '33630u'
GL_ASYNC_TEX_IMAGE_SGIX = 33628L # Variable c_uint '33628u'
GL_ATOMIC_COUNTER_BARRIER_BIT_EXT = 4096L # Variable c_uint '4096u'
GL_ATTACHED_SHADERS = 35717L # Variable c_uint '35717u'
GL_ATTENUATION_EXT = 33613L # Variable c_uint '33613u'
GL_ATTRIB_ARRAY_POINTER_NV = 34373L # Variable c_uint '34373u'
GL_ATTRIB_ARRAY_SIZE_NV = 34339L # Variable c_uint '34339u'
GL_ATTRIB_ARRAY_STRIDE_NV = 34340L # Variable c_uint '34340u'
GL_ATTRIB_ARRAY_TYPE_NV = 34341L # Variable c_uint '34341u'
GL_ATTRIB_STACK_DEPTH = 2992L # Variable c_uint '2992u'
GL_AUTO_NORMAL = 3456L # Variable c_uint '3456u'
GL_AUX0 = 1033L # Variable c_uint '1033u'
GL_AUX1 = 1034L # Variable c_uint '1034u'
GL_AUX2 = 1035L # Variable c_uint '1035u'
GL_AUX3 = 1036L # Variable c_uint '1036u'
GL_AUX_BUFFERS = 3072L # Variable c_uint '3072u'
GL_AUX_DEPTH_STENCIL_APPLE = 35348L # Variable c_uint '35348u'
GL_AVERAGE_EXT = 33589L # Variable c_uint '33589u'
GL_AVERAGE_HP = 33120L # Variable c_uint '33120u'
GL_BACK = 1029L # Variable c_uint '1029u'
GL_BACK_LEFT = 1026L # Variable c_uint '1026u'
GL_BACK_NORMALS_HINT_PGI = 107043L # Variable c_uint '107043u'
GL_BACK_PRIMARY_COLOR_NV = 35959L # Variable c_uint '35959u'
GL_BACK_RIGHT = 1027L # Variable c_uint '1027u'
GL_BACK_SECONDARY_COLOR_NV = 35960L # Variable c_uint '35960u'
GL_BGR = 32992L # Variable c_uint '32992u'
GL_BGRA = 32993L # Variable c_uint '32993u'
GL_BGRA_EXT = 32993L # Variable c_uint '32993u'
GL_BGRA_INTEGER = 36251L # Variable c_uint '36251u'
GL_BGRA_INTEGER_EXT = 36251L # Variable c_uint '36251u'
GL_BGR_EXT = 32992L # Variable c_uint '32992u'
GL_BGR_INTEGER = 36250L # Variable c_uint '36250u'
GL_BGR_INTEGER_EXT = 36250L # Variable c_uint '36250u'
GL_BIAS_BIT_ATI = 8L # Variable c_uint '8u'
GL_BIAS_BY_NEGATIVE_ONE_HALF_NV = 34113L # Variable c_uint '34113u'
GL_BINORMAL_ARRAY_EXT = 33850L # Variable c_uint '33850u'
GL_BINORMAL_ARRAY_POINTER_EXT = 33859L # Variable c_uint '33859u'
GL_BINORMAL_ARRAY_STRIDE_EXT = 33857L # Variable c_uint '33857u'
GL_BINORMAL_ARRAY_TYPE_EXT = 33856L # Variable c_uint '33856u'
GL_BITMAP = 6656L # Variable c_uint '6656u'
GL_BITMAP_TOKEN = 1796L # Variable c_uint '1796u'
GL_BLEND = 3042L # Variable c_uint '3042u'
GL_BLEND_COLOR = 32773L # Variable c_uint '32773u'
GL_BLEND_COLOR_EXT = 32773L # Variable c_uint '32773u'
GL_BLEND_DST = 3040L # Variable c_uint '3040u'
GL_BLEND_DST_ALPHA = 32970L # Variable c_uint '32970u'
GL_BLEND_DST_ALPHA_EXT = 32970L # Variable c_uint '32970u'
GL_BLEND_DST_RGB = 32968L # Variable c_uint '32968u'
GL_BLEND_DST_RGB_EXT = 32968L # Variable c_uint '32968u'
GL_BLEND_EQUATION = 32777L # Variable c_uint '32777u'
GL_BLEND_EQUATION_ALPHA = 34877L # Variable c_uint '34877u'
GL_BLEND_EQUATION_ALPHA_EXT = 34877L # Variable c_uint '34877u'
GL_BLEND_EQUATION_EXT = 32777L # Variable c_uint '32777u'
GL_BLEND_EQUATION_RGB = 32777L # Variable c_uint '32777u'
GL_BLEND_EQUATION_RGB_EXT = 32777L # Variable c_uint '32777u'
GL_BLEND_SRC = 3041L # Variable c_uint '3041u'
GL_BLEND_SRC_ALPHA = 32971L # Variable c_uint '32971u'
GL_BLEND_SRC_ALPHA_EXT = 32971L # Variable c_uint '32971u'
GL_BLEND_SRC_RGB = 32969L # Variable c_uint '32969u'
GL_BLEND_SRC_RGB_EXT = 32969L # Variable c_uint '32969u'
GL_BLUE = 6405L # Variable c_uint '6405u'
GL_BLUE_BIAS = 3355L # Variable c_uint '3355u'
GL_BLUE_BIT_ATI = 4L # Variable c_uint '4u'
GL_BLUE_BITS = 3412L # Variable c_uint '3412u'
GL_BLUE_INTEGER = 36246L # Variable c_uint '36246u'
GL_BLUE_INTEGER_EXT = 36246L # Variable c_uint '36246u'
GL_BLUE_MAX_CLAMP_INGR = 34150L # Variable c_uint '34150u'
GL_BLUE_MIN_CLAMP_INGR = 34146L # Variable c_uint '34146u'
GL_BLUE_SCALE = 3354L # Variable c_uint '3354u'
GL_BOOL = 35670L # Variable c_uint '35670u'
GL_BOOL_ARB = 35670L # Variable c_uint '35670u'
GL_BOOL_VEC2 = 35671L # Variable c_uint '35671u'
GL_BOOL_VEC2_ARB = 35671L # Variable c_uint '35671u'
GL_BOOL_VEC3 = 35672L # Variable c_uint '35672u'
GL_BOOL_VEC3_ARB = 35672L # Variable c_uint '35672u'
GL_BOOL_VEC4 = 35673L # Variable c_uint '35673u'
GL_BOOL_VEC4_ARB = 35673L # Variable c_uint '35673u'
GL_BUFFER_ACCESS = 35003L # Variable c_uint '35003u'
GL_BUFFER_ACCESS_ARB = 35003L # Variable c_uint '35003u'
GL_BUFFER_ACCESS_FLAGS = 37151L # Variable c_uint '37151u'
GL_BUFFER_FLUSHING_UNMAP_APPLE = 35347L # Variable c_uint '35347u'
GL_BUFFER_GPU_ADDRESS_NV = 36637L # Variable c_uint '36637u'
GL_BUFFER_MAP_LENGTH = 37152L # Variable c_uint '37152u'
GL_BUFFER_MAP_OFFSET = 37153L # Variable c_uint '37153u'
GL_BUFFER_MAPPED = 35004L # Variable c_uint '35004u'
GL_BUFFER_MAPPED_ARB = 35004L # Variable c_uint '35004u'
GL_BUFFER_MAP_POINTER = 35005L # Variable c_uint '35005u'
GL_BUFFER_MAP_POINTER_ARB = 35005L # Variable c_uint '35005u'
GL_BUFFER_OBJECT_APPLE = 34227L # Variable c_uint '34227u'
GL_BUFFER_SERIALIZED_MODIFY_APPLE = 35346L # Variable c_uint '35346u'
GL_BUFFER_SIZE = 34660L # Variable c_uint '34660u'
GL_BUFFER_SIZE_ARB = 34660L # Variable c_uint '34660u'
GL_BUFFER_UPDATE_BARRIER_BIT_EXT = 512L # Variable c_uint '512u'
GL_BUFFER_USAGE = 34661L # Variable c_uint '34661u'
GL_BUFFER_USAGE_ARB = 34661L # Variable c_uint '34661u'
GL_BUMP_ENVMAP_ATI = 34683L # Variable c_uint '34683u'
GL_BUMP_NUM_TEX_UNITS_ATI = 34679L # Variable c_uint '34679u'
GL_BUMP_ROT_MATRIX_ATI = 34677L # Variable c_uint '34677u'
GL_BUMP_ROT_MATRIX_SIZE_ATI = 34678L # Variable c_uint '34678u'
GL_BUMP_TARGET_ATI = 34684L # Variable c_uint '34684u'
GL_BUMP_TEX_UNITS_ATI = 34680L # Variable c_uint '34680u'
GL_BYTE = 5120L # Variable c_uint '5120u'
GL_C3F_V3F = 10788L # Variable c_uint '10788u'
GL_C4F_N3F_V3F = 10790L # Variable c_uint '10790u'
GL_C4UB_V2F = 10786L # Variable c_uint '10786u'
GL_C4UB_V3F = 10787L # Variable c_uint '10787u'
GL_CALLIGRAPHIC_FRAGMENT_SGIX = 33155L # Variable c_uint '33155u'
GL_CCW = 2305L # Variable c_uint '2305u'
GL_CLAMP = 10496L # Variable c_uint '10496u'
GL_CLAMP_FRAGMENT_COLOR = 35099L # Variable c_uint '35099u'
GL_CLAMP_FRAGMENT_COLOR_ARB = 35099L # Variable c_uint '35099u'
GL_CLAMP_READ_COLOR = 35100L # Variable c_uint '35100u'
GL_CLAMP_READ_COLOR_ARB = 35100L # Variable c_uint '35100u'
GL_CLAMP_TO_BORDER = 33069L # Variable c_uint '33069u'
GL_CLAMP_TO_BORDER_ARB = 33069L # Variable c_uint '33069u'
GL_CLAMP_TO_BORDER_SGIS = 33069L # Variable c_uint '33069u'
GL_CLAMP_TO_EDGE = 33071L # Variable c_uint '33071u'
GL_CLAMP_TO_EDGE_SGIS = 33071L # Variable c_uint '33071u'
GL_CLAMP_VERTEX_COLOR = 35098L # Variable c_uint '35098u'
GL_CLAMP_VERTEX_COLOR_ARB = 35098L # Variable c_uint '35098u'
GL_CLEAR = 5376L # Variable c_uint '5376u'
GL_CLIENT_ACTIVE_TEXTURE = 34017L # Variable c_uint '34017u'
GL_CLIENT_ACTIVE_TEXTURE_ARB = 34017L # Variable c_uint '34017u'
GL_CLIENT_ALL_ATTRIB_BITS = 4294967295L # Variable c_uint '4294967295u'
GL_CLIENT_ATTRIB_STACK_DEPTH = 2993L # Variable c_uint '2993u'
GL_CLIENT_PIXEL_STORE_BIT = 1L # Variable c_uint '1u'
GL_CLIENT_VERTEX_ARRAY_BIT = 2L # Variable c_uint '2u'
GL_CLIP_DISTANCE0 = 12288L # Variable c_uint '12288u'
GL_CLIP_DISTANCE1 = 12289L # Variable c_uint '12289u'
GL_CLIP_DISTANCE2 = 12290L # Variable c_uint '12290u'
GL_CLIP_DISTANCE3 = 12291L # Variable c_uint '12291u'
GL_CLIP_DISTANCE4 = 12292L # Variable c_uint '12292u'
GL_CLIP_DISTANCE5 = 12293L # Variable c_uint '12293u'
GL_CLIP_DISTANCE6 = 12294L # Variable c_uint '12294u'
GL_CLIP_DISTANCE7 = 12295L # Variable c_uint '12295u'
GL_CLIP_DISTANCE_NV = 35962L # Variable c_uint '35962u'
GL_CLIP_FAR_HINT_PGI = 107041L # Variable c_uint '107041u'
GL_CLIP_NEAR_HINT_PGI = 107040L # Variable c_uint '107040u'
GL_CLIP_PLANE0 = 12288L # Variable c_uint '12288u'
GL_CLIP_PLANE1 = 12289L # Variable c_uint '12289u'
GL_CLIP_PLANE2 = 12290L # Variable c_uint '12290u'
GL_CLIP_PLANE3 = 12291L # Variable c_uint '12291u'
GL_CLIP_PLANE4 = 12292L # Variable c_uint '12292u'
GL_CLIP_PLANE5 = 12293L # Variable c_uint '12293u'
GL_CLIP_VOLUME_CLIPPING_HINT_EXT = 33008L # Variable c_uint '33008u'
GL_CMYKA_EXT = 32781L # Variable c_uint '32781u'
GL_CMYK_EXT = 32780L # Variable c_uint '32780u'
GL_CND0_ATI = 35179L # Variable c_uint '35179u'
GL_CND_ATI = 35178L # Variable c_uint '35178u'
GL_COEFF = 2560L # Variable c_uint '2560u'
GL_COLOR = 6144L # Variable c_uint '6144u'
GL_COLOR3_BIT_PGI = 65536L # Variable c_uint '65536u'
GL_COLOR4_BIT_PGI = 131072L # Variable c_uint '131072u'
GL_COLOR_ALPHA_PAIRING_ATI = 35189L # Variable c_uint '35189u'
GL_COLOR_ARRAY = 32886L # Variable c_uint '32886u'
GL_COLOR_ARRAY_ADDRESS_NV = 36643L # Variable c_uint '36643u'
GL_COLOR_ARRAY_BUFFER_BINDING = 34968L # Variable c_uint '34968u'
GL_COLOR_ARRAY_BUFFER_BINDING_ARB = 34968L # Variable c_uint '34968u'
GL_COLOR_ARRAY_COUNT_EXT = 32900L # Variable c_uint '32900u'
GL_COLOR_ARRAY_EXT = 32886L # Variable c_uint '32886u'
GL_COLOR_ARRAY_LENGTH_NV = 36653L # Variable c_uint '36653u'
GL_COLOR_ARRAY_LIST_IBM = 103072L # Variable c_uint '103072u'
GL_COLOR_ARRAY_LIST_STRIDE_IBM = 103082L # Variable c_uint '103082u'
GL_COLOR_ARRAY_PARALLEL_POINTERS_INTEL = 33783L # Variable c_uint '33783u'
GL_COLOR_ARRAY_POINTER = 32912L # Variable c_uint '32912u'
GL_COLOR_ARRAY_POINTER_EXT = 32912L # Variable c_uint '32912u'
GL_COLOR_ARRAY_SIZE = 32897L # Variable c_uint '32897u'
GL_COLOR_ARRAY_SIZE_EXT = 32897L # Variable c_uint '32897u'
GL_COLOR_ARRAY_STRIDE = 32899L # Variable c_uint '32899u'
GL_COLOR_ARRAY_STRIDE_EXT = 32899L # Variable c_uint '32899u'
GL_COLOR_ARRAY_TYPE = 32898L # Variable c_uint '32898u'
GL_COLOR_ARRAY_TYPE_EXT = 32898L # Variable c_uint '32898u'
GL_COLOR_ATTACHMENT0 = 36064L # Variable c_uint '36064u'
GL_COLOR_ATTACHMENT0_EXT = 36064L # Variable c_uint '36064u'
GL_COLOR_ATTACHMENT10 = 36074L # Variable c_uint '36074u'
GL_COLOR_ATTACHMENT10_EXT = 36074L # Variable c_uint '36074u'
GL_COLOR_ATTACHMENT1 = 36065L # Variable c_uint '36065u'
GL_COLOR_ATTACHMENT11 = 36075L # Variable c_uint '36075u'
GL_COLOR_ATTACHMENT11_EXT = 36075L # Variable c_uint '36075u'
GL_COLOR_ATTACHMENT12 = 36076L # Variable c_uint '36076u'
GL_COLOR_ATTACHMENT12_EXT = 36076L # Variable c_uint '36076u'
GL_COLOR_ATTACHMENT13 = 36077L # Variable c_uint '36077u'
GL_COLOR_ATTACHMENT13_EXT = 36077L # Variable c_uint '36077u'
GL_COLOR_ATTACHMENT14 = 36078L # Variable c_uint '36078u'
GL_COLOR_ATTACHMENT14_EXT = 36078L # Variable c_uint '36078u'
GL_COLOR_ATTACHMENT15 = 36079L # Variable c_uint '36079u'
GL_COLOR_ATTACHMENT15_EXT = 36079L # Variable c_uint '36079u'
GL_COLOR_ATTACHMENT1_EXT = 36065L # Variable c_uint '36065u'
GL_COLOR_ATTACHMENT2 = 36066L # Variable c_uint '36066u'
GL_COLOR_ATTACHMENT2_EXT = 36066L # Variable c_uint '36066u'
GL_COLOR_ATTACHMENT3 = 36067L # Variable c_uint '36067u'
GL_COLOR_ATTACHMENT3_EXT = 36067L # Variable c_uint '36067u'
GL_COLOR_ATTACHMENT4 = 36068L # Variable c_uint '36068u'
GL_COLOR_ATTACHMENT4_EXT = 36068L # Variable c_uint '36068u'
GL_COLOR_ATTACHMENT5 = 36069L # Variable c_uint '36069u'
GL_COLOR_ATTACHMENT5_EXT = 36069L # Variable c_uint '36069u'
GL_COLOR_ATTACHMENT6 = 36070L # Variable c_uint '36070u'
GL_COLOR_ATTACHMENT6_EXT = 36070L # Variable c_uint '36070u'
GL_COLOR_ATTACHMENT7 = 36071L # Variable c_uint '36071u'
GL_COLOR_ATTACHMENT7_EXT = 36071L # Variable c_uint '36071u'
GL_COLOR_ATTACHMENT8 = 36072L # Variable c_uint '36072u'
GL_COLOR_ATTACHMENT8_EXT = 36072L # Variable c_uint '36072u'
GL_COLOR_ATTACHMENT9 = 36073L # Variable c_uint '36073u'
GL_COLOR_ATTACHMENT9_EXT = 36073L # Variable c_uint '36073u'
GL_COLOR_BUFFER_BIT = 16384L # Variable c_uint '16384u'
GL_COLOR_CLEAR_UNCLAMPED_VALUE_ATI = 34869L # Variable c_uint '34869u'
GL_COLOR_CLEAR_VALUE = 3106L # Variable c_uint '3106u'
GL_COLOR_FLOAT_APPLE = 35343L # Variable c_uint '35343u'
GL_COLOR_INDEX = 6400L # Variable c_uint '6400u'
GL_COLOR_INDEX12_EXT = 32998L # Variable c_uint '32998u'
GL_COLOR_INDEX16_EXT = 32999L # Variable c_uint '32999u'
GL_COLOR_INDEX1_EXT = 32994L # Variable c_uint '32994u'
GL_COLOR_INDEX2_EXT = 32995L # Variable c_uint '32995u'
GL_COLOR_INDEX4_EXT = 32996L # Variable c_uint '32996u'
GL_COLOR_INDEX8_EXT = 32997L # Variable c_uint '32997u'
GL_COLOR_INDEXES = 5635L # Variable c_uint '5635u'
GL_COLOR_LOGIC_OP = 3058L # Variable c_uint '3058u'
GL_COLOR_MATERIAL = 2903L # Variable c_uint '2903u'
GL_COLOR_MATERIAL_FACE = 2901L # Variable c_uint '2901u'
GL_COLOR_MATERIAL_PARAMETER = 2902L # Variable c_uint '2902u'
GL_COLOR_MATRIX = 32945L # Variable c_uint '32945u'
GL_COLOR_MATRIX_SGI = 32945L # Variable c_uint '32945u'
GL_COLOR_MATRIX_STACK_DEPTH = 32946L # Variable c_uint '32946u'
GL_COLOR_MATRIX_STACK_DEPTH_SGI = 32946L # Variable c_uint '32946u'
GL_COLOR_SAMPLES_NV = 36384L # Variable c_uint '36384u'
GL_COLOR_SUM = 33880L # Variable c_uint '33880u'
GL_COLOR_SUM_ARB = 33880L # Variable c_uint '33880u'
GL_COLOR_SUM_CLAMP_NV = 34127L # Variable c_uint '34127u'
GL_COLOR_SUM_EXT = 33880L # Variable c_uint '33880u'
GL_COLOR_TABLE = 32976L # Variable c_uint '32976u'
GL_COLOR_TABLE_ALPHA_SIZE = 32989L # Variable c_uint '32989u'
GL_COLOR_TABLE_ALPHA_SIZE_SGI = 32989L # Variable c_uint '32989u'
GL_COLOR_TABLE_BIAS = 32983L # Variable c_uint '32983u'
GL_COLOR_TABLE_BIAS_SGI = 32983L # Variable c_uint '32983u'
GL_COLOR_TABLE_BLUE_SIZE = 32988L # Variable c_uint '32988u'
GL_COLOR_TABLE_BLUE_SIZE_SGI = 32988L # Variable c_uint '32988u'
GL_COLOR_TABLE_FORMAT = 32984L # Variable c_uint '32984u'
GL_COLOR_TABLE_FORMAT_SGI = 32984L # Variable c_uint '32984u'
GL_COLOR_TABLE_GREEN_SIZE = 32987L # Variable c_uint '32987u'
GL_COLOR_TABLE_GREEN_SIZE_SGI = 32987L # Variable c_uint '32987u'
GL_COLOR_TABLE_INTENSITY_SIZE = 32991L # Variable c_uint '32991u'
GL_COLOR_TABLE_INTENSITY_SIZE_SGI = 32991L # Variable c_uint '32991u'
GL_COLOR_TABLE_LUMINANCE_SIZE = 32990L # Variable c_uint '32990u'
GL_COLOR_TABLE_LUMINANCE_SIZE_SGI = 32990L # Variable c_uint '32990u'
GL_COLOR_TABLE_RED_SIZE = 32986L # Variable c_uint '32986u'
GL_COLOR_TABLE_RED_SIZE_SGI = 32986L # Variable c_uint '32986u'
GL_COLOR_TABLE_SCALE = 32982L # Variable c_uint '32982u'
GL_COLOR_TABLE_SCALE_SGI = 32982L # Variable c_uint '32982u'
GL_COLOR_TABLE_SGI = 32976L # Variable c_uint '32976u'
GL_COLOR_TABLE_WIDTH = 32985L # Variable c_uint '32985u'
GL_COLOR_TABLE_WIDTH_SGI = 32985L # Variable c_uint '32985u'
GL_COLOR_WRITEMASK = 3107L # Variable c_uint '3107u'
GL_COMBINE = 34160L # Variable c_uint '34160u'
GL_COMBINE4_NV = 34051L # Variable c_uint '34051u'
GL_COMBINE_ALPHA = 34162L # Variable c_uint '34162u'
GL_COMBINE_ALPHA_ARB = 34162L # Variable c_uint '34162u'
GL_COMBINE_ALPHA_EXT = 34162L # Variable c_uint '34162u'
GL_COMBINE_ARB = 34160L # Variable c_uint '34160u'
GL_COMBINE_EXT = 34160L # Variable c_uint '34160u'
GL_COMBINER0_NV = 34128L # Variable c_uint '34128u'
GL_COMBINER1_NV = 34129L # Variable c_uint '34129u'
GL_COMBINER2_NV = 34130L # Variable c_uint '34130u'
GL_COMBINER3_NV = 34131L # Variable c_uint '34131u'
GL_COMBINER4_NV = 34132L # Variable c_uint '34132u'
GL_COMBINER5_NV = 34133L # Variable c_uint '34133u'
GL_COMBINER6_NV = 34134L # Variable c_uint '34134u'
GL_COMBINER7_NV = 34135L # Variable c_uint '34135u'
GL_COMBINER_AB_DOT_PRODUCT_NV = 34117L # Variable c_uint '34117u'
GL_COMBINER_AB_OUTPUT_NV = 34122L # Variable c_uint '34122u'
GL_COMBINER_BIAS_NV = 34121L # Variable c_uint '34121u'
GL_COMBINER_CD_DOT_PRODUCT_NV = 34118L # Variable c_uint '34118u'
GL_COMBINER_CD_OUTPUT_NV = 34123L # Variable c_uint '34123u'
GL_COMBINER_COMPONENT_USAGE_NV = 34116L # Variable c_uint '34116u'
GL_COMBINE_RGB = 34161L # Variable c_uint '34161u'
GL_COMBINE_RGB_ARB = 34161L # Variable c_uint '34161u'
GL_COMBINE_RGB_EXT = 34161L # Variable c_uint '34161u'
GL_COMBINER_INPUT_NV = 34114L # Variable c_uint '34114u'
GL_COMBINER_MAPPING_NV = 34115L # Variable c_uint '34115u'
GL_COMBINER_MUX_SUM_NV = 34119L # Variable c_uint '34119u'
GL_COMBINER_SCALE_NV = 34120L # Variable c_uint '34120u'
GL_COMBINER_SUM_OUTPUT_NV = 34124L # Variable c_uint '34124u'
GL_COMMAND_BARRIER_BIT_EXT = 64L # Variable c_uint '64u'
GL_COMPARE_REF_DEPTH_TO_TEXTURE_EXT = 34894L # Variable c_uint '34894u'
GL_COMPARE_REF_TO_TEXTURE = 34894L # Variable c_uint '34894u'
GL_COMPARE_R_TO_TEXTURE = 34894L # Variable c_uint '34894u'
GL_COMPARE_R_TO_TEXTURE_ARB = 34894L # Variable c_uint '34894u'
GL_COMPATIBLE_SUBROUTINES = 36427L # Variable c_uint '36427u'
GL_COMP_BIT_ATI = 2L # Variable c_uint '2u'
GL_COMPILE = 4864L # Variable c_uint '4864u'
GL_COMPILE_AND_EXECUTE = 4865L # Variable c_uint '4865u'
GL_COMPILE_STATUS = 35713L # Variable c_uint '35713u'
GL_COMPRESSED_ALPHA = 34025L # Variable c_uint '34025u'
GL_COMPRESSED_ALPHA_ARB = 34025L # Variable c_uint '34025u'
GL_COMPRESSED_INTENSITY = 34028L # Variable c_uint '34028u'
GL_COMPRESSED_INTENSITY_ARB = 34028L # Variable c_uint '34028u'
GL_COMPRESSED_LUMINANCE = 34026L # Variable c_uint '34026u'
GL_COMPRESSED_LUMINANCE_ALPHA = 34027L # Variable c_uint '34027u'
GL_COMPRESSED_LUMINANCE_ALPHA_ARB = 34027L # Variable c_uint '34027u'
GL_COMPRESSED_LUMINANCE_ALPHA_LATC2_EXT = 35954L # Variable c_uint '35954u'
GL_COMPRESSED_LUMINANCE_ARB = 34026L # Variable c_uint '34026u'
GL_COMPRESSED_LUMINANCE_LATC1_EXT = 35952L # Variable c_uint '35952u'
GL_COMPRESSED_RED = 33317L # Variable c_uint '33317u'
GL_COMPRESSED_RED_GREEN_RGTC2_EXT = 36285L # Variable c_uint '36285u'
GL_COMPRESSED_RED_RGTC1 = 36283L # Variable c_uint '36283u'
GL_COMPRESSED_RED_RGTC1_EXT = 36283L # Variable c_uint '36283u'
GL_COMPRESSED_RG = 33318L # Variable c_uint '33318u'
GL_COMPRESSED_RGB = 34029L # Variable c_uint '34029u'
GL_COMPRESSED_RGBA = 34030L # Variable c_uint '34030u'
GL_COMPRESSED_RGBA_ARB = 34030L # Variable c_uint '34030u'
GL_COMPRESSED_RGBA_BPTC_UNORM_ARB = 36492L # Variable c_uint '36492u'
GL_COMPRESSED_RGBA_FXT1_3DFX = 34481L # Variable c_uint '34481u'
GL_COMPRESSED_RGB_ARB = 34029L # Variable c_uint '34029u'
GL_COMPRESSED_RGBA_S3TC_DXT1_EXT = 33777L # Variable c_uint '33777u'
GL_COMPRESSED_RGBA_S3TC_DXT3_EXT = 33778L # Variable c_uint '33778u'
GL_COMPRESSED_RGBA_S3TC_DXT5_EXT = 33779L # Variable c_uint '33779u'
GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT_ARB = 36494L # Variable c_uint '36494u'
GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_ARB = 36495L # Variable c_uint '36495u'
GL_COMPRESSED_RGB_FXT1_3DFX = 34480L # Variable c_uint '34480u'
GL_COMPRESSED_RGB_S3TC_DXT1_EXT = 33776L # Variable c_uint '33776u'
GL_COMPRESSED_RG_RGTC2 = 36285L # Variable c_uint '36285u'
GL_COMPRESSED_SIGNED_LUMINANCE_ALPHA_LATC2_EXT = 35955L # Variable c_uint '35955u'
GL_COMPRESSED_SIGNED_LUMINANCE_LATC1_EXT = 35953L # Variable c_uint '35953u'
GL_COMPRESSED_SIGNED_RED_GREEN_RGTC2_EXT = 36286L # Variable c_uint '36286u'
GL_COMPRESSED_SIGNED_RED_RGTC1 = 36284L # Variable c_uint '36284u'
GL_COMPRESSED_SIGNED_RED_RGTC1_EXT = 36284L # Variable c_uint '36284u'
GL_COMPRESSED_SIGNED_RG_RGTC2 = 36286L # Variable c_uint '36286u'
GL_COMPRESSED_SLUMINANCE = 35914L # Variable c_uint '35914u'
GL_COMPRESSED_SLUMINANCE_ALPHA = 35915L # Variable c_uint '35915u'
GL_COMPRESSED_SLUMINANCE_ALPHA_EXT = 35915L # Variable c_uint '35915u'
GL_COMPRESSED_SLUMINANCE_EXT = 35914L # Variable c_uint '35914u'
GL_COMPRESSED_SRGB = 35912L # Variable c_uint '35912u'
GL_COMPRESSED_SRGB_ALPHA = 35913L # Variable c_uint '35913u'
GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM_ARB = 36493L # Variable c_uint '36493u'
GL_COMPRESSED_SRGB_ALPHA_EXT = 35913L # Variable c_uint '35913u'
GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT1_EXT = 35917L # Variable c_uint '35917u'
GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT3_EXT = 35918L # Variable c_uint '35918u'
GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT5_EXT = 35919L # Variable c_uint '35919u'
GL_COMPRESSED_SRGB_EXT = 35912L # Variable c_uint '35912u'
GL_COMPRESSED_SRGB_S3TC_DXT1_EXT = 35916L # Variable c_uint '35916u'
GL_COMPRESSED_TEXTURE_FORMATS = 34467L # Variable c_uint '34467u'
GL_COMPRESSED_TEXTURE_FORMATS_ARB = 34467L # Variable c_uint '34467u'
GL_CON_0_ATI = 35137L # Variable c_uint '35137u'
GL_CON_10_ATI = 35147L # Variable c_uint '35147u'
GL_CON_11_ATI = 35148L # Variable c_uint '35148u'
GL_CON_12_ATI = 35149L # Variable c_uint '35149u'
GL_CON_13_ATI = 35150L # Variable c_uint '35150u'
GL_CON_14_ATI = 35151L # Variable c_uint '35151u'
GL_CON_15_ATI = 35152L # Variable c_uint '35152u'
GL_CON_16_ATI = 35153L # Variable c_uint '35153u'
GL_CON_17_ATI = 35154L # Variable c_uint '35154u'
GL_CON_18_ATI = 35155L # Variable c_uint '35155u'
GL_CON_19_ATI = 35156L # Variable c_uint '35156u'
GL_CON_1_ATI = 35138L # Variable c_uint '35138u'
GL_CON_20_ATI = 35157L # Variable c_uint '35157u'
GL_CON_21_ATI = 35158L # Variable c_uint '35158u'
GL_CON_22_ATI = 35159L # Variable c_uint '35159u'
GL_CON_23_ATI = 35160L # Variable c_uint '35160u'
GL_CON_24_ATI = 35161L # Variable c_uint '35161u'
GL_CON_25_ATI = 35162L # Variable c_uint '35162u'
GL_CON_26_ATI = 35163L # Variable c_uint '35163u'
GL_CON_27_ATI = 35164L # Variable c_uint '35164u'
GL_CON_28_ATI = 35165L # Variable c_uint '35165u'
GL_CON_29_ATI = 35166L # Variable c_uint '35166u'
GL_CON_2_ATI = 35139L # Variable c_uint '35139u'
GL_CON_30_ATI = 35167L # Variable c_uint '35167u'
GL_CON_31_ATI = 35168L # Variable c_uint '35168u'
GL_CON_3_ATI = 35140L # Variable c_uint '35140u'
GL_CON_4_ATI = 35141L # Variable c_uint '35141u'
GL_CON_5_ATI = 35142L # Variable c_uint '35142u'
GL_CON_6_ATI = 35143L # Variable c_uint '35143u'
GL_CON_7_ATI = 35144L # Variable c_uint '35144u'
GL_CON_8_ATI = 35145L # Variable c_uint '35145u'
GL_CON_9_ATI = 35146L # Variable c_uint '35146u'
GL_CONDITION_SATISFIED = 37148L # Variable c_uint '37148u'
GL_CONSERVE_MEMORY_HINT_PGI = 107005L # Variable c_uint '107005u'
GL_CONSTANT = 34166L # Variable c_uint '34166u'
GL_CONSTANT_ALPHA = 32771L # Variable c_uint '32771u'
GL_CONSTANT_ALPHA_EXT = 32771L # Variable c_uint '32771u'
GL_CONSTANT_ARB = 34166L # Variable c_uint '34166u'
GL_CONSTANT_ATTENUATION = 4615L # Variable c_uint '4615u'
GL_CONSTANT_BORDER = 33105L # Variable c_uint '33105u'
GL_CONSTANT_BORDER_HP = 33105L # Variable c_uint '33105u'
GL_CONSTANT_COLOR0_NV = 34090L # Variable c_uint '34090u'
GL_CONSTANT_COLOR = 32769L # Variable c_uint '32769u'
GL_CONSTANT_COLOR1_NV = 34091L # Variable c_uint '34091u'
GL_CONSTANT_COLOR_EXT = 32769L # Variable c_uint '32769u'
GL_CONSTANT_EXT = 34166L # Variable c_uint '34166u'
GL_CONST_EYE_NV = 34533L # Variable c_uint '34533u'
GL_CONTEXT_COMPATIBILITY_PROFILE_BIT = 2L # Variable c_uint '2u'
GL_CONTEXT_CORE_PROFILE_BIT = 1L # Variable c_uint '1u'
GL_CONTEXT_FLAG_FORWARD_COMPATIBLE_BIT = 1L # Variable c_uint '1u'
GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT_ARB = 4L # Variable c_uint '4u'
GL_CONTEXT_FLAGS = 33310L # Variable c_uint '33310u'
GL_CONTEXT_PROFILE_MASK = 37158L # Variable c_uint '37158u'
GL_CONTINUOUS_AMD = 36871L # Variable c_uint '36871u'
GL_CONVOLUTION_1D = 32784L # Variable c_uint '32784u'
GL_CONVOLUTION_1D_EXT = 32784L # Variable c_uint '32784u'
GL_CONVOLUTION_2D = 32785L # Variable c_uint '32785u'
GL_CONVOLUTION_2D_EXT = 32785L # Variable c_uint '32785u'
GL_CONVOLUTION_BORDER_COLOR = 33108L # Variable c_uint '33108u'
GL_CONVOLUTION_BORDER_COLOR_HP = 33108L # Variable c_uint '33108u'
GL_CONVOLUTION_BORDER_MODE = 32787L # Variable c_uint '32787u'
GL_CONVOLUTION_BORDER_MODE_EXT = 32787L # Variable c_uint '32787u'
GL_CONVOLUTION_FILTER_BIAS = 32789L # Variable c_uint '32789u'
GL_CONVOLUTION_FILTER_BIAS_EXT = 32789L # Variable c_uint '32789u'
GL_CONVOLUTION_FILTER_SCALE = 32788L # Variable c_uint '32788u'
GL_CONVOLUTION_FILTER_SCALE_EXT = 32788L # Variable c_uint '32788u'
GL_CONVOLUTION_FORMAT = 32791L # Variable c_uint '32791u'
GL_CONVOLUTION_FORMAT_EXT = 32791L # Variable c_uint '32791u'
GL_CONVOLUTION_HEIGHT = 32793L # Variable c_uint '32793u'
GL_CONVOLUTION_HEIGHT_EXT = 32793L # Variable c_uint '32793u'
GL_CONVOLUTION_HINT_SGIX = 33558L # Variable c_uint '33558u'
GL_CONVOLUTION_WIDTH = 32792L # Variable c_uint '32792u'
GL_CONVOLUTION_WIDTH_EXT = 32792L # Variable c_uint '32792u'
GL_COORD_REPLACE = 34914L # Variable c_uint '34914u'
GL_COORD_REPLACE_ARB = 34914L # Variable c_uint '34914u'
GL_COORD_REPLACE_NV = 34914L # Variable c_uint '34914u'
GL_COPY = 5379L # Variable c_uint '5379u'
GL_COPY_INVERTED = 5388L # Variable c_uint '5388u'
GL_COPY_PIXEL_TOKEN = 1798L # Variable c_uint '1798u'
GL_COPY_READ_BUFFER = 36662L # Variable c_uint '36662u'
GL_COPY_WRITE_BUFFER = 36663L # Variable c_uint '36663u'
GL_COUNTER_RANGE_AMD = 35777L # Variable c_uint '35777u'
GL_COUNTER_TYPE_AMD = 35776L # Variable c_uint '35776u'
GL_COVERAGE_SAMPLES_NV = 32937L # Variable c_uint '32937u'
GL_CUBIC_EXT = 33588L # Variable c_uint '33588u'
GL_CUBIC_HP = 33119L # Variable c_uint '33119u'
GL_CULL_FACE = 2884L # Variable c_uint '2884u'
GL_CULL_FACE_MODE = 2885L # Variable c_uint '2885u'
GL_CULL_FRAGMENT_NV = 34535L # Variable c_uint '34535u'
GL_CULL_MODES_NV = 34528L # Variable c_uint '34528u'
GL_CULL_VERTEX_EXT = 33194L # Variable c_uint '33194u'
GL_CULL_VERTEX_EYE_POSITION_EXT = 33195L # Variable c_uint '33195u'
GL_CULL_VERTEX_IBM = 103050L # Variable c_uint '103050u'
GL_CULL_VERTEX_OBJECT_POSITION_EXT = 33196L # Variable c_uint '33196u'
GL_CURRENT_ATTRIB_NV = 34342L # Variable c_uint '34342u'
GL_CURRENT_BINORMAL_EXT = 33852L # Variable c_uint '33852u'
GL_CURRENT_BIT = 1L # Variable c_uint '1u'
GL_CURRENT_COLOR = 2816L # Variable c_uint '2816u'
GL_CURRENT_FOG_COORD = 33875L # Variable c_uint '33875u'
GL_CURRENT_FOG_COORDINATE = 33875L # Variable c_uint '33875u'
GL_CURRENT_FOG_COORDINATE_EXT = 33875L # Variable c_uint '33875u'
GL_CURRENT_INDEX = 2817L # Variable c_uint '2817u'
GL_CURRENT_MATRIX_ARB = 34369L # Variable c_uint '34369u'
GL_CURRENT_MATRIX_INDEX_ARB = 34885L # Variable c_uint '34885u'
GL_CURRENT_MATRIX_NV = 34369L # Variable c_uint '34369u'
GL_CURRENT_MATRIX_STACK_DEPTH_ARB = 34368L # Variable c_uint '34368u'
GL_CURRENT_MATRIX_STACK_DEPTH_NV = 34368L # Variable c_uint '34368u'
GL_CURRENT_NORMAL = 2818L # Variable c_uint '2818u'
GL_CURRENT_OCCLUSION_QUERY_ID_NV = 34917L # Variable c_uint '34917u'
GL_CURRENT_PALETTE_MATRIX_ARB = 34883L # Variable c_uint '34883u'
GL_CURRENT_PROGRAM = 35725L # Variable c_uint '35725u'
GL_CURRENT_QUERY = 34917L # Variable c_uint '34917u'
GL_CURRENT_QUERY_ARB = 34917L # Variable c_uint '34917u'
GL_CURRENT_RASTER_COLOR = 2820L # Variable c_uint '2820u'
GL_CURRENT_RASTER_DISTANCE = 2825L # Variable c_uint '2825u'
GL_CURRENT_RASTER_INDEX = 2821L # Variable c_uint '2821u'
GL_CURRENT_RASTER_NORMAL_SGIX = 33798L # Variable c_uint '33798u'
GL_CURRENT_RASTER_POSITION = 2823L # Variable c_uint '2823u'
GL_CURRENT_RASTER_POSITION_VALID = 2824L # Variable c_uint '2824u'
GL_CURRENT_RASTER_SECONDARY_COLOR = 33887L # Variable c_uint '33887u'
GL_CURRENT_RASTER_TEXTURE_COORDS = 2822L # Variable c_uint '2822u'
GL_CURRENT_SECONDARY_COLOR = 33881L # Variable c_uint '33881u'
GL_CURRENT_SECONDARY_COLOR_EXT = 33881L # Variable c_uint '33881u'
GL_CURRENT_TANGENT_EXT = 33851L # Variable c_uint '33851u'
GL_CURRENT_TEXTURE_COORDS = 2819L # Variable c_uint '2819u'
GL_CURRENT_TIME_NV = 36392L # Variable c_uint '36392u'
GL_CURRENT_VERTEX_ATTRIB = 34342L # Variable c_uint '34342u'
GL_CURRENT_VERTEX_ATTRIB_ARB = 34342L # Variable c_uint '34342u'
GL_CURRENT_VERTEX_EXT = 34786L # Variable c_uint '34786u'
GL_CURRENT_VERTEX_WEIGHT_EXT = 34059L # Variable c_uint '34059u'
GL_CURRENT_WEIGHT_ARB = 34472L # Variable c_uint '34472u'
GL_CW = 2304L # Variable c_uint '2304u'
GL_DATA_BUFFER_AMD = 37201L # Variable c_uint '37201u'
GL_DEBUG_ASSERT_MESA = 34651L # Variable c_uint '34651u'
GL_DEBUG_CALLBACK_FUNCTION_ARB = 33348L # Variable c_uint '33348u'
GL_DEBUG_CALLBACK_USER_PARAM_ARB = 33349L # Variable c_uint '33349u'
GL_DEBUG_CATEGORY_API_ERROR_AMD = 37193L # Variable c_uint '37193u'
GL_DEBUG_CATEGORY_APPLICATION_AMD = 37199L # Variable c_uint '37199u'
GL_DEBUG_CATEGORY_DEPRECATION_AMD = 37195L # Variable c_uint '37195u'
GL_DEBUG_CATEGORY_OTHER_AMD = 37200L # Variable c_uint '37200u'
GL_DEBUG_CATEGORY_PERFORMANCE_AMD = 37197L # Variable c_uint '37197u'
GL_DEBUG_CATEGORY_SHADER_COMPILER_AMD = 37198L # Variable c_uint '37198u'
GL_DEBUG_CATEGORY_UNDEFINED_BEHAVIOR_AMD = 37196L # Variable c_uint '37196u'
GL_DEBUG_CATEGORY_WINDOW_SYSTEM_AMD = 37194L # Variable c_uint '37194u'
GL_DEBUG_LOGGED_MESSAGES_AMD = 37189L # Variable c_uint '37189u'
GL_DEBUG_LOGGED_MESSAGES_ARB = 37189L # Variable c_uint '37189u'
GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH_ARB = 33347L # Variable c_uint '33347u'
GL_DEBUG_OBJECT_MESA = 34649L # Variable c_uint '34649u'
GL_DEBUG_OUTPUT_SYNCHRONOUS_ARB = 33346L # Variable c_uint '33346u'
GL_DEBUG_PRINT_MESA = 34650L # Variable c_uint '34650u'
GL_DEBUG_SEVERITY_HIGH_AMD = 37190L # Variable c_uint '37190u'
GL_DEBUG_SEVERITY_HIGH_ARB = 37190L # Variable c_uint '37190u'
GL_DEBUG_SEVERITY_LOW_AMD = 37192L # Variable c_uint '37192u'
GL_DEBUG_SEVERITY_LOW_ARB = 37192L # Variable c_uint '37192u'
GL_DEBUG_SEVERITY_MEDIUM_AMD = 37191L # Variable c_uint '37191u'
GL_DEBUG_SEVERITY_MEDIUM_ARB = 37191L # Variable c_uint '37191u'
GL_DEBUG_SOURCE_API_ARB = 33350L # Variable c_uint '33350u'
GL_DEBUG_SOURCE_APPLICATION_ARB = 33354L # Variable c_uint '33354u'
GL_DEBUG_SOURCE_OTHER_ARB = 33355L # Variable c_uint '33355u'
GL_DEBUG_SOURCE_SHADER_COMPILER_ARB = 33352L # Variable c_uint '33352u'
GL_DEBUG_SOURCE_THIRD_PARTY_ARB = 33353L # Variable c_uint '33353u'
GL_DEBUG_SOURCE_WINDOW_SYSTEM_ARB = 33351L # Variable c_uint '33351u'
GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR_ARB = 33357L # Variable c_uint '33357u'
GL_DEBUG_TYPE_ERROR_ARB = 33356L # Variable c_uint '33356u'
GL_DEBUG_TYPE_OTHER_ARB = 33361L # Variable c_uint '33361u'
GL_DEBUG_TYPE_PERFORMANCE_ARB = 33360L # Variable c_uint '33360u'
GL_DEBUG_TYPE_PORTABILITY_ARB = 33359L # Variable c_uint '33359u'
GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR_ARB = 33358L # Variable c_uint '33358u'
GL_DECAL = 8449L # Variable c_uint '8449u'
GL_DECR = 7683L # Variable c_uint '7683u'
GL_DECR_WRAP = 34056L # Variable c_uint '34056u'
GL_DECR_WRAP_EXT = 34056L # Variable c_uint '34056u'
GL_DEFORMATIONS_MASK_SGIX = 33174L # Variable c_uint '33174u'
GL_DELETE_STATUS = 35712L # Variable c_uint '35712u'
GL_DEPENDENT_AR_TEXTURE_2D_NV = 34537L # Variable c_uint '34537u'
GL_DEPENDENT_GB_TEXTURE_2D_NV = 34538L # Variable c_uint '34538u'
GL_DEPENDENT_HILO_TEXTURE_2D_NV = 34904L # Variable c_uint '34904u'
GL_DEPENDENT_RGB_TEXTURE_3D_NV = 34905L # Variable c_uint '34905u'
GL_DEPENDENT_RGB_TEXTURE_CUBE_MAP_NV = 34906L # Variable c_uint '34906u'
GL_DEPTH = 6145L # Variable c_uint '6145u'
GL_DEPTH24_STENCIL8 = 35056L # Variable c_uint '35056u'
GL_DEPTH24_STENCIL8_EXT = 35056L # Variable c_uint '35056u'
GL_DEPTH32F_STENCIL8 = 36013L # Variable c_uint '36013u'
GL_DEPTH32F_STENCIL8_NV = 36268L # Variable c_uint '36268u'
GL_DEPTH_ATTACHMENT = 36096L # Variable c_uint '36096u'
GL_DEPTH_ATTACHMENT_EXT = 36096L # Variable c_uint '36096u'
GL_DEPTH_BIAS = 3359L # Variable c_uint '3359u'
GL_DEPTH_BITS = 3414L # Variable c_uint '3414u'
GL_DEPTH_BOUNDS_EXT = 34961L # Variable c_uint '34961u'
GL_DEPTH_BOUNDS_TEST_EXT = 34960L # Variable c_uint '34960u'
GL_DEPTH_BUFFER = 33315L # Variable c_uint '33315u'
GL_DEPTH_BUFFER_BIT = 256L # Variable c_uint '256u'
GL_DEPTH_BUFFER_FLOAT_MODE_NV = 36271L # Variable c_uint '36271u'
GL_DEPTH_CLAMP = 34383L # Variable c_uint '34383u'
GL_DEPTH_CLAMP_FAR_AMD = 36895L # Variable c_uint '36895u'
GL_DEPTH_CLAMP_NEAR_AMD = 36894L # Variable c_uint '36894u'
GL_DEPTH_CLAMP_NV = 34383L # Variable c_uint '34383u'
GL_DEPTH_CLEAR_VALUE = 2931L # Variable c_uint '2931u'
GL_DEPTH_COMPONENT = 6402L # Variable c_uint '6402u'
GL_DEPTH_COMPONENT16 = 33189L # Variable c_uint '33189u'
GL_DEPTH_COMPONENT16_ARB = 33189L # Variable c_uint '33189u'
GL_DEPTH_COMPONENT16_SGIX = 33189L # Variable c_uint '33189u'
GL_DEPTH_COMPONENT24 = 33190L # Variable c_uint '33190u'
GL_DEPTH_COMPONENT24_ARB = 33190L # Variable c_uint '33190u'
GL_DEPTH_COMPONENT24_SGIX = 33190L # Variable c_uint '33190u'
GL_DEPTH_COMPONENT32 = 33191L # Variable c_uint '33191u'
GL_DEPTH_COMPONENT32_ARB = 33191L # Variable c_uint '33191u'
GL_DEPTH_COMPONENT32F = 36012L # Variable c_uint '36012u'
GL_DEPTH_COMPONENT32F_NV = 36267L # Variable c_uint '36267u'
GL_DEPTH_COMPONENT32_SGIX = 33191L # Variable c_uint '33191u'
GL_DEPTH_FUNC = 2932L # Variable c_uint '2932u'
GL_DEPTH_PASS_INSTRUMENT_COUNTERS_SGIX = 33553L # Variable c_uint '33553u'
GL_DEPTH_PASS_INSTRUMENT_MAX_SGIX = 33554L # Variable c_uint '33554u'
GL_DEPTH_PASS_INSTRUMENT_SGIX = 33552L # Variable c_uint '33552u'
GL_DEPTH_RANGE = 2928L # Variable c_uint '2928u'
GL_DEPTH_SCALE = 3358L # Variable c_uint '3358u'
GL_DEPTH_STENCIL = 34041L # Variable c_uint '34041u'
GL_DEPTH_STENCIL_ATTACHMENT = 33306L # Variable c_uint '33306u'
GL_DEPTH_STENCIL_EXT = 34041L # Variable c_uint '34041u'
GL_DEPTH_STENCIL_MESA = 34640L # Variable c_uint '34640u'
GL_DEPTH_STENCIL_NV = 34041L # Variable c_uint '34041u'
GL_DEPTH_STENCIL_TO_BGRA_NV = 34927L # Variable c_uint '34927u'
GL_DEPTH_STENCIL_TO_RGBA_NV = 34926L # Variable c_uint '34926u'
GL_DEPTH_TEST = 2929L # Variable c_uint '2929u'
GL_DEPTH_TEXTURE_MODE = 34891L # Variable c_uint '34891u'
GL_DEPTH_TEXTURE_MODE_ARB = 34891L # Variable c_uint '34891u'
GL_DEPTH_WRITEMASK = 2930L # Variable c_uint '2930u'
GL_DETAIL_TEXTURE_2D_BINDING_SGIS = 32918L # Variable c_uint '32918u'
GL_DETAIL_TEXTURE_2D_SGIS = 32917L # Variable c_uint '32917u'
GL_DETAIL_TEXTURE_FUNC_POINTS_SGIS = 32924L # Variable c_uint '32924u'
GL_DETAIL_TEXTURE_LEVEL_SGIS = 32922L # Variable c_uint '32922u'
GL_DETAIL_TEXTURE_MODE_SGIS = 32923L # Variable c_uint '32923u'
GL_DIFFUSE = 4609L # Variable c_uint '4609u'
GL_DISCARD_ATI = 34659L # Variable c_uint '34659u'
GL_DISCARD_NV = 34096L # Variable c_uint '34096u'
GL_DISCRETE_AMD = 36870L # Variable c_uint '36870u'
GL_DISTANCE_ATTENUATION_EXT = 33065L # Variable c_uint '33065u'
GL_DISTANCE_ATTENUATION_SGIS = 33065L # Variable c_uint '33065u'
GL_DITHER = 3024L # Variable c_uint '3024u'
GL_DOMAIN = 2562L # Variable c_uint '2562u'
GL_DONT_CARE = 4352L # Variable c_uint '4352u'
GL_DOT2_ADD_ATI = 35180L # Variable c_uint '35180u'
GL_DOT3_ATI = 35174L # Variable c_uint '35174u'
GL_DOT3_RGB = 34478L # Variable c_uint '34478u'
GL_DOT3_RGBA = 34479L # Variable c_uint '34479u'
GL_DOT3_RGBA_ARB = 34479L # Variable c_uint '34479u'
GL_DOT3_RGBA_EXT = 34625L # Variable c_uint '34625u'
GL_DOT3_RGB_ARB = 34478L # Variable c_uint '34478u'
GL_DOT3_RGB_EXT = 34624L # Variable c_uint '34624u'
GL_DOT4_ATI = 35175L # Variable c_uint '35175u'
GL_DOT_PRODUCT_AFFINE_DEPTH_REPLACE_NV = 34909L # Variable c_uint '34909u'
GL_DOT_PRODUCT_CONST_EYE_REFLECT_CUBE_MAP_NV = 34547L # Variable c_uint '34547u'
GL_DOT_PRODUCT_DEPTH_REPLACE_NV = 34541L # Variable c_uint '34541u'
GL_DOT_PRODUCT_DIFFUSE_CUBE_MAP_NV = 34545L # Variable c_uint '34545u'
GL_DOT_PRODUCT_NV = 34540L # Variable c_uint '34540u'
GL_DOT_PRODUCT_PASS_THROUGH_NV = 34907L # Variable c_uint '34907u'
GL_DOT_PRODUCT_REFLECT_CUBE_MAP_NV = 34546L # Variable c_uint '34546u'
GL_DOT_PRODUCT_TEXTURE_1D_NV = 34908L # Variable c_uint '34908u'
GL_DOT_PRODUCT_TEXTURE_2D_NV = 34542L # Variable c_uint '34542u'
GL_DOT_PRODUCT_TEXTURE_3D_NV = 34543L # Variable c_uint '34543u'
GL_DOT_PRODUCT_TEXTURE_CUBE_MAP_NV = 34544L # Variable c_uint '34544u'
GL_DOT_PRODUCT_TEXTURE_RECTANGLE_NV = 34382L # Variable c_uint '34382u'
GL_DOUBLE = 5130L # Variable c_uint '5130u'
GL_DOUBLEBUFFER = 3122L # Variable c_uint '3122u'
GL_DOUBLE_MAT2 = 36678L # Variable c_uint '36678u'
GL_DOUBLE_MAT2_EXT = 36678L # Variable c_uint '36678u'
GL_DOUBLE_MAT3 = 36679L # Variable c_uint '36679u'
GL_DOUBLE_MAT3_EXT = 36679L # Variable c_uint '36679u'
GL_DOUBLE_MAT4 = 36680L # Variable c_uint '36680u'
GL_DOUBLE_MAT4_EXT = 36680L # Variable c_uint '36680u'
GL_DOUBLE_VEC2 = 36860L # Variable c_uint '36860u'
GL_DOUBLE_VEC2_EXT = 36860L # Variable c_uint '36860u'
GL_DOUBLE_VEC3 = 36861L # Variable c_uint '36861u'
GL_DOUBLE_VEC3_EXT = 36861L # Variable c_uint '36861u'
GL_DOUBLE_VEC4 = 36862L # Variable c_uint '36862u'
GL_DOUBLE_VEC4_EXT = 36862L # Variable c_uint '36862u'
GL_DRAW_BUFFER0 = 34853L # Variable c_uint '34853u'
GL_DRAW_BUFFER0_ARB = 34853L # Variable c_uint '34853u'
GL_DRAW_BUFFER0_ATI = 34853L # Variable c_uint '34853u'
GL_DRAW_BUFFER = 3073L # Variable c_uint '3073u'
GL_DRAW_BUFFER10 = 34863L # Variable c_uint '34863u'
GL_DRAW_BUFFER10_ARB = 34863L # Variable c_uint '34863u'
GL_DRAW_BUFFER10_ATI = 34863L # Variable c_uint '34863u'
GL_DRAW_BUFFER1 = 34854L # Variable c_uint '34854u'
GL_DRAW_BUFFER11 = 34864L # Variable c_uint '34864u'
GL_DRAW_BUFFER11_ARB = 34864L # Variable c_uint '34864u'
GL_DRAW_BUFFER11_ATI = 34864L # Variable c_uint '34864u'
GL_DRAW_BUFFER12 = 34865L # Variable c_uint '34865u'
GL_DRAW_BUFFER12_ARB = 34865L # Variable c_uint '34865u'
GL_DRAW_BUFFER12_ATI = 34865L # Variable c_uint '34865u'
GL_DRAW_BUFFER13 = 34866L # Variable c_uint '34866u'
GL_DRAW_BUFFER13_ARB = 34866L # Variable c_uint '34866u'
GL_DRAW_BUFFER13_ATI = 34866L # Variable c_uint '34866u'
GL_DRAW_BUFFER14 = 34867L # Variable c_uint '34867u'
GL_DRAW_BUFFER14_ARB = 34867L # Variable c_uint '34867u'
GL_DRAW_BUFFER14_ATI = 34867L # Variable c_uint '34867u'
GL_DRAW_BUFFER15 = 34868L # Variable c_uint '34868u'
GL_DRAW_BUFFER15_ARB = 34868L # Variable c_uint '34868u'
GL_DRAW_BUFFER15_ATI = 34868L # Variable c_uint '34868u'
GL_DRAW_BUFFER1_ARB = 34854L # Variable c_uint '34854u'
GL_DRAW_BUFFER1_ATI = 34854L # Variable c_uint '34854u'
GL_DRAW_BUFFER2 = 34855L # Variable c_uint '34855u'
GL_DRAW_BUFFER2_ARB = 34855L # Variable c_uint '34855u'
GL_DRAW_BUFFER2_ATI = 34855L # Variable c_uint '34855u'
GL_DRAW_BUFFER3 = 34856L # Variable c_uint '34856u'
GL_DRAW_BUFFER3_ARB = 34856L # Variable c_uint '34856u'
GL_DRAW_BUFFER3_ATI = 34856L # Variable c_uint '34856u'
GL_DRAW_BUFFER4 = 34857L # Variable c_uint '34857u'
GL_DRAW_BUFFER4_ARB = 34857L # Variable c_uint '34857u'
GL_DRAW_BUFFER4_ATI = 34857L # Variable c_uint '34857u'
GL_DRAW_BUFFER5 = 34858L # Variable c_uint '34858u'
GL_DRAW_BUFFER5_ARB = 34858L # Variable c_uint '34858u'
GL_DRAW_BUFFER5_ATI = 34858L # Variable c_uint '34858u'
GL_DRAW_BUFFER6 = 34859L # Variable c_uint '34859u'
GL_DRAW_BUFFER6_ARB = 34859L # Variable c_uint '34859u'
GL_DRAW_BUFFER6_ATI = 34859L # Variable c_uint '34859u'
GL_DRAW_BUFFER7 = 34860L # Variable c_uint '34860u'
GL_DRAW_BUFFER7_ARB = 34860L # Variable c_uint '34860u'
GL_DRAW_BUFFER7_ATI = 34860L # Variable c_uint '34860u'
GL_DRAW_BUFFER8 = 34861L # Variable c_uint '34861u'
GL_DRAW_BUFFER8_ARB = 34861L # Variable c_uint '34861u'
GL_DRAW_BUFFER8_ATI = 34861L # Variable c_uint '34861u'
GL_DRAW_BUFFER9 = 34862L # Variable c_uint '34862u'
GL_DRAW_BUFFER9_ARB = 34862L # Variable c_uint '34862u'
GL_DRAW_BUFFER9_ATI = 34862L # Variable c_uint '34862u'
GL_DRAW_FRAMEBUFFER = 36009L # Variable c_uint '36009u'
GL_DRAW_FRAMEBUFFER_EXT = 36009L # Variable c_uint '36009u'
GL_DRAW_INDIRECT_ADDRESS_NV = 36673L # Variable c_uint '36673u'
GL_DRAW_INDIRECT_BUFFER = 36671L # Variable c_uint '36671u'
GL_DRAW_INDIRECT_BUFFER_BINDING = 36675L # Variable c_uint '36675u'
GL_DRAW_INDIRECT_LENGTH_NV = 36674L # Variable c_uint '36674u'
GL_DRAW_INDIRECT_UNIFIED_NV = 36672L # Variable c_uint '36672u'
GL_DRAW_PIXELS_APPLE = 35338L # Variable c_uint '35338u'
GL_DRAW_PIXEL_TOKEN = 1797L # Variable c_uint '1797u'
GL_DS_BIAS_NV = 34582L # Variable c_uint '34582u'
GL_DSDT8_MAG8_INTENSITY8_NV = 34571L # Variable c_uint '34571u'
GL_DSDT8_MAG8_NV = 34570L # Variable c_uint '34570u'
GL_DSDT8_NV = 34569L # Variable c_uint '34569u'
GL_DSDT_MAG_INTENSITY_NV = 34524L # Variable c_uint '34524u'
GL_DSDT_MAG_NV = 34550L # Variable c_uint '34550u'
GL_DSDT_MAG_VIB_NV = 34551L # Variable c_uint '34551u'
GL_DSDT_NV = 34549L # Variable c_uint '34549u'
GL_DS_SCALE_NV = 34576L # Variable c_uint '34576u'
GL_DST_ALPHA = 772L # Variable c_uint '772u'
GL_DST_COLOR = 774L # Variable c_uint '774u'
GL_DT_BIAS_NV = 34583L # Variable c_uint '34583u'
GL_DT_SCALE_NV = 34577L # Variable c_uint '34577u'
GL_DU8DV8_ATI = 34682L # Variable c_uint '34682u'
GL_DUAL_ALPHA12_SGIS = 33042L # Variable c_uint '33042u'
GL_DUAL_ALPHA16_SGIS = 33043L # Variable c_uint '33043u'
GL_DUAL_ALPHA4_SGIS = 33040L # Variable c_uint '33040u'
GL_DUAL_ALPHA8_SGIS = 33041L # Variable c_uint '33041u'
GL_DUAL_INTENSITY12_SGIS = 33050L # Variable c_uint '33050u'
GL_DUAL_INTENSITY16_SGIS = 33051L # Variable c_uint '33051u'
GL_DUAL_INTENSITY4_SGIS = 33048L # Variable c_uint '33048u'
GL_DUAL_INTENSITY8_SGIS = 33049L # Variable c_uint '33049u'
GL_DUAL_LUMINANCE12_SGIS = 33046L # Variable c_uint '33046u'
GL_DUAL_LUMINANCE16_SGIS = 33047L # Variable c_uint '33047u'
GL_DUAL_LUMINANCE4_SGIS = 33044L # Variable c_uint '33044u'
GL_DUAL_LUMINANCE8_SGIS = 33045L # Variable c_uint '33045u'
GL_DUAL_LUMINANCE_ALPHA4_SGIS = 33052L # Variable c_uint '33052u'
GL_DUAL_LUMINANCE_ALPHA8_SGIS = 33053L # Variable c_uint '33053u'
GL_DUAL_TEXTURE_SELECT_SGIS = 33060L # Variable c_uint '33060u'
GL_DUDV_ATI = 34681L # Variable c_uint '34681u'
GL_DYNAMIC_ATI = 34657L # Variable c_uint '34657u'
GL_DYNAMIC_COPY = 35050L # Variable c_uint '35050u'
GL_DYNAMIC_COPY_ARB = 35050L # Variable c_uint '35050u'
GL_DYNAMIC_DRAW = 35048L # Variable c_uint '35048u'
GL_DYNAMIC_DRAW_ARB = 35048L # Variable c_uint '35048u'
GL_DYNAMIC_READ = 35049L # Variable c_uint '35049u'
GL_DYNAMIC_READ_ARB = 35049L # Variable c_uint '35049u'
GL_EDGE_FLAG = 2883L # Variable c_uint '2883u'
GL_EDGE_FLAG_ARRAY = 32889L # Variable c_uint '32889u'
GL_EDGE_FLAG_ARRAY_ADDRESS_NV = 36646L # Variable c_uint '36646u'
GL_EDGE_FLAG_ARRAY_BUFFER_BINDING = 34971L # Variable c_uint '34971u'
GL_EDGE_FLAG_ARRAY_BUFFER_BINDING_ARB = 34971L # Variable c_uint '34971u'
GL_EDGE_FLAG_ARRAY_COUNT_EXT = 32909L # Variable c_uint '32909u'
GL_EDGE_FLAG_ARRAY_EXT = 32889L # Variable c_uint '32889u'
GL_EDGE_FLAG_ARRAY_LENGTH_NV = 36656L # Variable c_uint '36656u'
GL_EDGE_FLAG_ARRAY_LIST_IBM = 103075L # Variable c_uint '103075u'
GL_EDGE_FLAG_ARRAY_LIST_STRIDE_IBM = 103085L # Variable c_uint '103085u'
GL_EDGE_FLAG_ARRAY_POINTER = 32915L # Variable c_uint '32915u'
GL_EDGE_FLAG_ARRAY_POINTER_EXT = 32915L # Variable c_uint '32915u'
GL_EDGE_FLAG_ARRAY_STRIDE = 32908L # Variable c_uint '32908u'
GL_EDGE_FLAG_ARRAY_STRIDE_EXT = 32908L # Variable c_uint '32908u'
GL_EDGEFLAG_BIT_PGI = 262144L # Variable c_uint '262144u'
GL_EIGHTH_BIT_ATI = 32L # Variable c_uint '32u'
GL_ELEMENT_ARRAY_ADDRESS_NV = 36649L # Variable c_uint '36649u'
GL_ELEMENT_ARRAY_APPLE = 35340L # Variable c_uint '35340u'
GL_ELEMENT_ARRAY_ATI = 34664L # Variable c_uint '34664u'
GL_ELEMENT_ARRAY_BARRIER_BIT_EXT = 2L # Variable c_uint '2u'
GL_ELEMENT_ARRAY_BUFFER = 34963L # Variable c_uint '34963u'
GL_ELEMENT_ARRAY_BUFFER_ARB = 34963L # Variable c_uint '34963u'
GL_ELEMENT_ARRAY_BUFFER_BINDING = 34965L # Variable c_uint '34965u'
GL_ELEMENT_ARRAY_BUFFER_BINDING_ARB = 34965L # Variable c_uint '34965u'
GL_ELEMENT_ARRAY_LENGTH_NV = 36659L # Variable c_uint '36659u'
GL_ELEMENT_ARRAY_POINTER_APPLE = 35342L # Variable c_uint '35342u'
GL_ELEMENT_ARRAY_POINTER_ATI = 34666L # Variable c_uint '34666u'
GL_ELEMENT_ARRAY_TYPE_APPLE = 35341L # Variable c_uint '35341u'
GL_ELEMENT_ARRAY_TYPE_ATI = 34665L # Variable c_uint '34665u'
GL_ELEMENT_ARRAY_UNIFIED_NV = 36639L # Variable c_uint '36639u'
GL_EMBOSS_CONSTANT_NV = 34142L # Variable c_uint '34142u'
GL_EMBOSS_LIGHT_NV = 34141L # Variable c_uint '34141u'
GL_EMBOSS_MAP_NV = 34143L # Variable c_uint '34143u'
GL_EMISSION = 5632L # Variable c_uint '5632u'
GL_ENABLE_BIT = 8192L # Variable c_uint '8192u'
GL_EQUAL = 514L # Variable c_uint '514u'
GL_EQUIV = 5385L # Variable c_uint '5385u'
GL_E_TIMES_F_NV = 34097L # Variable c_uint '34097u'
GL_EVAL_2D_NV = 34496L # Variable c_uint '34496u'
GL_EVAL_BIT = 65536L # Variable c_uint '65536u'
GL_EVAL_FRACTIONAL_TESSELLATION_NV = 34501L # Variable c_uint '34501u'
GL_EVAL_TRIANGULAR_2D_NV = 34497L # Variable c_uint '34497u'
GL_EVAL_VERTEX_ATTRIB0_NV = 34502L # Variable c_uint '34502u'
GL_EVAL_VERTEX_ATTRIB10_NV = 34512L # Variable c_uint '34512u'
GL_EVAL_VERTEX_ATTRIB11_NV = 34513L # Variable c_uint '34513u'
GL_EVAL_VERTEX_ATTRIB12_NV = 34514L # Variable c_uint '34514u'
GL_EVAL_VERTEX_ATTRIB13_NV = 34515L # Variable c_uint '34515u'
GL_EVAL_VERTEX_ATTRIB14_NV = 34516L # Variable c_uint '34516u'
GL_EVAL_VERTEX_ATTRIB15_NV = 34517L # Variable c_uint '34517u'
GL_EVAL_VERTEX_ATTRIB1_NV = 34503L # Variable c_uint '34503u'
GL_EVAL_VERTEX_ATTRIB2_NV = 34504L # Variable c_uint '34504u'
GL_EVAL_VERTEX_ATTRIB3_NV = 34505L # Variable c_uint '34505u'
GL_EVAL_VERTEX_ATTRIB4_NV = 34506L # Variable c_uint '34506u'
GL_EVAL_VERTEX_ATTRIB5_NV = 34507L # Variable c_uint '34507u'
GL_EVAL_VERTEX_ATTRIB6_NV = 34508L # Variable c_uint '34508u'
GL_EVAL_VERTEX_ATTRIB7_NV = 34509L # Variable c_uint '34509u'
GL_EVAL_VERTEX_ATTRIB8_NV = 34510L # Variable c_uint '34510u'
GL_EVAL_VERTEX_ATTRIB9_NV = 34511L # Variable c_uint '34511u'
GL_EXP = 2048L # Variable c_uint '2048u'
GL_EXP2 = 2049L # Variable c_uint '2049u'
GL_EXPAND_NEGATE_NV = 34105L # Variable c_uint '34105u'
GL_EXPAND_NORMAL_NV = 34104L # Variable c_uint '34104u'
GL_EXTENSIONS = 7939L # Variable c_uint '7939u'
GL_EYE_DISTANCE_TO_LINE_SGIS = 33266L # Variable c_uint '33266u'
GL_EYE_DISTANCE_TO_POINT_SGIS = 33264L # Variable c_uint '33264u'
GL_EYE_LINEAR = 9216L # Variable c_uint '9216u'
GL_EYE_LINE_SGIS = 33270L # Variable c_uint '33270u'
GL_EYE_PLANE = 9474L # Variable c_uint '9474u'
GL_EYE_PLANE_ABSOLUTE_NV = 34140L # Variable c_uint '34140u'
GL_EYE_POINT_SGIS = 33268L # Variable c_uint '33268u'
GL_EYE_RADIAL_NV = 34139L # Variable c_uint '34139u'
GL_FAILURE_NV = 36912L # Variable c_uint '36912u'
GL_FALSE = 0L # Variable c_uint '0u'
GL_FASTEST = 4353L # Variable c_uint '4353u'
GL_FEEDBACK = 7169L # Variable c_uint '7169u'
GL_FEEDBACK_BUFFER_POINTER = 3568L # Variable c_uint '3568u'
GL_FEEDBACK_BUFFER_SIZE = 3569L # Variable c_uint '3569u'
GL_FEEDBACK_BUFFER_TYPE = 3570L # Variable c_uint '3570u'
GL_FENCE_APPLE = 35339L # Variable c_uint '35339u'
GL_FENCE_CONDITION_NV = 34036L # Variable c_uint '34036u'
GL_FENCE_STATUS_NV = 34035L # Variable c_uint '34035u'
GL_FIELD_LOWER_NV = 36899L # Variable c_uint '36899u'
GL_FIELDS_NV = 36391L # Variable c_uint '36391u'
GL_FIELD_UPPER_NV = 36898L # Variable c_uint '36898u'
GL_FILL = 6914L # Variable c_uint '6914u'
GL_FILTER4_SGIS = 33094L # Variable c_uint '33094u'
GL_FIRST_VERTEX_CONVENTION = 36429L # Variable c_uint '36429u'
GL_FIRST_VERTEX_CONVENTION_EXT = 36429L # Variable c_uint '36429u'
GL_FIXED = 5132L # Variable c_uint '5132u'
GL_FIXED_ONLY = 35101L # Variable c_uint '35101u'
GL_FIXED_ONLY_ARB = 35101L # Variable c_uint '35101u'
GL_FLAT = 7424L # Variable c_uint '7424u'
GL_FLOAT = 5126L # Variable c_uint '5126u'
GL_FLOAT16_NV = 36856L # Variable c_uint '36856u'
GL_FLOAT16_VEC2_NV = 36857L # Variable c_uint '36857u'
GL_FLOAT16_VEC3_NV = 36858L # Variable c_uint '36858u'
GL_FLOAT16_VEC4_NV = 36859L # Variable c_uint '36859u'
GL_FLOAT_32_UNSIGNED_INT_24_8_REV = 36269L # Variable c_uint '36269u'
GL_FLOAT_32_UNSIGNED_INT_24_8_REV_NV = 36269L # Variable c_uint '36269u'
GL_FLOAT_CLEAR_COLOR_VALUE_NV = 34957L # Variable c_uint '34957u'
GL_FLOAT_MAT2 = 35674L # Variable c_uint '35674u'
GL_FLOAT_MAT2_ARB = 35674L # Variable c_uint '35674u'
GL_FLOAT_MAT3 = 35675L # Variable c_uint '35675u'
GL_FLOAT_MAT3_ARB = 35675L # Variable c_uint '35675u'
GL_FLOAT_MAT4 = 35676L # Variable c_uint '35676u'
GL_FLOAT_MAT4_ARB = 35676L # Variable c_uint '35676u'
GL_FLOAT_R16_NV = 34948L # Variable c_uint '34948u'
GL_FLOAT_R32_NV = 34949L # Variable c_uint '34949u'
GL_FLOAT_RG16_NV = 34950L # Variable c_uint '34950u'
GL_FLOAT_RG32_NV = 34951L # Variable c_uint '34951u'
GL_FLOAT_RGB16_NV = 34952L # Variable c_uint '34952u'
GL_FLOAT_RGB32_NV = 34953L # Variable c_uint '34953u'
GL_FLOAT_RGBA16_NV = 34954L # Variable c_uint '34954u'
GL_FLOAT_RGBA32_NV = 34955L # Variable c_uint '34955u'
GL_FLOAT_RGBA_MODE_NV = 34958L # Variable c_uint '34958u'
GL_FLOAT_RGBA_NV = 34947L # Variable c_uint '34947u'
GL_FLOAT_RGB_NV = 34946L # Variable c_uint '34946u'
GL_FLOAT_RG_NV = 34945L # Variable c_uint '34945u'
GL_FLOAT_R_NV = 34944L # Variable c_uint '34944u'
GL_FLOAT_VEC2 = 35664L # Variable c_uint '35664u'
GL_FLOAT_VEC2_ARB = 35664L # Variable c_uint '35664u'
GL_FLOAT_VEC3 = 35665L # Variable c_uint '35665u'
GL_FLOAT_VEC3_ARB = 35665L # Variable c_uint '35665u'
GL_FLOAT_VEC4 = 35666L # Variable c_uint '35666u'
GL_FLOAT_VEC4_ARB = 35666L # Variable c_uint '35666u'
GL_FOG = 2912L # Variable c_uint '2912u'
GL_FOG_BIT = 128L # Variable c_uint '128u'
GL_FOG_COLOR = 2918L # Variable c_uint '2918u'
GL_FOG_COORD = 33873L # Variable c_uint '33873u'
GL_FOG_COORD_ARRAY = 33879L # Variable c_uint '33879u'
GL_FOG_COORD_ARRAY_ADDRESS_NV = 36648L # Variable c_uint '36648u'
GL_FOG_COORD_ARRAY_BUFFER_BINDING = 34973L # Variable c_uint '34973u'
GL_FOG_COORD_ARRAY_LENGTH_NV = 36658L # Variable c_uint '36658u'
GL_FOG_COORD_ARRAY_POINTER = 33878L # Variable c_uint '33878u'
GL_FOG_COORD_ARRAY_STRIDE = 33877L # Variable c_uint '33877u'
GL_FOG_COORD_ARRAY_TYPE = 33876L # Variable c_uint '33876u'
GL_FOG_COORDINATE = 33873L # Variable c_uint '33873u'
GL_FOG_COORDINATE_ARRAY = 33879L # Variable c_uint '33879u'
GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING = 34973L # Variable c_uint '34973u'
GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING_ARB = 34973L # Variable c_uint '34973u'
GL_FOG_COORDINATE_ARRAY_EXT = 33879L # Variable c_uint '33879u'
GL_FOG_COORDINATE_ARRAY_LIST_IBM = 103076L # Variable c_uint '103076u'
GL_FOG_COORDINATE_ARRAY_LIST_STRIDE_IBM = 103086L # Variable c_uint '103086u'
GL_FOG_COORDINATE_ARRAY_POINTER = 33878L # Variable c_uint '33878u'
GL_FOG_COORDINATE_ARRAY_POINTER_EXT = 33878L # Variable c_uint '33878u'
GL_FOG_COORDINATE_ARRAY_STRIDE = 33877L # Variable c_uint '33877u'
GL_FOG_COORDINATE_ARRAY_STRIDE_EXT = 33877L # Variable c_uint '33877u'
GL_FOG_COORDINATE_ARRAY_TYPE = 33876L # Variable c_uint '33876u'
GL_FOG_COORDINATE_ARRAY_TYPE_EXT = 33876L # Variable c_uint '33876u'
GL_FOG_COORDINATE_EXT = 33873L # Variable c_uint '33873u'
GL_FOG_COORDINATE_SOURCE = 33872L # Variable c_uint '33872u'
GL_FOG_COORDINATE_SOURCE_EXT = 33872L # Variable c_uint '33872u'
GL_FOG_COORD_SRC = 33872L # Variable c_uint '33872u'
GL_FOG_DENSITY = 2914L # Variable c_uint '2914u'
GL_FOG_DISTANCE_MODE_NV = 34138L # Variable c_uint '34138u'
GL_FOG_END = 2916L # Variable c_uint '2916u'
GL_FOG_FUNC_POINTS_SGIS = 33067L # Variable c_uint '33067u'
GL_FOG_FUNC_SGIS = 33066L # Variable c_uint '33066u'
GL_FOG_HINT = 3156L # Variable c_uint '3156u'
GL_FOG_INDEX = 2913L # Variable c_uint '2913u'
GL_FOG_MODE = 2917L # Variable c_uint '2917u'
GL_FOG_OFFSET_SGIX = 33176L # Variable c_uint '33176u'
GL_FOG_OFFSET_VALUE_SGIX = 33177L # Variable c_uint '33177u'
GL_FOG_SCALE_SGIX = 33276L # Variable c_uint '33276u'
GL_FOG_SCALE_VALUE_SGIX = 33277L # Variable c_uint '33277u'
GL_FOG_SPECULAR_TEXTURE_WIN = 33004L # Variable c_uint '33004u'
GL_FOG_START = 2915L # Variable c_uint '2915u'
GL_FORCE_BLUE_TO_ONE_NV = 34912L # Variable c_uint '34912u'
GL_FORMAT_SUBSAMPLE_24_24_OML = 35202L # Variable c_uint '35202u'
GL_FORMAT_SUBSAMPLE_244_244_OML = 35203L # Variable c_uint '35203u'
GL_FRACTIONAL_EVEN = 36476L # Variable c_uint '36476u'
GL_FRACTIONAL_ODD = 36475L # Variable c_uint '36475u'
GL_FRAGMENT_COLOR_EXT = 33612L # Variable c_uint '33612u'
GL_FRAGMENT_COLOR_MATERIAL_FACE_SGIX = 33794L # Variable c_uint '33794u'
GL_FRAGMENT_COLOR_MATERIAL_PARAMETER_SGIX = 33795L # Variable c_uint '33795u'
GL_FRAGMENT_COLOR_MATERIAL_SGIX = 33793L # Variable c_uint '33793u'
GL_FRAGMENT_DEPTH = 33874L # Variable c_uint '33874u'
GL_FRAGMENT_DEPTH_EXT = 33874L # Variable c_uint '33874u'
GL_FRAGMENT_INTERPOLATION_OFFSET_BITS = 36445L # Variable c_uint '36445u'
GL_FRAGMENT_LIGHT0_SGIX = 33804L # Variable c_uint '33804u'
GL_FRAGMENT_LIGHT1_SGIX = 33805L # Variable c_uint '33805u'
GL_FRAGMENT_LIGHT2_SGIX = 33806L # Variable c_uint '33806u'
GL_FRAGMENT_LIGHT3_SGIX = 33807L # Variable c_uint '33807u'
GL_FRAGMENT_LIGHT4_SGIX = 33808L # Variable c_uint '33808u'
GL_FRAGMENT_LIGHT5_SGIX = 33809L # Variable c_uint '33809u'
GL_FRAGMENT_LIGHT6_SGIX = 33810L # Variable c_uint '33810u'
GL_FRAGMENT_LIGHT7_SGIX = 33811L # Variable c_uint '33811u'
GL_FRAGMENT_LIGHTING_SGIX = 33792L # Variable c_uint '33792u'
GL_FRAGMENT_LIGHT_MODEL_AMBIENT_SGIX = 33802L # Variable c_uint '33802u'
GL_FRAGMENT_LIGHT_MODEL_LOCAL_VIEWER_SGIX = 33800L # Variable c_uint '33800u'
GL_FRAGMENT_LIGHT_MODEL_NORMAL_INTERPOLATION_SGIX = 33803L # Variable c_uint '33803u'
GL_FRAGMENT_LIGHT_MODEL_TWO_SIDE_SGIX = 33801L # Variable c_uint '33801u'
GL_FRAGMENT_MATERIAL_EXT = 33609L # Variable c_uint '33609u'
GL_FRAGMENT_NORMAL_EXT = 33610L # Variable c_uint '33610u'
GL_FRAGMENT_PROGRAM_ARB = 34820L # Variable c_uint '34820u'
GL_FRAGMENT_PROGRAM_BINDING_NV = 34931L # Variable c_uint '34931u'
GL_FRAGMENT_PROGRAM_CALLBACK_DATA_MESA = 35763L # Variable c_uint '35763u'
GL_FRAGMENT_PROGRAM_CALLBACK_FUNC_MESA = 35762L # Variable c_uint '35762u'
GL_FRAGMENT_PROGRAM_CALLBACK_MESA = 35761L # Variable c_uint '35761u'
GL_FRAGMENT_PROGRAM_INTERPOLATION_OFFSET_BITS_NV = 36445L # Variable c_uint '36445u'
GL_FRAGMENT_PROGRAM_NV = 34928L # Variable c_uint '34928u'
GL_FRAGMENT_PROGRAM_PARAMETER_BUFFER_NV = 36260L # Variable c_uint '36260u'
GL_FRAGMENT_PROGRAM_POSITION_MESA = 35760L # Variable c_uint '35760u'
GL_FRAGMENT_SHADER = 35632L # Variable c_uint '35632u'
GL_FRAGMENT_SHADER_ARB = 35632L # Variable c_uint '35632u'
GL_FRAGMENT_SHADER_ATI = 35104L # Variable c_uint '35104u'
GL_FRAGMENT_SHADER_BIT = 2L # Variable c_uint '2u'
GL_FRAGMENT_SHADER_DERIVATIVE_HINT = 35723L # Variable c_uint '35723u'
GL_FRAGMENT_SHADER_DERIVATIVE_HINT_ARB = 35723L # Variable c_uint '35723u'
GL_FRAMEBUFFER = 36160L # Variable c_uint '36160u'
GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE = 33301L # Variable c_uint '33301u'
GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE = 33300L # Variable c_uint '33300u'
GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING = 33296L # Variable c_uint '33296u'
GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE = 33297L # Variable c_uint '33297u'
GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE = 33302L # Variable c_uint '33302u'
GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE = 33299L # Variable c_uint '33299u'
GL_FRAMEBUFFER_ATTACHMENT_LAYERED = 36263L # Variable c_uint '36263u'
GL_FRAMEBUFFER_ATTACHMENT_LAYERED_ARB = 36263L # Variable c_uint '36263u'
GL_FRAMEBUFFER_ATTACHMENT_LAYERED_EXT = 36263L # Variable c_uint '36263u'
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME = 36049L # Variable c_uint '36049u'
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_EXT = 36049L # Variable c_uint '36049u'
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE = 36048L # Variable c_uint '36048u'
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_EXT = 36048L # Variable c_uint '36048u'
GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE = 33298L # Variable c_uint '33298u'
GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE = 33303L # Variable c_uint '33303u'
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_3D_ZOFFSET_EXT = 36052L # Variable c_uint '36052u'
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE = 36051L # Variable c_uint '36051u'
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_EXT = 36051L # Variable c_uint '36051u'
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER = 36052L # Variable c_uint '36052u'
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER_EXT = 36052L # Variable c_uint '36052u'
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL = 36050L # Variable c_uint '36050u'
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_EXT = 36050L # Variable c_uint '36050u'
GL_FRAMEBUFFER_BARRIER_BIT_EXT = 1024L # Variable c_uint '1024u'
GL_FRAMEBUFFER_BINDING = 36006L # Variable c_uint '36006u'
GL_FRAMEBUFFER_BINDING_EXT = 36006L # Variable c_uint '36006u'
GL_FRAMEBUFFER_COMPLETE = 36053L # Variable c_uint '36053u'
GL_FRAMEBUFFER_COMPLETE_EXT = 36053L # Variable c_uint '36053u'
GL_FRAMEBUFFER_DEFAULT = 33304L # Variable c_uint '33304u'
GL_FRAMEBUFFER_EXT = 36160L # Variable c_uint '36160u'
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT = 36054L # Variable c_uint '36054u'
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_EXT = 36054L # Variable c_uint '36054u'
GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_EXT = 36057L # Variable c_uint '36057u'
GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER = 36059L # Variable c_uint '36059u'
GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER_EXT = 36059L # Variable c_uint '36059u'
GL_FRAMEBUFFER_INCOMPLETE_FORMATS_EXT = 36058L # Variable c_uint '36058u'
GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_ARB = 36265L # Variable c_uint '36265u'
GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_EXT = 36265L # Variable c_uint '36265u'
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS = 36264L # Variable c_uint '36264u'
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_ARB = 36264L # Variable c_uint '36264u'
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_EXT = 36264L # Variable c_uint '36264u'
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT = 36055L # Variable c_uint '36055u'
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_EXT = 36055L # Variable c_uint '36055u'
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE = 36182L # Variable c_uint '36182u'
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_EXT = 36182L # Variable c_uint '36182u'
GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER = 36060L # Variable c_uint '36060u'
GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER_EXT = 36060L # Variable c_uint '36060u'
GL_FRAMEBUFFER_SRGB = 36281L # Variable c_uint '36281u'
GL_FRAMEBUFFER_SRGB_CAPABLE_EXT = 36282L # Variable c_uint '36282u'
GL_FRAMEBUFFER_SRGB_EXT = 36281L # Variable c_uint '36281u'
GL_FRAMEBUFFER_UNDEFINED = 33305L # Variable c_uint '33305u'
GL_FRAMEBUFFER_UNSUPPORTED = 36061L # Variable c_uint '36061u'
GL_FRAMEBUFFER_UNSUPPORTED_EXT = 36061L # Variable c_uint '36061u'
GL_FRAME_NV = 36390L # Variable c_uint '36390u'
GL_FRAMEZOOM_FACTOR_SGIX = 33164L # Variable c_uint '33164u'
GL_FRAMEZOOM_SGIX = 33163L # Variable c_uint '33163u'
GL_FRONT = 1028L # Variable c_uint '1028u'
GL_FRONT_AND_BACK = 1032L # Variable c_uint '1032u'
GL_FRONT_FACE = 2886L # Variable c_uint '2886u'
GL_FRONT_LEFT = 1024L # Variable c_uint '1024u'
GL_FRONT_RIGHT = 1025L # Variable c_uint '1025u'
GL_FULL_RANGE_EXT = 34785L # Variable c_uint '34785u'
GL_FULL_STIPPLE_HINT_PGI = 107033L # Variable c_uint '107033u'
GL_FUNC_ADD = 32774L # Variable c_uint '32774u'
GL_FUNC_ADD_EXT = 32774L # Variable c_uint '32774u'
GL_FUNC_REVERSE_SUBTRACT = 32779L # Variable c_uint '32779u'
GL_FUNC_REVERSE_SUBTRACT_EXT = 32779L # Variable c_uint '32779u'
GL_FUNC_SUBTRACT = 32778L # Variable c_uint '32778u'
GL_FUNC_SUBTRACT_EXT = 32778L # Variable c_uint '32778u'
GL_GENERATE_MIPMAP = 33169L # Variable c_uint '33169u'
GL_GENERATE_MIPMAP_HINT = 33170L # Variable c_uint '33170u'
GL_GENERATE_MIPMAP_HINT_SGIS = 33170L # Variable c_uint '33170u'
GL_GENERATE_MIPMAP_SGIS = 33169L # Variable c_uint '33169u'
GL_GENERIC_ATTRIB_NV = 35965L # Variable c_uint '35965u'
GL_GEOMETRY_DEFORMATION_BIT_SGIX = 2L # Variable c_uint '2u'
GL_GEOMETRY_DEFORMATION_SGIX = 33172L # Variable c_uint '33172u'
GL_GEOMETRY_INPUT_TYPE = 35095L # Variable c_uint '35095u'
GL_GEOMETRY_INPUT_TYPE_ARB = 36315L # Variable c_uint '36315u'
GL_GEOMETRY_INPUT_TYPE_EXT = 36315L # Variable c_uint '36315u'
GL_GEOMETRY_OUTPUT_TYPE = 35096L # Variable c_uint '35096u'
GL_GEOMETRY_OUTPUT_TYPE_ARB = 36316L # Variable c_uint '36316u'
GL_GEOMETRY_OUTPUT_TYPE_EXT = 36316L # Variable c_uint '36316u'
GL_GEOMETRY_PROGRAM_NV = 35878L # Variable c_uint '35878u'
GL_GEOMETRY_PROGRAM_PARAMETER_BUFFER_NV = 36259L # Variable c_uint '36259u'
GL_GEOMETRY_SHADER = 36313L # Variable c_uint '36313u'
GL_GEOMETRY_SHADER_ARB = 36313L # Variable c_uint '36313u'
GL_GEOMETRY_SHADER_BIT = 4L # Variable c_uint '4u'
GL_GEOMETRY_SHADER_EXT = 36313L # Variable c_uint '36313u'
GL_GEOMETRY_SHADER_INVOCATIONS = 34943L # Variable c_uint '34943u'
GL_GEOMETRY_VERTICES_OUT = 35094L # Variable c_uint '35094u'
GL_GEOMETRY_VERTICES_OUT_ARB = 36314L # Variable c_uint '36314u'
GL_GEOMETRY_VERTICES_OUT_EXT = 36314L # Variable c_uint '36314u'
GL_GEQUAL = 518L # Variable c_uint '518u'
GL_GLEXT_VERSION = 66L # Variable c_uint '66u'
GL_GLOBAL_ALPHA_FACTOR_SUN = 33242L # Variable c_uint '33242u'
GL_GLOBAL_ALPHA_SUN = 33241L # Variable c_uint '33241u'
GL_GPU_ADDRESS_NV = 36660L # Variable c_uint '36660u'
GL_GREATER = 516L # Variable c_uint '516u'
GL_GREEN = 6404L # Variable c_uint '6404u'
GL_GREEN_BIAS = 3353L # Variable c_uint '3353u'
GL_GREEN_BIT_ATI = 2L # Variable c_uint '2u'
GL_GREEN_BITS = 3411L # Variable c_uint '3411u'
GL_GREEN_INTEGER = 36245L # Variable c_uint '36245u'
GL_GREEN_INTEGER_EXT = 36245L # Variable c_uint '36245u'
GL_GREEN_MAX_CLAMP_INGR = 34149L # Variable c_uint '34149u'
GL_GREEN_MIN_CLAMP_INGR = 34145L # Variable c_uint '34145u'
GL_GREEN_SCALE = 3352L # Variable c_uint '3352u'
GL_GUILTY_CONTEXT_RESET_ARB = 33363L # Variable c_uint '33363u'
GL_HALF_APPLE = 5131L # Variable c_uint '5131u'
GL_HALF_BIAS_NEGATE_NV = 34107L # Variable c_uint '34107u'
GL_HALF_BIAS_NORMAL_NV = 34106L # Variable c_uint '34106u'
GL_HALF_BIT_ATI = 8L # Variable c_uint '8u'
GL_HALF_FLOAT = 5131L # Variable c_uint '5131u'
GL_HALF_FLOAT_ARB = 5131L # Variable c_uint '5131u'
GL_HALF_FLOAT_NV = 5131L # Variable c_uint '5131u'
GL_HI_BIAS_NV = 34580L # Variable c_uint '34580u'
GL_HIGH_FLOAT = 36338L # Variable c_uint '36338u'
GL_HIGH_INT = 36341L # Variable c_uint '36341u'
GL_HILO16_NV = 34552L # Variable c_uint '34552u'
GL_HILO8_NV = 34910L # Variable c_uint '34910u'
GL_HILO_NV = 34548L # Variable c_uint '34548u'
GL_HINT_BIT = 32768L # Variable c_uint '32768u'
GL_HI_SCALE_NV = 34574L # Variable c_uint '34574u'
GL_HISTOGRAM = 32804L # Variable c_uint '32804u'
GL_HISTOGRAM_ALPHA_SIZE = 32811L # Variable c_uint '32811u'
GL_HISTOGRAM_ALPHA_SIZE_EXT = 32811L # Variable c_uint '32811u'
GL_HISTOGRAM_BLUE_SIZE = 32810L # Variable c_uint '32810u'
GL_HISTOGRAM_BLUE_SIZE_EXT = 32810L # Variable c_uint '32810u'
GL_HISTOGRAM_EXT = 32804L # Variable c_uint '32804u'
GL_HISTOGRAM_FORMAT = 32807L # Variable c_uint '32807u'
GL_HISTOGRAM_FORMAT_EXT = 32807L # Variable c_uint '32807u'
GL_HISTOGRAM_GREEN_SIZE = 32809L # Variable c_uint '32809u'
GL_HISTOGRAM_GREEN_SIZE_EXT = 32809L # Variable c_uint '32809u'
GL_HISTOGRAM_LUMINANCE_SIZE = 32812L # Variable c_uint '32812u'
GL_HISTOGRAM_LUMINANCE_SIZE_EXT = 32812L # Variable c_uint '32812u'
GL_HISTOGRAM_RED_SIZE = 32808L # Variable c_uint '32808u'
GL_HISTOGRAM_RED_SIZE_EXT = 32808L # Variable c_uint '32808u'
GL_HISTOGRAM_SINK = 32813L # Variable c_uint '32813u'
GL_HISTOGRAM_SINK_EXT = 32813L # Variable c_uint '32813u'
GL_HISTOGRAM_WIDTH = 32806L # Variable c_uint '32806u'
GL_HISTOGRAM_WIDTH_EXT = 32806L # Variable c_uint '32806u'
GL_IDENTITY_NV = 34346L # Variable c_uint '34346u'
GL_IGNORE_BORDER_HP = 33104L # Variable c_uint '33104u'
GL_IMAGE_1D_ARRAY_EXT = 36946L # Variable c_uint '36946u'
GL_IMAGE_1D_EXT = 36940L # Variable c_uint '36940u'
GL_IMAGE_2D_ARRAY_EXT = 36947L # Variable c_uint '36947u'
GL_IMAGE_2D_EXT = 36941L # Variable c_uint '36941u'
GL_IMAGE_2D_MULTISAMPLE_ARRAY_EXT = 36950L # Variable c_uint '36950u'
GL_IMAGE_2D_MULTISAMPLE_EXT = 36949L # Variable c_uint '36949u'
GL_IMAGE_2D_RECT_EXT = 36943L # Variable c_uint '36943u'
GL_IMAGE_3D_EXT = 36942L # Variable c_uint '36942u'
GL_IMAGE_BINDING_ACCESS_EXT = 36670L # Variable c_uint '36670u'
GL_IMAGE_BINDING_FORMAT_EXT = 36974L # Variable c_uint '36974u'
GL_IMAGE_BINDING_LAYERED_EXT = 36668L # Variable c_uint '36668u'
GL_IMAGE_BINDING_LAYER_EXT = 36669L # Variable c_uint '36669u'
GL_IMAGE_BINDING_LEVEL_EXT = 36667L # Variable c_uint '36667u'
GL_IMAGE_BINDING_NAME_EXT = 36666L # Variable c_uint '36666u'
GL_IMAGE_BUFFER_EXT = 36945L # Variable c_uint '36945u'
GL_IMAGE_CUBE_EXT = 36944L # Variable c_uint '36944u'
GL_IMAGE_CUBE_MAP_ARRAY_EXT = 36948L # Variable c_uint '36948u'
GL_IMAGE_CUBIC_WEIGHT_HP = 33118L # Variable c_uint '33118u'
GL_IMAGE_MAG_FILTER_HP = 33116L # Variable c_uint '33116u'
GL_IMAGE_MIN_FILTER_HP = 33117L # Variable c_uint '33117u'
GL_IMAGE_ROTATE_ANGLE_HP = 33113L # Variable c_uint '33113u'
GL_IMAGE_ROTATE_ORIGIN_X_HP = 33114L # Variable c_uint '33114u'
GL_IMAGE_ROTATE_ORIGIN_Y_HP = 33115L # Variable c_uint '33115u'
GL_IMAGE_SCALE_X_HP = 33109L # Variable c_uint '33109u'
GL_IMAGE_SCALE_Y_HP = 33110L # Variable c_uint '33110u'
GL_IMAGE_TRANSFORM_2D_HP = 33121L # Variable c_uint '33121u'
GL_IMAGE_TRANSLATE_X_HP = 33111L # Variable c_uint '33111u'
GL_IMAGE_TRANSLATE_Y_HP = 33112L # Variable c_uint '33112u'
GL_IMPLEMENTATION_COLOR_READ_FORMAT = 35739L # Variable c_uint '35739u'
GL_IMPLEMENTATION_COLOR_READ_FORMAT_OES = 35739L # Variable c_uint '35739u'
GL_IMPLEMENTATION_COLOR_READ_TYPE = 35738L # Variable c_uint '35738u'
GL_IMPLEMENTATION_COLOR_READ_TYPE_OES = 35738L # Variable c_uint '35738u'
GL_INCR = 7682L # Variable c_uint '7682u'
GL_INCR_WRAP = 34055L # Variable c_uint '34055u'
GL_INCR_WRAP_EXT = 34055L # Variable c_uint '34055u'
GL_INDEX = 33314L # Variable c_uint '33314u'
GL_INDEX_ARRAY = 32887L # Variable c_uint '32887u'
GL_INDEX_ARRAY_ADDRESS_NV = 36644L # Variable c_uint '36644u'
GL_INDEX_ARRAY_BUFFER_BINDING = 34969L # Variable c_uint '34969u'
GL_INDEX_ARRAY_BUFFER_BINDING_ARB = 34969L # Variable c_uint '34969u'
GL_INDEX_ARRAY_COUNT_EXT = 32903L # Variable c_uint '32903u'
GL_INDEX_ARRAY_EXT = 32887L # Variable c_uint '32887u'
GL_INDEX_ARRAY_LENGTH_NV = 36654L # Variable c_uint '36654u'
GL_INDEX_ARRAY_LIST_IBM = 103073L # Variable c_uint '103073u'
GL_INDEX_ARRAY_LIST_STRIDE_IBM = 103083L # Variable c_uint '103083u'
GL_INDEX_ARRAY_POINTER = 32913L # Variable c_uint '32913u'
GL_INDEX_ARRAY_POINTER_EXT = 32913L # Variable c_uint '32913u'
GL_INDEX_ARRAY_STRIDE = 32902L # Variable c_uint '32902u'
GL_INDEX_ARRAY_STRIDE_EXT = 32902L # Variable c_uint '32902u'
GL_INDEX_ARRAY_TYPE = 32901L # Variable c_uint '32901u'
GL_INDEX_ARRAY_TYPE_EXT = 32901L # Variable c_uint '32901u'
GL_INDEX_BIT_PGI = 524288L # Variable c_uint '524288u'
GL_INDEX_BITS = 3409L # Variable c_uint '3409u'
GL_INDEX_CLEAR_VALUE = 3104L # Variable c_uint '3104u'
GL_INDEX_LOGIC_OP = 3057L # Variable c_uint '3057u'
GL_INDEX_MATERIAL_EXT = 33208L # Variable c_uint '33208u'
GL_INDEX_MATERIAL_FACE_EXT = 33210L # Variable c_uint '33210u'
GL_INDEX_MATERIAL_PARAMETER_EXT = 33209L # Variable c_uint '33209u'
GL_INDEX_MODE = 3120L # Variable c_uint '3120u'
GL_INDEX_OFFSET = 3347L # Variable c_uint '3347u'
GL_INDEX_SHIFT = 3346L # Variable c_uint '3346u'
GL_INDEX_TEST_EXT = 33205L # Variable c_uint '33205u'
GL_INDEX_TEST_FUNC_EXT = 33206L # Variable c_uint '33206u'
GL_INDEX_TEST_REF_EXT = 33207L # Variable c_uint '33207u'
GL_INDEX_WRITEMASK = 3105L # Variable c_uint '3105u'
GL_INFO_LOG_LENGTH = 35716L # Variable c_uint '35716u'
GL_INNOCENT_CONTEXT_RESET_ARB = 33364L # Variable c_uint '33364u'
GL_INSTRUMENT_BUFFER_POINTER_SGIX = 33152L # Variable c_uint '33152u'
GL_INSTRUMENT_MEASUREMENTS_SGIX = 33153L # Variable c_uint '33153u'
GL_INT = 5124L # Variable c_uint '5124u'
GL_INT16_NV = 36836L # Variable c_uint '36836u'
GL_INT16_VEC2_NV = 36837L # Variable c_uint '36837u'
GL_INT16_VEC3_NV = 36838L # Variable c_uint '36838u'
GL_INT16_VEC4_NV = 36839L # Variable c_uint '36839u'
GL_INT_2_10_10_10_REV = 36255L # Variable c_uint '36255u'
GL_INT64_NV = 5134L # Variable c_uint '5134u'
GL_INT64_VEC2_NV = 36841L # Variable c_uint '36841u'
GL_INT64_VEC3_NV = 36842L # Variable c_uint '36842u'
GL_INT64_VEC4_NV = 36843L # Variable c_uint '36843u'
GL_INT8_NV = 36832L # Variable c_uint '36832u'
GL_INT8_VEC2_NV = 36833L # Variable c_uint '36833u'
GL_INT8_VEC3_NV = 36834L # Variable c_uint '36834u'
GL_INT8_VEC4_NV = 36835L # Variable c_uint '36835u'
GL_INTENSITY = 32841L # Variable c_uint '32841u'
GL_INTENSITY12 = 32844L # Variable c_uint '32844u'
GL_INTENSITY12_EXT = 32844L # Variable c_uint '32844u'
GL_INTENSITY16 = 32845L # Variable c_uint '32845u'
GL_INTENSITY16_EXT = 32845L # Variable c_uint '32845u'
GL_INTENSITY16F_ARB = 34845L # Variable c_uint '34845u'
GL_INTENSITY16I_EXT = 36235L # Variable c_uint '36235u'
GL_INTENSITY16_SNORM = 36891L # Variable c_uint '36891u'
GL_INTENSITY16UI_EXT = 36217L # Variable c_uint '36217u'
GL_INTENSITY32F_ARB = 34839L # Variable c_uint '34839u'
GL_INTENSITY32I_EXT = 36229L # Variable c_uint '36229u'
GL_INTENSITY32UI_EXT = 36211L # Variable c_uint '36211u'
GL_INTENSITY4 = 32842L # Variable c_uint '32842u'
GL_INTENSITY4_EXT = 32842L # Variable c_uint '32842u'
GL_INTENSITY8 = 32843L # Variable c_uint '32843u'
GL_INTENSITY8_EXT = 32843L # Variable c_uint '32843u'
GL_INTENSITY8I_EXT = 36241L # Variable c_uint '36241u'
GL_INTENSITY8_SNORM = 36887L # Variable c_uint '36887u'
GL_INTENSITY8UI_EXT = 36223L # Variable c_uint '36223u'
GL_INTENSITY_EXT = 32841L # Variable c_uint '32841u'
GL_INTENSITY_FLOAT16_APPLE = 34845L # Variable c_uint '34845u'
GL_INTENSITY_FLOAT16_ATI = 34845L # Variable c_uint '34845u'
GL_INTENSITY_FLOAT32_APPLE = 34839L # Variable c_uint '34839u'
GL_INTENSITY_FLOAT32_ATI = 34839L # Variable c_uint '34839u'
GL_INTENSITY_SNORM = 36883L # Variable c_uint '36883u'
GL_INTERLACE_OML = 35200L # Variable c_uint '35200u'
GL_INTERLACE_READ_INGR = 34152L # Variable c_uint '34152u'
GL_INTERLACE_READ_OML = 35201L # Variable c_uint '35201u'
GL_INTERLACE_SGIX = 32916L # Variable c_uint '32916u'
GL_INTERLEAVED_ATTRIBS = 35980L # Variable c_uint '35980u'
GL_INTERLEAVED_ATTRIBS_EXT = 35980L # Variable c_uint '35980u'
GL_INTERLEAVED_ATTRIBS_NV = 35980L # Variable c_uint '35980u'
GL_INTERPOLATE = 34165L # Variable c_uint '34165u'
GL_INTERPOLATE_ARB = 34165L # Variable c_uint '34165u'
GL_INTERPOLATE_EXT = 34165L # Variable c_uint '34165u'
GL_INT_IMAGE_1D_ARRAY_EXT = 36957L # Variable c_uint '36957u'
GL_INT_IMAGE_1D_EXT = 36951L # Variable c_uint '36951u'
GL_INT_IMAGE_2D_ARRAY_EXT = 36958L # Variable c_uint '36958u'
GL_INT_IMAGE_2D_EXT = 36952L # Variable c_uint '36952u'
GL_INT_IMAGE_2D_MULTISAMPLE_ARRAY_EXT = 36961L # Variable c_uint '36961u'
GL_INT_IMAGE_2D_MULTISAMPLE_EXT = 36960L # Variable c_uint '36960u'
GL_INT_IMAGE_2D_RECT_EXT = 36954L # Variable c_uint '36954u'
GL_INT_IMAGE_3D_EXT = 36953L # Variable c_uint '36953u'
GL_INT_IMAGE_BUFFER_EXT = 36956L # Variable c_uint '36956u'
GL_INT_IMAGE_CUBE_EXT = 36955L # Variable c_uint '36955u'
GL_INT_IMAGE_CUBE_MAP_ARRAY_EXT = 36959L # Variable c_uint '36959u'
GL_INT_SAMPLER_1D = 36297L # Variable c_uint '36297u'
GL_INT_SAMPLER_1D_ARRAY = 36302L # Variable c_uint '36302u'
GL_INT_SAMPLER_1D_ARRAY_EXT = 36302L # Variable c_uint '36302u'
GL_INT_SAMPLER_1D_EXT = 36297L # Variable c_uint '36297u'
GL_INT_SAMPLER_2D = 36298L # Variable c_uint '36298u'
GL_INT_SAMPLER_2D_ARRAY = 36303L # Variable c_uint '36303u'
GL_INT_SAMPLER_2D_ARRAY_EXT = 36303L # Variable c_uint '36303u'
GL_INT_SAMPLER_2D_EXT = 36298L # Variable c_uint '36298u'
GL_INT_SAMPLER_2D_MULTISAMPLE = 37129L # Variable c_uint '37129u'
GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 37132L # Variable c_uint '37132u'
GL_INT_SAMPLER_2D_RECT = 36301L # Variable c_uint '36301u'
GL_INT_SAMPLER_2D_RECT_EXT = 36301L # Variable c_uint '36301u'
GL_INT_SAMPLER_3D = 36299L # Variable c_uint '36299u'
GL_INT_SAMPLER_3D_EXT = 36299L # Variable c_uint '36299u'
GL_INT_SAMPLER_BUFFER = 36304L # Variable c_uint '36304u'
GL_INT_SAMPLER_BUFFER_AMD = 36866L # Variable c_uint '36866u'
GL_INT_SAMPLER_BUFFER_EXT = 36304L # Variable c_uint '36304u'
GL_INT_SAMPLER_CUBE = 36300L # Variable c_uint '36300u'
GL_INT_SAMPLER_CUBE_EXT = 36300L # Variable c_uint '36300u'
GL_INT_SAMPLER_CUBE_MAP_ARRAY = 36878L # Variable c_uint '36878u'
GL_INT_SAMPLER_CUBE_MAP_ARRAY_ARB = 36878L # Variable c_uint '36878u'
GL_INT_SAMPLER_RENDERBUFFER_NV = 36439L # Variable c_uint '36439u'
GL_INT_VEC2 = 35667L # Variable c_uint '35667u'
GL_INT_VEC2_ARB = 35667L # Variable c_uint '35667u'
GL_INT_VEC3 = 35668L # Variable c_uint '35668u'
GL_INT_VEC3_ARB = 35668L # Variable c_uint '35668u'
GL_INT_VEC4 = 35669L # Variable c_uint '35669u'
GL_INT_VEC4_ARB = 35669L # Variable c_uint '35669u'
GL_INVALID_ENUM = 1280L # Variable c_uint '1280u'
GL_INVALID_FRAMEBUFFER_OPERATION = 1286L # Variable c_uint '1286u'
GL_INVALID_FRAMEBUFFER_OPERATION_EXT = 1286L # Variable c_uint '1286u'
GL_INVALID_OPERATION = 1282L # Variable c_uint '1282u'
GL_INVALID_VALUE = 1281L # Variable c_uint '1281u'
GL_INVARIANT_DATATYPE_EXT = 34795L # Variable c_uint '34795u'
GL_INVARIANT_EXT = 34754L # Variable c_uint '34754u'
GL_INVARIANT_VALUE_EXT = 34794L # Variable c_uint '34794u'
GL_INVERSE_NV = 34347L # Variable c_uint '34347u'
GL_INVERSE_TRANSPOSE_NV = 34349L # Variable c_uint '34349u'
GL_INVERT = 5386L # Variable c_uint '5386u'
GL_INVERTED_SCREEN_W_REND = 33937L # Variable c_uint '33937u'
GL_IR_INSTRUMENT1_SGIX = 33151L # Variable c_uint '33151u'
GL_ISOLINES = 36474L # Variable c_uint '36474u'
GL_IUI_N3F_V2F_EXT = 33199L # Variable c_uint '33199u'
GL_IUI_N3F_V3F_EXT = 33200L # Variable c_uint '33200u'
GL_IUI_V2F_EXT = 33197L # Variable c_uint '33197u'
GL_IUI_V3F_EXT = 33198L # Variable c_uint '33198u'
GL_KEEP = 7680L # Variable c_uint '7680u'
GL_LAST_VERTEX_CONVENTION = 36430L # Variable c_uint '36430u'
GL_LAST_VERTEX_CONVENTION_EXT = 36430L # Variable c_uint '36430u'
GL_LAST_VIDEO_CAPTURE_STATUS_NV = 36903L # Variable c_uint '36903u'
GL_LAYER_NV = 36266L # Variable c_uint '36266u'
GL_LAYER_PROVOKING_VERTEX = 33374L # Variable c_uint '33374u'
GL_LEFT = 1030L # Variable c_uint '1030u'
GL_LEQUAL = 515L # Variable c_uint '515u'
GL_LERP_ATI = 35177L # Variable c_uint '35177u'
GL_LESS = 513L # Variable c_uint '513u'
GL_LIGHT0 = 16384L # Variable c_uint '16384u'
GL_LIGHT1 = 16385L # Variable c_uint '16385u'
GL_LIGHT2 = 16386L # Variable c_uint '16386u'
GL_LIGHT3 = 16387L # Variable c_uint '16387u'
GL_LIGHT4 = 16388L # Variable c_uint '16388u'
GL_LIGHT5 = 16389L # Variable c_uint '16389u'
GL_LIGHT6 = 16390L # Variable c_uint '16390u'
GL_LIGHT7 = 16391L # Variable c_uint '16391u'
GL_LIGHT_ENV_MODE_SGIX = 33799L # Variable c_uint '33799u'
GL_LIGHTING = 2896L # Variable c_uint '2896u'
GL_LIGHTING_BIT = 64L # Variable c_uint '64u'
GL_LIGHT_MODEL_AMBIENT = 2899L # Variable c_uint '2899u'
GL_LIGHT_MODEL_COLOR_CONTROL = 33272L # Variable c_uint '33272u'
GL_LIGHT_MODEL_COLOR_CONTROL_EXT = 33272L # Variable c_uint '33272u'
GL_LIGHT_MODEL_LOCAL_VIEWER = 2897L # Variable c_uint '2897u'
GL_LIGHT_MODEL_SPECULAR_VECTOR_APPLE = 34224L # Variable c_uint '34224u'
GL_LIGHT_MODEL_TWO_SIDE = 2898L # Variable c_uint '2898u'
GL_LINE = 6913L # Variable c_uint '6913u'
GL_LINEAR = 9729L # Variable c_uint '9729u'
GL_LINEAR_ATTENUATION = 4616L # Variable c_uint '4616u'
GL_LINEAR_CLIPMAP_LINEAR_SGIX = 33136L # Variable c_uint '33136u'
GL_LINEAR_CLIPMAP_NEAREST_SGIX = 33871L # Variable c_uint '33871u'
GL_LINEAR_DETAIL_ALPHA_SGIS = 32920L # Variable c_uint '32920u'
GL_LINEAR_DETAIL_COLOR_SGIS = 32921L # Variable c_uint '32921u'
GL_LINEAR_DETAIL_SGIS = 32919L # Variable c_uint '32919u'
GL_LINEAR_MIPMAP_LINEAR = 9987L # Variable c_uint '9987u'
GL_LINEAR_MIPMAP_NEAREST = 9985L # Variable c_uint '9985u'
GL_LINEAR_SHARPEN_ALPHA_SGIS = 32942L # Variable c_uint '32942u'
GL_LINEAR_SHARPEN_COLOR_SGIS = 32943L # Variable c_uint '32943u'
GL_LINEAR_SHARPEN_SGIS = 32941L # Variable c_uint '32941u'
GL_LINE_BIT = 4L # Variable c_uint '4u'
GL_LINE_LOOP = 2L # Variable c_uint '2u'
GL_LINE_RESET_TOKEN = 1799L # Variable c_uint '1799u'
GL_LINES = 1L # Variable c_uint '1u'
GL_LINES_ADJACENCY = 10L # Variable c_uint '10u'
GL_LINES_ADJACENCY_ARB = 10L # Variable c_uint '10u'
GL_LINES_ADJACENCY_EXT = 10L # Variable c_uint '10u'
GL_LINE_SMOOTH = 2848L # Variable c_uint '2848u'
GL_LINE_SMOOTH_HINT = 3154L # Variable c_uint '3154u'
GL_LINE_STIPPLE = 2852L # Variable c_uint '2852u'
GL_LINE_STIPPLE_PATTERN = 2853L # Variable c_uint '2853u'
GL_LINE_STIPPLE_REPEAT = 2854L # Variable c_uint '2854u'
GL_LINE_STRIP = 3L # Variable c_uint '3u'
GL_LINE_STRIP_ADJACENCY = 11L # Variable c_uint '11u'
GL_LINE_STRIP_ADJACENCY_ARB = 11L # Variable c_uint '11u'
GL_LINE_STRIP_ADJACENCY_EXT = 11L # Variable c_uint '11u'
GL_LINE_TOKEN = 1794L # Variable c_uint '1794u'
GL_LINE_WIDTH = 2849L # Variable c_uint '2849u'
GL_LINE_WIDTH_GRANULARITY = 2851L # Variable c_uint '2851u'
GL_LINE_WIDTH_RANGE = 2850L # Variable c_uint '2850u'
GL_LINK_STATUS = 35714L # Variable c_uint '35714u'
GL_LIST_BASE = 2866L # Variable c_uint '2866u'
GL_LIST_BIT = 131072L # Variable c_uint '131072u'
GL_LIST_INDEX = 2867L # Variable c_uint '2867u'
GL_LIST_MODE = 2864L # Variable c_uint '2864u'
GL_LIST_PRIORITY_SGIX = 33154L # Variable c_uint '33154u'
GL_LOAD = 257L # Variable c_uint '257u'
GL_LO_BIAS_NV = 34581L # Variable c_uint '34581u'
GL_LOCAL_CONSTANT_DATATYPE_EXT = 34797L # Variable c_uint '34797u'
GL_LOCAL_CONSTANT_EXT = 34755L # Variable c_uint '34755u'
GL_LOCAL_CONSTANT_VALUE_EXT = 34796L # Variable c_uint '34796u'
GL_LOCAL_EXT = 34756L # Variable c_uint '34756u'
GL_LOGIC_OP = 3057L # Variable c_uint '3057u'
GL_LOGIC_OP_MODE = 3056L # Variable c_uint '3056u'
GL_LO_SCALE_NV = 34575L # Variable c_uint '34575u'
GL_LOSE_CONTEXT_ON_RESET_ARB = 33362L # Variable c_uint '33362u'
GL_LOWER_LEFT = 36001L # Variable c_uint '36001u'
GL_LOW_FLOAT = 36336L # Variable c_uint '36336u'
GL_LOW_INT = 36339L # Variable c_uint '36339u'
GL_LUMINANCE = 6409L # Variable c_uint '6409u'
GL_LUMINANCE12 = 32833L # Variable c_uint '32833u'
GL_LUMINANCE12_ALPHA12 = 32839L # Variable c_uint '32839u'
GL_LUMINANCE12_ALPHA12_EXT = 32839L # Variable c_uint '32839u'
GL_LUMINANCE12_ALPHA4 = 32838L # Variable c_uint '32838u'
GL_LUMINANCE12_ALPHA4_EXT = 32838L # Variable c_uint '32838u'
GL_LUMINANCE12_EXT = 32833L # Variable c_uint '32833u'
GL_LUMINANCE16 = 32834L # Variable c_uint '32834u'
GL_LUMINANCE16_ALPHA16 = 32840L # Variable c_uint '32840u'
GL_LUMINANCE16_ALPHA16_EXT = 32840L # Variable c_uint '32840u'
GL_LUMINANCE16_ALPHA16_SNORM = 36890L # Variable c_uint '36890u'
GL_LUMINANCE16_EXT = 32834L # Variable c_uint '32834u'
GL_LUMINANCE16F_ARB = 34846L # Variable c_uint '34846u'
GL_LUMINANCE16I_EXT = 36236L # Variable c_uint '36236u'
GL_LUMINANCE16_SNORM = 36889L # Variable c_uint '36889u'
GL_LUMINANCE16UI_EXT = 36218L # Variable c_uint '36218u'
GL_LUMINANCE32F_ARB = 34840L # Variable c_uint '34840u'
GL_LUMINANCE32I_EXT = 36230L # Variable c_uint '36230u'
GL_LUMINANCE32UI_EXT = 36212L # Variable c_uint '36212u'
GL_LUMINANCE4 = 32831L # Variable c_uint '32831u'
GL_LUMINANCE4_ALPHA4 = 32835L # Variable c_uint '32835u'
GL_LUMINANCE4_ALPHA4_EXT = 32835L # Variable c_uint '32835u'
GL_LUMINANCE4_EXT = 32831L # Variable c_uint '32831u'
GL_LUMINANCE6_ALPHA2 = 32836L # Variable c_uint '32836u'
GL_LUMINANCE6_ALPHA2_EXT = 32836L # Variable c_uint '32836u'
GL_LUMINANCE8 = 32832L # Variable c_uint '32832u'
GL_LUMINANCE8_ALPHA8 = 32837L # Variable c_uint '32837u'
GL_LUMINANCE8_ALPHA8_EXT = 32837L # Variable c_uint '32837u'
GL_LUMINANCE8_ALPHA8_SNORM = 36886L # Variable c_uint '36886u'
GL_LUMINANCE8_EXT = 32832L # Variable c_uint '32832u'
GL_LUMINANCE8I_EXT = 36242L # Variable c_uint '36242u'
GL_LUMINANCE8_SNORM = 36885L # Variable c_uint '36885u'
GL_LUMINANCE8UI_EXT = 36224L # Variable c_uint '36224u'
GL_LUMINANCE_ALPHA = 6410L # Variable c_uint '6410u'
GL_LUMINANCE_ALPHA16F_ARB = 34847L # Variable c_uint '34847u'
GL_LUMINANCE_ALPHA16I_EXT = 36237L # Variable c_uint '36237u'
GL_LUMINANCE_ALPHA16UI_EXT = 36219L # Variable c_uint '36219u'
GL_LUMINANCE_ALPHA32F_ARB = 34841L # Variable c_uint '34841u'
GL_LUMINANCE_ALPHA32I_EXT = 36231L # Variable c_uint '36231u'
GL_LUMINANCE_ALPHA32UI_EXT = 36213L # Variable c_uint '36213u'
GL_LUMINANCE_ALPHA8I_EXT = 36243L # Variable c_uint '36243u'
GL_LUMINANCE_ALPHA8UI_EXT = 36225L # Variable c_uint '36225u'
GL_LUMINANCE_ALPHA_FLOAT16_APPLE = 34847L # Variable c_uint '34847u'
GL_LUMINANCE_ALPHA_FLOAT16_ATI = 34847L # Variable c_uint '34847u'
GL_LUMINANCE_ALPHA_FLOAT32_APPLE = 34841L # Variable c_uint '34841u'
GL_LUMINANCE_ALPHA_FLOAT32_ATI = 34841L # Variable c_uint '34841u'
GL_LUMINANCE_ALPHA_INTEGER_EXT = 36253L # Variable c_uint '36253u'
GL_LUMINANCE_ALPHA_SNORM = 36882L # Variable c_uint '36882u'
GL_LUMINANCE_FLOAT16_APPLE = 34846L # Variable c_uint '34846u'
GL_LUMINANCE_FLOAT16_ATI = 34846L # Variable c_uint '34846u'
GL_LUMINANCE_FLOAT32_APPLE = 34840L # Variable c_uint '34840u'
GL_LUMINANCE_FLOAT32_ATI = 34840L # Variable c_uint '34840u'
GL_LUMINANCE_INTEGER_EXT = 36252L # Variable c_uint '36252u'
GL_LUMINANCE_SNORM = 36881L # Variable c_uint '36881u'
GL_MAD_ATI = 35176L # Variable c_uint '35176u'
GL_MAGNITUDE_BIAS_NV = 34584L # Variable c_uint '34584u'
GL_MAGNITUDE_SCALE_NV = 34578L # Variable c_uint '34578u'
GL_MAJOR_VERSION = 33307L # Variable c_uint '33307u'
GL_MAP1_BINORMAL_EXT = 33862L # Variable c_uint '33862u'
GL_MAP1_COLOR_4 = 3472L # Variable c_uint '3472u'
GL_MAP1_GRID_DOMAIN = 3536L # Variable c_uint '3536u'
GL_MAP1_GRID_SEGMENTS = 3537L # Variable c_uint '3537u'
GL_MAP1_INDEX = 3473L # Variable c_uint '3473u'
GL_MAP1_NORMAL = 3474L # Variable c_uint '3474u'
GL_MAP1_TANGENT_EXT = 33860L # Variable c_uint '33860u'
GL_MAP1_TEXTURE_COORD_1 = 3475L # Variable c_uint '3475u'
GL_MAP1_TEXTURE_COORD_2 = 3476L # Variable c_uint '3476u'
GL_MAP1_TEXTURE_COORD_3 = 3477L # Variable c_uint '3477u'
GL_MAP1_TEXTURE_COORD_4 = 3478L # Variable c_uint '3478u'
GL_MAP1_VERTEX_3 = 3479L # Variable c_uint '3479u'
GL_MAP1_VERTEX_4 = 3480L # Variable c_uint '3480u'
GL_MAP1_VERTEX_ATTRIB0_4_NV = 34400L # Variable c_uint '34400u'
GL_MAP1_VERTEX_ATTRIB10_4_NV = 34410L # Variable c_uint '34410u'
GL_MAP1_VERTEX_ATTRIB11_4_NV = 34411L # Variable c_uint '34411u'
GL_MAP1_VERTEX_ATTRIB12_4_NV = 34412L # Variable c_uint '34412u'
GL_MAP1_VERTEX_ATTRIB13_4_NV = 34413L # Variable c_uint '34413u'
GL_MAP1_VERTEX_ATTRIB14_4_NV = 34414L # Variable c_uint '34414u'
GL_MAP1_VERTEX_ATTRIB1_4_NV = 34401L # Variable c_uint '34401u'
GL_MAP1_VERTEX_ATTRIB15_4_NV = 34415L # Variable c_uint '34415u'
GL_MAP1_VERTEX_ATTRIB2_4_NV = 34402L # Variable c_uint '34402u'
GL_MAP1_VERTEX_ATTRIB3_4_NV = 34403L # Variable c_uint '34403u'
GL_MAP1_VERTEX_ATTRIB4_4_NV = 34404L # Variable c_uint '34404u'
GL_MAP1_VERTEX_ATTRIB5_4_NV = 34405L # Variable c_uint '34405u'
GL_MAP1_VERTEX_ATTRIB6_4_NV = 34406L # Variable c_uint '34406u'
GL_MAP1_VERTEX_ATTRIB7_4_NV = 34407L # Variable c_uint '34407u'
GL_MAP1_VERTEX_ATTRIB8_4_NV = 34408L # Variable c_uint '34408u'
GL_MAP1_VERTEX_ATTRIB9_4_NV = 34409L # Variable c_uint '34409u'
GL_MAP2_BINORMAL_EXT = 33863L # Variable c_uint '33863u'
GL_MAP2_COLOR_4 = 3504L # Variable c_uint '3504u'
GL_MAP2_GRID_DOMAIN = 3538L # Variable c_uint '3538u'
GL_MAP2_GRID_SEGMENTS = 3539L # Variable c_uint '3539u'
GL_MAP2_INDEX = 3505L # Variable c_uint '3505u'
GL_MAP2_NORMAL = 3506L # Variable c_uint '3506u'
GL_MAP2_TANGENT_EXT = 33861L # Variable c_uint '33861u'
GL_MAP2_TEXTURE_COORD_1 = 3507L # Variable c_uint '3507u'
GL_MAP2_TEXTURE_COORD_2 = 3508L # Variable c_uint '3508u'
GL_MAP2_TEXTURE_COORD_3 = 3509L # Variable c_uint '3509u'
GL_MAP2_TEXTURE_COORD_4 = 3510L # Variable c_uint '3510u'
GL_MAP2_VERTEX_3 = 3511L # Variable c_uint '3511u'
GL_MAP2_VERTEX_4 = 3512L # Variable c_uint '3512u'
GL_MAP2_VERTEX_ATTRIB0_4_NV = 34416L # Variable c_uint '34416u'
GL_MAP2_VERTEX_ATTRIB10_4_NV = 34426L # Variable c_uint '34426u'
GL_MAP2_VERTEX_ATTRIB11_4_NV = 34427L # Variable c_uint '34427u'
GL_MAP2_VERTEX_ATTRIB12_4_NV = 34428L # Variable c_uint '34428u'
GL_MAP2_VERTEX_ATTRIB13_4_NV = 34429L # Variable c_uint '34429u'
GL_MAP2_VERTEX_ATTRIB14_4_NV = 34430L # Variable c_uint '34430u'
GL_MAP2_VERTEX_ATTRIB1_4_NV = 34417L # Variable c_uint '34417u'
GL_MAP2_VERTEX_ATTRIB15_4_NV = 34431L # Variable c_uint '34431u'
GL_MAP2_VERTEX_ATTRIB2_4_NV = 34418L # Variable c_uint '34418u'
GL_MAP2_VERTEX_ATTRIB3_4_NV = 34419L # Variable c_uint '34419u'
GL_MAP2_VERTEX_ATTRIB4_4_NV = 34420L # Variable c_uint '34420u'
GL_MAP2_VERTEX_ATTRIB5_4_NV = 34421L # Variable c_uint '34421u'
GL_MAP2_VERTEX_ATTRIB6_4_NV = 34422L # Variable c_uint '34422u'
GL_MAP2_VERTEX_ATTRIB7_4_NV = 34423L # Variable c_uint '34423u'
GL_MAP2_VERTEX_ATTRIB8_4_NV = 34424L # Variable c_uint '34424u'
GL_MAP2_VERTEX_ATTRIB9_4_NV = 34425L # Variable c_uint '34425u'
GL_MAP_ATTRIB_U_ORDER_NV = 34499L # Variable c_uint '34499u'
GL_MAP_ATTRIB_V_ORDER_NV = 34500L # Variable c_uint '34500u'
GL_MAP_COLOR = 3344L # Variable c_uint '3344u'
GL_MAP_FLUSH_EXPLICIT_BIT = 16L # Variable c_uint '16u'
GL_MAP_INVALIDATE_BUFFER_BIT = 8L # Variable c_uint '8u'
GL_MAP_INVALIDATE_RANGE_BIT = 4L # Variable c_uint '4u'
GL_MAP_READ_BIT = 1L # Variable c_uint '1u'
GL_MAP_STENCIL = 3345L # Variable c_uint '3345u'
GL_MAP_TESSELLATION_NV = 34498L # Variable c_uint '34498u'
GL_MAP_UNSYNCHRONIZED_BIT = 32L # Variable c_uint '32u'
GL_MAP_WRITE_BIT = 2L # Variable c_uint '2u'
GL_MAT_AMBIENT_AND_DIFFUSE_BIT_PGI = 2097152L # Variable c_uint '2097152u'
GL_MAT_AMBIENT_BIT_PGI = 1048576L # Variable c_uint '1048576u'
GL_MAT_COLOR_INDEXES_BIT_PGI = 16777216L # Variable c_uint '16777216u'
GL_MAT_DIFFUSE_BIT_PGI = 4194304L # Variable c_uint '4194304u'
GL_MAT_EMISSION_BIT_PGI = 8388608L # Variable c_uint '8388608u'
GL_MATERIAL_SIDE_HINT_PGI = 107052L # Variable c_uint '107052u'
GL_MATRIX0_ARB = 35008L # Variable c_uint '35008u'
GL_MATRIX0_NV = 34352L # Variable c_uint '34352u'
GL_MATRIX10_ARB = 35018L # Variable c_uint '35018u'
GL_MATRIX11_ARB = 35019L # Variable c_uint '35019u'
GL_MATRIX12_ARB = 35020L # Variable c_uint '35020u'
GL_MATRIX13_ARB = 35021L # Variable c_uint '35021u'
GL_MATRIX14_ARB = 35022L # Variable c_uint '35022u'
GL_MATRIX15_ARB = 35023L # Variable c_uint '35023u'
GL_MATRIX16_ARB = 35024L # Variable c_uint '35024u'
GL_MATRIX17_ARB = 35025L # Variable c_uint '35025u'
GL_MATRIX18_ARB = 35026L # Variable c_uint '35026u'
GL_MATRIX19_ARB = 35027L # Variable c_uint '35027u'
GL_MATRIX1_ARB = 35009L # Variable c_uint '35009u'
GL_MATRIX1_NV = 34353L # Variable c_uint '34353u'
GL_MATRIX20_ARB = 35028L # Variable c_uint '35028u'
GL_MATRIX21_ARB = 35029L # Variable c_uint '35029u'
GL_MATRIX22_ARB = 35030L # Variable c_uint '35030u'
GL_MATRIX23_ARB = 35031L # Variable c_uint '35031u'
GL_MATRIX24_ARB = 35032L # Variable c_uint '35032u'
GL_MATRIX25_ARB = 35033L # Variable c_uint '35033u'
GL_MATRIX26_ARB = 35034L # Variable c_uint '35034u'
GL_MATRIX27_ARB = 35035L # Variable c_uint '35035u'
GL_MATRIX28_ARB = 35036L # Variable c_uint '35036u'
GL_MATRIX29_ARB = 35037L # Variable c_uint '35037u'
GL_MATRIX2_ARB = 35010L # Variable c_uint '35010u'
GL_MATRIX2_NV = 34354L # Variable c_uint '34354u'
GL_MATRIX30_ARB = 35038L # Variable c_uint '35038u'
GL_MATRIX31_ARB = 35039L # Variable c_uint '35039u'
GL_MATRIX3_ARB = 35011L # Variable c_uint '35011u'
GL_MATRIX3_NV = 34355L # Variable c_uint '34355u'
GL_MATRIX4_ARB = 35012L # Variable c_uint '35012u'
GL_MATRIX4_NV = 34356L # Variable c_uint '34356u'
GL_MATRIX5_ARB = 35013L # Variable c_uint '35013u'
GL_MATRIX5_NV = 34357L # Variable c_uint '34357u'
GL_MATRIX6_ARB = 35014L # Variable c_uint '35014u'
GL_MATRIX6_NV = 34358L # Variable c_uint '34358u'
GL_MATRIX7_ARB = 35015L # Variable c_uint '35015u'
GL_MATRIX7_NV = 34359L # Variable c_uint '34359u'
GL_MATRIX8_ARB = 35016L # Variable c_uint '35016u'
GL_MATRIX9_ARB = 35017L # Variable c_uint '35017u'
GL_MATRIX_EXT = 34752L # Variable c_uint '34752u'
GL_MATRIX_INDEX_ARRAY_ARB = 34884L # Variable c_uint '34884u'
GL_MATRIX_INDEX_ARRAY_POINTER_ARB = 34889L # Variable c_uint '34889u'
GL_MATRIX_INDEX_ARRAY_SIZE_ARB = 34886L # Variable c_uint '34886u'
GL_MATRIX_INDEX_ARRAY_STRIDE_ARB = 34888L # Variable c_uint '34888u'
GL_MATRIX_INDEX_ARRAY_TYPE_ARB = 34887L # Variable c_uint '34887u'
GL_MATRIX_MODE = 2976L # Variable c_uint '2976u'
GL_MATRIX_PALETTE_ARB = 34880L # Variable c_uint '34880u'
GL_MAT_SHININESS_BIT_PGI = 33554432L # Variable c_uint '33554432u'
GL_MAT_SPECULAR_BIT_PGI = 67108864L # Variable c_uint '67108864u'
GL_MAX = 32776L # Variable c_uint '32776u'
GL_MAX_3D_TEXTURE_SIZE = 32883L # Variable c_uint '32883u'
GL_MAX_3D_TEXTURE_SIZE_EXT = 32883L # Variable c_uint '32883u'
GL_MAX_4D_TEXTURE_SIZE_SGIS = 33080L # Variable c_uint '33080u'
GL_MAX_ACTIVE_LIGHTS_SGIX = 33797L # Variable c_uint '33797u'
GL_MAX_ARRAY_TEXTURE_LAYERS = 35071L # Variable c_uint '35071u'
GL_MAX_ARRAY_TEXTURE_LAYERS_EXT = 35071L # Variable c_uint '35071u'
GL_MAX_ASYNC_DRAW_PIXELS_SGIX = 33632L # Variable c_uint '33632u'
GL_MAX_ASYNC_HISTOGRAM_SGIX = 33581L # Variable c_uint '33581u'
GL_MAX_ASYNC_READ_PIXELS_SGIX = 33633L # Variable c_uint '33633u'
GL_MAX_ASYNC_TEX_IMAGE_SGIX = 33631L # Variable c_uint '33631u'
GL_MAX_ATTRIB_STACK_DEPTH = 3381L # Variable c_uint '3381u'
GL_MAX_BINDABLE_UNIFORM_SIZE_EXT = 36333L # Variable c_uint '36333u'
GL_MAX_CLIENT_ATTRIB_STACK_DEPTH = 3387L # Variable c_uint '3387u'
GL_MAX_CLIP_DISTANCES = 3378L # Variable c_uint '3378u'
GL_MAX_CLIPMAP_DEPTH_SGIX = 33143L # Variable c_uint '33143u'
GL_MAX_CLIPMAP_VIRTUAL_DEPTH_SGIX = 33144L # Variable c_uint '33144u'
GL_MAX_CLIP_PLANES = 3378L # Variable c_uint '3378u'
GL_MAX_COLOR_ATTACHMENTS = 36063L # Variable c_uint '36063u'
GL_MAX_COLOR_ATTACHMENTS_EXT = 36063L # Variable c_uint '36063u'
GL_MAX_COLOR_MATRIX_STACK_DEPTH = 32947L # Variable c_uint '32947u'
GL_MAX_COLOR_MATRIX_STACK_DEPTH_SGI = 32947L # Variable c_uint '32947u'
GL_MAX_COLOR_TEXTURE_SAMPLES = 37134L # Variable c_uint '37134u'
GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS = 35379L # Variable c_uint '35379u'
GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS = 35378L # Variable c_uint '35378u'
GL_MAX_COMBINED_IMAGE_UNITS_AND_FRAGMENT_OUTPUTS_EXT = 36665L # Variable c_uint '36665u'
GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS = 36382L # Variable c_uint '36382u'
GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS = 36383L # Variable c_uint '36383u'
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS = 35661L # Variable c_uint '35661u'
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS_ARB = 35661L # Variable c_uint '35661u'
GL_MAX_COMBINED_UNIFORM_BLOCKS = 35374L # Variable c_uint '35374u'
GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS = 35377L # Variable c_uint '35377u'
GL_MAX_CONVOLUTION_HEIGHT = 32795L # Variable c_uint '32795u'
GL_MAX_CONVOLUTION_HEIGHT_EXT = 32795L # Variable c_uint '32795u'
GL_MAX_CONVOLUTION_WIDTH = 32794L # Variable c_uint '32794u'
GL_MAX_CONVOLUTION_WIDTH_EXT = 32794L # Variable c_uint '32794u'
GL_MAX_CUBE_MAP_TEXTURE_SIZE = 34076L # Variable c_uint '34076u'
GL_MAX_CUBE_MAP_TEXTURE_SIZE_ARB = 34076L # Variable c_uint '34076u'
GL_MAX_CUBE_MAP_TEXTURE_SIZE_EXT = 34076L # Variable c_uint '34076u'
GL_MAX_DEBUG_LOGGED_MESSAGES_AMD = 37188L # Variable c_uint '37188u'
GL_MAX_DEBUG_LOGGED_MESSAGES_ARB = 37188L # Variable c_uint '37188u'
GL_MAX_DEBUG_MESSAGE_LENGTH_ARB = 37187L # Variable c_uint '37187u'
GL_MAX_DEFORMATION_ORDER_SGIX = 33175L # Variable c_uint '33175u'
GL_MAX_DEPTH_TEXTURE_SAMPLES = 37135L # Variable c_uint '37135u'
GL_MAX_DRAW_BUFFERS = 34852L # Variable c_uint '34852u'
GL_MAX_DRAW_BUFFERS_ARB = 34852L # Variable c_uint '34852u'
GL_MAX_DRAW_BUFFERS_ATI = 34852L # Variable c_uint '34852u'
GL_MAX_DUAL_SOURCE_DRAW_BUFFERS = 35068L # Variable c_uint '35068u'
GL_MAX_ELEMENTS_INDICES = 33001L # Variable c_uint '33001u'
GL_MAX_ELEMENTS_INDICES_EXT = 33001L # Variable c_uint '33001u'
GL_MAX_ELEMENTS_VERTICES = 33000L # Variable c_uint '33000u'
GL_MAX_ELEMENTS_VERTICES_EXT = 33000L # Variable c_uint '33000u'
GL_MAX_EVAL_ORDER = 3376L # Variable c_uint '3376u'
GL_MAX_EXT = 32776L # Variable c_uint '32776u'
GL_MAX_FOG_FUNC_POINTS_SGIS = 33068L # Variable c_uint '33068u'
GL_MAX_FRAGMENT_BINDABLE_UNIFORMS_EXT = 36323L # Variable c_uint '36323u'
GL_MAX_FRAGMENT_INPUT_COMPONENTS = 37157L # Variable c_uint '37157u'
GL_MAX_FRAGMENT_INTERPOLATION_OFFSET = 36444L # Variable c_uint '36444u'
GL_MAX_FRAGMENT_INTERPOLATION_OFFSET_NV = 36444L # Variable c_uint '36444u'
GL_MAX_FRAGMENT_LIGHTS_SGIX = 33796L # Variable c_uint '33796u'
GL_MAX_FRAGMENT_PROGRAM_LOCAL_PARAMETERS_NV = 34920L # Variable c_uint '34920u'
GL_MAX_FRAGMENT_UNIFORM_BLOCKS = 35373L # Variable c_uint '35373u'
GL_MAX_FRAGMENT_UNIFORM_COMPONENTS = 35657L # Variable c_uint '35657u'
GL_MAX_FRAGMENT_UNIFORM_COMPONENTS_ARB = 35657L # Variable c_uint '35657u'
GL_MAX_FRAGMENT_UNIFORM_VECTORS = 36349L # Variable c_uint '36349u'
GL_MAX_FRAMEZOOM_FACTOR_SGIX = 33165L # Variable c_uint '33165u'
GL_MAX_GENERAL_COMBINERS_NV = 34125L # Variable c_uint '34125u'
GL_MAX_GEOMETRY_BINDABLE_UNIFORMS_EXT = 36324L # Variable c_uint '36324u'
GL_MAX_GEOMETRY_INPUT_COMPONENTS = 37155L # Variable c_uint '37155u'
GL_MAX_GEOMETRY_OUTPUT_COMPONENTS = 37156L # Variable c_uint '37156u'
GL_MAX_GEOMETRY_OUTPUT_VERTICES = 36320L # Variable c_uint '36320u'
GL_MAX_GEOMETRY_OUTPUT_VERTICES_ARB = 36320L # Variable c_uint '36320u'
GL_MAX_GEOMETRY_OUTPUT_VERTICES_EXT = 36320L # Variable c_uint '36320u'
GL_MAX_GEOMETRY_PROGRAM_INVOCATIONS_NV = 36442L # Variable c_uint '36442u'
GL_MAX_GEOMETRY_SHADER_INVOCATIONS = 36442L # Variable c_uint '36442u'
GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS = 35881L # Variable c_uint '35881u'
GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_ARB = 35881L # Variable c_uint '35881u'
GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_EXT = 35881L # Variable c_uint '35881u'
GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS = 36321L # Variable c_uint '36321u'
GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_ARB = 36321L # Variable c_uint '36321u'
GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_EXT = 36321L # Variable c_uint '36321u'
GL_MAX_GEOMETRY_UNIFORM_BLOCKS = 35372L # Variable c_uint '35372u'
GL_MAX_GEOMETRY_UNIFORM_COMPONENTS = 36319L # Variable c_uint '36319u'
GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_ARB = 36319L # Variable c_uint '36319u'
GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_EXT = 36319L # Variable c_uint '36319u'
GL_MAX_GEOMETRY_VARYING_COMPONENTS_ARB = 36317L # Variable c_uint '36317u'
GL_MAX_GEOMETRY_VARYING_COMPONENTS_EXT = 36317L # Variable c_uint '36317u'
GL_MAX_IMAGE_SAMPLES_EXT = 36973L # Variable c_uint '36973u'
GL_MAX_IMAGE_UNITS_EXT = 36664L # Variable c_uint '36664u'
GL_MAX_INTEGER_SAMPLES = 37136L # Variable c_uint '37136u'
GL_MAX_LIGHTS = 3377L # Variable c_uint '3377u'
GL_MAX_LIST_NESTING = 2865L # Variable c_uint '2865u'
GL_MAX_MAP_TESSELLATION_NV = 34518L # Variable c_uint '34518u'
GL_MAX_MATRIX_PALETTE_STACK_DEPTH_ARB = 34881L # Variable c_uint '34881u'
GL_MAX_MODELVIEW_STACK_DEPTH = 3382L # Variable c_uint '3382u'
GL_MAX_MULTISAMPLE_COVERAGE_MODES_NV = 36369L # Variable c_uint '36369u'
GL_MAX_NAME_STACK_DEPTH = 3383L # Variable c_uint '3383u'
GL_MAX_OPTIMIZED_VERTEX_SHADER_INSTRUCTIONS_EXT = 34762L # Variable c_uint '34762u'
GL_MAX_OPTIMIZED_VERTEX_SHADER_INVARIANTS_EXT = 34765L # Variable c_uint '34765u'
GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = 34764L # Variable c_uint '34764u'
GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCALS_EXT = 34766L # Variable c_uint '34766u'
GL_MAX_OPTIMIZED_VERTEX_SHADER_VARIANTS_EXT = 34763L # Variable c_uint '34763u'
GL_MAX_PALETTE_MATRICES_ARB = 34882L # Variable c_uint '34882u'
GL_MAX_PATCH_VERTICES = 36477L # Variable c_uint '36477u'
GL_MAX_PIXEL_MAP_TABLE = 3380L # Variable c_uint '3380u'
GL_MAX_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT = 33591L # Variable c_uint '33591u'
GL_MAX_PN_TRIANGLES_TESSELATION_LEVEL_ATI = 34801L # Variable c_uint '34801u'
GL_MAX_PROGRAM_ADDRESS_REGISTERS_ARB = 34993L # Variable c_uint '34993u'
GL_MAX_PROGRAM_ALU_INSTRUCTIONS_ARB = 34827L # Variable c_uint '34827u'
GL_MAX_PROGRAM_ATTRIB_COMPONENTS_NV = 35080L # Variable c_uint '35080u'
GL_MAX_PROGRAM_ATTRIBS_ARB = 34989L # Variable c_uint '34989u'
GL_MAX_PROGRAM_CALL_DEPTH_NV = 35061L # Variable c_uint '35061u'
GL_MAX_PROGRAM_ENV_PARAMETERS_ARB = 34997L # Variable c_uint '34997u'
GL_MAX_PROGRAM_EXEC_INSTRUCTIONS_NV = 35060L # Variable c_uint '35060u'
GL_MAX_PROGRAM_GENERIC_ATTRIBS_NV = 36261L # Variable c_uint '36261u'
GL_MAX_PROGRAM_GENERIC_RESULTS_NV = 36262L # Variable c_uint '36262u'
GL_MAX_PROGRAM_IF_DEPTH_NV = 35062L # Variable c_uint '35062u'
GL_MAX_PROGRAM_INSTRUCTIONS_ARB = 34977L # Variable c_uint '34977u'
GL_MAX_PROGRAM_LOCAL_PARAMETERS_ARB = 34996L # Variable c_uint '34996u'
GL_MAX_PROGRAM_LOOP_COUNT_NV = 35064L # Variable c_uint '35064u'
GL_MAX_PROGRAM_LOOP_DEPTH_NV = 35063L # Variable c_uint '35063u'
GL_MAX_PROGRAM_MATRICES_ARB = 34351L # Variable c_uint '34351u'
GL_MAX_PROGRAM_MATRIX_STACK_DEPTH_ARB = 34350L # Variable c_uint '34350u'
GL_MAX_PROGRAM_NATIVE_ADDRESS_REGISTERS_ARB = 34995L # Variable c_uint '34995u'
GL_MAX_PROGRAM_NATIVE_ALU_INSTRUCTIONS_ARB = 34830L # Variable c_uint '34830u'
GL_MAX_PROGRAM_NATIVE_ATTRIBS_ARB = 34991L # Variable c_uint '34991u'
GL_MAX_PROGRAM_NATIVE_INSTRUCTIONS_ARB = 34979L # Variable c_uint '34979u'
GL_MAX_PROGRAM_NATIVE_PARAMETERS_ARB = 34987L # Variable c_uint '34987u'
GL_MAX_PROGRAM_NATIVE_TEMPORARIES_ARB = 34983L # Variable c_uint '34983u'
GL_MAX_PROGRAM_NATIVE_TEX_INDIRECTIONS_ARB = 34832L # Variable c_uint '34832u'
GL_MAX_PROGRAM_NATIVE_TEX_INSTRUCTIONS_ARB = 34831L # Variable c_uint '34831u'
GL_MAX_PROGRAM_OUTPUT_VERTICES_NV = 35879L # Variable c_uint '35879u'
GL_MAX_PROGRAM_PARAMETER_BUFFER_BINDINGS_NV = 36256L # Variable c_uint '36256u'
GL_MAX_PROGRAM_PARAMETER_BUFFER_SIZE_NV = 36257L # Variable c_uint '36257u'
GL_MAX_PROGRAM_PARAMETERS_ARB = 34985L # Variable c_uint '34985u'
GL_MAX_PROGRAM_PATCH_ATTRIBS_NV = 34520L # Variable c_uint '34520u'
GL_MAX_PROGRAM_RESULT_COMPONENTS_NV = 35081L # Variable c_uint '35081u'
GL_MAX_PROGRAM_SUBROUTINE_NUM_NV = 36677L # Variable c_uint '36677u'
GL_MAX_PROGRAM_SUBROUTINE_PARAMETERS_NV = 36676L # Variable c_uint '36676u'
GL_MAX_PROGRAM_TEMPORARIES_ARB = 34981L # Variable c_uint '34981u'
GL_MAX_PROGRAM_TEXEL_OFFSET = 35077L # Variable c_uint '35077u'
GL_MAX_PROGRAM_TEXEL_OFFSET_NV = 35077L # Variable c_uint '35077u'
GL_MAX_PROGRAM_TEX_INDIRECTIONS_ARB = 34829L # Variable c_uint '34829u'
GL_MAX_PROGRAM_TEX_INSTRUCTIONS_ARB = 34828L # Variable c_uint '34828u'
GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET = 36447L # Variable c_uint '36447u'
GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET_ARB = 36447L # Variable c_uint '36447u'
GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET_NV = 36447L # Variable c_uint '36447u'
GL_MAX_PROGRAM_TOTAL_OUTPUT_COMPONENTS_NV = 35880L # Variable c_uint '35880u'
GL_MAX_PROJECTION_STACK_DEPTH = 3384L # Variable c_uint '3384u'
GL_MAX_RATIONAL_EVAL_ORDER_NV = 34519L # Variable c_uint '34519u'
GL_MAX_RECTANGLE_TEXTURE_SIZE = 34040L # Variable c_uint '34040u'
GL_MAX_RECTANGLE_TEXTURE_SIZE_ARB = 34040L # Variable c_uint '34040u'
GL_MAX_RECTANGLE_TEXTURE_SIZE_NV = 34040L # Variable c_uint '34040u'
GL_MAX_RENDERBUFFER_SIZE = 34024L # Variable c_uint '34024u'
GL_MAX_RENDERBUFFER_SIZE_EXT = 34024L # Variable c_uint '34024u'
GL_MAX_SAMPLE_MASK_WORDS = 36441L # Variable c_uint '36441u'
GL_MAX_SAMPLE_MASK_WORDS_NV = 36441L # Variable c_uint '36441u'
GL_MAX_SAMPLES = 36183L # Variable c_uint '36183u'
GL_MAX_SAMPLES_EXT = 36183L # Variable c_uint '36183u'
GL_MAX_SERVER_WAIT_TIMEOUT = 37137L # Variable c_uint '37137u'
GL_MAX_SHADER_BUFFER_ADDRESS_NV = 36661L # Variable c_uint '36661u'
GL_MAX_SHININESS_NV = 34052L # Variable c_uint '34052u'
GL_MAX_SPOT_EXPONENT_NV = 34053L # Variable c_uint '34053u'
GL_MAX_SUBROUTINES = 36327L # Variable c_uint '36327u'
GL_MAX_SUBROUTINE_UNIFORM_LOCATIONS = 36328L # Variable c_uint '36328u'
GL_MAX_TESS_CONTROL_INPUT_COMPONENTS = 34924L # Variable c_uint '34924u'
GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS = 36483L # Variable c_uint '36483u'
GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS = 36481L # Variable c_uint '36481u'
GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS = 36485L # Variable c_uint '36485u'
GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS = 36489L # Variable c_uint '36489u'
GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS = 36479L # Variable c_uint '36479u'
GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS = 34925L # Variable c_uint '34925u'
GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS = 36486L # Variable c_uint '36486u'
GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS = 36482L # Variable c_uint '36482u'
GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS = 36490L # Variable c_uint '36490u'
GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS = 36480L # Variable c_uint '36480u'
GL_MAX_TESS_GEN_LEVEL = 36478L # Variable c_uint '36478u'
GL_MAX_TESS_PATCH_COMPONENTS = 36484L # Variable c_uint '36484u'
GL_MAX_TEXTURE_BUFFER_SIZE = 35883L # Variable c_uint '35883u'
GL_MAX_TEXTURE_BUFFER_SIZE_ARB = 35883L # Variable c_uint '35883u'
GL_MAX_TEXTURE_BUFFER_SIZE_EXT = 35883L # Variable c_uint '35883u'
GL_MAX_TEXTURE_COORDS = 34929L # Variable c_uint '34929u'
GL_MAX_TEXTURE_COORDS_ARB = 34929L # Variable c_uint '34929u'
GL_MAX_TEXTURE_COORDS_NV = 34929L # Variable c_uint '34929u'
GL_MAX_TEXTURE_IMAGE_UNITS = 34930L # Variable c_uint '34930u'
GL_MAX_TEXTURE_IMAGE_UNITS_ARB = 34930L # Variable c_uint '34930u'
GL_MAX_TEXTURE_IMAGE_UNITS_NV = 34930L # Variable c_uint '34930u'
GL_MAX_TEXTURE_LOD_BIAS = 34045L # Variable c_uint '34045u'
GL_MAX_TEXTURE_LOD_BIAS_EXT = 34045L # Variable c_uint '34045u'
GL_MAX_TEXTURE_MAX_ANISOTROPY_EXT = 34047L # Variable c_uint '34047u'
GL_MAX_TEXTURE_SIZE = 3379L # Variable c_uint '3379u'
GL_MAX_TEXTURE_STACK_DEPTH = 3385L # Variable c_uint '3385u'
GL_MAX_TEXTURE_UNITS = 34018L # Variable c_uint '34018u'
GL_MAX_TEXTURE_UNITS_ARB = 34018L # Variable c_uint '34018u'
GL_MAX_TRACK_MATRICES_NV = 34351L # Variable c_uint '34351u'
GL_MAX_TRACK_MATRIX_STACK_DEPTH_NV = 34350L # Variable c_uint '34350u'
GL_MAX_TRANSFORM_FEEDBACK_BUFFERS = 36464L # Variable c_uint '36464u'
GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_ATTRIBS_NV = 35978L # Variable c_uint '35978u'
GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS = 35978L # Variable c_uint '35978u'
GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS_EXT = 35978L # Variable c_uint '35978u'
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS = 35979L # Variable c_uint '35979u'
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS_EXT = 35979L # Variable c_uint '35979u'
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS_NV = 35979L # Variable c_uint '35979u'
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS = 35968L # Variable c_uint '35968u'
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS_EXT = 35968L # Variable c_uint '35968u'
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS_NV = 35968L # Variable c_uint '35968u'
GL_MAX_UNIFORM_BLOCK_SIZE = 35376L # Variable c_uint '35376u'
GL_MAX_UNIFORM_BUFFER_BINDINGS = 35375L # Variable c_uint '35375u'
GL_MAX_VARYING_COMPONENTS = 35659L # Variable c_uint '35659u'
GL_MAX_VARYING_COMPONENTS_EXT = 35659L # Variable c_uint '35659u'
GL_MAX_VARYING_FLOATS = 35659L # Variable c_uint '35659u'
GL_MAX_VARYING_FLOATS_ARB = 35659L # Variable c_uint '35659u'
GL_MAX_VARYING_VECTORS = 36348L # Variable c_uint '36348u'
GL_MAX_VERTEX_ARRAY_RANGE_ELEMENT_NV = 34080L # Variable c_uint '34080u'
GL_MAX_VERTEX_ATTRIBS = 34921L # Variable c_uint '34921u'
GL_MAX_VERTEX_ATTRIBS_ARB = 34921L # Variable c_uint '34921u'
GL_MAX_VERTEX_BINDABLE_UNIFORMS_EXT = 36322L # Variable c_uint '36322u'
GL_MAX_VERTEX_HINT_PGI = 107053L # Variable c_uint '107053u'
GL_MAX_VERTEX_OUTPUT_COMPONENTS = 37154L # Variable c_uint '37154u'
GL_MAX_VERTEX_SHADER_INSTRUCTIONS_EXT = 34757L # Variable c_uint '34757u'
GL_MAX_VERTEX_SHADER_INVARIANTS_EXT = 34759L # Variable c_uint '34759u'
GL_MAX_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = 34760L # Variable c_uint '34760u'
GL_MAX_VERTEX_SHADER_LOCALS_EXT = 34761L # Variable c_uint '34761u'
GL_MAX_VERTEX_SHADER_VARIANTS_EXT = 34758L # Variable c_uint '34758u'
GL_MAX_VERTEX_STREAMS = 36465L # Variable c_uint '36465u'
GL_MAX_VERTEX_STREAMS_ATI = 34667L # Variable c_uint '34667u'
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS = 35660L # Variable c_uint '35660u'
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS_ARB = 35660L # Variable c_uint '35660u'
GL_MAX_VERTEX_UNIFORM_BLOCKS = 35371L # Variable c_uint '35371u'
GL_MAX_VERTEX_UNIFORM_COMPONENTS = 35658L # Variable c_uint '35658u'
GL_MAX_VERTEX_UNIFORM_COMPONENTS_ARB = 35658L # Variable c_uint '35658u'
GL_MAX_VERTEX_UNIFORM_VECTORS = 36347L # Variable c_uint '36347u'
GL_MAX_VERTEX_UNITS_ARB = 34468L # Variable c_uint '34468u'
GL_MAX_VERTEX_VARYING_COMPONENTS_ARB = 36318L # Variable c_uint '36318u'
GL_MAX_VERTEX_VARYING_COMPONENTS_EXT = 36318L # Variable c_uint '36318u'
GL_MAX_VIEWPORT_DIMS = 3386L # Variable c_uint '3386u'
GL_MAX_VIEWPORTS = 33371L # Variable c_uint '33371u'
GL_MEDIUM_FLOAT = 36337L # Variable c_uint '36337u'
GL_MEDIUM_INT = 36340L # Variable c_uint '36340u'
GL_MIN = 32775L # Variable c_uint '32775u'
GL_MIN_EXT = 32775L # Variable c_uint '32775u'
GL_MIN_FRAGMENT_INTERPOLATION_OFFSET = 36443L # Variable c_uint '36443u'
GL_MIN_FRAGMENT_INTERPOLATION_OFFSET_NV = 36443L # Variable c_uint '36443u'
GL_MINMAX = 32814L # Variable c_uint '32814u'
GL_MINMAX_EXT = 32814L # Variable c_uint '32814u'
GL_MINMAX_FORMAT = 32815L # Variable c_uint '32815u'
GL_MINMAX_FORMAT_EXT = 32815L # Variable c_uint '32815u'
GL_MINMAX_SINK = 32816L # Variable c_uint '32816u'
GL_MINMAX_SINK_EXT = 32816L # Variable c_uint '32816u'
GL_MINOR_VERSION = 33308L # Variable c_uint '33308u'
GL_MIN_PROGRAM_TEXEL_OFFSET = 35076L # Variable c_uint '35076u'
GL_MIN_PROGRAM_TEXEL_OFFSET_NV = 35076L # Variable c_uint '35076u'
GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET = 36446L # Variable c_uint '36446u'
GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET_ARB = 36446L # Variable c_uint '36446u'
GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET_NV = 36446L # Variable c_uint '36446u'
GL_MIN_SAMPLE_SHADING_VALUE = 35895L # Variable c_uint '35895u'
GL_MIN_SAMPLE_SHADING_VALUE_ARB = 35895L # Variable c_uint '35895u'
GL_MIRROR_CLAMP_ATI = 34626L # Variable c_uint '34626u'
GL_MIRROR_CLAMP_EXT = 34626L # Variable c_uint '34626u'
GL_MIRROR_CLAMP_TO_BORDER_EXT = 35090L # Variable c_uint '35090u'
GL_MIRROR_CLAMP_TO_EDGE_ATI = 34627L # Variable c_uint '34627u'
GL_MIRROR_CLAMP_TO_EDGE_EXT = 34627L # Variable c_uint '34627u'
GL_MIRRORED_REPEAT = 33648L # Variable c_uint '33648u'
GL_MIRRORED_REPEAT_ARB = 33648L # Variable c_uint '33648u'
GL_MIRRORED_REPEAT_IBM = 33648L # Variable c_uint '33648u'
GL_MODELVIEW0_ARB = 5888L # Variable c_uint '5888u'
GL_MODELVIEW = 5888L # Variable c_uint '5888u'
GL_MODELVIEW10_ARB = 34602L # Variable c_uint '34602u'
GL_MODELVIEW11_ARB = 34603L # Variable c_uint '34603u'
GL_MODELVIEW12_ARB = 34604L # Variable c_uint '34604u'
GL_MODELVIEW13_ARB = 34605L # Variable c_uint '34605u'
GL_MODELVIEW14_ARB = 34606L # Variable c_uint '34606u'
GL_MODELVIEW15_ARB = 34607L # Variable c_uint '34607u'
GL_MODELVIEW16_ARB = 34608L # Variable c_uint '34608u'
GL_MODELVIEW17_ARB = 34609L # Variable c_uint '34609u'
GL_MODELVIEW18_ARB = 34610L # Variable c_uint '34610u'
GL_MODELVIEW19_ARB = 34611L # Variable c_uint '34611u'
GL_MODELVIEW1_ARB = 34058L # Variable c_uint '34058u'
GL_MODELVIEW1_EXT = 34058L # Variable c_uint '34058u'
GL_MODELVIEW1_MATRIX_EXT = 34054L # Variable c_uint '34054u'
GL_MODELVIEW1_STACK_DEPTH_EXT = 34050L # Variable c_uint '34050u'
GL_MODELVIEW20_ARB = 34612L # Variable c_uint '34612u'
GL_MODELVIEW21_ARB = 34613L # Variable c_uint '34613u'
GL_MODELVIEW22_ARB = 34614L # Variable c_uint '34614u'
GL_MODELVIEW23_ARB = 34615L # Variable c_uint '34615u'
GL_MODELVIEW24_ARB = 34616L # Variable c_uint '34616u'
GL_MODELVIEW25_ARB = 34617L # Variable c_uint '34617u'
GL_MODELVIEW26_ARB = 34618L # Variable c_uint '34618u'
GL_MODELVIEW27_ARB = 34619L # Variable c_uint '34619u'
GL_MODELVIEW28_ARB = 34620L # Variable c_uint '34620u'
GL_MODELVIEW29_ARB = 34621L # Variable c_uint '34621u'
GL_MODELVIEW2_ARB = 34594L # Variable c_uint '34594u'
GL_MODELVIEW30_ARB = 34622L # Variable c_uint '34622u'
GL_MODELVIEW31_ARB = 34623L # Variable c_uint '34623u'
GL_MODELVIEW3_ARB = 34595L # Variable c_uint '34595u'
GL_MODELVIEW4_ARB = 34596L # Variable c_uint '34596u'
GL_MODELVIEW5_ARB = 34597L # Variable c_uint '34597u'
GL_MODELVIEW6_ARB = 34598L # Variable c_uint '34598u'
GL_MODELVIEW7_ARB = 34599L # Variable c_uint '34599u'
GL_MODELVIEW8_ARB = 34600L # Variable c_uint '34600u'
GL_MODELVIEW9_ARB = 34601L # Variable c_uint '34601u'
GL_MODELVIEW_MATRIX = 2982L # Variable c_uint '2982u'
GL_MODELVIEW_PROJECTION_NV = 34345L # Variable c_uint '34345u'
GL_MODELVIEW_STACK_DEPTH = 2979L # Variable c_uint '2979u'
GL_MODULATE = 8448L # Variable c_uint '8448u'
GL_MODULATE_ADD_ATI = 34628L # Variable c_uint '34628u'
GL_MODULATE_SIGNED_ADD_ATI = 34629L # Variable c_uint '34629u'
GL_MODULATE_SUBTRACT_ATI = 34630L # Variable c_uint '34630u'
GL_MOV_ATI = 35169L # Variable c_uint '35169u'
GL_MUL_ATI = 35172L # Variable c_uint '35172u'
GL_MULT = 259L # Variable c_uint '259u'
GL_MULTISAMPLE = 32925L # Variable c_uint '32925u'
GL_MULTISAMPLE_3DFX = 34482L # Variable c_uint '34482u'
GL_MULTISAMPLE_ARB = 32925L # Variable c_uint '32925u'
GL_MULTISAMPLE_BIT = 536870912L # Variable c_uint '536870912u'
GL_MULTISAMPLE_BIT_3DFX = 536870912L # Variable c_uint '536870912u'
GL_MULTISAMPLE_BIT_ARB = 536870912L # Variable c_uint '536870912u'
GL_MULTISAMPLE_BIT_EXT = 536870912L # Variable c_uint '536870912u'
GL_MULTISAMPLE_COVERAGE_MODES_NV = 36370L # Variable c_uint '36370u'
GL_MULTISAMPLE_EXT = 32925L # Variable c_uint '32925u'
GL_MULTISAMPLE_FILTER_HINT_NV = 34100L # Variable c_uint '34100u'
GL_MULTISAMPLE_SGIS = 32925L # Variable c_uint '32925u'
GL_MVP_MATRIX_EXT = 34787L # Variable c_uint '34787u'
GL_N3F_V3F = 10789L # Variable c_uint '10789u'
GL_NAMED_STRING_LENGTH_ARB = 36329L # Variable c_uint '36329u'
GL_NAMED_STRING_TYPE_ARB = 36330L # Variable c_uint '36330u'
GL_NAME_STACK_DEPTH = 3440L # Variable c_uint '3440u'
GL_NAND = 5390L # Variable c_uint '5390u'
GL_NATIVE_GRAPHICS_BEGIN_HINT_PGI = 107011L # Variable c_uint '107011u'
GL_NATIVE_GRAPHICS_END_HINT_PGI = 107012L # Variable c_uint '107012u'
GL_NATIVE_GRAPHICS_HANDLE_PGI = 107010L # Variable c_uint '107010u'
GL_NEAREST = 9728L # Variable c_uint '9728u'
GL_NEAREST_CLIPMAP_LINEAR_SGIX = 33870L # Variable c_uint '33870u'
GL_NEAREST_CLIPMAP_NEAREST_SGIX = 33869L # Variable c_uint '33869u'
GL_NEAREST_MIPMAP_LINEAR = 9986L # Variable c_uint '9986u'
GL_NEAREST_MIPMAP_NEAREST = 9984L # Variable c_uint '9984u'
GL_NEGATE_BIT_ATI = 4L # Variable c_uint '4u'
GL_NEGATIVE_ONE_EXT = 34783L # Variable c_uint '34783u'
GL_NEGATIVE_W_EXT = 34780L # Variable c_uint '34780u'
GL_NEGATIVE_X_EXT = 34777L # Variable c_uint '34777u'
GL_NEGATIVE_Y_EXT = 34778L # Variable c_uint '34778u'
GL_NEGATIVE_Z_EXT = 34779L # Variable c_uint '34779u'
GL_NEVER = 512L # Variable c_uint '512u'
GL_NEXT_VIDEO_CAPTURE_BUFFER_STATUS_NV = 36901L # Variable c_uint '36901u'
GL_NICEST = 4354L # Variable c_uint '4354u'
GL_NO_ERROR = 0L # Variable c_uint '0u'
GL_NONE = 0L # Variable c_uint '0u'
GL_NOOP = 5381L # Variable c_uint '5381u'
GL_NOR = 5384L # Variable c_uint '5384u'
GL_NO_RESET_NOTIFICATION_ARB = 33377L # Variable c_uint '33377u'
GL_NORMAL_ARRAY = 32885L # Variable c_uint '32885u'
GL_NORMAL_ARRAY_ADDRESS_NV = 36642L # Variable c_uint '36642u'
GL_NORMAL_ARRAY_BUFFER_BINDING = 34967L # Variable c_uint '34967u'
GL_NORMAL_ARRAY_BUFFER_BINDING_ARB = 34967L # Variable c_uint '34967u'
GL_NORMAL_ARRAY_COUNT_EXT = 32896L # Variable c_uint '32896u'
GL_NORMAL_ARRAY_EXT = 32885L # Variable c_uint '32885u'
GL_NORMAL_ARRAY_LENGTH_NV = 36652L # Variable c_uint '36652u'
GL_NORMAL_ARRAY_LIST_IBM = 103071L # Variable c_uint '103071u'
GL_NORMAL_ARRAY_LIST_STRIDE_IBM = 103081L # Variable c_uint '103081u'
GL_NORMAL_ARRAY_PARALLEL_POINTERS_INTEL = 33782L # Variable c_uint '33782u'
GL_NORMAL_ARRAY_POINTER = 32911L # Variable c_uint '32911u'
GL_NORMAL_ARRAY_POINTER_EXT = 32911L # Variable c_uint '32911u'
GL_NORMAL_ARRAY_STRIDE = 32895L # Variable c_uint '32895u'
GL_NORMAL_ARRAY_STRIDE_EXT = 32895L # Variable c_uint '32895u'
GL_NORMAL_ARRAY_TYPE = 32894L # Variable c_uint '32894u'
GL_NORMAL_ARRAY_TYPE_EXT = 32894L # Variable c_uint '32894u'
GL_NORMAL_BIT_PGI = 134217728L # Variable c_uint '134217728u'
GL_NORMALIZE = 2977L # Variable c_uint '2977u'
GL_NORMALIZED_RANGE_EXT = 34784L # Variable c_uint '34784u'
GL_NORMAL_MAP = 34065L # Variable c_uint '34065u'
GL_NORMAL_MAP_ARB = 34065L # Variable c_uint '34065u'
GL_NORMAL_MAP_EXT = 34065L # Variable c_uint '34065u'
GL_NORMAL_MAP_NV = 34065L # Variable c_uint '34065u'
GL_NOTEQUAL = 517L # Variable c_uint '517u'
GL_NUM_COMPATIBLE_SUBROUTINES = 36426L # Variable c_uint '36426u'
GL_NUM_COMPRESSED_TEXTURE_FORMATS = 34466L # Variable c_uint '34466u'
GL_NUM_COMPRESSED_TEXTURE_FORMATS_ARB = 34466L # Variable c_uint '34466u'
GL_NUM_EXTENSIONS = 33309L # Variable c_uint '33309u'
GL_NUM_FILL_STREAMS_NV = 36393L # Variable c_uint '36393u'
GL_NUM_FRAGMENT_CONSTANTS_ATI = 35183L # Variable c_uint '35183u'
GL_NUM_FRAGMENT_REGISTERS_ATI = 35182L # Variable c_uint '35182u'
GL_NUM_GENERAL_COMBINERS_NV = 34126L # Variable c_uint '34126u'
GL_NUM_INPUT_INTERPOLATOR_COMPONENTS_ATI = 35187L # Variable c_uint '35187u'
GL_NUM_INSTRUCTIONS_PER_PASS_ATI = 35185L # Variable c_uint '35185u'
GL_NUM_INSTRUCTIONS_TOTAL_ATI = 35186L # Variable c_uint '35186u'
GL_NUM_LOOPBACK_COMPONENTS_ATI = 35188L # Variable c_uint '35188u'
GL_NUM_PASSES_ATI = 35184L # Variable c_uint '35184u'
GL_NUM_PROGRAM_BINARY_FORMATS = 34814L # Variable c_uint '34814u'
GL_NUM_SHADER_BINARY_FORMATS = 36345L # Variable c_uint '36345u'
GL_NUM_VIDEO_CAPTURE_STREAMS_NV = 36900L # Variable c_uint '36900u'
GL_OBJECT_ACTIVE_ATTRIBUTE_MAX_LENGTH_ARB = 35722L # Variable c_uint '35722u'
GL_OBJECT_ACTIVE_ATTRIBUTES_ARB = 35721L # Variable c_uint '35721u'
GL_OBJECT_ACTIVE_UNIFORM_MAX_LENGTH_ARB = 35719L # Variable c_uint '35719u'
GL_OBJECT_ACTIVE_UNIFORMS_ARB = 35718L # Variable c_uint '35718u'
GL_OBJECT_ATTACHED_OBJECTS_ARB = 35717L # Variable c_uint '35717u'
GL_OBJECT_BUFFER_SIZE_ATI = 34660L # Variable c_uint '34660u'
GL_OBJECT_BUFFER_USAGE_ATI = 34661L # Variable c_uint '34661u'
GL_OBJECT_COMPILE_STATUS_ARB = 35713L # Variable c_uint '35713u'
GL_OBJECT_DELETE_STATUS_ARB = 35712L # Variable c_uint '35712u'
GL_OBJECT_DISTANCE_TO_LINE_SGIS = 33267L # Variable c_uint '33267u'
GL_OBJECT_DISTANCE_TO_POINT_SGIS = 33265L # Variable c_uint '33265u'
GL_OBJECT_INFO_LOG_LENGTH_ARB = 35716L # Variable c_uint '35716u'
GL_OBJECT_LINEAR = 9217L # Variable c_uint '9217u'
GL_OBJECT_LINE_SGIS = 33271L # Variable c_uint '33271u'
GL_OBJECT_LINK_STATUS_ARB = 35714L # Variable c_uint '35714u'
GL_OBJECT_PLANE = 9473L # Variable c_uint '9473u'
GL_OBJECT_POINT_SGIS = 33269L # Variable c_uint '33269u'
GL_OBJECT_SHADER_SOURCE_LENGTH_ARB = 35720L # Variable c_uint '35720u'
GL_OBJECT_SUBTYPE_ARB = 35663L # Variable c_uint '35663u'
GL_OBJECT_TYPE = 37138L # Variable c_uint '37138u'
GL_OBJECT_TYPE_ARB = 35662L # Variable c_uint '35662u'
GL_OBJECT_VALIDATE_STATUS_ARB = 35715L # Variable c_uint '35715u'
GL_OCCLUSION_TEST_HP = 33125L # Variable c_uint '33125u'
GL_OCCLUSION_TEST_RESULT_HP = 33126L # Variable c_uint '33126u'
GL_OFFSET_HILO_PROJECTIVE_TEXTURE_2D_NV = 34902L # Variable c_uint '34902u'
GL_OFFSET_HILO_PROJECTIVE_TEXTURE_RECTANGLE_NV = 34903L # Variable c_uint '34903u'
GL_OFFSET_HILO_TEXTURE_2D_NV = 34900L # Variable c_uint '34900u'
GL_OFFSET_HILO_TEXTURE_RECTANGLE_NV = 34901L # Variable c_uint '34901u'
GL_OFFSET_PROJECTIVE_TEXTURE_2D_NV = 34896L # Variable c_uint '34896u'
GL_OFFSET_PROJECTIVE_TEXTURE_2D_SCALE_NV = 34897L # Variable c_uint '34897u'
GL_OFFSET_PROJECTIVE_TEXTURE_RECTANGLE_NV = 34898L # Variable c_uint '34898u'
GL_OFFSET_PROJECTIVE_TEXTURE_RECTANGLE_SCALE_NV = 34899L # Variable c_uint '34899u'
GL_OFFSET_TEXTURE_2D_NV = 34536L # Variable c_uint '34536u'
GL_OFFSET_TEXTURE_BIAS_NV = 34531L # Variable c_uint '34531u'
GL_OFFSET_TEXTURE_MATRIX_NV = 34529L # Variable c_uint '34529u'
GL_OFFSET_TEXTURE_RECTANGLE_NV = 34380L # Variable c_uint '34380u'
GL_OFFSET_TEXTURE_RECTANGLE_SCALE_NV = 34381L # Variable c_uint '34381u'
GL_OFFSET_TEXTURE_SCALE_NV = 34530L # Variable c_uint '34530u'
GL_ONE = 1L # Variable c_uint '1u'
GL_ONE_EXT = 34782L # Variable c_uint '34782u'
GL_ONE_MINUS_CONSTANT_ALPHA = 32772L # Variable c_uint '32772u'
GL_ONE_MINUS_CONSTANT_ALPHA_EXT = 32772L # Variable c_uint '32772u'
GL_ONE_MINUS_CONSTANT_COLOR = 32770L # Variable c_uint '32770u'
GL_ONE_MINUS_CONSTANT_COLOR_EXT = 32770L # Variable c_uint '32770u'
GL_ONE_MINUS_DST_ALPHA = 773L # Variable c_uint '773u'
GL_ONE_MINUS_DST_COLOR = 775L # Variable c_uint '775u'
GL_ONE_MINUS_SRC1_ALPHA = 35067L # Variable c_uint '35067u'
GL_ONE_MINUS_SRC1_COLOR = 35066L # Variable c_uint '35066u'
GL_ONE_MINUS_SRC_ALPHA = 771L # Variable c_uint '771u'
GL_ONE_MINUS_SRC_COLOR = 769L # Variable c_uint '769u'
GL_OP_ADD_EXT = 34695L # Variable c_uint '34695u'
GL_OP_CLAMP_EXT = 34702L # Variable c_uint '34702u'
GL_OP_CROSS_PRODUCT_EXT = 34711L # Variable c_uint '34711u'
GL_OP_DOT3_EXT = 34692L # Variable c_uint '34692u'
GL_OP_DOT4_EXT = 34693L # Variable c_uint '34693u'
GL_OPERAND0_ALPHA = 34200L # Variable c_uint '34200u'
GL_OPERAND0_ALPHA_ARB = 34200L # Variable c_uint '34200u'
GL_OPERAND0_ALPHA_EXT = 34200L # Variable c_uint '34200u'
GL_OPERAND0_RGB = 34192L # Variable c_uint '34192u'
GL_OPERAND0_RGB_ARB = 34192L # Variable c_uint '34192u'
GL_OPERAND0_RGB_EXT = 34192L # Variable c_uint '34192u'
GL_OPERAND1_ALPHA = 34201L # Variable c_uint '34201u'
GL_OPERAND1_ALPHA_ARB = 34201L # Variable c_uint '34201u'
GL_OPERAND1_ALPHA_EXT = 34201L # Variable c_uint '34201u'
GL_OPERAND1_RGB = 34193L # Variable c_uint '34193u'
GL_OPERAND1_RGB_ARB = 34193L # Variable c_uint '34193u'
GL_OPERAND1_RGB_EXT = 34193L # Variable c_uint '34193u'
GL_OPERAND2_ALPHA = 34202L # Variable c_uint '34202u'
GL_OPERAND2_ALPHA_ARB = 34202L # Variable c_uint '34202u'
GL_OPERAND2_ALPHA_EXT = 34202L # Variable c_uint '34202u'
GL_OPERAND2_RGB = 34194L # Variable c_uint '34194u'
GL_OPERAND2_RGB_ARB = 34194L # Variable c_uint '34194u'
GL_OPERAND2_RGB_EXT = 34194L # Variable c_uint '34194u'
GL_OPERAND3_ALPHA_NV = 34203L # Variable c_uint '34203u'
GL_OPERAND3_RGB_NV = 34195L # Variable c_uint '34195u'
GL_OP_EXP_BASE_2_EXT = 34705L # Variable c_uint '34705u'
GL_OP_FLOOR_EXT = 34703L # Variable c_uint '34703u'
GL_OP_FRAC_EXT = 34697L # Variable c_uint '34697u'
GL_OP_INDEX_EXT = 34690L # Variable c_uint '34690u'
GL_OP_LOG_BASE_2_EXT = 34706L # Variable c_uint '34706u'
GL_OP_MADD_EXT = 34696L # Variable c_uint '34696u'
GL_OP_MAX_EXT = 34698L # Variable c_uint '34698u'
GL_OP_MIN_EXT = 34699L # Variable c_uint '34699u'
GL_OP_MOV_EXT = 34713L # Variable c_uint '34713u'
GL_OP_MUL_EXT = 34694L # Variable c_uint '34694u'
GL_OP_MULTIPLY_MATRIX_EXT = 34712L # Variable c_uint '34712u'
GL_OP_NEGATE_EXT = 34691L # Variable c_uint '34691u'
GL_OP_POWER_EXT = 34707L # Variable c_uint '34707u'
GL_OP_RECIP_EXT = 34708L # Variable c_uint '34708u'
GL_OP_RECIP_SQRT_EXT = 34709L # Variable c_uint '34709u'
GL_OP_ROUND_EXT = 34704L # Variable c_uint '34704u'
GL_OP_SET_GE_EXT = 34700L # Variable c_uint '34700u'
GL_OP_SET_LT_EXT = 34701L # Variable c_uint '34701u'
GL_OP_SUB_EXT = 34710L # Variable c_uint '34710u'
GL_OR = 5383L # Variable c_uint '5383u'
GL_ORDER = 2561L # Variable c_uint '2561u'
GL_OR_INVERTED = 5389L # Variable c_uint '5389u'
GL_OR_REVERSE = 5387L # Variable c_uint '5387u'
GL_OUT_OF_MEMORY = 1285L # Variable c_uint '1285u'
GL_OUTPUT_COLOR0_EXT = 34715L # Variable c_uint '34715u'
GL_OUTPUT_COLOR1_EXT = 34716L # Variable c_uint '34716u'
GL_OUTPUT_FOG_EXT = 34749L # Variable c_uint '34749u'
GL_OUTPUT_TEXTURE_COORD0_EXT = 34717L # Variable c_uint '34717u'
GL_OUTPUT_TEXTURE_COORD10_EXT = 34727L # Variable c_uint '34727u'
GL_OUTPUT_TEXTURE_COORD11_EXT = 34728L # Variable c_uint '34728u'
GL_OUTPUT_TEXTURE_COORD12_EXT = 34729L # Variable c_uint '34729u'
GL_OUTPUT_TEXTURE_COORD13_EXT = 34730L # Variable c_uint '34730u'
GL_OUTPUT_TEXTURE_COORD14_EXT = 34731L # Variable c_uint '34731u'
GL_OUTPUT_TEXTURE_COORD15_EXT = 34732L # Variable c_uint '34732u'
GL_OUTPUT_TEXTURE_COORD16_EXT = 34733L # Variable c_uint '34733u'
GL_OUTPUT_TEXTURE_COORD17_EXT = 34734L # Variable c_uint '34734u'
GL_OUTPUT_TEXTURE_COORD18_EXT = 34735L # Variable c_uint '34735u'
GL_OUTPUT_TEXTURE_COORD19_EXT = 34736L # Variable c_uint '34736u'
GL_OUTPUT_TEXTURE_COORD1_EXT = 34718L # Variable c_uint '34718u'
GL_OUTPUT_TEXTURE_COORD20_EXT = 34737L # Variable c_uint '34737u'
GL_OUTPUT_TEXTURE_COORD21_EXT = 34738L # Variable c_uint '34738u'
GL_OUTPUT_TEXTURE_COORD22_EXT = 34739L # Variable c_uint '34739u'
GL_OUTPUT_TEXTURE_COORD23_EXT = 34740L # Variable c_uint '34740u'
GL_OUTPUT_TEXTURE_COORD24_EXT = 34741L # Variable c_uint '34741u'
GL_OUTPUT_TEXTURE_COORD25_EXT = 34742L # Variable c_uint '34742u'
GL_OUTPUT_TEXTURE_COORD26_EXT = 34743L # Variable c_uint '34743u'
GL_OUTPUT_TEXTURE_COORD27_EXT = 34744L # Variable c_uint '34744u'
GL_OUTPUT_TEXTURE_COORD28_EXT = 34745L # Variable c_uint '34745u'
GL_OUTPUT_TEXTURE_COORD29_EXT = 34746L # Variable c_uint '34746u'
GL_OUTPUT_TEXTURE_COORD2_EXT = 34719L # Variable c_uint '34719u'
GL_OUTPUT_TEXTURE_COORD30_EXT = 34747L # Variable c_uint '34747u'
GL_OUTPUT_TEXTURE_COORD31_EXT = 34748L # Variable c_uint '34748u'
GL_OUTPUT_TEXTURE_COORD3_EXT = 34720L # Variable c_uint '34720u'
GL_OUTPUT_TEXTURE_COORD4_EXT = 34721L # Variable c_uint '34721u'
GL_OUTPUT_TEXTURE_COORD5_EXT = 34722L # Variable c_uint '34722u'
GL_OUTPUT_TEXTURE_COORD6_EXT = 34723L # Variable c_uint '34723u'
GL_OUTPUT_TEXTURE_COORD7_EXT = 34724L # Variable c_uint '34724u'
GL_OUTPUT_TEXTURE_COORD8_EXT = 34725L # Variable c_uint '34725u'
GL_OUTPUT_TEXTURE_COORD9_EXT = 34726L # Variable c_uint '34726u'
GL_OUTPUT_VERTEX_EXT = 34714L # Variable c_uint '34714u'
GL_PACK_ALIGNMENT = 3333L # Variable c_uint '3333u'
GL_PACK_CMYK_HINT_EXT = 32782L # Variable c_uint '32782u'
GL_PACK_IMAGE_DEPTH_SGIS = 33073L # Variable c_uint '33073u'
GL_PACK_IMAGE_HEIGHT = 32876L # Variable c_uint '32876u'
GL_PACK_IMAGE_HEIGHT_EXT = 32876L # Variable c_uint '32876u'
GL_PACK_INVERT_MESA = 34648L # Variable c_uint '34648u'
GL_PACK_LSB_FIRST = 3329L # Variable c_uint '3329u'
GL_PACK_RESAMPLE_OML = 35204L # Variable c_uint '35204u'
GL_PACK_RESAMPLE_SGIX = 33836L # Variable c_uint '33836u'
GL_PACK_ROW_BYTES_APPLE = 35349L # Variable c_uint '35349u'
GL_PACK_ROW_LENGTH = 3330L # Variable c_uint '3330u'
GL_PACK_SKIP_IMAGES = 32875L # Variable c_uint '32875u'
GL_PACK_SKIP_IMAGES_EXT = 32875L # Variable c_uint '32875u'
GL_PACK_SKIP_PIXELS = 3332L # Variable c_uint '3332u'
GL_PACK_SKIP_ROWS = 3331L # Variable c_uint '3331u'
GL_PACK_SKIP_VOLUMES_SGIS = 33072L # Variable c_uint '33072u'
GL_PACK_SUBSAMPLE_RATE_SGIX = 34208L # Variable c_uint '34208u'
GL_PACK_SWAP_BYTES = 3328L # Variable c_uint '3328u'
GL_PARALLEL_ARRAYS_INTEL = 33780L # Variable c_uint '33780u'
GL_PARTIAL_SUCCESS_NV = 36910L # Variable c_uint '36910u'
GL_PASS_THROUGH_NV = 34534L # Variable c_uint '34534u'
GL_PASS_THROUGH_TOKEN = 1792L # Variable c_uint '1792u'
GL_PATCH_DEFAULT_INNER_LEVEL = 36467L # Variable c_uint '36467u'
GL_PATCH_DEFAULT_OUTER_LEVEL = 36468L # Variable c_uint '36468u'
GL_PATCHES = 14L # Variable c_uint '14u'
GL_PATCH_VERTICES = 36466L # Variable c_uint '36466u'
GL_PERCENTAGE_AMD = 35779L # Variable c_uint '35779u'
GL_PERFMON_RESULT_AMD = 35782L # Variable c_uint '35782u'
GL_PERFMON_RESULT_AVAILABLE_AMD = 35780L # Variable c_uint '35780u'
GL_PERFMON_RESULT_SIZE_AMD = 35781L # Variable c_uint '35781u'
GL_PERFORMANCE_MONITOR_AMD = 37202L # Variable c_uint '37202u'
GL_PERSPECTIVE_CORRECTION_HINT = 3152L # Variable c_uint '3152u'
GL_PER_STAGE_CONSTANTS_NV = 34101L # Variable c_uint '34101u'
GL_PERTURB_EXT = 34222L # Variable c_uint '34222u'
GL_PHONG_HINT_WIN = 33003L # Variable c_uint '33003u'
GL_PHONG_WIN = 33002L # Variable c_uint '33002u'
GL_PIXEL_BUFFER_BARRIER_BIT_EXT = 128L # Variable c_uint '128u'
GL_PIXEL_COUNT_AVAILABLE_NV = 34919L # Variable c_uint '34919u'
GL_PIXEL_COUNTER_BITS_NV = 34916L # Variable c_uint '34916u'
GL_PIXEL_COUNT_NV = 34918L # Variable c_uint '34918u'
GL_PIXEL_CUBIC_WEIGHT_EXT = 33587L # Variable c_uint '33587u'
GL_PIXEL_FRAGMENT_ALPHA_SOURCE_SGIS = 33621L # Variable c_uint '33621u'
GL_PIXEL_FRAGMENT_RGB_SOURCE_SGIS = 33620L # Variable c_uint '33620u'
GL_PIXEL_GROUP_COLOR_SGIS = 33622L # Variable c_uint '33622u'
GL_PIXEL_MAG_FILTER_EXT = 33585L # Variable c_uint '33585u'
GL_PIXEL_MAP_A_TO_A = 3193L # Variable c_uint '3193u'
GL_PIXEL_MAP_A_TO_A_SIZE = 3257L # Variable c_uint '3257u'
GL_PIXEL_MAP_B_TO_B = 3192L # Variable c_uint '3192u'
GL_PIXEL_MAP_B_TO_B_SIZE = 3256L # Variable c_uint '3256u'
GL_PIXEL_MAP_G_TO_G = 3191L # Variable c_uint '3191u'
GL_PIXEL_MAP_G_TO_G_SIZE = 3255L # Variable c_uint '3255u'
GL_PIXEL_MAP_I_TO_A = 3189L # Variable c_uint '3189u'
GL_PIXEL_MAP_I_TO_A_SIZE = 3253L # Variable c_uint '3253u'
GL_PIXEL_MAP_I_TO_B = 3188L # Variable c_uint '3188u'
GL_PIXEL_MAP_I_TO_B_SIZE = 3252L # Variable c_uint '3252u'
GL_PIXEL_MAP_I_TO_G = 3187L # Variable c_uint '3187u'
GL_PIXEL_MAP_I_TO_G_SIZE = 3251L # Variable c_uint '3251u'
GL_PIXEL_MAP_I_TO_I = 3184L # Variable c_uint '3184u'
GL_PIXEL_MAP_I_TO_I_SIZE = 3248L # Variable c_uint '3248u'
GL_PIXEL_MAP_I_TO_R = 3186L # Variable c_uint '3186u'
GL_PIXEL_MAP_I_TO_R_SIZE = 3250L # Variable c_uint '3250u'
GL_PIXEL_MAP_R_TO_R = 3190L # Variable c_uint '3190u'
GL_PIXEL_MAP_R_TO_R_SIZE = 3254L # Variable c_uint '3254u'
GL_PIXEL_MAP_S_TO_S = 3185L # Variable c_uint '3185u'
GL_PIXEL_MAP_S_TO_S_SIZE = 3249L # Variable c_uint '3249u'
GL_PIXEL_MIN_FILTER_EXT = 33586L # Variable c_uint '33586u'
GL_PIXEL_MODE_BIT = 32L # Variable c_uint '32u'
GL_PIXEL_PACK_BUFFER = 35051L # Variable c_uint '35051u'
GL_PIXEL_PACK_BUFFER_ARB = 35051L # Variable c_uint '35051u'
GL_PIXEL_PACK_BUFFER_BINDING = 35053L # Variable c_uint '35053u'
GL_PIXEL_PACK_BUFFER_BINDING_ARB = 35053L # Variable c_uint '35053u'
GL_PIXEL_PACK_BUFFER_BINDING_EXT = 35053L # Variable c_uint '35053u'
GL_PIXEL_PACK_BUFFER_EXT = 35051L # Variable c_uint '35051u'
GL_PIXEL_SUBSAMPLE_2424_SGIX = 34211L # Variable c_uint '34211u'
GL_PIXEL_SUBSAMPLE_4242_SGIX = 34212L # Variable c_uint '34212u'
GL_PIXEL_SUBSAMPLE_4444_SGIX = 34210L # Variable c_uint '34210u'
GL_PIXEL_TEX_GEN_ALPHA_LS_SGIX = 33161L # Variable c_uint '33161u'
GL_PIXEL_TEX_GEN_ALPHA_MS_SGIX = 33162L # Variable c_uint '33162u'
GL_PIXEL_TEX_GEN_ALPHA_NO_REPLACE_SGIX = 33160L # Variable c_uint '33160u'
GL_PIXEL_TEX_GEN_ALPHA_REPLACE_SGIX = 33159L # Variable c_uint '33159u'
GL_PIXEL_TEX_GEN_MODE_SGIX = 33579L # Variable c_uint '33579u'
GL_PIXEL_TEX_GEN_Q_CEILING_SGIX = 33156L # Variable c_uint '33156u'
GL_PIXEL_TEX_GEN_Q_FLOOR_SGIX = 33158L # Variable c_uint '33158u'
GL_PIXEL_TEX_GEN_Q_ROUND_SGIX = 33157L # Variable c_uint '33157u'
GL_PIXEL_TEX_GEN_SGIX = 33081L # Variable c_uint '33081u'
GL_PIXEL_TEXTURE_SGIS = 33619L # Variable c_uint '33619u'
GL_PIXEL_TILE_BEST_ALIGNMENT_SGIX = 33086L # Variable c_uint '33086u'
GL_PIXEL_TILE_CACHE_INCREMENT_SGIX = 33087L # Variable c_uint '33087u'
GL_PIXEL_TILE_CACHE_SIZE_SGIX = 33093L # Variable c_uint '33093u'
GL_PIXEL_TILE_GRID_DEPTH_SGIX = 33092L # Variable c_uint '33092u'
GL_PIXEL_TILE_GRID_HEIGHT_SGIX = 33091L # Variable c_uint '33091u'
GL_PIXEL_TILE_GRID_WIDTH_SGIX = 33090L # Variable c_uint '33090u'
GL_PIXEL_TILE_HEIGHT_SGIX = 33089L # Variable c_uint '33089u'
GL_PIXEL_TILE_WIDTH_SGIX = 33088L # Variable c_uint '33088u'
GL_PIXEL_TRANSFORM_2D_EXT = 33584L # Variable c_uint '33584u'
GL_PIXEL_TRANSFORM_2D_MATRIX_EXT = 33592L # Variable c_uint '33592u'
GL_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT = 33590L # Variable c_uint '33590u'
GL_PIXEL_UNPACK_BUFFER = 35052L # Variable c_uint '35052u'
GL_PIXEL_UNPACK_BUFFER_ARB = 35052L # Variable c_uint '35052u'
GL_PIXEL_UNPACK_BUFFER_BINDING = 35055L # Variable c_uint '35055u'
GL_PIXEL_UNPACK_BUFFER_BINDING_ARB = 35055L # Variable c_uint '35055u'
GL_PIXEL_UNPACK_BUFFER_BINDING_EXT = 35055L # Variable c_uint '35055u'
GL_PIXEL_UNPACK_BUFFER_EXT = 35052L # Variable c_uint '35052u'
GL_PN_TRIANGLES_ATI = 34800L # Variable c_uint '34800u'
GL_PN_TRIANGLES_NORMAL_MODE_ATI = 34803L # Variable c_uint '34803u'
GL_PN_TRIANGLES_NORMAL_MODE_LINEAR_ATI = 34807L # Variable c_uint '34807u'
GL_PN_TRIANGLES_NORMAL_MODE_QUADRATIC_ATI = 34808L # Variable c_uint '34808u'
GL_PN_TRIANGLES_POINT_MODE_ATI = 34802L # Variable c_uint '34802u'
GL_PN_TRIANGLES_POINT_MODE_CUBIC_ATI = 34806L # Variable c_uint '34806u'
GL_PN_TRIANGLES_POINT_MODE_LINEAR_ATI = 34805L # Variable c_uint '34805u'
GL_PN_TRIANGLES_TESSELATION_LEVEL_ATI = 34804L # Variable c_uint '34804u'
GL_POINT = 6912L # Variable c_uint '6912u'
GL_POINT_BIT = 2L # Variable c_uint '2u'
GL_POINT_DISTANCE_ATTENUATION = 33065L # Variable c_uint '33065u'
GL_POINT_DISTANCE_ATTENUATION_ARB = 33065L # Variable c_uint '33065u'
GL_POINT_FADE_THRESHOLD_SIZE = 33064L # Variable c_uint '33064u'
GL_POINT_FADE_THRESHOLD_SIZE_ARB = 33064L # Variable c_uint '33064u'
GL_POINT_FADE_THRESHOLD_SIZE_EXT = 33064L # Variable c_uint '33064u'
GL_POINT_FADE_THRESHOLD_SIZE_SGIS = 33064L # Variable c_uint '33064u'
GL_POINTS = 0L # Variable c_uint '0u'
GL_POINT_SIZE = 2833L # Variable c_uint '2833u'
GL_POINT_SIZE_GRANULARITY = 2835L # Variable c_uint '2835u'
GL_POINT_SIZE_MAX = 33063L # Variable c_uint '33063u'
GL_POINT_SIZE_MAX_ARB = 33063L # Variable c_uint '33063u'
GL_POINT_SIZE_MAX_EXT = 33063L # Variable c_uint '33063u'
GL_POINT_SIZE_MAX_SGIS = 33063L # Variable c_uint '33063u'
GL_POINT_SIZE_MIN = 33062L # Variable c_uint '33062u'
GL_POINT_SIZE_MIN_ARB = 33062L # Variable c_uint '33062u'
GL_POINT_SIZE_MIN_EXT = 33062L # Variable c_uint '33062u'
GL_POINT_SIZE_MIN_SGIS = 33062L # Variable c_uint '33062u'
GL_POINT_SIZE_RANGE = 2834L # Variable c_uint '2834u'
GL_POINT_SMOOTH = 2832L # Variable c_uint '2832u'
GL_POINT_SMOOTH_HINT = 3153L # Variable c_uint '3153u'
GL_POINT_SPRITE = 34913L # Variable c_uint '34913u'
GL_POINT_SPRITE_ARB = 34913L # Variable c_uint '34913u'
GL_POINT_SPRITE_COORD_ORIGIN = 36000L # Variable c_uint '36000u'
GL_POINT_SPRITE_NV = 34913L # Variable c_uint '34913u'
GL_POINT_SPRITE_R_MODE_NV = 34915L # Variable c_uint '34915u'
GL_POINT_TOKEN = 1793L # Variable c_uint '1793u'
GL_POLYGON = 9L # Variable c_uint '9u'
GL_POLYGON_BIT = 8L # Variable c_uint '8u'
GL_POLYGON_MODE = 2880L # Variable c_uint '2880u'
GL_POLYGON_OFFSET_BIAS_EXT = 32825L # Variable c_uint '32825u'
GL_POLYGON_OFFSET_EXT = 32823L # Variable c_uint '32823u'
GL_POLYGON_OFFSET_FACTOR = 32824L # Variable c_uint '32824u'
GL_POLYGON_OFFSET_FACTOR_EXT = 32824L # Variable c_uint '32824u'
GL_POLYGON_OFFSET_FILL = 32823L # Variable c_uint '32823u'
GL_POLYGON_OFFSET_LINE = 10754L # Variable c_uint '10754u'
GL_POLYGON_OFFSET_POINT = 10753L # Variable c_uint '10753u'
GL_POLYGON_OFFSET_UNITS = 10752L # Variable c_uint '10752u'
GL_POLYGON_SMOOTH = 2881L # Variable c_uint '2881u'
GL_POLYGON_SMOOTH_HINT = 3155L # Variable c_uint '3155u'
GL_POLYGON_STIPPLE = 2882L # Variable c_uint '2882u'
GL_POLYGON_STIPPLE_BIT = 16L # Variable c_uint '16u'
GL_POLYGON_TOKEN = 1795L # Variable c_uint '1795u'
GL_POSITION = 4611L # Variable c_uint '4611u'
GL_POST_COLOR_MATRIX_ALPHA_BIAS = 32955L # Variable c_uint '32955u'
GL_POST_COLOR_MATRIX_ALPHA_BIAS_SGI = 32955L # Variable c_uint '32955u'
GL_POST_COLOR_MATRIX_ALPHA_SCALE = 32951L # Variable c_uint '32951u'
GL_POST_COLOR_MATRIX_ALPHA_SCALE_SGI = 32951L # Variable c_uint '32951u'
GL_POST_COLOR_MATRIX_BLUE_BIAS = 32954L # Variable c_uint '32954u'
GL_POST_COLOR_MATRIX_BLUE_BIAS_SGI = 32954L # Variable c_uint '32954u'
GL_POST_COLOR_MATRIX_BLUE_SCALE = 32950L # Variable c_uint '32950u'
GL_POST_COLOR_MATRIX_BLUE_SCALE_SGI = 32950L # Variable c_uint '32950u'
GL_POST_COLOR_MATRIX_COLOR_TABLE = 32978L # Variable c_uint '32978u'
GL_POST_COLOR_MATRIX_COLOR_TABLE_SGI = 32978L # Variable c_uint '32978u'
GL_POST_COLOR_MATRIX_GREEN_BIAS = 32953L # Variable c_uint '32953u'
GL_POST_COLOR_MATRIX_GREEN_BIAS_SGI = 32953L # Variable c_uint '32953u'
GL_POST_COLOR_MATRIX_GREEN_SCALE = 32949L # Variable c_uint '32949u'
GL_POST_COLOR_MATRIX_GREEN_SCALE_SGI = 32949L # Variable c_uint '32949u'
GL_POST_COLOR_MATRIX_RED_BIAS = 32952L # Variable c_uint '32952u'
GL_POST_COLOR_MATRIX_RED_BIAS_SGI = 32952L # Variable c_uint '32952u'
GL_POST_COLOR_MATRIX_RED_SCALE = 32948L # Variable c_uint '32948u'
GL_POST_COLOR_MATRIX_RED_SCALE_SGI = 32948L # Variable c_uint '32948u'
GL_POST_CONVOLUTION_ALPHA_BIAS = 32803L # Variable c_uint '32803u'
GL_POST_CONVOLUTION_ALPHA_BIAS_EXT = 32803L # Variable c_uint '32803u'
GL_POST_CONVOLUTION_ALPHA_SCALE = 32799L # Variable c_uint '32799u'
GL_POST_CONVOLUTION_ALPHA_SCALE_EXT = 32799L # Variable c_uint '32799u'
GL_POST_CONVOLUTION_BLUE_BIAS = 32802L # Variable c_uint '32802u'
GL_POST_CONVOLUTION_BLUE_BIAS_EXT = 32802L # Variable c_uint '32802u'
GL_POST_CONVOLUTION_BLUE_SCALE = 32798L # Variable c_uint '32798u'
GL_POST_CONVOLUTION_BLUE_SCALE_EXT = 32798L # Variable c_uint '32798u'
GL_POST_CONVOLUTION_COLOR_TABLE = 32977L # Variable c_uint '32977u'
GL_POST_CONVOLUTION_COLOR_TABLE_SGI = 32977L # Variable c_uint '32977u'
GL_POST_CONVOLUTION_GREEN_BIAS = 32801L # Variable c_uint '32801u'
GL_POST_CONVOLUTION_GREEN_BIAS_EXT = 32801L # Variable c_uint '32801u'
GL_POST_CONVOLUTION_GREEN_SCALE = 32797L # Variable c_uint '32797u'
GL_POST_CONVOLUTION_GREEN_SCALE_EXT = 32797L # Variable c_uint '32797u'
GL_POST_CONVOLUTION_RED_BIAS = 32800L # Variable c_uint '32800u'
GL_POST_CONVOLUTION_RED_BIAS_EXT = 32800L # Variable c_uint '32800u'
GL_POST_CONVOLUTION_RED_SCALE = 32796L # Variable c_uint '32796u'
GL_POST_CONVOLUTION_RED_SCALE_EXT = 32796L # Variable c_uint '32796u'
GL_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP = 33122L # Variable c_uint '33122u'
GL_POST_TEXTURE_FILTER_BIAS_RANGE_SGIX = 33147L # Variable c_uint '33147u'
GL_POST_TEXTURE_FILTER_BIAS_SGIX = 33145L # Variable c_uint '33145u'
GL_POST_TEXTURE_FILTER_SCALE_RANGE_SGIX = 33148L # Variable c_uint '33148u'
GL_POST_TEXTURE_FILTER_SCALE_SGIX = 33146L # Variable c_uint '33146u'
GL_PREFER_DOUBLEBUFFER_HINT_PGI = 107000L # Variable c_uint '107000u'
GL_PRESENT_DURATION_NV = 36395L # Variable c_uint '36395u'
GL_PRESENT_TIME_NV = 36394L # Variable c_uint '36394u'
GL_PRESERVE_ATI = 34658L # Variable c_uint '34658u'
GL_PREVIOUS = 34168L # Variable c_uint '34168u'
GL_PREVIOUS_ARB = 34168L # Variable c_uint '34168u'
GL_PREVIOUS_EXT = 34168L # Variable c_uint '34168u'
GL_PREVIOUS_TEXTURE_INPUT_NV = 34532L # Variable c_uint '34532u'
GL_PRIMARY_COLOR = 34167L # Variable c_uint '34167u'
GL_PRIMARY_COLOR_ARB = 34167L # Variable c_uint '34167u'
GL_PRIMARY_COLOR_EXT = 34167L # Variable c_uint '34167u'
GL_PRIMARY_COLOR_NV = 34092L # Variable c_uint '34092u'
GL_PRIMITIVE_ID_NV = 35964L # Variable c_uint '35964u'
GL_PRIMITIVE_RESTART = 36765L # Variable c_uint '36765u'
GL_PRIMITIVE_RESTART_INDEX = 36766L # Variable c_uint '36766u'
GL_PRIMITIVE_RESTART_INDEX_NV = 34137L # Variable c_uint '34137u'
GL_PRIMITIVE_RESTART_NV = 34136L # Variable c_uint '34136u'
GL_PRIMITIVES_GENERATED = 35975L # Variable c_uint '35975u'
GL_PRIMITIVES_GENERATED_EXT = 35975L # Variable c_uint '35975u'
GL_PRIMITIVES_GENERATED_NV = 35975L # Variable c_uint '35975u'
GL_PROGRAM_ADDRESS_REGISTERS_ARB = 34992L # Variable c_uint '34992u'
GL_PROGRAM_ALU_INSTRUCTIONS_ARB = 34821L # Variable c_uint '34821u'
GL_PROGRAM_ATTRIB_COMPONENTS_NV = 35078L # Variable c_uint '35078u'
GL_PROGRAM_ATTRIBS_ARB = 34988L # Variable c_uint '34988u'
GL_PROGRAM_BINARY_FORMATS = 34815L # Variable c_uint '34815u'
GL_PROGRAM_BINARY_LENGTH = 34625L # Variable c_uint '34625u'
GL_PROGRAM_BINARY_RETRIEVABLE_HINT = 33367L # Variable c_uint '33367u'
GL_PROGRAM_BINDING_ARB = 34423L # Variable c_uint '34423u'
GL_PROGRAM_ERROR_POSITION_ARB = 34379L # Variable c_uint '34379u'
GL_PROGRAM_ERROR_POSITION_NV = 34379L # Variable c_uint '34379u'
GL_PROGRAM_ERROR_STRING_ARB = 34932L # Variable c_uint '34932u'
GL_PROGRAM_ERROR_STRING_NV = 34932L # Variable c_uint '34932u'
GL_PROGRAM_FORMAT_ARB = 34934L # Variable c_uint '34934u'
GL_PROGRAM_FORMAT_ASCII_ARB = 34933L # Variable c_uint '34933u'
GL_PROGRAM_INSTRUCTIONS_ARB = 34976L # Variable c_uint '34976u'
GL_PROGRAM_LENGTH_ARB = 34343L # Variable c_uint '34343u'
GL_PROGRAM_LENGTH_NV = 34343L # Variable c_uint '34343u'
GL_PROGRAM_MATRIX_EXT = 36397L # Variable c_uint '36397u'
GL_PROGRAM_MATRIX_STACK_DEPTH_EXT = 36399L # Variable c_uint '36399u'
GL_PROGRAM_NATIVE_ADDRESS_REGISTERS_ARB = 34994L # Variable c_uint '34994u'
GL_PROGRAM_NATIVE_ALU_INSTRUCTIONS_ARB = 34824L # Variable c_uint '34824u'
GL_PROGRAM_NATIVE_ATTRIBS_ARB = 34990L # Variable c_uint '34990u'
GL_PROGRAM_NATIVE_INSTRUCTIONS_ARB = 34978L # Variable c_uint '34978u'
GL_PROGRAM_NATIVE_PARAMETERS_ARB = 34986L # Variable c_uint '34986u'
GL_PROGRAM_NATIVE_TEMPORARIES_ARB = 34982L # Variable c_uint '34982u'
GL_PROGRAM_NATIVE_TEX_INDIRECTIONS_ARB = 34826L # Variable c_uint '34826u'
GL_PROGRAM_NATIVE_TEX_INSTRUCTIONS_ARB = 34825L # Variable c_uint '34825u'
GL_PROGRAM_OBJECT_ARB = 35648L # Variable c_uint '35648u'
GL_PROGRAM_PARAMETER_NV = 34372L # Variable c_uint '34372u'
GL_PROGRAM_PARAMETERS_ARB = 34984L # Variable c_uint '34984u'
GL_PROGRAM_PIPELINE_BINDING = 33370L # Variable c_uint '33370u'
GL_PROGRAM_POINT_SIZE = 34370L # Variable c_uint '34370u'
GL_PROGRAM_POINT_SIZE_ARB = 34370L # Variable c_uint '34370u'
GL_PROGRAM_POINT_SIZE_EXT = 34370L # Variable c_uint '34370u'
GL_PROGRAM_RESIDENT_NV = 34375L # Variable c_uint '34375u'
GL_PROGRAM_RESULT_COMPONENTS_NV = 35079L # Variable c_uint '35079u'
GL_PROGRAM_SEPARABLE = 33368L # Variable c_uint '33368u'
GL_PROGRAM_STRING_ARB = 34344L # Variable c_uint '34344u'
GL_PROGRAM_STRING_NV = 34344L # Variable c_uint '34344u'
GL_PROGRAM_TARGET_NV = 34374L # Variable c_uint '34374u'
GL_PROGRAM_TEMPORARIES_ARB = 34980L # Variable c_uint '34980u'
GL_PROGRAM_TEX_INDIRECTIONS_ARB = 34823L # Variable c_uint '34823u'
GL_PROGRAM_TEX_INSTRUCTIONS_ARB = 34822L # Variable c_uint '34822u'
GL_PROGRAM_UNDER_NATIVE_LIMITS_ARB = 34998L # Variable c_uint '34998u'
GL_PROJECTION = 5889L # Variable c_uint '5889u'
GL_PROJECTION_MATRIX = 2983L # Variable c_uint '2983u'
GL_PROJECTION_STACK_DEPTH = 2980L # Variable c_uint '2980u'
GL_PROVOKING_VERTEX = 36431L # Variable c_uint '36431u'
GL_PROVOKING_VERTEX_EXT = 36431L # Variable c_uint '36431u'
GL_PROXY_COLOR_TABLE = 32979L # Variable c_uint '32979u'
GL_PROXY_COLOR_TABLE_SGI = 32979L # Variable c_uint '32979u'
GL_PROXY_HISTOGRAM = 32805L # Variable c_uint '32805u'
GL_PROXY_HISTOGRAM_EXT = 32805L # Variable c_uint '32805u'
GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE = 32981L # Variable c_uint '32981u'
GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE_SGI = 32981L # Variable c_uint '32981u'
GL_PROXY_POST_CONVOLUTION_COLOR_TABLE = 32980L # Variable c_uint '32980u'
GL_PROXY_POST_CONVOLUTION_COLOR_TABLE_SGI = 32980L # Variable c_uint '32980u'
GL_PROXY_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP = 33123L # Variable c_uint '33123u'
GL_PROXY_TEXTURE_1D = 32867L # Variable c_uint '32867u'
GL_PROXY_TEXTURE_1D_ARRAY = 35865L # Variable c_uint '35865u'
GL_PROXY_TEXTURE_1D_ARRAY_EXT = 35865L # Variable c_uint '35865u'
GL_PROXY_TEXTURE_1D_EXT = 32867L # Variable c_uint '32867u'
GL_PROXY_TEXTURE_1D_STACK_MESAX = 34651L # Variable c_uint '34651u'
GL_PROXY_TEXTURE_2D = 32868L # Variable c_uint '32868u'
GL_PROXY_TEXTURE_2D_ARRAY = 35867L # Variable c_uint '35867u'
GL_PROXY_TEXTURE_2D_ARRAY_EXT = 35867L # Variable c_uint '35867u'
GL_PROXY_TEXTURE_2D_EXT = 32868L # Variable c_uint '32868u'
GL_PROXY_TEXTURE_2D_MULTISAMPLE = 37121L # Variable c_uint '37121u'
GL_PROXY_TEXTURE_2D_MULTISAMPLE_ARRAY = 37123L # Variable c_uint '37123u'
GL_PROXY_TEXTURE_2D_STACK_MESAX = 34652L # Variable c_uint '34652u'
GL_PROXY_TEXTURE_3D = 32880L # Variable c_uint '32880u'
GL_PROXY_TEXTURE_3D_EXT = 32880L # Variable c_uint '32880u'
GL_PROXY_TEXTURE_4D_SGIS = 33077L # Variable c_uint '33077u'
GL_PROXY_TEXTURE_COLOR_TABLE_SGI = 32957L # Variable c_uint '32957u'
GL_PROXY_TEXTURE_CUBE_MAP = 34075L # Variable c_uint '34075u'
GL_PROXY_TEXTURE_CUBE_MAP_ARB = 34075L # Variable c_uint '34075u'
GL_PROXY_TEXTURE_CUBE_MAP_ARRAY = 36875L # Variable c_uint '36875u'
GL_PROXY_TEXTURE_CUBE_MAP_ARRAY_ARB = 36875L # Variable c_uint '36875u'
GL_PROXY_TEXTURE_CUBE_MAP_EXT = 34075L # Variable c_uint '34075u'
GL_PROXY_TEXTURE_RECTANGLE = 34039L # Variable c_uint '34039u'
GL_PROXY_TEXTURE_RECTANGLE_ARB = 34039L # Variable c_uint '34039u'
GL_PROXY_TEXTURE_RECTANGLE_NV = 34039L # Variable c_uint '34039u'
GL_PURGEABLE_APPLE = 35357L # Variable c_uint '35357u'
GL_Q = 8195L # Variable c_uint '8195u'
GL_QUAD_ALPHA4_SGIS = 33054L # Variable c_uint '33054u'
GL_QUAD_ALPHA8_SGIS = 33055L # Variable c_uint '33055u'
GL_QUAD_INTENSITY4_SGIS = 33058L # Variable c_uint '33058u'
GL_QUAD_INTENSITY8_SGIS = 33059L # Variable c_uint '33059u'
GL_QUAD_LUMINANCE4_SGIS = 33056L # Variable c_uint '33056u'
GL_QUAD_LUMINANCE8_SGIS = 33057L # Variable c_uint '33057u'
GL_QUAD_MESH_SUN = 34324L # Variable c_uint '34324u'
GL_QUADRATIC_ATTENUATION = 4617L # Variable c_uint '4617u'
GL_QUADS = 7L # Variable c_uint '7u'
GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION = 36428L # Variable c_uint '36428u'
GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION_EXT = 36428L # Variable c_uint '36428u'
GL_QUAD_STRIP = 8L # Variable c_uint '8u'
GL_QUAD_TEXTURE_SELECT_SGIS = 33061L # Variable c_uint '33061u'
GL_QUARTER_BIT_ATI = 16L # Variable c_uint '16u'
GL_QUERY_BY_REGION_NO_WAIT = 36374L # Variable c_uint '36374u'
GL_QUERY_BY_REGION_NO_WAIT_NV = 36374L # Variable c_uint '36374u'
GL_QUERY_BY_REGION_WAIT = 36373L # Variable c_uint '36373u'
GL_QUERY_BY_REGION_WAIT_NV = 36373L # Variable c_uint '36373u'
GL_QUERY_COUNTER_BITS = 34916L # Variable c_uint '34916u'
GL_QUERY_COUNTER_BITS_ARB = 34916L # Variable c_uint '34916u'
GL_QUERY_NO_WAIT = 36372L # Variable c_uint '36372u'
GL_QUERY_NO_WAIT_NV = 36372L # Variable c_uint '36372u'
GL_QUERY_OBJECT_AMD = 37203L # Variable c_uint '37203u'
GL_QUERY_RESULT = 34918L # Variable c_uint '34918u'
GL_QUERY_RESULT_ARB = 34918L # Variable c_uint '34918u'
GL_QUERY_RESULT_AVAILABLE = 34919L # Variable c_uint '34919u'
GL_QUERY_RESULT_AVAILABLE_ARB = 34919L # Variable c_uint '34919u'
GL_QUERY_WAIT = 36371L # Variable c_uint '36371u'
GL_QUERY_WAIT_NV = 36371L # Variable c_uint '36371u'
GL_R = 8194L # Variable c_uint '8194u'
GL_R11F_G11F_B10F = 35898L # Variable c_uint '35898u'
GL_R11F_G11F_B10F_EXT = 35898L # Variable c_uint '35898u'
GL_R16 = 33322L # Variable c_uint '33322u'
GL_R16F = 33325L # Variable c_uint '33325u'
GL_R16I = 33331L # Variable c_uint '33331u'
GL_R16_SNORM = 36760L # Variable c_uint '36760u'
GL_R16UI = 33332L # Variable c_uint '33332u'
GL_R1UI_C3F_V3F_SUN = 34246L # Variable c_uint '34246u'
GL_R1UI_C4F_N3F_V3F_SUN = 34248L # Variable c_uint '34248u'
GL_R1UI_C4UB_V3F_SUN = 34245L # Variable c_uint '34245u'
GL_R1UI_N3F_V3F_SUN = 34247L # Variable c_uint '34247u'
GL_R1UI_T2F_C4F_N3F_V3F_SUN = 34251L # Variable c_uint '34251u'
GL_R1UI_T2F_N3F_V3F_SUN = 34250L # Variable c_uint '34250u'
GL_R1UI_T2F_V3F_SUN = 34249L # Variable c_uint '34249u'
GL_R1UI_V3F_SUN = 34244L # Variable c_uint '34244u'
GL_R32F = 33326L # Variable c_uint '33326u'
GL_R32I = 33333L # Variable c_uint '33333u'
GL_R32UI = 33334L # Variable c_uint '33334u'
GL_R3_G3_B2 = 10768L # Variable c_uint '10768u'
GL_R8 = 33321L # Variable c_uint '33321u'
GL_R8I = 33329L # Variable c_uint '33329u'
GL_R8_SNORM = 36756L # Variable c_uint '36756u'
GL_R8UI = 33330L # Variable c_uint '33330u'
GL_RASTERIZER_DISCARD = 35977L # Variable c_uint '35977u'
GL_RASTERIZER_DISCARD_EXT = 35977L # Variable c_uint '35977u'
GL_RASTERIZER_DISCARD_NV = 35977L # Variable c_uint '35977u'
GL_RASTER_POSITION_UNCLIPPED_IBM = 103010L # Variable c_uint '103010u'
GL_READ_BUFFER = 3074L # Variable c_uint '3074u'
GL_READ_FRAMEBUFFER = 36008L # Variable c_uint '36008u'
GL_READ_FRAMEBUFFER_BINDING = 36010L # Variable c_uint '36010u'
GL_READ_FRAMEBUFFER_BINDING_EXT = 36010L # Variable c_uint '36010u'
GL_READ_FRAMEBUFFER_EXT = 36008L # Variable c_uint '36008u'
GL_READ_ONLY = 35000L # Variable c_uint '35000u'
GL_READ_ONLY_ARB = 35000L # Variable c_uint '35000u'
GL_READ_PIXEL_DATA_RANGE_LENGTH_NV = 34939L # Variable c_uint '34939u'
GL_READ_PIXEL_DATA_RANGE_NV = 34937L # Variable c_uint '34937u'
GL_READ_PIXEL_DATA_RANGE_POINTER_NV = 34941L # Variable c_uint '34941u'
GL_READ_WRITE = 35002L # Variable c_uint '35002u'
GL_READ_WRITE_ARB = 35002L # Variable c_uint '35002u'
GL_RECLAIM_MEMORY_HINT_PGI = 107006L # Variable c_uint '107006u'
GL_RED = 6403L # Variable c_uint '6403u'
GL_RED_BIAS = 3349L # Variable c_uint '3349u'
GL_RED_BIT_ATI = 1L # Variable c_uint '1u'
GL_RED_BITS = 3410L # Variable c_uint '3410u'
GL_RED_INTEGER = 36244L # Variable c_uint '36244u'
GL_RED_INTEGER_EXT = 36244L # Variable c_uint '36244u'
GL_RED_MAX_CLAMP_INGR = 34148L # Variable c_uint '34148u'
GL_RED_MIN_CLAMP_INGR = 34144L # Variable c_uint '34144u'
GL_RED_SCALE = 3348L # Variable c_uint '3348u'
GL_RED_SNORM = 36752L # Variable c_uint '36752u'
GL_REDUCE = 32790L # Variable c_uint '32790u'
GL_REDUCE_EXT = 32790L # Variable c_uint '32790u'
GL_REFERENCE_PLANE_EQUATION_SGIX = 33150L # Variable c_uint '33150u'
GL_REFERENCE_PLANE_SGIX = 33149L # Variable c_uint '33149u'
GL_REFLECTION_MAP = 34066L # Variable c_uint '34066u'
GL_REFLECTION_MAP_ARB = 34066L # Variable c_uint '34066u'
GL_REFLECTION_MAP_EXT = 34066L # Variable c_uint '34066u'
GL_REFLECTION_MAP_NV = 34066L # Variable c_uint '34066u'
GL_REG_0_ATI = 35105L # Variable c_uint '35105u'
GL_REG_10_ATI = 35115L # Variable c_uint '35115u'
GL_REG_11_ATI = 35116L # Variable c_uint '35116u'
GL_REG_12_ATI = 35117L # Variable c_uint '35117u'
GL_REG_13_ATI = 35118L # Variable c_uint '35118u'
GL_REG_14_ATI = 35119L # Variable c_uint '35119u'
GL_REG_15_ATI = 35120L # Variable c_uint '35120u'
GL_REG_16_ATI = 35121L # Variable c_uint '35121u'
GL_REG_17_ATI = 35122L # Variable c_uint '35122u'
GL_REG_18_ATI = 35123L # Variable c_uint '35123u'
GL_REG_19_ATI = 35124L # Variable c_uint '35124u'
GL_REG_1_ATI = 35106L # Variable c_uint '35106u'
GL_REG_20_ATI = 35125L # Variable c_uint '35125u'
GL_REG_21_ATI = 35126L # Variable c_uint '35126u'
GL_REG_22_ATI = 35127L # Variable c_uint '35127u'
GL_REG_23_ATI = 35128L # Variable c_uint '35128u'
GL_REG_24_ATI = 35129L # Variable c_uint '35129u'
GL_REG_25_ATI = 35130L # Variable c_uint '35130u'
GL_REG_26_ATI = 35131L # Variable c_uint '35131u'
GL_REG_27_ATI = 35132L # Variable c_uint '35132u'
GL_REG_28_ATI = 35133L # Variable c_uint '35133u'
GL_REG_29_ATI = 35134L # Variable c_uint '35134u'
GL_REG_2_ATI = 35107L # Variable c_uint '35107u'
GL_REG_30_ATI = 35135L # Variable c_uint '35135u'
GL_REG_31_ATI = 35136L # Variable c_uint '35136u'
GL_REG_3_ATI = 35108L # Variable c_uint '35108u'
GL_REG_4_ATI = 35109L # Variable c_uint '35109u'
GL_REG_5_ATI = 35110L # Variable c_uint '35110u'
GL_REG_6_ATI = 35111L # Variable c_uint '35111u'
GL_REG_7_ATI = 35112L # Variable c_uint '35112u'
GL_REG_8_ATI = 35113L # Variable c_uint '35113u'
GL_REG_9_ATI = 35114L # Variable c_uint '35114u'
GL_REGISTER_COMBINERS_NV = 34082L # Variable c_uint '34082u'
GL_RELEASED_APPLE = 35353L # Variable c_uint '35353u'
GL_RENDER = 7168L # Variable c_uint '7168u'
GL_RENDERBUFFER = 36161L # Variable c_uint '36161u'
GL_RENDERBUFFER_ALPHA_SIZE = 36179L # Variable c_uint '36179u'
GL_RENDERBUFFER_ALPHA_SIZE_EXT = 36179L # Variable c_uint '36179u'
GL_RENDERBUFFER_BINDING = 36007L # Variable c_uint '36007u'
GL_RENDERBUFFER_BINDING_EXT = 36007L # Variable c_uint '36007u'
GL_RENDERBUFFER_BLUE_SIZE = 36178L # Variable c_uint '36178u'
GL_RENDERBUFFER_BLUE_SIZE_EXT = 36178L # Variable c_uint '36178u'
GL_RENDERBUFFER_COLOR_SAMPLES_NV = 36368L # Variable c_uint '36368u'
GL_RENDERBUFFER_COVERAGE_SAMPLES_NV = 36011L # Variable c_uint '36011u'
GL_RENDERBUFFER_DEPTH_SIZE = 36180L # Variable c_uint '36180u'
GL_RENDERBUFFER_DEPTH_SIZE_EXT = 36180L # Variable c_uint '36180u'
GL_RENDERBUFFER_EXT = 36161L # Variable c_uint '36161u'
GL_RENDERBUFFER_FREE_MEMORY_ATI = 34813L # Variable c_uint '34813u'
GL_RENDERBUFFER_GREEN_SIZE = 36177L # Variable c_uint '36177u'
GL_RENDERBUFFER_GREEN_SIZE_EXT = 36177L # Variable c_uint '36177u'
GL_RENDERBUFFER_HEIGHT = 36163L # Variable c_uint '36163u'
GL_RENDERBUFFER_HEIGHT_EXT = 36163L # Variable c_uint '36163u'
GL_RENDERBUFFER_INTERNAL_FORMAT = 36164L # Variable c_uint '36164u'
GL_RENDERBUFFER_INTERNAL_FORMAT_EXT = 36164L # Variable c_uint '36164u'
GL_RENDERBUFFER_RED_SIZE = 36176L # Variable c_uint '36176u'
GL_RENDERBUFFER_RED_SIZE_EXT = 36176L # Variable c_uint '36176u'
GL_RENDERBUFFER_SAMPLES = 36011L # Variable c_uint '36011u'
GL_RENDERBUFFER_SAMPLES_EXT = 36011L # Variable c_uint '36011u'
GL_RENDERBUFFER_STENCIL_SIZE = 36181L # Variable c_uint '36181u'
GL_RENDERBUFFER_STENCIL_SIZE_EXT = 36181L # Variable c_uint '36181u'
GL_RENDERBUFFER_WIDTH = 36162L # Variable c_uint '36162u'
GL_RENDERBUFFER_WIDTH_EXT = 36162L # Variable c_uint '36162u'
GL_RENDERER = 7937L # Variable c_uint '7937u'
GL_RENDER_MODE = 3136L # Variable c_uint '3136u'
GL_REPEAT = 10497L # Variable c_uint '10497u'
GL_REPLACE = 7681L # Variable c_uint '7681u'
GL_REPLACE_EXT = 32866L # Variable c_uint '32866u'
GL_REPLACEMENT_CODE_ARRAY_POINTER_SUN = 34243L # Variable c_uint '34243u'
GL_REPLACEMENT_CODE_ARRAY_STRIDE_SUN = 34242L # Variable c_uint '34242u'
GL_REPLACEMENT_CODE_ARRAY_SUN = 34240L # Variable c_uint '34240u'
GL_REPLACEMENT_CODE_ARRAY_TYPE_SUN = 34241L # Variable c_uint '34241u'
GL_REPLACEMENT_CODE_SUN = 33240L # Variable c_uint '33240u'
GL_REPLACE_MIDDLE_SUN = 2L # Variable c_uint '2u'
GL_REPLACE_OLDEST_SUN = 3L # Variable c_uint '3u'
GL_REPLICATE_BORDER = 33107L # Variable c_uint '33107u'
GL_REPLICATE_BORDER_HP = 33107L # Variable c_uint '33107u'
GL_RESAMPLE_AVERAGE_OML = 35208L # Variable c_uint '35208u'
GL_RESAMPLE_DECIMATE_OML = 35209L # Variable c_uint '35209u'
GL_RESAMPLE_DECIMATE_SGIX = 33840L # Variable c_uint '33840u'
GL_RESAMPLE_REPLICATE_OML = 35206L # Variable c_uint '35206u'
GL_RESAMPLE_REPLICATE_SGIX = 33838L # Variable c_uint '33838u'
GL_RESAMPLE_ZERO_FILL_OML = 35207L # Variable c_uint '35207u'
GL_RESAMPLE_ZERO_FILL_SGIX = 33839L # Variable c_uint '33839u'
GL_RESCALE_NORMAL = 32826L # Variable c_uint '32826u'
GL_RESCALE_NORMAL_EXT = 32826L # Variable c_uint '32826u'
GL_RESET_NOTIFICATION_STRATEGY_ARB = 33366L # Variable c_uint '33366u'
GL_RESTART_SUN = 1L # Variable c_uint '1u'
GL_RETAINED_APPLE = 35355L # Variable c_uint '35355u'
GL_RETURN = 258L # Variable c_uint '258u'
GL_RG = 33319L # Variable c_uint '33319u'
GL_RG16 = 33324L # Variable c_uint '33324u'
GL_RG16F = 33327L # Variable c_uint '33327u'
GL_RG16I = 33337L # Variable c_uint '33337u'
GL_RG16_SNORM = 36761L # Variable c_uint '36761u'
GL_RG16UI = 33338L # Variable c_uint '33338u'
GL_RG32F = 33328L # Variable c_uint '33328u'
GL_RG32I = 33339L # Variable c_uint '33339u'
GL_RG32UI = 33340L # Variable c_uint '33340u'
GL_RG8 = 33323L # Variable c_uint '33323u'
GL_RG8I = 33335L # Variable c_uint '33335u'
GL_RG8_SNORM = 36757L # Variable c_uint '36757u'
GL_RG8UI = 33336L # Variable c_uint '33336u'
GL_RGB = 6407L # Variable c_uint '6407u'
GL_RGB10 = 32850L # Variable c_uint '32850u'
GL_RGB10_A2 = 32857L # Variable c_uint '32857u'
GL_RGB10_A2_EXT = 32857L # Variable c_uint '32857u'
GL_RGB10_A2UI = 36975L # Variable c_uint '36975u'
GL_RGB10_EXT = 32850L # Variable c_uint '32850u'
GL_RGB12 = 32851L # Variable c_uint '32851u'
GL_RGB12_EXT = 32851L # Variable c_uint '32851u'
GL_RGB16 = 32852L # Variable c_uint '32852u'
GL_RGB16_EXT = 32852L # Variable c_uint '32852u'
GL_RGB16F = 34843L # Variable c_uint '34843u'
GL_RGB16F_ARB = 34843L # Variable c_uint '34843u'
GL_RGB16I = 36233L # Variable c_uint '36233u'
GL_RGB16I_EXT = 36233L # Variable c_uint '36233u'
GL_RGB16_SNORM = 36762L # Variable c_uint '36762u'
GL_RGB16UI = 36215L # Variable c_uint '36215u'
GL_RGB16UI_EXT = 36215L # Variable c_uint '36215u'
GL_RGB2_EXT = 32846L # Variable c_uint '32846u'
GL_RGB32F = 34837L # Variable c_uint '34837u'
GL_RGB32F_ARB = 34837L # Variable c_uint '34837u'
GL_RGB32I = 36227L # Variable c_uint '36227u'
GL_RGB32I_EXT = 36227L # Variable c_uint '36227u'
GL_RGB32UI = 36209L # Variable c_uint '36209u'
GL_RGB32UI_EXT = 36209L # Variable c_uint '36209u'
GL_RGB4 = 32847L # Variable c_uint '32847u'
GL_RGB_422_APPLE = 35359L # Variable c_uint '35359u'
GL_RGB4_EXT = 32847L # Variable c_uint '32847u'
GL_RGB4_S3TC = 33697L # Variable c_uint '33697u'
GL_RGB5 = 32848L # Variable c_uint '32848u'
GL_RGB5_A1 = 32855L # Variable c_uint '32855u'
GL_RGB5_A1_EXT = 32855L # Variable c_uint '32855u'
GL_RGB5_EXT = 32848L # Variable c_uint '32848u'
GL_RGB8 = 32849L # Variable c_uint '32849u'
GL_RGB8_EXT = 32849L # Variable c_uint '32849u'
GL_RGB8I = 36239L # Variable c_uint '36239u'
GL_RGB8I_EXT = 36239L # Variable c_uint '36239u'
GL_RGB8_SNORM = 36758L # Variable c_uint '36758u'
GL_RGB8UI = 36221L # Variable c_uint '36221u'
GL_RGB8UI_EXT = 36221L # Variable c_uint '36221u'
GL_RGB9_E5 = 35901L # Variable c_uint '35901u'
GL_RGB9_E5_EXT = 35901L # Variable c_uint '35901u'
GL_RGBA = 6408L # Variable c_uint '6408u'
GL_RGBA12 = 32858L # Variable c_uint '32858u'
GL_RGBA12_EXT = 32858L # Variable c_uint '32858u'
GL_RGBA16 = 32859L # Variable c_uint '32859u'
GL_RGBA16_EXT = 32859L # Variable c_uint '32859u'
GL_RGBA16F = 34842L # Variable c_uint '34842u'
GL_RGBA16F_ARB = 34842L # Variable c_uint '34842u'
GL_RGBA16I = 36232L # Variable c_uint '36232u'
GL_RGBA16I_EXT = 36232L # Variable c_uint '36232u'
GL_RGBA16_SNORM = 36763L # Variable c_uint '36763u'
GL_RGBA16UI = 36214L # Variable c_uint '36214u'
GL_RGBA16UI_EXT = 36214L # Variable c_uint '36214u'
GL_RGBA2 = 32853L # Variable c_uint '32853u'
GL_RGBA2_EXT = 32853L # Variable c_uint '32853u'
GL_RGBA32F = 34836L # Variable c_uint '34836u'
GL_RGBA32F_ARB = 34836L # Variable c_uint '34836u'
GL_RGBA32I = 36226L # Variable c_uint '36226u'
GL_RGBA32I_EXT = 36226L # Variable c_uint '36226u'
GL_RGBA32UI = 36208L # Variable c_uint '36208u'
GL_RGBA32UI_EXT = 36208L # Variable c_uint '36208u'
GL_RGBA4 = 32854L # Variable c_uint '32854u'
GL_RGBA4_EXT = 32854L # Variable c_uint '32854u'
GL_RGBA4_S3TC = 33699L # Variable c_uint '33699u'
GL_RGBA8 = 32856L # Variable c_uint '32856u'
GL_RGBA8_EXT = 32856L # Variable c_uint '32856u'
GL_RGBA8I = 36238L # Variable c_uint '36238u'
GL_RGBA8I_EXT = 36238L # Variable c_uint '36238u'
GL_RGBA8_SNORM = 36759L # Variable c_uint '36759u'
GL_RGBA8UI = 36220L # Variable c_uint '36220u'
GL_RGBA8UI_EXT = 36220L # Variable c_uint '36220u'
GL_RGBA_FLOAT16_APPLE = 34842L # Variable c_uint '34842u'
GL_RGBA_FLOAT16_ATI = 34842L # Variable c_uint '34842u'
GL_RGBA_FLOAT32_APPLE = 34836L # Variable c_uint '34836u'
GL_RGBA_FLOAT32_ATI = 34836L # Variable c_uint '34836u'
GL_RGBA_FLOAT_MODE_ARB = 34848L # Variable c_uint '34848u'
GL_RGBA_INTEGER = 36249L # Variable c_uint '36249u'
GL_RGBA_INTEGER_EXT = 36249L # Variable c_uint '36249u'
GL_RGBA_INTEGER_MODE_EXT = 36254L # Variable c_uint '36254u'
GL_RGBA_MODE = 3121L # Variable c_uint '3121u'
GL_RGBA_S3TC = 33698L # Variable c_uint '33698u'
GL_RGBA_SIGNED_COMPONENTS_EXT = 35900L # Variable c_uint '35900u'
GL_RGBA_SNORM = 36755L # Variable c_uint '36755u'
GL_RGBA_UNSIGNED_DOT_PRODUCT_MAPPING_NV = 34521L # Variable c_uint '34521u'
GL_RGB_FLOAT16_APPLE = 34843L # Variable c_uint '34843u'
GL_RGB_FLOAT16_ATI = 34843L # Variable c_uint '34843u'
GL_RGB_FLOAT32_APPLE = 34837L # Variable c_uint '34837u'
GL_RGB_FLOAT32_ATI = 34837L # Variable c_uint '34837u'
GL_RGB_INTEGER = 36248L # Variable c_uint '36248u'
GL_RGB_INTEGER_EXT = 36248L # Variable c_uint '36248u'
GL_RGB_S3TC = 33696L # Variable c_uint '33696u'
GL_RGB_SCALE = 34163L # Variable c_uint '34163u'
GL_RGB_SCALE_ARB = 34163L # Variable c_uint '34163u'
GL_RGB_SCALE_EXT = 34163L # Variable c_uint '34163u'
GL_RGB_SNORM = 36754L # Variable c_uint '36754u'
GL_RG_INTEGER = 33320L # Variable c_uint '33320u'
GL_RG_SNORM = 36753L # Variable c_uint '36753u'
GL_RIGHT = 1031L # Variable c_uint '1031u'
GL_S = 8192L # Variable c_uint '8192u'
GL_SAMPLE_ALPHA_TO_COVERAGE = 32926L # Variable c_uint '32926u'
GL_SAMPLE_ALPHA_TO_COVERAGE_ARB = 32926L # Variable c_uint '32926u'
GL_SAMPLE_ALPHA_TO_MASK_EXT = 32926L # Variable c_uint '32926u'
GL_SAMPLE_ALPHA_TO_MASK_SGIS = 32926L # Variable c_uint '32926u'
GL_SAMPLE_ALPHA_TO_ONE = 32927L # Variable c_uint '32927u'
GL_SAMPLE_ALPHA_TO_ONE_ARB = 32927L # Variable c_uint '32927u'
GL_SAMPLE_ALPHA_TO_ONE_EXT = 32927L # Variable c_uint '32927u'
GL_SAMPLE_ALPHA_TO_ONE_SGIS = 32927L # Variable c_uint '32927u'
GL_SAMPLE_BUFFERS = 32936L # Variable c_uint '32936u'
GL_SAMPLE_BUFFERS_3DFX = 34483L # Variable c_uint '34483u'
GL_SAMPLE_BUFFERS_ARB = 32936L # Variable c_uint '32936u'
GL_SAMPLE_BUFFERS_EXT = 32936L # Variable c_uint '32936u'
GL_SAMPLE_BUFFERS_SGIS = 32936L # Variable c_uint '32936u'
GL_SAMPLE_COVERAGE = 32928L # Variable c_uint '32928u'
GL_SAMPLE_COVERAGE_ARB = 32928L # Variable c_uint '32928u'
GL_SAMPLE_COVERAGE_INVERT = 32939L # Variable c_uint '32939u'
GL_SAMPLE_COVERAGE_INVERT_ARB = 32939L # Variable c_uint '32939u'
GL_SAMPLE_COVERAGE_VALUE = 32938L # Variable c_uint '32938u'
GL_SAMPLE_COVERAGE_VALUE_ARB = 32938L # Variable c_uint '32938u'
GL_SAMPLE_MASK = 36433L # Variable c_uint '36433u'
GL_SAMPLE_MASK_EXT = 32928L # Variable c_uint '32928u'
GL_SAMPLE_MASK_INVERT_EXT = 32939L # Variable c_uint '32939u'
GL_SAMPLE_MASK_INVERT_SGIS = 32939L # Variable c_uint '32939u'
GL_SAMPLE_MASK_NV = 36433L # Variable c_uint '36433u'
GL_SAMPLE_MASK_SGIS = 32928L # Variable c_uint '32928u'
GL_SAMPLE_MASK_VALUE = 36434L # Variable c_uint '36434u'
GL_SAMPLE_MASK_VALUE_EXT = 32938L # Variable c_uint '32938u'
GL_SAMPLE_MASK_VALUE_NV = 36434L # Variable c_uint '36434u'
GL_SAMPLE_MASK_VALUE_SGIS = 32938L # Variable c_uint '32938u'
GL_SAMPLE_PATTERN_EXT = 32940L # Variable c_uint '32940u'
GL_SAMPLE_PATTERN_SGIS = 32940L # Variable c_uint '32940u'
GL_SAMPLE_POSITION = 36432L # Variable c_uint '36432u'
GL_SAMPLE_POSITION_NV = 36432L # Variable c_uint '36432u'
GL_SAMPLER_1D = 35677L # Variable c_uint '35677u'
GL_SAMPLER_1D_ARB = 35677L # Variable c_uint '35677u'
GL_SAMPLER_1D_ARRAY = 36288L # Variable c_uint '36288u'
GL_SAMPLER_1D_ARRAY_EXT = 36288L # Variable c_uint '36288u'
GL_SAMPLER_1D_ARRAY_SHADOW = 36291L # Variable c_uint '36291u'
GL_SAMPLER_1D_ARRAY_SHADOW_EXT = 36291L # Variable c_uint '36291u'
GL_SAMPLER_1D_SHADOW = 35681L # Variable c_uint '35681u'
GL_SAMPLER_1D_SHADOW_ARB = 35681L # Variable c_uint '35681u'
GL_SAMPLER_2D = 35678L # Variable c_uint '35678u'
GL_SAMPLER_2D_ARB = 35678L # Variable c_uint '35678u'
GL_SAMPLER_2D_ARRAY = 36289L # Variable c_uint '36289u'
GL_SAMPLER_2D_ARRAY_EXT = 36289L # Variable c_uint '36289u'
GL_SAMPLER_2D_ARRAY_SHADOW = 36292L # Variable c_uint '36292u'
GL_SAMPLER_2D_ARRAY_SHADOW_EXT = 36292L # Variable c_uint '36292u'
GL_SAMPLER_2D_MULTISAMPLE = 37128L # Variable c_uint '37128u'
GL_SAMPLER_2D_MULTISAMPLE_ARRAY = 37131L # Variable c_uint '37131u'
GL_SAMPLER_2D_RECT = 35683L # Variable c_uint '35683u'
GL_SAMPLER_2D_RECT_ARB = 35683L # Variable c_uint '35683u'
GL_SAMPLER_2D_RECT_SHADOW = 35684L # Variable c_uint '35684u'
GL_SAMPLER_2D_RECT_SHADOW_ARB = 35684L # Variable c_uint '35684u'
GL_SAMPLER_2D_SHADOW = 35682L # Variable c_uint '35682u'
GL_SAMPLER_2D_SHADOW_ARB = 35682L # Variable c_uint '35682u'
GL_SAMPLER_3D = 35679L # Variable c_uint '35679u'
GL_SAMPLER_3D_ARB = 35679L # Variable c_uint '35679u'
GL_SAMPLER_BINDING = 35097L # Variable c_uint '35097u'
GL_SAMPLER_BUFFER = 36290L # Variable c_uint '36290u'
GL_SAMPLER_BUFFER_AMD = 36865L # Variable c_uint '36865u'
GL_SAMPLER_BUFFER_EXT = 36290L # Variable c_uint '36290u'
GL_SAMPLER_CUBE = 35680L # Variable c_uint '35680u'
GL_SAMPLER_CUBE_ARB = 35680L # Variable c_uint '35680u'
GL_SAMPLER_CUBE_MAP_ARRAY = 36876L # Variable c_uint '36876u'
GL_SAMPLER_CUBE_MAP_ARRAY_ARB = 36876L # Variable c_uint '36876u'
GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW = 36877L # Variable c_uint '36877u'
GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW_ARB = 36877L # Variable c_uint '36877u'
GL_SAMPLER_CUBE_SHADOW = 36293L # Variable c_uint '36293u'
GL_SAMPLER_CUBE_SHADOW_EXT = 36293L # Variable c_uint '36293u'
GL_SAMPLER_OBJECT_AMD = 37205L # Variable c_uint '37205u'
GL_SAMPLER_RENDERBUFFER_NV = 36438L # Variable c_uint '36438u'
GL_SAMPLES = 32937L # Variable c_uint '32937u'
GL_SAMPLES_3DFX = 34484L # Variable c_uint '34484u'
GL_SAMPLES_ARB = 32937L # Variable c_uint '32937u'
GL_SAMPLES_EXT = 32937L # Variable c_uint '32937u'
GL_SAMPLE_SHADING = 35894L # Variable c_uint '35894u'
GL_SAMPLE_SHADING_ARB = 35894L # Variable c_uint '35894u'
GL_SAMPLES_PASSED = 35092L # Variable c_uint '35092u'
GL_SAMPLES_PASSED_ARB = 35092L # Variable c_uint '35092u'
GL_SAMPLES_SGIS = 32937L # Variable c_uint '32937u'
GL_SATURATE_BIT_ATI = 64L # Variable c_uint '64u'
GL_SCALAR_EXT = 34750L # Variable c_uint '34750u'
GL_SCALEBIAS_HINT_SGIX = 33570L # Variable c_uint '33570u'
GL_SCALE_BY_FOUR_NV = 34111L # Variable c_uint '34111u'
GL_SCALE_BY_ONE_HALF_NV = 34112L # Variable c_uint '34112u'
GL_SCALE_BY_TWO_NV = 34110L # Variable c_uint '34110u'
GL_SCISSOR_BIT = 524288L # Variable c_uint '524288u'
GL_SCISSOR_BOX = 3088L # Variable c_uint '3088u'
GL_SCISSOR_TEST = 3089L # Variable c_uint '3089u'
GL_SCREEN_COORDINATES_REND = 33936L # Variable c_uint '33936u'
GL_SECONDARY_COLOR_ARRAY = 33886L # Variable c_uint '33886u'
GL_SECONDARY_COLOR_ARRAY_ADDRESS_NV = 36647L # Variable c_uint '36647u'
GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING = 34972L # Variable c_uint '34972u'
GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING_ARB = 34972L # Variable c_uint '34972u'
GL_SECONDARY_COLOR_ARRAY_EXT = 33886L # Variable c_uint '33886u'
GL_SECONDARY_COLOR_ARRAY_LENGTH_NV = 36657L # Variable c_uint '36657u'
GL_SECONDARY_COLOR_ARRAY_LIST_IBM = 103077L # Variable c_uint '103077u'
GL_SECONDARY_COLOR_ARRAY_LIST_STRIDE_IBM = 103087L # Variable c_uint '103087u'
GL_SECONDARY_COLOR_ARRAY_POINTER = 33885L # Variable c_uint '33885u'
GL_SECONDARY_COLOR_ARRAY_POINTER_EXT = 33885L # Variable c_uint '33885u'
GL_SECONDARY_COLOR_ARRAY_SIZE = 33882L # Variable c_uint '33882u'
GL_SECONDARY_COLOR_ARRAY_SIZE_EXT = 33882L # Variable c_uint '33882u'
GL_SECONDARY_COLOR_ARRAY_STRIDE = 33884L # Variable c_uint '33884u'
GL_SECONDARY_COLOR_ARRAY_STRIDE_EXT = 33884L # Variable c_uint '33884u'
GL_SECONDARY_COLOR_ARRAY_TYPE = 33883L # Variable c_uint '33883u'
GL_SECONDARY_COLOR_ARRAY_TYPE_EXT = 33883L # Variable c_uint '33883u'
GL_SECONDARY_COLOR_NV = 34093L # Variable c_uint '34093u'
GL_SECONDARY_INTERPOLATOR_ATI = 35181L # Variable c_uint '35181u'
GL_SELECT = 7170L # Variable c_uint '7170u'
GL_SELECTION_BUFFER_POINTER = 3571L # Variable c_uint '3571u'
GL_SELECTION_BUFFER_SIZE = 3572L # Variable c_uint '3572u'
GL_SEPARABLE_2D = 32786L # Variable c_uint '32786u'
GL_SEPARABLE_2D_EXT = 32786L # Variable c_uint '32786u'
GL_SEPARATE_ATTRIBS = 35981L # Variable c_uint '35981u'
GL_SEPARATE_ATTRIBS_EXT = 35981L # Variable c_uint '35981u'
GL_SEPARATE_ATTRIBS_NV = 35981L # Variable c_uint '35981u'
GL_SEPARATE_SPECULAR_COLOR = 33274L # Variable c_uint '33274u'
GL_SEPARATE_SPECULAR_COLOR_EXT = 33274L # Variable c_uint '33274u'
GL_SET = 5391L # Variable c_uint '5391u'
GL_SHADE_MODEL = 2900L # Variable c_uint '2900u'
GL_SHADER_COMPILER = 36346L # Variable c_uint '36346u'
GL_SHADER_CONSISTENT_NV = 34525L # Variable c_uint '34525u'
GL_SHADER_GLOBAL_ACCESS_BARRIER_BIT_NV = 16L # Variable c_uint '16u'
GL_SHADER_IMAGE_ACCESS_BARRIER_BIT_EXT = 32L # Variable c_uint '32u'
GL_SHADER_INCLUDE_ARB = 36270L # Variable c_uint '36270u'
GL_SHADER_OBJECT_ARB = 35656L # Variable c_uint '35656u'
GL_SHADER_OPERATION_NV = 34527L # Variable c_uint '34527u'
GL_SHADER_SOURCE_LENGTH = 35720L # Variable c_uint '35720u'
GL_SHADER_TYPE = 35663L # Variable c_uint '35663u'
GL_SHADING_LANGUAGE_VERSION = 35724L # Variable c_uint '35724u'
GL_SHADING_LANGUAGE_VERSION_ARB = 35724L # Variable c_uint '35724u'
GL_SHADOW_AMBIENT_SGIX = 32959L # Variable c_uint '32959u'
GL_SHADOW_ATTENUATION_EXT = 33614L # Variable c_uint '33614u'
GL_SHARED_TEXTURE_PALETTE_EXT = 33275L # Variable c_uint '33275u'
GL_SHARPEN_TEXTURE_FUNC_POINTS_SGIS = 32944L # Variable c_uint '32944u'
GL_SHININESS = 5633L # Variable c_uint '5633u'
GL_SHORT = 5122L # Variable c_uint '5122u'
GL_SIGNALED = 37145L # Variable c_uint '37145u'
GL_SIGNED_ALPHA8_NV = 34566L # Variable c_uint '34566u'
GL_SIGNED_ALPHA_NV = 34565L # Variable c_uint '34565u'
GL_SIGNED_HILO16_NV = 34554L # Variable c_uint '34554u'
GL_SIGNED_HILO8_NV = 34911L # Variable c_uint '34911u'
GL_SIGNED_HILO_NV = 34553L # Variable c_uint '34553u'
GL_SIGNED_IDENTITY_NV = 34108L # Variable c_uint '34108u'
GL_SIGNED_INTENSITY8_NV = 34568L # Variable c_uint '34568u'
GL_SIGNED_INTENSITY_NV = 34567L # Variable c_uint '34567u'
GL_SIGNED_LUMINANCE8_ALPHA8_NV = 34564L # Variable c_uint '34564u'
GL_SIGNED_LUMINANCE8_NV = 34562L # Variable c_uint '34562u'
GL_SIGNED_LUMINANCE_ALPHA_NV = 34563L # Variable c_uint '34563u'
GL_SIGNED_LUMINANCE_NV = 34561L # Variable c_uint '34561u'
GL_SIGNED_NEGATE_NV = 34109L # Variable c_uint '34109u'
GL_SIGNED_NORMALIZED = 36764L # Variable c_uint '36764u'
GL_SIGNED_RGB8_NV = 34559L # Variable c_uint '34559u'
GL_SIGNED_RGB8_UNSIGNED_ALPHA8_NV = 34573L # Variable c_uint '34573u'
GL_SIGNED_RGBA8_NV = 34556L # Variable c_uint '34556u'
GL_SIGNED_RGBA_NV = 34555L # Variable c_uint '34555u'
GL_SIGNED_RGB_NV = 34558L # Variable c_uint '34558u'
GL_SIGNED_RGB_UNSIGNED_ALPHA_NV = 34572L # Variable c_uint '34572u'
GL_SINGLE_COLOR = 33273L # Variable c_uint '33273u'
GL_SINGLE_COLOR_EXT = 33273L # Variable c_uint '33273u'
GL_SLICE_ACCUM_SUN = 34252L # Variable c_uint '34252u'
GL_SLUMINANCE = 35910L # Variable c_uint '35910u'
GL_SLUMINANCE8 = 35911L # Variable c_uint '35911u'
GL_SLUMINANCE8_ALPHA8 = 35909L # Variable c_uint '35909u'
GL_SLUMINANCE8_ALPHA8_EXT = 35909L # Variable c_uint '35909u'
GL_SLUMINANCE8_EXT = 35911L # Variable c_uint '35911u'
GL_SLUMINANCE_ALPHA = 35908L # Variable c_uint '35908u'
GL_SLUMINANCE_ALPHA_EXT = 35908L # Variable c_uint '35908u'
GL_SLUMINANCE_EXT = 35910L # Variable c_uint '35910u'
GL_SMOOTH = 7425L # Variable c_uint '7425u'
GL_SMOOTH_LINE_WIDTH_GRANULARITY = 2851L # Variable c_uint '2851u'
GL_SMOOTH_LINE_WIDTH_RANGE = 2850L # Variable c_uint '2850u'
GL_SMOOTH_POINT_SIZE_GRANULARITY = 2835L # Variable c_uint '2835u'
GL_SMOOTH_POINT_SIZE_RANGE = 2834L # Variable c_uint '2834u'
GL_SOURCE0_ALPHA = 34184L # Variable c_uint '34184u'
GL_SOURCE0_ALPHA_ARB = 34184L # Variable c_uint '34184u'
GL_SOURCE0_ALPHA_EXT = 34184L # Variable c_uint '34184u'
GL_SOURCE0_RGB = 34176L # Variable c_uint '34176u'
GL_SOURCE0_RGB_ARB = 34176L # Variable c_uint '34176u'
GL_SOURCE0_RGB_EXT = 34176L # Variable c_uint '34176u'
GL_SOURCE1_ALPHA = 34185L # Variable c_uint '34185u'
GL_SOURCE1_ALPHA_ARB = 34185L # Variable c_uint '34185u'
GL_SOURCE1_ALPHA_EXT = 34185L # Variable c_uint '34185u'
GL_SOURCE1_RGB = 34177L # Variable c_uint '34177u'
GL_SOURCE1_RGB_ARB = 34177L # Variable c_uint '34177u'
GL_SOURCE1_RGB_EXT = 34177L # Variable c_uint '34177u'
GL_SOURCE2_ALPHA = 34186L # Variable c_uint '34186u'
GL_SOURCE2_ALPHA_ARB = 34186L # Variable c_uint '34186u'
GL_SOURCE2_ALPHA_EXT = 34186L # Variable c_uint '34186u'
GL_SOURCE2_RGB = 34178L # Variable c_uint '34178u'
GL_SOURCE2_RGB_ARB = 34178L # Variable c_uint '34178u'
GL_SOURCE2_RGB_EXT = 34178L # Variable c_uint '34178u'
GL_SOURCE3_ALPHA_NV = 34187L # Variable c_uint '34187u'
GL_SOURCE3_RGB_NV = 34179L # Variable c_uint '34179u'
GL_SPARE0_NV = 34094L # Variable c_uint '34094u'
GL_SPARE0_PLUS_SECONDARY_COLOR_NV = 34098L # Variable c_uint '34098u'
GL_SPARE1_NV = 34095L # Variable c_uint '34095u'
GL_SPECULAR = 4610L # Variable c_uint '4610u'
GL_SPHERE_MAP = 9218L # Variable c_uint '9218u'
GL_SPOT_CUTOFF = 4614L # Variable c_uint '4614u'
GL_SPOT_DIRECTION = 4612L # Variable c_uint '4612u'
GL_SPOT_EXPONENT = 4613L # Variable c_uint '4613u'
GL_SPRITE_AXIAL_SGIX = 33100L # Variable c_uint '33100u'
GL_SPRITE_AXIS_SGIX = 33098L # Variable c_uint '33098u'
GL_SPRITE_EYE_ALIGNED_SGIX = 33102L # Variable c_uint '33102u'
GL_SPRITE_MODE_SGIX = 33097L # Variable c_uint '33097u'
GL_SPRITE_OBJECT_ALIGNED_SGIX = 33101L # Variable c_uint '33101u'
GL_SPRITE_SGIX = 33096L # Variable c_uint '33096u'
GL_SPRITE_TRANSLATION_SGIX = 33099L # Variable c_uint '33099u'
GL_SRC0_ALPHA = 34184L # Variable c_uint '34184u'
GL_SRC0_RGB = 34176L # Variable c_uint '34176u'
GL_SRC1_ALPHA = 34185L # Variable c_uint '34185u'
GL_SRC1_COLOR = 35065L # Variable c_uint '35065u'
GL_SRC1_RGB = 34177L # Variable c_uint '34177u'
GL_SRC2_ALPHA = 34186L # Variable c_uint '34186u'
GL_SRC2_RGB = 34178L # Variable c_uint '34178u'
GL_SRC_ALPHA = 770L # Variable c_uint '770u'
GL_SRC_ALPHA_SATURATE = 776L # Variable c_uint '776u'
GL_SRC_COLOR = 768L # Variable c_uint '768u'
GL_SRGB = 35904L # Variable c_uint '35904u'
GL_SRGB8 = 35905L # Variable c_uint '35905u'
GL_SRGB8_ALPHA8 = 35907L # Variable c_uint '35907u'
GL_SRGB8_ALPHA8_EXT = 35907L # Variable c_uint '35907u'
GL_SRGB8_EXT = 35905L # Variable c_uint '35905u'
GL_SRGB_ALPHA = 35906L # Variable c_uint '35906u'
GL_SRGB_ALPHA_EXT = 35906L # Variable c_uint '35906u'
GL_SRGB_EXT = 35904L # Variable c_uint '35904u'
GL_STACK_OVERFLOW = 1283L # Variable c_uint '1283u'
GL_STACK_UNDERFLOW = 1284L # Variable c_uint '1284u'
GL_STATIC_ATI = 34656L # Variable c_uint '34656u'
GL_STATIC_COPY = 35046L # Variable c_uint '35046u'
GL_STATIC_COPY_ARB = 35046L # Variable c_uint '35046u'
GL_STATIC_DRAW = 35044L # Variable c_uint '35044u'
GL_STATIC_DRAW_ARB = 35044L # Variable c_uint '35044u'
GL_STATIC_READ = 35045L # Variable c_uint '35045u'
GL_STATIC_READ_ARB = 35045L # Variable c_uint '35045u'
GL_STENCIL = 6146L # Variable c_uint '6146u'
GL_STENCIL_ATTACHMENT = 36128L # Variable c_uint '36128u'
GL_STENCIL_ATTACHMENT_EXT = 36128L # Variable c_uint '36128u'
GL_STENCIL_BACK_FAIL = 34817L # Variable c_uint '34817u'
GL_STENCIL_BACK_FAIL_ATI = 34817L # Variable c_uint '34817u'
GL_STENCIL_BACK_FUNC = 34816L # Variable c_uint '34816u'
GL_STENCIL_BACK_FUNC_ATI = 34816L # Variable c_uint '34816u'
GL_STENCIL_BACK_PASS_DEPTH_FAIL = 34818L # Variable c_uint '34818u'
GL_STENCIL_BACK_PASS_DEPTH_FAIL_ATI = 34818L # Variable c_uint '34818u'
GL_STENCIL_BACK_PASS_DEPTH_PASS = 34819L # Variable c_uint '34819u'
GL_STENCIL_BACK_PASS_DEPTH_PASS_ATI = 34819L # Variable c_uint '34819u'
GL_STENCIL_BACK_REF = 36003L # Variable c_uint '36003u'
GL_STENCIL_BACK_VALUE_MASK = 36004L # Variable c_uint '36004u'
GL_STENCIL_BACK_WRITEMASK = 36005L # Variable c_uint '36005u'
GL_STENCIL_BITS = 3415L # Variable c_uint '3415u'
GL_STENCIL_BUFFER = 33316L # Variable c_uint '33316u'
GL_STENCIL_BUFFER_BIT = 1024L # Variable c_uint '1024u'
GL_STENCIL_CLEAR_TAG_VALUE_EXT = 35059L # Variable c_uint '35059u'
GL_STENCIL_CLEAR_VALUE = 2961L # Variable c_uint '2961u'
GL_STENCIL_FAIL = 2964L # Variable c_uint '2964u'
GL_STENCIL_FUNC = 2962L # Variable c_uint '2962u'
GL_STENCIL_INDEX = 6401L # Variable c_uint '6401u'
GL_STENCIL_INDEX1 = 36166L # Variable c_uint '36166u'
GL_STENCIL_INDEX16 = 36169L # Variable c_uint '36169u'
GL_STENCIL_INDEX16_EXT = 36169L # Variable c_uint '36169u'
GL_STENCIL_INDEX1_EXT = 36166L # Variable c_uint '36166u'
GL_STENCIL_INDEX4 = 36167L # Variable c_uint '36167u'
GL_STENCIL_INDEX4_EXT = 36167L # Variable c_uint '36167u'
GL_STENCIL_INDEX8 = 36168L # Variable c_uint '36168u'
GL_STENCIL_INDEX8_EXT = 36168L # Variable c_uint '36168u'
GL_STENCIL_PASS_DEPTH_FAIL = 2965L # Variable c_uint '2965u'
GL_STENCIL_PASS_DEPTH_PASS = 2966L # Variable c_uint '2966u'
GL_STENCIL_REF = 2967L # Variable c_uint '2967u'
GL_STENCIL_TAG_BITS_EXT = 35058L # Variable c_uint '35058u'
GL_STENCIL_TEST = 2960L # Variable c_uint '2960u'
GL_STENCIL_TEST_TWO_SIDE_EXT = 35088L # Variable c_uint '35088u'
GL_STENCIL_VALUE_MASK = 2963L # Variable c_uint '2963u'
GL_STENCIL_WRITEMASK = 2968L # Variable c_uint '2968u'
GL_STEREO = 3123L # Variable c_uint '3123u'
GL_STORAGE_CACHED_APPLE = 34238L # Variable c_uint '34238u'
GL_STORAGE_CLIENT_APPLE = 34228L # Variable c_uint '34228u'
GL_STORAGE_PRIVATE_APPLE = 34237L # Variable c_uint '34237u'
GL_STORAGE_SHARED_APPLE = 34239L # Variable c_uint '34239u'
GL_STREAM_COPY = 35042L # Variable c_uint '35042u'
GL_STREAM_COPY_ARB = 35042L # Variable c_uint '35042u'
GL_STREAM_DRAW = 35040L # Variable c_uint '35040u'
GL_STREAM_DRAW_ARB = 35040L # Variable c_uint '35040u'
GL_STREAM_READ = 35041L # Variable c_uint '35041u'
GL_STREAM_READ_ARB = 35041L # Variable c_uint '35041u'
GL_STRICT_DEPTHFUNC_HINT_PGI = 107030L # Variable c_uint '107030u'
GL_STRICT_LIGHTING_HINT_PGI = 107031L # Variable c_uint '107031u'
GL_STRICT_SCISSOR_HINT_PGI = 107032L # Variable c_uint '107032u'
GL_SUB_ATI = 35173L # Variable c_uint '35173u'
GL_SUBPIXEL_BITS = 3408L # Variable c_uint '3408u'
GL_SUBTRACT = 34023L # Variable c_uint '34023u'
GL_SUBTRACT_ARB = 34023L # Variable c_uint '34023u'
GL_SUCCESS_NV = 36911L # Variable c_uint '36911u'
GL_SURFACE_MAPPED_NV = 34560L # Variable c_uint '34560u'
GL_SURFACE_REGISTERED_NV = 34557L # Variable c_uint '34557u'
GL_SURFACE_STATE_NV = 34539L # Variable c_uint '34539u'
GL_SWIZZLE_STQ_ATI = 35191L # Variable c_uint '35191u'
GL_SWIZZLE_STQ_DQ_ATI = 35193L # Variable c_uint '35193u'
GL_SWIZZLE_STR_ATI = 35190L # Variable c_uint '35190u'
GL_SWIZZLE_STR_DR_ATI = 35192L # Variable c_uint '35192u'
GL_SWIZZLE_STRQ_ATI = 35194L # Variable c_uint '35194u'
GL_SWIZZLE_STRQ_DQ_ATI = 35195L # Variable c_uint '35195u'
GL_SYNC_CL_EVENT_ARB = 33344L # Variable c_uint '33344u'
GL_SYNC_CL_EVENT_COMPLETE_ARB = 33345L # Variable c_uint '33345u'
GL_SYNC_CONDITION = 37139L # Variable c_uint '37139u'
GL_SYNC_FENCE = 37142L # Variable c_uint '37142u'
GL_SYNC_FLAGS = 37141L # Variable c_uint '37141u'
GL_SYNC_FLUSH_COMMANDS_BIT = 1L # Variable c_uint '1u'
GL_SYNC_GPU_COMMANDS_COMPLETE = 37143L # Variable c_uint '37143u'
GL_SYNC_STATUS = 37140L # Variable c_uint '37140u'
GL_T = 8193L # Variable c_uint '8193u'
GL_T2F_C3F_V3F = 10794L # Variable c_uint '10794u'
GL_T2F_C4F_N3F_V3F = 10796L # Variable c_uint '10796u'
GL_T2F_C4UB_V3F = 10793L # Variable c_uint '10793u'
GL_T2F_IUI_N3F_V2F_EXT = 33203L # Variable c_uint '33203u'
GL_T2F_IUI_N3F_V3F_EXT = 33204L # Variable c_uint '33204u'
GL_T2F_IUI_V2F_EXT = 33201L # Variable c_uint '33201u'
GL_T2F_IUI_V3F_EXT = 33202L # Variable c_uint '33202u'
GL_T2F_N3F_V3F = 10795L # Variable c_uint '10795u'
GL_T2F_V3F = 10791L # Variable c_uint '10791u'
GL_T4F_C4F_N3F_V4F = 10797L # Variable c_uint '10797u'
GL_T4F_V4F = 10792L # Variable c_uint '10792u'
GL_TABLE_TOO_LARGE = 32817L # Variable c_uint '32817u'
GL_TABLE_TOO_LARGE_EXT = 32817L # Variable c_uint '32817u'
GL_TANGENT_ARRAY_EXT = 33849L # Variable c_uint '33849u'
GL_TANGENT_ARRAY_POINTER_EXT = 33858L # Variable c_uint '33858u'
GL_TANGENT_ARRAY_STRIDE_EXT = 33855L # Variable c_uint '33855u'
GL_TANGENT_ARRAY_TYPE_EXT = 33854L # Variable c_uint '33854u'
GL_TESS_CONTROL_OUTPUT_VERTICES = 36469L # Variable c_uint '36469u'
GL_TESS_CONTROL_PROGRAM_NV = 35102L # Variable c_uint '35102u'
GL_TESS_CONTROL_PROGRAM_PARAMETER_BUFFER_NV = 35956L # Variable c_uint '35956u'
GL_TESS_CONTROL_SHADER = 36488L # Variable c_uint '36488u'
GL_TESS_CONTROL_SHADER_BIT = 8L # Variable c_uint '8u'
GL_TESSELLATION_FACTOR_AMD = 36869L # Variable c_uint '36869u'
GL_TESSELLATION_MODE_AMD = 36868L # Variable c_uint '36868u'
GL_TESS_EVALUATION_PROGRAM_NV = 35103L # Variable c_uint '35103u'
GL_TESS_EVALUATION_PROGRAM_PARAMETER_BUFFER_NV = 35957L # Variable c_uint '35957u'
GL_TESS_EVALUATION_SHADER = 36487L # Variable c_uint '36487u'
GL_TESS_EVALUATION_SHADER_BIT = 16L # Variable c_uint '16u'
GL_TESS_GEN_MODE = 36470L # Variable c_uint '36470u'
GL_TESS_GEN_POINT_MODE = 36473L # Variable c_uint '36473u'
GL_TESS_GEN_SPACING = 36471L # Variable c_uint '36471u'
GL_TESS_GEN_VERTEX_ORDER = 36472L # Variable c_uint '36472u'
GL_TEXCOORD1_BIT_PGI = 268435456L # Variable c_uint '268435456u'
GL_TEXCOORD2_BIT_PGI = 536870912L # Variable c_uint '536870912u'
GL_TEXCOORD3_BIT_PGI = 1073741824L # Variable c_uint '1073741824u'
GL_TEXCOORD4_BIT_PGI = 2147483648L # Variable c_uint '2147483648u'
GL_TEXT_FRAGMENT_SHADER_ATI = 33280L # Variable c_uint '33280u'
GL_TEXTURE0 = 33984L # Variable c_uint '33984u'
GL_TEXTURE0_ARB = 33984L # Variable c_uint '33984u'
GL_TEXTURE = 5890L # Variable c_uint '5890u'
GL_TEXTURE10 = 33994L # Variable c_uint '33994u'
GL_TEXTURE10_ARB = 33994L # Variable c_uint '33994u'
GL_TEXTURE1 = 33985L # Variable c_uint '33985u'
GL_TEXTURE11 = 33995L # Variable c_uint '33995u'
GL_TEXTURE11_ARB = 33995L # Variable c_uint '33995u'
GL_TEXTURE12 = 33996L # Variable c_uint '33996u'
GL_TEXTURE12_ARB = 33996L # Variable c_uint '33996u'
GL_TEXTURE13 = 33997L # Variable c_uint '33997u'
GL_TEXTURE13_ARB = 33997L # Variable c_uint '33997u'
GL_TEXTURE14 = 33998L # Variable c_uint '33998u'
GL_TEXTURE14_ARB = 33998L # Variable c_uint '33998u'
GL_TEXTURE15 = 33999L # Variable c_uint '33999u'
GL_TEXTURE15_ARB = 33999L # Variable c_uint '33999u'
GL_TEXTURE16 = 34000L # Variable c_uint '34000u'
GL_TEXTURE16_ARB = 34000L # Variable c_uint '34000u'
GL_TEXTURE17 = 34001L # Variable c_uint '34001u'
GL_TEXTURE17_ARB = 34001L # Variable c_uint '34001u'
GL_TEXTURE18 = 34002L # Variable c_uint '34002u'
GL_TEXTURE18_ARB = 34002L # Variable c_uint '34002u'
GL_TEXTURE19 = 34003L # Variable c_uint '34003u'
GL_TEXTURE19_ARB = 34003L # Variable c_uint '34003u'
GL_TEXTURE1_ARB = 33985L # Variable c_uint '33985u'
GL_TEXTURE_1D = 3552L # Variable c_uint '3552u'
GL_TEXTURE_1D_ARRAY = 35864L # Variable c_uint '35864u'
GL_TEXTURE_1D_ARRAY_EXT = 35864L # Variable c_uint '35864u'
GL_TEXTURE_1D_BINDING_EXT = 32872L # Variable c_uint '32872u'
GL_TEXTURE_1D_STACK_BINDING_MESAX = 34653L # Variable c_uint '34653u'
GL_TEXTURE_1D_STACK_MESAX = 34649L # Variable c_uint '34649u'
GL_TEXTURE20 = 34004L # Variable c_uint '34004u'
GL_TEXTURE20_ARB = 34004L # Variable c_uint '34004u'
GL_TEXTURE2 = 33986L # Variable c_uint '33986u'
GL_TEXTURE21 = 34005L # Variable c_uint '34005u'
GL_TEXTURE21_ARB = 34005L # Variable c_uint '34005u'
GL_TEXTURE22 = 34006L # Variable c_uint '34006u'
GL_TEXTURE22_ARB = 34006L # Variable c_uint '34006u'
GL_TEXTURE23 = 34007L # Variable c_uint '34007u'
GL_TEXTURE23_ARB = 34007L # Variable c_uint '34007u'
GL_TEXTURE24 = 34008L # Variable c_uint '34008u'
GL_TEXTURE24_ARB = 34008L # Variable c_uint '34008u'
GL_TEXTURE25 = 34009L # Variable c_uint '34009u'
GL_TEXTURE25_ARB = 34009L # Variable c_uint '34009u'
GL_TEXTURE26 = 34010L # Variable c_uint '34010u'
GL_TEXTURE26_ARB = 34010L # Variable c_uint '34010u'
GL_TEXTURE27 = 34011L # Variable c_uint '34011u'
GL_TEXTURE27_ARB = 34011L # Variable c_uint '34011u'
GL_TEXTURE28 = 34012L # Variable c_uint '34012u'
GL_TEXTURE28_ARB = 34012L # Variable c_uint '34012u'
GL_TEXTURE29 = 34013L # Variable c_uint '34013u'
GL_TEXTURE29_ARB = 34013L # Variable c_uint '34013u'
GL_TEXTURE2_ARB = 33986L # Variable c_uint '33986u'
GL_TEXTURE_2D = 3553L # Variable c_uint '3553u'
GL_TEXTURE_2D_ARRAY = 35866L # Variable c_uint '35866u'
GL_TEXTURE_2D_ARRAY_EXT = 35866L # Variable c_uint '35866u'
GL_TEXTURE_2D_BINDING_EXT = 32873L # Variable c_uint '32873u'
GL_TEXTURE_2D_MULTISAMPLE = 37120L # Variable c_uint '37120u'
GL_TEXTURE_2D_MULTISAMPLE_ARRAY = 37122L # Variable c_uint '37122u'
GL_TEXTURE_2D_STACK_BINDING_MESAX = 34654L # Variable c_uint '34654u'
GL_TEXTURE_2D_STACK_MESAX = 34650L # Variable c_uint '34650u'
GL_TEXTURE30 = 34014L # Variable c_uint '34014u'
GL_TEXTURE30_ARB = 34014L # Variable c_uint '34014u'
GL_TEXTURE3 = 33987L # Variable c_uint '33987u'
GL_TEXTURE31 = 34015L # Variable c_uint '34015u'
GL_TEXTURE31_ARB = 34015L # Variable c_uint '34015u'
GL_TEXTURE3_ARB = 33987L # Variable c_uint '33987u'
GL_TEXTURE_3D = 32879L # Variable c_uint '32879u'
GL_TEXTURE_3D_BINDING_EXT = 32874L # Variable c_uint '32874u'
GL_TEXTURE_3D_EXT = 32879L # Variable c_uint '32879u'
GL_TEXTURE4 = 33988L # Variable c_uint '33988u'
GL_TEXTURE4_ARB = 33988L # Variable c_uint '33988u'
GL_TEXTURE_4D_BINDING_SGIS = 33103L # Variable c_uint '33103u'
GL_TEXTURE_4D_SGIS = 33076L # Variable c_uint '33076u'
GL_TEXTURE_4DSIZE_SGIS = 33078L # Variable c_uint '33078u'
GL_TEXTURE5 = 33989L # Variable c_uint '33989u'
GL_TEXTURE5_ARB = 33989L # Variable c_uint '33989u'
GL_TEXTURE6 = 33990L # Variable c_uint '33990u'
GL_TEXTURE6_ARB = 33990L # Variable c_uint '33990u'
GL_TEXTURE7 = 33991L # Variable c_uint '33991u'
GL_TEXTURE7_ARB = 33991L # Variable c_uint '33991u'
GL_TEXTURE8 = 33992L # Variable c_uint '33992u'
GL_TEXTURE8_ARB = 33992L # Variable c_uint '33992u'
GL_TEXTURE9 = 33993L # Variable c_uint '33993u'
GL_TEXTURE9_ARB = 33993L # Variable c_uint '33993u'
GL_TEXTURE_ALPHA_SIZE = 32863L # Variable c_uint '32863u'
GL_TEXTURE_ALPHA_SIZE_EXT = 32863L # Variable c_uint '32863u'
GL_TEXTURE_ALPHA_TYPE = 35859L # Variable c_uint '35859u'
GL_TEXTURE_ALPHA_TYPE_ARB = 35859L # Variable c_uint '35859u'
GL_TEXTURE_APPLICATION_MODE_EXT = 33615L # Variable c_uint '33615u'
GL_TEXTURE_BASE_LEVEL = 33084L # Variable c_uint '33084u'
GL_TEXTURE_BASE_LEVEL_SGIS = 33084L # Variable c_uint '33084u'
GL_TEXTURE_BINDING_1D = 32872L # Variable c_uint '32872u'
GL_TEXTURE_BINDING_1D_ARRAY = 35868L # Variable c_uint '35868u'
GL_TEXTURE_BINDING_1D_ARRAY_EXT = 35868L # Variable c_uint '35868u'
GL_TEXTURE_BINDING_2D = 32873L # Variable c_uint '32873u'
GL_TEXTURE_BINDING_2D_ARRAY = 35869L # Variable c_uint '35869u'
GL_TEXTURE_BINDING_2D_ARRAY_EXT = 35869L # Variable c_uint '35869u'
GL_TEXTURE_BINDING_2D_MULTISAMPLE = 37124L # Variable c_uint '37124u'
GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY = 37125L # Variable c_uint '37125u'
GL_TEXTURE_BINDING_3D = 32874L # Variable c_uint '32874u'
GL_TEXTURE_BINDING_BUFFER = 35884L # Variable c_uint '35884u'
GL_TEXTURE_BINDING_BUFFER_ARB = 35884L # Variable c_uint '35884u'
GL_TEXTURE_BINDING_BUFFER_EXT = 35884L # Variable c_uint '35884u'
GL_TEXTURE_BINDING_CUBE_MAP = 34068L # Variable c_uint '34068u'
GL_TEXTURE_BINDING_CUBE_MAP_ARB = 34068L # Variable c_uint '34068u'
GL_TEXTURE_BINDING_CUBE_MAP_ARRAY = 36874L # Variable c_uint '36874u'
GL_TEXTURE_BINDING_CUBE_MAP_ARRAY_ARB = 36874L # Variable c_uint '36874u'
GL_TEXTURE_BINDING_CUBE_MAP_EXT = 34068L # Variable c_uint '34068u'
GL_TEXTURE_BINDING_RECTANGLE = 34038L # Variable c_uint '34038u'
GL_TEXTURE_BINDING_RECTANGLE_ARB = 34038L # Variable c_uint '34038u'
GL_TEXTURE_BINDING_RECTANGLE_NV = 34038L # Variable c_uint '34038u'
GL_TEXTURE_BINDING_RENDERBUFFER_NV = 36435L # Variable c_uint '36435u'
GL_TEXTURE_BIT = 262144L # Variable c_uint '262144u'
GL_TEXTURE_BLUE_SIZE = 32862L # Variable c_uint '32862u'
GL_TEXTURE_BLUE_SIZE_EXT = 32862L # Variable c_uint '32862u'
GL_TEXTURE_BLUE_TYPE = 35858L # Variable c_uint '35858u'
GL_TEXTURE_BLUE_TYPE_ARB = 35858L # Variable c_uint '35858u'
GL_TEXTURE_BORDER = 4101L # Variable c_uint '4101u'
GL_TEXTURE_BORDER_COLOR = 4100L # Variable c_uint '4100u'
GL_TEXTURE_BORDER_VALUES_NV = 34586L # Variable c_uint '34586u'
GL_TEXTURE_BUFFER = 35882L # Variable c_uint '35882u'
GL_TEXTURE_BUFFER_ARB = 35882L # Variable c_uint '35882u'
GL_TEXTURE_BUFFER_DATA_STORE_BINDING = 35885L # Variable c_uint '35885u'
GL_TEXTURE_BUFFER_DATA_STORE_BINDING_ARB = 35885L # Variable c_uint '35885u'
GL_TEXTURE_BUFFER_DATA_STORE_BINDING_EXT = 35885L # Variable c_uint '35885u'
GL_TEXTURE_BUFFER_EXT = 35882L # Variable c_uint '35882u'
GL_TEXTURE_BUFFER_FORMAT = 35886L # Variable c_uint '35886u'
GL_TEXTURE_BUFFER_FORMAT_ARB = 35886L # Variable c_uint '35886u'
GL_TEXTURE_BUFFER_FORMAT_EXT = 35886L # Variable c_uint '35886u'
GL_TEXTURE_CLIPMAP_CENTER_SGIX = 33137L # Variable c_uint '33137u'
GL_TEXTURE_CLIPMAP_DEPTH_SGIX = 33142L # Variable c_uint '33142u'
GL_TEXTURE_CLIPMAP_FRAME_SGIX = 33138L # Variable c_uint '33138u'
GL_TEXTURE_CLIPMAP_LOD_OFFSET_SGIX = 33141L # Variable c_uint '33141u'
GL_TEXTURE_CLIPMAP_OFFSET_SGIX = 33139L # Variable c_uint '33139u'
GL_TEXTURE_CLIPMAP_VIRTUAL_DEPTH_SGIX = 33140L # Variable c_uint '33140u'
GL_TEXTURE_COLOR_TABLE_SGI = 32956L # Variable c_uint '32956u'
GL_TEXTURE_COLOR_WRITEMASK_SGIS = 33263L # Variable c_uint '33263u'
GL_TEXTURE_COMPARE_FAIL_VALUE_ARB = 32959L # Variable c_uint '32959u'
GL_TEXTURE_COMPARE_FUNC = 34893L # Variable c_uint '34893u'
GL_TEXTURE_COMPARE_FUNC_ARB = 34893L # Variable c_uint '34893u'
GL_TEXTURE_COMPARE_MODE = 34892L # Variable c_uint '34892u'
GL_TEXTURE_COMPARE_MODE_ARB = 34892L # Variable c_uint '34892u'
GL_TEXTURE_COMPARE_OPERATOR_SGIX = 33179L # Variable c_uint '33179u'
GL_TEXTURE_COMPARE_SGIX = 33178L # Variable c_uint '33178u'
GL_TEXTURE_COMPONENTS = 4099L # Variable c_uint '4099u'
GL_TEXTURE_COMPRESSED = 34465L # Variable c_uint '34465u'
GL_TEXTURE_COMPRESSED_ARB = 34465L # Variable c_uint '34465u'
GL_TEXTURE_COMPRESSED_IMAGE_SIZE = 34464L # Variable c_uint '34464u'
GL_TEXTURE_COMPRESSED_IMAGE_SIZE_ARB = 34464L # Variable c_uint '34464u'
GL_TEXTURE_COMPRESSION_HINT = 34031L # Variable c_uint '34031u'
GL_TEXTURE_COMPRESSION_HINT_ARB = 34031L # Variable c_uint '34031u'
GL_TEXTURE_CONSTANT_DATA_SUNX = 33238L # Variable c_uint '33238u'
GL_TEXTURE_COORD_ARRAY = 32888L # Variable c_uint '32888u'
GL_TEXTURE_COORD_ARRAY_ADDRESS_NV = 36645L # Variable c_uint '36645u'
GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING = 34970L # Variable c_uint '34970u'
GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING_ARB = 34970L # Variable c_uint '34970u'
GL_TEXTURE_COORD_ARRAY_COUNT_EXT = 32907L # Variable c_uint '32907u'
GL_TEXTURE_COORD_ARRAY_EXT = 32888L # Variable c_uint '32888u'
GL_TEXTURE_COORD_ARRAY_LENGTH_NV = 36655L # Variable c_uint '36655u'
GL_TEXTURE_COORD_ARRAY_LIST_IBM = 103074L # Variable c_uint '103074u'
GL_TEXTURE_COORD_ARRAY_LIST_STRIDE_IBM = 103084L # Variable c_uint '103084u'
GL_TEXTURE_COORD_ARRAY_PARALLEL_POINTERS_INTEL = 33784L # Variable c_uint '33784u'
GL_TEXTURE_COORD_ARRAY_POINTER = 32914L # Variable c_uint '32914u'
GL_TEXTURE_COORD_ARRAY_POINTER_EXT = 32914L # Variable c_uint '32914u'
GL_TEXTURE_COORD_ARRAY_SIZE = 32904L # Variable c_uint '32904u'
GL_TEXTURE_COORD_ARRAY_SIZE_EXT = 32904L # Variable c_uint '32904u'
GL_TEXTURE_COORD_ARRAY_STRIDE = 32906L # Variable c_uint '32906u'
GL_TEXTURE_COORD_ARRAY_STRIDE_EXT = 32906L # Variable c_uint '32906u'
GL_TEXTURE_COORD_ARRAY_TYPE = 32905L # Variable c_uint '32905u'
GL_TEXTURE_COORD_ARRAY_TYPE_EXT = 32905L # Variable c_uint '32905u'
GL_TEXTURE_COORD_NV = 35961L # Variable c_uint '35961u'
GL_TEXTURE_CUBE_MAP = 34067L # Variable c_uint '34067u'
GL_TEXTURE_CUBE_MAP_ARB = 34067L # Variable c_uint '34067u'
GL_TEXTURE_CUBE_MAP_ARRAY = 36873L # Variable c_uint '36873u'
GL_TEXTURE_CUBE_MAP_ARRAY_ARB = 36873L # Variable c_uint '36873u'
GL_TEXTURE_CUBE_MAP_EXT = 34067L # Variable c_uint '34067u'
GL_TEXTURE_CUBE_MAP_NEGATIVE_X = 34070L # Variable c_uint '34070u'
GL_TEXTURE_CUBE_MAP_NEGATIVE_X_ARB = 34070L # Variable c_uint '34070u'
GL_TEXTURE_CUBE_MAP_NEGATIVE_X_EXT = 34070L # Variable c_uint '34070u'
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y = 34072L # Variable c_uint '34072u'
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_ARB = 34072L # Variable c_uint '34072u'
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_EXT = 34072L # Variable c_uint '34072u'
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z = 34074L # Variable c_uint '34074u'
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_ARB = 34074L # Variable c_uint '34074u'
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_EXT = 34074L # Variable c_uint '34074u'
GL_TEXTURE_CUBE_MAP_POSITIVE_X = 34069L # Variable c_uint '34069u'
GL_TEXTURE_CUBE_MAP_POSITIVE_X_ARB = 34069L # Variable c_uint '34069u'
GL_TEXTURE_CUBE_MAP_POSITIVE_X_EXT = 34069L # Variable c_uint '34069u'
GL_TEXTURE_CUBE_MAP_POSITIVE_Y = 34071L # Variable c_uint '34071u'
GL_TEXTURE_CUBE_MAP_POSITIVE_Y_ARB = 34071L # Variable c_uint '34071u'
GL_TEXTURE_CUBE_MAP_POSITIVE_Y_EXT = 34071L # Variable c_uint '34071u'
GL_TEXTURE_CUBE_MAP_POSITIVE_Z = 34073L # Variable c_uint '34073u'
GL_TEXTURE_CUBE_MAP_POSITIVE_Z_ARB = 34073L # Variable c_uint '34073u'
GL_TEXTURE_CUBE_MAP_POSITIVE_Z_EXT = 34073L # Variable c_uint '34073u'
GL_TEXTURE_CUBE_MAP_SEAMLESS = 34895L # Variable c_uint '34895u'
GL_TEXTURE_DEFORMATION_BIT_SGIX = 1L # Variable c_uint '1u'
GL_TEXTURE_DEFORMATION_SGIX = 33173L # Variable c_uint '33173u'
GL_TEXTURE_DEPTH = 32881L # Variable c_uint '32881u'
GL_TEXTURE_DEPTH_EXT = 32881L # Variable c_uint '32881u'
GL_TEXTURE_DEPTH_SIZE = 34890L # Variable c_uint '34890u'
GL_TEXTURE_DEPTH_SIZE_ARB = 34890L # Variable c_uint '34890u'
GL_TEXTURE_DEPTH_TYPE = 35862L # Variable c_uint '35862u'
GL_TEXTURE_DEPTH_TYPE_ARB = 35862L # Variable c_uint '35862u'
GL_TEXTURE_DS_SIZE_NV = 34589L # Variable c_uint '34589u'
GL_TEXTURE_DT_SIZE_NV = 34590L # Variable c_uint '34590u'
GL_TEXTURE_ENV = 8960L # Variable c_uint '8960u'
GL_TEXTURE_ENV_BIAS_SGIX = 32958L # Variable c_uint '32958u'
GL_TEXTURE_ENV_COLOR = 8705L # Variable c_uint '8705u'
GL_TEXTURE_ENV_MODE = 8704L # Variable c_uint '8704u'
GL_TEXTURE_FETCH_BARRIER_BIT_EXT = 8L # Variable c_uint '8u'
GL_TEXTURE_FILTER4_SIZE_SGIS = 33095L # Variable c_uint '33095u'
GL_TEXTURE_FILTER_CONTROL = 34048L # Variable c_uint '34048u'
GL_TEXTURE_FILTER_CONTROL_EXT = 34048L # Variable c_uint '34048u'
GL_TEXTURE_FIXED_SAMPLE_LOCATIONS = 37127L # Variable c_uint '37127u'
GL_TEXTURE_FLOAT_COMPONENTS_NV = 34956L # Variable c_uint '34956u'
GL_TEXTURE_FREE_MEMORY_ATI = 34812L # Variable c_uint '34812u'
GL_TEXTURE_GEN_MODE = 9472L # Variable c_uint '9472u'
GL_TEXTURE_GEN_Q = 3171L # Variable c_uint '3171u'
GL_TEXTURE_GEN_R = 3170L # Variable c_uint '3170u'
GL_TEXTURE_GEN_S = 3168L # Variable c_uint '3168u'
GL_TEXTURE_GEN_T = 3169L # Variable c_uint '3169u'
GL_TEXTURE_GEQUAL_R_SGIX = 33181L # Variable c_uint '33181u'
GL_TEXTURE_GREEN_SIZE = 32861L # Variable c_uint '32861u'
GL_TEXTURE_GREEN_SIZE_EXT = 32861L # Variable c_uint '32861u'
GL_TEXTURE_GREEN_TYPE = 35857L # Variable c_uint '35857u'
GL_TEXTURE_GREEN_TYPE_ARB = 35857L # Variable c_uint '35857u'
GL_TEXTURE_HEIGHT = 4097L # Variable c_uint '4097u'
GL_TEXTURE_HI_SIZE_NV = 34587L # Variable c_uint '34587u'
GL_TEXTURE_INDEX_SIZE_EXT = 33005L # Variable c_uint '33005u'
GL_TEXTURE_INTENSITY_SIZE = 32865L # Variable c_uint '32865u'
GL_TEXTURE_INTENSITY_SIZE_EXT = 32865L # Variable c_uint '32865u'
GL_TEXTURE_INTENSITY_TYPE = 35861L # Variable c_uint '35861u'
GL_TEXTURE_INTENSITY_TYPE_ARB = 35861L # Variable c_uint '35861u'
GL_TEXTURE_INTERNAL_FORMAT = 4099L # Variable c_uint '4099u'
GL_TEXTURE_LEQUAL_R_SGIX = 33180L # Variable c_uint '33180u'
GL_TEXTURE_LIGHT_EXT = 33616L # Variable c_uint '33616u'
GL_TEXTURE_LIGHTING_MODE_HP = 33127L # Variable c_uint '33127u'
GL_TEXTURE_LOD_BIAS = 34049L # Variable c_uint '34049u'
GL_TEXTURE_LOD_BIAS_EXT = 34049L # Variable c_uint '34049u'
GL_TEXTURE_LOD_BIAS_R_SGIX = 33168L # Variable c_uint '33168u'
GL_TEXTURE_LOD_BIAS_S_SGIX = 33166L # Variable c_uint '33166u'
GL_TEXTURE_LOD_BIAS_T_SGIX = 33167L # Variable c_uint '33167u'
GL_TEXTURE_LO_SIZE_NV = 34588L # Variable c_uint '34588u'
GL_TEXTURE_LUMINANCE_SIZE = 32864L # Variable c_uint '32864u'
GL_TEXTURE_LUMINANCE_SIZE_EXT = 32864L # Variable c_uint '32864u'
GL_TEXTURE_LUMINANCE_TYPE = 35860L # Variable c_uint '35860u'
GL_TEXTURE_LUMINANCE_TYPE_ARB = 35860L # Variable c_uint '35860u'
GL_TEXTURE_MAG_FILTER = 10240L # Variable c_uint '10240u'
GL_TEXTURE_MAG_SIZE_NV = 34591L # Variable c_uint '34591u'
GL_TEXTURE_MATERIAL_FACE_EXT = 33617L # Variable c_uint '33617u'
GL_TEXTURE_MATERIAL_PARAMETER_EXT = 33618L # Variable c_uint '33618u'
GL_TEXTURE_MATRIX = 2984L # Variable c_uint '2984u'
GL_TEXTURE_MAX_ANISOTROPY_EXT = 34046L # Variable c_uint '34046u'
GL_TEXTURE_MAX_CLAMP_R_SGIX = 33643L # Variable c_uint '33643u'
GL_TEXTURE_MAX_CLAMP_S_SGIX = 33641L # Variable c_uint '33641u'
GL_TEXTURE_MAX_CLAMP_T_SGIX = 33642L # Variable c_uint '33642u'
GL_TEXTURE_MAX_LEVEL = 33085L # Variable c_uint '33085u'
GL_TEXTURE_MAX_LEVEL_SGIS = 33085L # Variable c_uint '33085u'
GL_TEXTURE_MAX_LOD = 33083L # Variable c_uint '33083u'
GL_TEXTURE_MAX_LOD_SGIS = 33083L # Variable c_uint '33083u'
GL_TEXTURE_MIN_FILTER = 10241L # Variable c_uint '10241u'
GL_TEXTURE_MIN_LOD = 33082L # Variable c_uint '33082u'
GL_TEXTURE_MIN_LOD_SGIS = 33082L # Variable c_uint '33082u'
GL_TEXTURE_MULTI_BUFFER_HINT_SGIX = 33070L # Variable c_uint '33070u'
GL_TEXTURE_NORMAL_EXT = 34223L # Variable c_uint '34223u'
GL_TEXTURE_POST_SPECULAR_HP = 33128L # Variable c_uint '33128u'
GL_TEXTURE_PRE_SPECULAR_HP = 33129L # Variable c_uint '33129u'
GL_TEXTURE_PRIORITY = 32870L # Variable c_uint '32870u'
GL_TEXTURE_PRIORITY_EXT = 32870L # Variable c_uint '32870u'
GL_TEXTURE_RANGE_LENGTH_APPLE = 34231L # Variable c_uint '34231u'
GL_TEXTURE_RANGE_POINTER_APPLE = 34232L # Variable c_uint '34232u'
GL_TEXTURE_RECTANGLE = 34037L # Variable c_uint '34037u'
GL_TEXTURE_RECTANGLE_ARB = 34037L # Variable c_uint '34037u'
GL_TEXTURE_RECTANGLE_NV = 34037L # Variable c_uint '34037u'
GL_TEXTURE_RED_SIZE = 32860L # Variable c_uint '32860u'
GL_TEXTURE_RED_SIZE_EXT = 32860L # Variable c_uint '32860u'
GL_TEXTURE_RED_TYPE = 35856L # Variable c_uint '35856u'
GL_TEXTURE_RED_TYPE_ARB = 35856L # Variable c_uint '35856u'
GL_TEXTURE_RENDERBUFFER_DATA_STORE_BINDING_NV = 36436L # Variable c_uint '36436u'
GL_TEXTURE_RENDERBUFFER_NV = 36437L # Variable c_uint '36437u'
GL_TEXTURE_RESIDENT = 32871L # Variable c_uint '32871u'
GL_TEXTURE_RESIDENT_EXT = 32871L # Variable c_uint '32871u'
GL_TEXTURE_SAMPLES = 37126L # Variable c_uint '37126u'
GL_TEXTURE_SHADER_NV = 34526L # Variable c_uint '34526u'
GL_TEXTURE_SHARED_SIZE = 35903L # Variable c_uint '35903u'
GL_TEXTURE_SHARED_SIZE_EXT = 35903L # Variable c_uint '35903u'
GL_TEXTURE_STACK_DEPTH = 2981L # Variable c_uint '2981u'
GL_TEXTURE_STENCIL_SIZE = 35057L # Variable c_uint '35057u'
GL_TEXTURE_STENCIL_SIZE_EXT = 35057L # Variable c_uint '35057u'
GL_TEXTURE_STORAGE_HINT_APPLE = 34236L # Variable c_uint '34236u'
GL_TEXTURE_SWIZZLE_A = 36421L # Variable c_uint '36421u'
GL_TEXTURE_SWIZZLE_A_EXT = 36421L # Variable c_uint '36421u'
GL_TEXTURE_SWIZZLE_B = 36420L # Variable c_uint '36420u'
GL_TEXTURE_SWIZZLE_B_EXT = 36420L # Variable c_uint '36420u'
GL_TEXTURE_SWIZZLE_G = 36419L # Variable c_uint '36419u'
GL_TEXTURE_SWIZZLE_G_EXT = 36419L # Variable c_uint '36419u'
GL_TEXTURE_SWIZZLE_R = 36418L # Variable c_uint '36418u'
GL_TEXTURE_SWIZZLE_R_EXT = 36418L # Variable c_uint '36418u'
GL_TEXTURE_SWIZZLE_RGBA = 36422L # Variable c_uint '36422u'
GL_TEXTURE_SWIZZLE_RGBA_EXT = 36422L # Variable c_uint '36422u'
GL_TEXTURE_TOO_LARGE_EXT = 32869L # Variable c_uint '32869u'
GL_TEXTURE_UNSIGNED_REMAP_MODE_NV = 34959L # Variable c_uint '34959u'
GL_TEXTURE_UPDATE_BARRIER_BIT_EXT = 256L # Variable c_uint '256u'
GL_TEXTURE_WIDTH = 4096L # Variable c_uint '4096u'
GL_TEXTURE_WRAP_Q_SGIS = 33079L # Variable c_uint '33079u'
GL_TEXTURE_WRAP_R = 32882L # Variable c_uint '32882u'
GL_TEXTURE_WRAP_R_EXT = 32882L # Variable c_uint '32882u'
GL_TEXTURE_WRAP_S = 10242L # Variable c_uint '10242u'
GL_TEXTURE_WRAP_T = 10243L # Variable c_uint '10243u'
GL_TIME_ELAPSED = 35007L # Variable c_uint '35007u'
GL_TIME_ELAPSED_EXT = 35007L # Variable c_uint '35007u'
GL_TIMEOUT_EXPIRED = 37147L # Variable c_uint '37147u'
GL_TIMESTAMP = 36392L # Variable c_uint '36392u'
GL_TRACK_MATRIX_NV = 34376L # Variable c_uint '34376u'
GL_TRACK_MATRIX_TRANSFORM_NV = 34377L # Variable c_uint '34377u'
GL_TRANSFORM_BIT = 4096L # Variable c_uint '4096u'
GL_TRANSFORM_FEEDBACK = 36386L # Variable c_uint '36386u'
GL_TRANSFORM_FEEDBACK_ATTRIBS_NV = 35966L # Variable c_uint '35966u'
GL_TRANSFORM_FEEDBACK_BARRIER_BIT_EXT = 2048L # Variable c_uint '2048u'
GL_TRANSFORM_FEEDBACK_BINDING = 36389L # Variable c_uint '36389u'
GL_TRANSFORM_FEEDBACK_BINDING_NV = 36389L # Variable c_uint '36389u'
GL_TRANSFORM_FEEDBACK_BUFFER = 35982L # Variable c_uint '35982u'
GL_TRANSFORM_FEEDBACK_BUFFER_ACTIVE = 36388L # Variable c_uint '36388u'
GL_TRANSFORM_FEEDBACK_BUFFER_ACTIVE_NV = 36388L # Variable c_uint '36388u'
GL_TRANSFORM_FEEDBACK_BUFFER_BINDING = 35983L # Variable c_uint '35983u'
GL_TRANSFORM_FEEDBACK_BUFFER_BINDING_EXT = 35983L # Variable c_uint '35983u'
GL_TRANSFORM_FEEDBACK_BUFFER_BINDING_NV = 35983L # Variable c_uint '35983u'
GL_TRANSFORM_FEEDBACK_BUFFER_EXT = 35982L # Variable c_uint '35982u'
GL_TRANSFORM_FEEDBACK_BUFFER_MODE = 35967L # Variable c_uint '35967u'
GL_TRANSFORM_FEEDBACK_BUFFER_MODE_EXT = 35967L # Variable c_uint '35967u'
GL_TRANSFORM_FEEDBACK_BUFFER_MODE_NV = 35967L # Variable c_uint '35967u'
GL_TRANSFORM_FEEDBACK_BUFFER_NV = 35982L # Variable c_uint '35982u'
GL_TRANSFORM_FEEDBACK_BUFFER_PAUSED = 36387L # Variable c_uint '36387u'
GL_TRANSFORM_FEEDBACK_BUFFER_PAUSED_NV = 36387L # Variable c_uint '36387u'
GL_TRANSFORM_FEEDBACK_BUFFER_SIZE = 35973L # Variable c_uint '35973u'
GL_TRANSFORM_FEEDBACK_BUFFER_SIZE_EXT = 35973L # Variable c_uint '35973u'
GL_TRANSFORM_FEEDBACK_BUFFER_SIZE_NV = 35973L # Variable c_uint '35973u'
GL_TRANSFORM_FEEDBACK_BUFFER_START = 35972L # Variable c_uint '35972u'
GL_TRANSFORM_FEEDBACK_BUFFER_START_EXT = 35972L # Variable c_uint '35972u'
GL_TRANSFORM_FEEDBACK_BUFFER_START_NV = 35972L # Variable c_uint '35972u'
GL_TRANSFORM_FEEDBACK_NV = 36386L # Variable c_uint '36386u'
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN = 35976L # Variable c_uint '35976u'
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN_EXT = 35976L # Variable c_uint '35976u'
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN_NV = 35976L # Variable c_uint '35976u'
GL_TRANSFORM_FEEDBACK_RECORD_NV = 35974L # Variable c_uint '35974u'
GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH = 35958L # Variable c_uint '35958u'
GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH_EXT = 35958L # Variable c_uint '35958u'
GL_TRANSFORM_FEEDBACK_VARYINGS = 35971L # Variable c_uint '35971u'
GL_TRANSFORM_FEEDBACK_VARYINGS_EXT = 35971L # Variable c_uint '35971u'
GL_TRANSFORM_FEEDBACK_VARYINGS_NV = 35971L # Variable c_uint '35971u'
GL_TRANSFORM_HINT_APPLE = 34225L # Variable c_uint '34225u'
GL_TRANSPOSE_COLOR_MATRIX = 34022L # Variable c_uint '34022u'
GL_TRANSPOSE_COLOR_MATRIX_ARB = 34022L # Variable c_uint '34022u'
GL_TRANSPOSE_CURRENT_MATRIX_ARB = 34999L # Variable c_uint '34999u'
GL_TRANSPOSE_MODELVIEW_MATRIX = 34019L # Variable c_uint '34019u'
GL_TRANSPOSE_MODELVIEW_MATRIX_ARB = 34019L # Variable c_uint '34019u'
GL_TRANSPOSE_NV = 34348L # Variable c_uint '34348u'
GL_TRANSPOSE_PROGRAM_MATRIX_EXT = 36398L # Variable c_uint '36398u'
GL_TRANSPOSE_PROJECTION_MATRIX = 34020L # Variable c_uint '34020u'
GL_TRANSPOSE_PROJECTION_MATRIX_ARB = 34020L # Variable c_uint '34020u'
GL_TRANSPOSE_TEXTURE_MATRIX = 34021L # Variable c_uint '34021u'
GL_TRANSPOSE_TEXTURE_MATRIX_ARB = 34021L # Variable c_uint '34021u'
GL_TRIANGLE_FAN = 6L # Variable c_uint '6u'
GL_TRIANGLE_LIST_SUN = 33239L # Variable c_uint '33239u'
GL_TRIANGLE_MESH_SUN = 34325L # Variable c_uint '34325u'
GL_TRIANGLES = 4L # Variable c_uint '4u'
GL_TRIANGLES_ADJACENCY = 12L # Variable c_uint '12u'
GL_TRIANGLES_ADJACENCY_ARB = 12L # Variable c_uint '12u'
GL_TRIANGLES_ADJACENCY_EXT = 12L # Variable c_uint '12u'
GL_TRIANGLE_STRIP = 5L # Variable c_uint '5u'
GL_TRIANGLE_STRIP_ADJACENCY = 13L # Variable c_uint '13u'
GL_TRIANGLE_STRIP_ADJACENCY_ARB = 13L # Variable c_uint '13u'
GL_TRIANGLE_STRIP_ADJACENCY_EXT = 13L # Variable c_uint '13u'
GL_TRUE = 1L # Variable c_uint '1u'
GL_TYPE_RGBA_FLOAT_ATI = 34848L # Variable c_uint '34848u'
GLU_AUTO_LOAD_MATRIX = 100200L # Variable c_uint '100200u'
GLU_BEGIN = 100100L # Variable c_uint '100100u'
GLU_CCW = 100121L # Variable c_uint '100121u'
GLU_CULLING = 100201L # Variable c_uint '100201u'
GLU_CW = 100120L # Variable c_uint '100120u'
GLU_DISPLAY_MODE = 100204L # Variable c_uint '100204u'
GLU_DOMAIN_DISTANCE = 100217L # Variable c_uint '100217u'
GLU_EDGE_FLAG = 100104L # Variable c_uint '100104u'
GLU_END = 100102L # Variable c_uint '100102u'
GLU_ERROR = 100103L # Variable c_uint '100103u'
GLU_EXTENSIONS = 100801L # Variable c_uint '100801u'
GLU_EXTERIOR = 100123L # Variable c_uint '100123u'
GLU_FALSE = 0L # Variable c_uint '0u'
GLU_FILL = 100012L # Variable c_uint '100012u'
GLU_FLAT = 100001L # Variable c_uint '100001u'
GLU_INCOMPATIBLE_GL_VERSION = 100903L # Variable c_uint '100903u'
GLU_INSIDE = 100021L # Variable c_uint '100021u'
GLU_INTERIOR = 100122L # Variable c_uint '100122u'
GLU_INVALID_ENUM = 100900L # Variable c_uint '100900u'
GLU_INVALID_OPERATION = 100904L # Variable c_uint '100904u'
GLU_INVALID_VALUE = 100901L # Variable c_uint '100901u'
GLU_LINE = 100011L # Variable c_uint '100011u'
GLU_MAP1_TRIM_2 = 100210L # Variable c_uint '100210u'
GLU_MAP1_TRIM_3 = 100211L # Variable c_uint '100211u'
GL_UNDEFINED_APPLE = 35356L # Variable c_uint '35356u'
GL_UNDEFINED_VERTEX = 33376L # Variable c_uint '33376u'
GL_UNIFORM_ARRAY_STRIDE = 35388L # Variable c_uint '35388u'
GL_UNIFORM_BARRIER_BIT_EXT = 4L # Variable c_uint '4u'
GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES = 35395L # Variable c_uint '35395u'
GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS = 35394L # Variable c_uint '35394u'
GL_UNIFORM_BLOCK_BINDING = 35391L # Variable c_uint '35391u'
GL_UNIFORM_BLOCK_DATA_SIZE = 35392L # Variable c_uint '35392u'
GL_UNIFORM_BLOCK_INDEX = 35386L # Variable c_uint '35386u'
GL_UNIFORM_BLOCK_NAME_LENGTH = 35393L # Variable c_uint '35393u'
GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER = 35398L # Variable c_uint '35398u'
GL_UNIFORM_BLOCK_REFERENCED_BY_GEOMETRY_SHADER = 35397L # Variable c_uint '35397u'
GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_CONTROL_SHADER = 34032L # Variable c_uint '34032u'
GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_EVALUATION_SHADER = 34033L # Variable c_uint '34033u'
GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER = 35396L # Variable c_uint '35396u'
GL_UNIFORM_BUFFER = 35345L # Variable c_uint '35345u'
GL_UNIFORM_BUFFER_BINDING = 35368L # Variable c_uint '35368u'
GL_UNIFORM_BUFFER_BINDING_EXT = 36335L # Variable c_uint '36335u'
GL_UNIFORM_BUFFER_EXT = 36334L # Variable c_uint '36334u'
GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT = 35380L # Variable c_uint '35380u'
GL_UNIFORM_BUFFER_SIZE = 35370L # Variable c_uint '35370u'
GL_UNIFORM_BUFFER_START = 35369L # Variable c_uint '35369u'
GL_UNIFORM_IS_ROW_MAJOR = 35390L # Variable c_uint '35390u'
GL_UNIFORM_MATRIX_STRIDE = 35389L # Variable c_uint '35389u'
GL_UNIFORM_NAME_LENGTH = 35385L # Variable c_uint '35385u'
GL_UNIFORM_OFFSET = 35387L # Variable c_uint '35387u'
GL_UNIFORM_SIZE = 35384L # Variable c_uint '35384u'
GL_UNIFORM_TYPE = 35383L # Variable c_uint '35383u'
GL_UNKNOWN_CONTEXT_RESET_ARB = 33365L # Variable c_uint '33365u'
GLU_NONE = 100002L # Variable c_uint '100002u'
GL_UNPACK_ALIGNMENT = 3317L # Variable c_uint '3317u'
GL_UNPACK_CLIENT_STORAGE_APPLE = 34226L # Variable c_uint '34226u'
GL_UNPACK_CMYK_HINT_EXT = 32783L # Variable c_uint '32783u'
GL_UNPACK_CONSTANT_DATA_SUNX = 33237L # Variable c_uint '33237u'
GL_UNPACK_IMAGE_DEPTH_SGIS = 33075L # Variable c_uint '33075u'
GL_UNPACK_IMAGE_HEIGHT = 32878L # Variable c_uint '32878u'
GL_UNPACK_IMAGE_HEIGHT_EXT = 32878L # Variable c_uint '32878u'
GL_UNPACK_LSB_FIRST = 3313L # Variable c_uint '3313u'
GL_UNPACK_RESAMPLE_OML = 35205L # Variable c_uint '35205u'
GL_UNPACK_RESAMPLE_SGIX = 33837L # Variable c_uint '33837u'
GL_UNPACK_ROW_BYTES_APPLE = 35350L # Variable c_uint '35350u'
GL_UNPACK_ROW_LENGTH = 3314L # Variable c_uint '3314u'
GL_UNPACK_SKIP_IMAGES = 32877L # Variable c_uint '32877u'
GL_UNPACK_SKIP_IMAGES_EXT = 32877L # Variable c_uint '32877u'
GL_UNPACK_SKIP_PIXELS = 3316L # Variable c_uint '3316u'
GL_UNPACK_SKIP_ROWS = 3315L # Variable c_uint '3315u'
GL_UNPACK_SKIP_VOLUMES_SGIS = 33074L # Variable c_uint '33074u'
GL_UNPACK_SUBSAMPLE_RATE_SGIX = 34209L # Variable c_uint '34209u'
GL_UNPACK_SWAP_BYTES = 3312L # Variable c_uint '3312u'
GL_UNSIGNALED = 37144L # Variable c_uint '37144u'
GL_UNSIGNED_BYTE = 5121L # Variable c_uint '5121u'
GL_UNSIGNED_BYTE_2_3_3_REV = 33634L # Variable c_uint '33634u'
GL_UNSIGNED_BYTE_3_3_2 = 32818L # Variable c_uint '32818u'
GL_UNSIGNED_BYTE_3_3_2_EXT = 32818L # Variable c_uint '32818u'
GL_UNSIGNED_IDENTITY_NV = 34102L # Variable c_uint '34102u'
GL_UNSIGNED_INT = 5125L # Variable c_uint '5125u'
GL_UNSIGNED_INT_10_10_10_2 = 32822L # Variable c_uint '32822u'
GL_UNSIGNED_INT_10_10_10_2_EXT = 32822L # Variable c_uint '32822u'
GL_UNSIGNED_INT_10F_11F_11F_REV = 35899L # Variable c_uint '35899u'
GL_UNSIGNED_INT_10F_11F_11F_REV_EXT = 35899L # Variable c_uint '35899u'
GL_UNSIGNED_INT16_NV = 36848L # Variable c_uint '36848u'
GL_UNSIGNED_INT16_VEC2_NV = 36849L # Variable c_uint '36849u'
GL_UNSIGNED_INT16_VEC3_NV = 36850L # Variable c_uint '36850u'
GL_UNSIGNED_INT16_VEC4_NV = 36851L # Variable c_uint '36851u'
GL_UNSIGNED_INT_2_10_10_10_REV = 33640L # Variable c_uint '33640u'
GL_UNSIGNED_INT_24_8 = 34042L # Variable c_uint '34042u'
GL_UNSIGNED_INT_24_8_EXT = 34042L # Variable c_uint '34042u'
GL_UNSIGNED_INT_24_8_MESA = 34641L # Variable c_uint '34641u'
GL_UNSIGNED_INT_24_8_NV = 34042L # Variable c_uint '34042u'
GL_UNSIGNED_INT_5_9_9_9_REV = 35902L # Variable c_uint '35902u'
GL_UNSIGNED_INT_5_9_9_9_REV_EXT = 35902L # Variable c_uint '35902u'
GL_UNSIGNED_INT64_AMD = 35778L # Variable c_uint '35778u'
GL_UNSIGNED_INT64_NV = 5135L # Variable c_uint '5135u'
GL_UNSIGNED_INT64_VEC2_NV = 36853L # Variable c_uint '36853u'
GL_UNSIGNED_INT64_VEC3_NV = 36854L # Variable c_uint '36854u'
GL_UNSIGNED_INT64_VEC4_NV = 36855L # Variable c_uint '36855u'
GL_UNSIGNED_INT_8_24_REV_MESA = 34642L # Variable c_uint '34642u'
GL_UNSIGNED_INT_8_8_8_8 = 32821L # Variable c_uint '32821u'
GL_UNSIGNED_INT_8_8_8_8_EXT = 32821L # Variable c_uint '32821u'
GL_UNSIGNED_INT_8_8_8_8_REV = 33639L # Variable c_uint '33639u'
GL_UNSIGNED_INT_8_8_S8_S8_REV_NV = 34523L # Variable c_uint '34523u'
GL_UNSIGNED_INT8_NV = 36844L # Variable c_uint '36844u'
GL_UNSIGNED_INT8_VEC2_NV = 36845L # Variable c_uint '36845u'
GL_UNSIGNED_INT8_VEC3_NV = 36846L # Variable c_uint '36846u'
GL_UNSIGNED_INT8_VEC4_NV = 36847L # Variable c_uint '36847u'
GL_UNSIGNED_INT_IMAGE_1D_ARRAY_EXT = 36968L # Variable c_uint '36968u'
GL_UNSIGNED_INT_IMAGE_1D_EXT = 36962L # Variable c_uint '36962u'
GL_UNSIGNED_INT_IMAGE_2D_ARRAY_EXT = 36969L # Variable c_uint '36969u'
GL_UNSIGNED_INT_IMAGE_2D_EXT = 36963L # Variable c_uint '36963u'
GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_ARRAY_EXT = 36972L # Variable c_uint '36972u'
GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_EXT = 36971L # Variable c_uint '36971u'
GL_UNSIGNED_INT_IMAGE_2D_RECT_EXT = 36965L # Variable c_uint '36965u'
GL_UNSIGNED_INT_IMAGE_3D_EXT = 36964L # Variable c_uint '36964u'
GL_UNSIGNED_INT_IMAGE_BUFFER_EXT = 36967L # Variable c_uint '36967u'
GL_UNSIGNED_INT_IMAGE_CUBE_EXT = 36966L # Variable c_uint '36966u'
GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY_EXT = 36970L # Variable c_uint '36970u'
GL_UNSIGNED_INT_S8_S8_8_8_NV = 34522L # Variable c_uint '34522u'
GL_UNSIGNED_INT_SAMPLER_1D = 36305L # Variable c_uint '36305u'
GL_UNSIGNED_INT_SAMPLER_1D_ARRAY = 36310L # Variable c_uint '36310u'
GL_UNSIGNED_INT_SAMPLER_1D_ARRAY_EXT = 36310L # Variable c_uint '36310u'
GL_UNSIGNED_INT_SAMPLER_1D_EXT = 36305L # Variable c_uint '36305u'
GL_UNSIGNED_INT_SAMPLER_2D = 36306L # Variable c_uint '36306u'
GL_UNSIGNED_INT_SAMPLER_2D_ARRAY = 36311L # Variable c_uint '36311u'
GL_UNSIGNED_INT_SAMPLER_2D_ARRAY_EXT = 36311L # Variable c_uint '36311u'
GL_UNSIGNED_INT_SAMPLER_2D_EXT = 36306L # Variable c_uint '36306u'
GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE = 37130L # Variable c_uint '37130u'
GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 37133L # Variable c_uint '37133u'
GL_UNSIGNED_INT_SAMPLER_2D_RECT = 36309L # Variable c_uint '36309u'
GL_UNSIGNED_INT_SAMPLER_2D_RECT_EXT = 36309L # Variable c_uint '36309u'
GL_UNSIGNED_INT_SAMPLER_3D = 36307L # Variable c_uint '36307u'
GL_UNSIGNED_INT_SAMPLER_3D_EXT = 36307L # Variable c_uint '36307u'
GL_UNSIGNED_INT_SAMPLER_BUFFER = 36312L # Variable c_uint '36312u'
GL_UNSIGNED_INT_SAMPLER_BUFFER_AMD = 36867L # Variable c_uint '36867u'
GL_UNSIGNED_INT_SAMPLER_BUFFER_EXT = 36312L # Variable c_uint '36312u'
GL_UNSIGNED_INT_SAMPLER_CUBE = 36308L # Variable c_uint '36308u'
GL_UNSIGNED_INT_SAMPLER_CUBE_EXT = 36308L # Variable c_uint '36308u'
GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY = 36879L # Variable c_uint '36879u'
GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY_ARB = 36879L # Variable c_uint '36879u'
GL_UNSIGNED_INT_SAMPLER_RENDERBUFFER_NV = 36440L # Variable c_uint '36440u'
GL_UNSIGNED_INT_VEC2 = 36294L # Variable c_uint '36294u'
GL_UNSIGNED_INT_VEC2_EXT = 36294L # Variable c_uint '36294u'
GL_UNSIGNED_INT_VEC3 = 36295L # Variable c_uint '36295u'
GL_UNSIGNED_INT_VEC3_EXT = 36295L # Variable c_uint '36295u'
GL_UNSIGNED_INT_VEC4 = 36296L # Variable c_uint '36296u'
GL_UNSIGNED_INT_VEC4_EXT = 36296L # Variable c_uint '36296u'
GL_UNSIGNED_INVERT_NV = 34103L # Variable c_uint '34103u'
GL_UNSIGNED_NORMALIZED = 35863L # Variable c_uint '35863u'
GL_UNSIGNED_NORMALIZED_ARB = 35863L # Variable c_uint '35863u'
GL_UNSIGNED_SHORT = 5123L # Variable c_uint '5123u'
GL_UNSIGNED_SHORT_1_15_REV_MESA = 34644L # Variable c_uint '34644u'
GL_UNSIGNED_SHORT_15_1_MESA = 34643L # Variable c_uint '34643u'
GL_UNSIGNED_SHORT_1_5_5_5_REV = 33638L # Variable c_uint '33638u'
GL_UNSIGNED_SHORT_4_4_4_4 = 32819L # Variable c_uint '32819u'
GL_UNSIGNED_SHORT_4_4_4_4_EXT = 32819L # Variable c_uint '32819u'
GL_UNSIGNED_SHORT_4_4_4_4_REV = 33637L # Variable c_uint '33637u'
GL_UNSIGNED_SHORT_5_5_5_1 = 32820L # Variable c_uint '32820u'
GL_UNSIGNED_SHORT_5_5_5_1_EXT = 32820L # Variable c_uint '32820u'
GL_UNSIGNED_SHORT_5_6_5 = 33635L # Variable c_uint '33635u'
GL_UNSIGNED_SHORT_5_6_5_REV = 33636L # Variable c_uint '33636u'
GL_UNSIGNED_SHORT_8_8_APPLE = 34234L # Variable c_uint '34234u'
GL_UNSIGNED_SHORT_8_8_MESA = 34234L # Variable c_uint '34234u'
GL_UNSIGNED_SHORT_8_8_REV_APPLE = 34235L # Variable c_uint '34235u'
GL_UNSIGNED_SHORT_8_8_REV_MESA = 34235L # Variable c_uint '34235u'
GLU_NURBS_BEGIN = 100164L # Variable c_uint '100164u'
GLU_NURBS_BEGIN_DATA = 100170L # Variable c_uint '100170u'
GLU_NURBS_BEGIN_DATA_EXT = 100170L # Variable c_uint '100170u'
GLU_NURBS_BEGIN_EXT = 100164L # Variable c_uint '100164u'
GLU_NURBS_COLOR = 100167L # Variable c_uint '100167u'
GLU_NURBS_COLOR_DATA = 100173L # Variable c_uint '100173u'
GLU_NURBS_COLOR_DATA_EXT = 100173L # Variable c_uint '100173u'
GLU_NURBS_COLOR_EXT = 100167L # Variable c_uint '100167u'
GLU_NURBS_END = 100169L # Variable c_uint '100169u'
GLU_NURBS_END_DATA = 100175L # Variable c_uint '100175u'
GLU_NURBS_END_DATA_EXT = 100175L # Variable c_uint '100175u'
GLU_NURBS_END_EXT = 100169L # Variable c_uint '100169u'
GLU_NURBS_ERROR = 100103L # Variable c_uint '100103u'
GLU_NURBS_ERROR10 = 100260L # Variable c_uint '100260u'
GLU_NURBS_ERROR1 = 100251L # Variable c_uint '100251u'
GLU_NURBS_ERROR11 = 100261L # Variable c_uint '100261u'
GLU_NURBS_ERROR12 = 100262L # Variable c_uint '100262u'
GLU_NURBS_ERROR13 = 100263L # Variable c_uint '100263u'
GLU_NURBS_ERROR14 = 100264L # Variable c_uint '100264u'
GLU_NURBS_ERROR15 = 100265L # Variable c_uint '100265u'
GLU_NURBS_ERROR16 = 100266L # Variable c_uint '100266u'
GLU_NURBS_ERROR17 = 100267L # Variable c_uint '100267u'
GLU_NURBS_ERROR18 = 100268L # Variable c_uint '100268u'
GLU_NURBS_ERROR19 = 100269L # Variable c_uint '100269u'
GLU_NURBS_ERROR20 = 100270L # Variable c_uint '100270u'
GLU_NURBS_ERROR2 = 100252L # Variable c_uint '100252u'
GLU_NURBS_ERROR21 = 100271L # Variable c_uint '100271u'
GLU_NURBS_ERROR22 = 100272L # Variable c_uint '100272u'
GLU_NURBS_ERROR23 = 100273L # Variable c_uint '100273u'
GLU_NURBS_ERROR24 = 100274L # Variable c_uint '100274u'
GLU_NURBS_ERROR25 = 100275L # Variable c_uint '100275u'
GLU_NURBS_ERROR26 = 100276L # Variable c_uint '100276u'
GLU_NURBS_ERROR27 = 100277L # Variable c_uint '100277u'
GLU_NURBS_ERROR28 = 100278L # Variable c_uint '100278u'
GLU_NURBS_ERROR29 = 100279L # Variable c_uint '100279u'
GLU_NURBS_ERROR30 = 100280L # Variable c_uint '100280u'
GLU_NURBS_ERROR3 = 100253L # Variable c_uint '100253u'
GLU_NURBS_ERROR31 = 100281L # Variable c_uint '100281u'
GLU_NURBS_ERROR32 = 100282L # Variable c_uint '100282u'
GLU_NURBS_ERROR33 = 100283L # Variable c_uint '100283u'
GLU_NURBS_ERROR34 = 100284L # Variable c_uint '100284u'
GLU_NURBS_ERROR35 = 100285L # Variable c_uint '100285u'
GLU_NURBS_ERROR36 = 100286L # Variable c_uint '100286u'
GLU_NURBS_ERROR37 = 100287L # Variable c_uint '100287u'
GLU_NURBS_ERROR4 = 100254L # Variable c_uint '100254u'
GLU_NURBS_ERROR5 = 100255L # Variable c_uint '100255u'
GLU_NURBS_ERROR6 = 100256L # Variable c_uint '100256u'
GLU_NURBS_ERROR7 = 100257L # Variable c_uint '100257u'
GLU_NURBS_ERROR8 = 100258L # Variable c_uint '100258u'
GLU_NURBS_ERROR9 = 100259L # Variable c_uint '100259u'
GLU_NURBS_MODE = 100160L # Variable c_uint '100160u'
GLU_NURBS_MODE_EXT = 100160L # Variable c_uint '100160u'
GLU_NURBS_NORMAL = 100166L # Variable c_uint '100166u'
GLU_NURBS_NORMAL_DATA = 100172L # Variable c_uint '100172u'
GLU_NURBS_NORMAL_DATA_EXT = 100172L # Variable c_uint '100172u'
GLU_NURBS_NORMAL_EXT = 100166L # Variable c_uint '100166u'
GLU_NURBS_RENDERER = 100162L # Variable c_uint '100162u'
GLU_NURBS_RENDERER_EXT = 100162L # Variable c_uint '100162u'
GLU_NURBS_TESSELLATOR = 100161L # Variable c_uint '100161u'
GLU_NURBS_TESSELLATOR_EXT = 100161L # Variable c_uint '100161u'
GLU_NURBS_TEX_COORD_DATA_EXT = 100174L # Variable c_uint '100174u'
GLU_NURBS_TEX_COORD_EXT = 100168L # Variable c_uint '100168u'
GLU_NURBS_TEXTURE_COORD = 100168L # Variable c_uint '100168u'
GLU_NURBS_TEXTURE_COORD_DATA = 100174L # Variable c_uint '100174u'
GLU_NURBS_VERTEX = 100165L # Variable c_uint '100165u'
GLU_NURBS_VERTEX_DATA = 100171L # Variable c_uint '100171u'
GLU_NURBS_VERTEX_DATA_EXT = 100171L # Variable c_uint '100171u'
GLU_NURBS_VERTEX_EXT = 100165L # Variable c_uint '100165u'
GLU_OBJECT_PARAMETRIC_ERROR = 100208L # Variable c_uint '100208u'
GLU_OBJECT_PARAMETRIC_ERROR_EXT = 100208L # Variable c_uint '100208u'
GLU_OBJECT_PATH_LENGTH = 100209L # Variable c_uint '100209u'
GLU_OBJECT_PATH_LENGTH_EXT = 100209L # Variable c_uint '100209u'
GLU_OUTLINE_PATCH = 100241L # Variable c_uint '100241u'
GLU_OUTLINE_POLYGON = 100240L # Variable c_uint '100240u'
GLU_OUT_OF_MEMORY = 100902L # Variable c_uint '100902u'
GLU_OUTSIDE = 100020L # Variable c_uint '100020u'
GLU_PARAMETRIC_ERROR = 100216L # Variable c_uint '100216u'
GLU_PARAMETRIC_TOLERANCE = 100202L # Variable c_uint '100202u'
GLU_PATH_LENGTH = 100215L # Variable c_uint '100215u'
GLU_POINT = 100010L # Variable c_uint '100010u'
GL_UPPER_LEFT = 36002L # Variable c_uint '36002u'
GLU_SAMPLING_METHOD = 100205L # Variable c_uint '100205u'
GLU_SAMPLING_TOLERANCE = 100203L # Variable c_uint '100203u'
GLU_SILHOUETTE = 100013L # Variable c_uint '100013u'
GLU_SMOOTH = 100000L # Variable c_uint '100000u'
GLUT_ACCUM = 4L # Variable c_uint '4u'
GLUT_ACTION_CONTINUE_EXECUTION = 2L # Variable c_uint '2u'
GLUT_ACTION_EXIT = 0L # Variable c_uint '0u'
GLUT_ACTION_GLUTMAINLOOP_RETURNS = 1L # Variable c_uint '1u'
GLUT_ACTION_ON_WINDOW_CLOSE = 505L # Variable c_uint '505u'
GLUT_ACTIVE_ALT = 4L # Variable c_uint '4u'
GLUT_ACTIVE_CTRL = 2L # Variable c_uint '2u'
GLUT_ACTIVE_SHIFT = 1L # Variable c_uint '1u'
GLUT_ALLOW_DIRECT_CONTEXT = 1L # Variable c_uint '1u'
GLUT_ALPHA = 8L # Variable c_uint '8u'
GLUT_API_VERSION = 4L # Variable c_uint '4u'
GLUT_AUX = 4096L # Variable c_uint '4096u'
GLUT_AUX1 = 4096L # Variable c_uint '4096u'
GLUT_AUX2 = 8192L # Variable c_uint '8192u'
GLUT_AUX3 = 16384L # Variable c_uint '16384u'
GLUT_AUX4 = 32768L # Variable c_uint '32768u'
GLUT_BLUE = 2L # Variable c_uint '2u'
GLUT_BORDERLESS = 2048L # Variable c_uint '2048u'
GLUT_CAPTIONLESS = 1024L # Variable c_uint '1024u'
GLUT_COMPATIBILITY_PROFILE = 2L # Variable c_uint '2u'
GLUT_CORE_PROFILE = 1L # Variable c_uint '1u'
GLUT_CREATE_NEW_CONTEXT = 0L # Variable c_uint '0u'
GLUT_CURSOR_BOTTOM_LEFT_CORNER = 19L # Variable c_uint '19u'
GLUT_CURSOR_BOTTOM_RIGHT_CORNER = 18L # Variable c_uint '18u'
GLUT_CURSOR_BOTTOM_SIDE = 13L # Variable c_uint '13u'
GLUT_CURSOR_CROSSHAIR = 9L # Variable c_uint '9u'
GLUT_CURSOR_CYCLE = 5L # Variable c_uint '5u'
GLUT_CURSOR_DESTROY = 3L # Variable c_uint '3u'
GLUT_CURSOR_FULL_CROSSHAIR = 102L # Variable c_uint '102u'
GLUT_CURSOR_HELP = 4L # Variable c_uint '4u'
GLUT_CURSOR_INFO = 2L # Variable c_uint '2u'
GLUT_CURSOR_INHERIT = 100L # Variable c_uint '100u'
GLUT_CURSOR_LEFT_ARROW = 1L # Variable c_uint '1u'
GLUT_CURSOR_LEFT_RIGHT = 11L # Variable c_uint '11u'
GLUT_CURSOR_LEFT_SIDE = 14L # Variable c_uint '14u'
GLUT_CURSOR_NONE = 101L # Variable c_uint '101u'
GLUT_CURSOR_RIGHT_ARROW = 0L # Variable c_uint '0u'
GLUT_CURSOR_RIGHT_SIDE = 15L # Variable c_uint '15u'
GLUT_CURSOR_SPRAY = 6L # Variable c_uint '6u'
GLUT_CURSOR_TEXT = 8L # Variable c_uint '8u'
GLUT_CURSOR_TOP_LEFT_CORNER = 16L # Variable c_uint '16u'
GLUT_CURSOR_TOP_RIGHT_CORNER = 17L # Variable c_uint '17u'
GLUT_CURSOR_TOP_SIDE = 12L # Variable c_uint '12u'
GLUT_CURSOR_UP_DOWN = 10L # Variable c_uint '10u'
GLUT_CURSOR_WAIT = 7L # Variable c_uint '7u'
GLUT_DEBUG = 1L # Variable c_uint '1u'
GLUT_DEPTH = 16L # Variable c_uint '16u'
GLUT_DEVICE_IGNORE_KEY_REPEAT = 610L # Variable c_uint '610u'
GLUT_DEVICE_KEY_REPEAT = 611L # Variable c_uint '611u'
GLUT_DIRECT_RENDERING = 510L # Variable c_uint '510u'
GLUT_DISPLAY_MODE_POSSIBLE = 400L # Variable c_uint '400u'
GLUT_DOUBLE = 2L # Variable c_uint '2u'
GLUT_DOWN = 0L # Variable c_uint '0u'
GLUT_ELAPSED_TIME = 700L # Variable c_uint '700u'
GLUT_ENTERED = 1L # Variable c_uint '1u'
GLU_TESS_BEGIN = 100100L # Variable c_uint '100100u'
GLU_TESS_BEGIN_DATA = 100106L # Variable c_uint '100106u'
GLU_TESS_BOUNDARY_ONLY = 100141L # Variable c_uint '100141u'
GLU_TESS_COMBINE = 100105L # Variable c_uint '100105u'
GLU_TESS_COMBINE_DATA = 100111L # Variable c_uint '100111u'
GLU_TESS_COORD_TOO_LARGE = 100155L # Variable c_uint '100155u'
GLU_TESS_EDGE_FLAG = 100104L # Variable c_uint '100104u'
GLU_TESS_EDGE_FLAG_DATA = 100110L # Variable c_uint '100110u'
GLU_TESS_END = 100102L # Variable c_uint '100102u'
GLU_TESS_END_DATA = 100108L # Variable c_uint '100108u'
GLU_TESS_ERROR = 100103L # Variable c_uint '100103u'
GLU_TESS_ERROR1 = 100151L # Variable c_uint '100151u'
GLU_TESS_ERROR2 = 100152L # Variable c_uint '100152u'
GLU_TESS_ERROR3 = 100153L # Variable c_uint '100153u'
GLU_TESS_ERROR4 = 100154L # Variable c_uint '100154u'
GLU_TESS_ERROR5 = 100155L # Variable c_uint '100155u'
GLU_TESS_ERROR6 = 100156L # Variable c_uint '100156u'
GLU_TESS_ERROR7 = 100157L # Variable c_uint '100157u'
GLU_TESS_ERROR8 = 100158L # Variable c_uint '100158u'
GLU_TESS_ERROR_DATA = 100109L # Variable c_uint '100109u'
GLU_TESS_MISSING_BEGIN_CONTOUR = 100152L # Variable c_uint '100152u'
GLU_TESS_MISSING_BEGIN_POLYGON = 100151L # Variable c_uint '100151u'
GLU_TESS_MISSING_END_CONTOUR = 100154L # Variable c_uint '100154u'
GLU_TESS_MISSING_END_POLYGON = 100153L # Variable c_uint '100153u'
GLU_TESS_NEED_COMBINE_CALLBACK = 100156L # Variable c_uint '100156u'
GLU_TESS_TOLERANCE = 100142L # Variable c_uint '100142u'
GLU_TESS_VERTEX = 100101L # Variable c_uint '100101u'
GLU_TESS_VERTEX_DATA = 100107L # Variable c_uint '100107u'
GLU_TESS_WINDING_ABS_GEQ_TWO = 100134L # Variable c_uint '100134u'
GLU_TESS_WINDING_NEGATIVE = 100133L # Variable c_uint '100133u'
GLU_TESS_WINDING_NONZERO = 100131L # Variable c_uint '100131u'
GLU_TESS_WINDING_ODD = 100130L # Variable c_uint '100130u'
GLU_TESS_WINDING_POSITIVE = 100132L # Variable c_uint '100132u'
GLU_TESS_WINDING_RULE = 100140L # Variable c_uint '100140u'
GLUT_FORCE_DIRECT_CONTEXT = 3L # Variable c_uint '3u'
GLUT_FORCE_INDIRECT_CONTEXT = 0L # Variable c_uint '0u'
GLUT_FORWARD_COMPATIBLE = 2L # Variable c_uint '2u'
GLUT_FULL_SCREEN = 511L # Variable c_uint '511u'
GLUT_FULLY_COVERED = 3L # Variable c_uint '3u'
GLUT_FULLY_RETAINED = 1L # Variable c_uint '1u'
GLUT_GAME_MODE_ACTIVE = 0L # Variable c_uint '0u'
GLUT_GAME_MODE_DISPLAY_CHANGED = 6L # Variable c_uint '6u'
GLUT_GAME_MODE_HEIGHT = 3L # Variable c_uint '3u'
GLUT_GAME_MODE_PIXEL_DEPTH = 4L # Variable c_uint '4u'
GLUT_GAME_MODE_POSSIBLE = 1L # Variable c_uint '1u'
GLUT_GAME_MODE_REFRESH_RATE = 5L # Variable c_uint '5u'
GLUT_GAME_MODE_WIDTH = 2L # Variable c_uint '2u'
GLUT_GREEN = 1L # Variable c_uint '1u'
GLUT_HAS_DIAL_AND_BUTTON_BOX = 603L # Variable c_uint '603u'
GLUT_HAS_JOYSTICK = 612L # Variable c_uint '612u'
GLUT_HAS_KEYBOARD = 600L # Variable c_uint '600u'
GLUT_HAS_MOUSE = 601L # Variable c_uint '601u'
GLUT_HAS_OVERLAY = 802L # Variable c_uint '802u'
GLUT_HAS_SPACEBALL = 602L # Variable c_uint '602u'
GLUT_HAS_TABLET = 604L # Variable c_uint '604u'
GLUT_HIDDEN = 0L # Variable c_uint '0u'
GLUT_INDEX = 1L # Variable c_uint '1u'
GLUT_INIT_DISPLAY_MODE = 504L # Variable c_uint '504u'
GLUT_INIT_FLAGS = 514L # Variable c_uint '514u'
GLUT_INIT_MAJOR_VERSION = 512L # Variable c_uint '512u'
GLUT_INIT_MINOR_VERSION = 513L # Variable c_uint '513u'
GLUT_INIT_PROFILE = 515L # Variable c_uint '515u'
GLUT_INIT_STATE = 124L # Variable c_uint '124u'
GLUT_INIT_WINDOW_HEIGHT = 503L # Variable c_uint '503u'
GLUT_INIT_WINDOW_WIDTH = 502L # Variable c_uint '502u'
GLUT_INIT_WINDOW_X = 500L # Variable c_uint '500u'
GLUT_INIT_WINDOW_Y = 501L # Variable c_uint '501u'
GLUT_JOYSTICK_AXES = 615L # Variable c_uint '615u'
GLUT_JOYSTICK_BUTTON_A = 1L # Variable c_uint '1u'
GLUT_JOYSTICK_BUTTON_B = 2L # Variable c_uint '2u'
GLUT_JOYSTICK_BUTTON_C = 4L # Variable c_uint '4u'
GLUT_JOYSTICK_BUTTON_D = 8L # Variable c_uint '8u'
GLUT_JOYSTICK_BUTTONS = 614L # Variable c_uint '614u'
GLUT_JOYSTICK_POLL_RATE = 616L # Variable c_uint '616u'
GLUT_KEY_BEGIN = 110L # Variable c_uint '110u'
GLUT_KEY_DELETE = 111L # Variable c_uint '111u'
GLUT_KEY_DOWN = 103L # Variable c_uint '103u'
GLUT_KEY_END = 107L # Variable c_uint '107u'
GLUT_KEY_F10 = 10L # Variable c_uint '10u'
GLUT_KEY_F1 = 1L # Variable c_uint '1u'
GLUT_KEY_F11 = 11L # Variable c_uint '11u'
GLUT_KEY_F12 = 12L # Variable c_uint '12u'
GLUT_KEY_F2 = 2L # Variable c_uint '2u'
GLUT_KEY_F3 = 3L # Variable c_uint '3u'
GLUT_KEY_F4 = 4L # Variable c_uint '4u'
GLUT_KEY_F5 = 5L # Variable c_uint '5u'
GLUT_KEY_F6 = 6L # Variable c_uint '6u'
GLUT_KEY_F7 = 7L # Variable c_uint '7u'
GLUT_KEY_F8 = 8L # Variable c_uint '8u'
GLUT_KEY_F9 = 9L # Variable c_uint '9u'
GLUT_KEY_HOME = 106L # Variable c_uint '106u'
GLUT_KEY_INSERT = 108L # Variable c_uint '108u'
GLUT_KEY_LEFT = 100L # Variable c_uint '100u'
GLUT_KEY_NUM_LOCK = 109L # Variable c_uint '109u'
GLUT_KEY_PAGE_DOWN = 105L # Variable c_uint '105u'
GLUT_KEY_PAGE_UP = 104L # Variable c_uint '104u'
GLUT_KEY_REPEAT_DEFAULT = 2L # Variable c_uint '2u'
GLUT_KEY_REPEAT_OFF = 0L # Variable c_uint '0u'
GLUT_KEY_REPEAT_ON = 1L # Variable c_uint '1u'
GLUT_KEY_RIGHT = 102L # Variable c_uint '102u'
GLUT_KEY_UP = 101L # Variable c_uint '101u'
GLUT_LAYER_IN_USE = 801L # Variable c_uint '801u'
GLUT_LEFT = 0L # Variable c_uint '0u'
GLUT_LEFT_BUTTON = 0L # Variable c_uint '0u'
GLUT_LUMINANCE = 512L # Variable c_uint '512u'
GLUT_MENU_IN_USE = 1L # Variable c_uint '1u'
GLUT_MENU_NOT_IN_USE = 0L # Variable c_uint '0u'
GLUT_MENU_NUM_ITEMS = 300L # Variable c_uint '300u'
GLUT_MIDDLE_BUTTON = 1L # Variable c_uint '1u'
GLUT_MULTISAMPLE = 128L # Variable c_uint '128u'
GLUT_NORMAL = 0L # Variable c_uint '0u'
GLUT_NORMAL_DAMAGED = 804L # Variable c_uint '804u'
GLUT_NOT_VISIBLE = 0L # Variable c_uint '0u'
GLUT_NUM_BUTTON_BOX_BUTTONS = 607L # Variable c_uint '607u'
GLUT_NUM_DIALS = 608L # Variable c_uint '608u'
GLUT_NUM_MOUSE_BUTTONS = 605L # Variable c_uint '605u'
GLUT_NUM_SPACEBALL_BUTTONS = 606L # Variable c_uint '606u'
GLUT_NUM_TABLET_BUTTONS = 609L # Variable c_uint '609u'
GLUT_OVERLAY = 1L # Variable c_uint '1u'
GLUT_OVERLAY_DAMAGED = 805L # Variable c_uint '805u'
GLUT_OVERLAY_POSSIBLE = 800L # Variable c_uint '800u'
GLUT_OWNS_JOYSTICK = 613L # Variable c_uint '613u'
GLUT_PARTIALLY_RETAINED = 2L # Variable c_uint '2u'
GLUT_RED = 0L # Variable c_uint '0u'
GLUT_RENDERING_CONTEXT = 509L # Variable c_uint '509u'
GLUT_RGB = 0L # Variable c_uint '0u'
GLUT_RGBA = 0L # Variable c_uint '0u'
GLUT_RIGHT_BUTTON = 2L # Variable c_uint '2u'
GLU_TRUE = 1L # Variable c_uint '1u'
GLUT_SCREEN_HEIGHT = 201L # Variable c_uint '201u'
GLUT_SCREEN_HEIGHT_MM = 203L # Variable c_uint '203u'
GLUT_SCREEN_WIDTH = 200L # Variable c_uint '200u'
GLUT_SCREEN_WIDTH_MM = 202L # Variable c_uint '202u'
GLUT_SINGLE = 0L # Variable c_uint '0u'
GLUT_SRGB = 4096L # Variable c_uint '4096u'
GLUT_STENCIL = 32L # Variable c_uint '32u'
GLUT_STEREO = 256L # Variable c_uint '256u'
GLUT_TRANSPARENT_INDEX = 803L # Variable c_uint '803u'
GLUT_TRY_DIRECT_CONTEXT = 2L # Variable c_uint '2u'
GLUT_UP = 1L # Variable c_uint '1u'
GLUT_USE_CURRENT_CONTEXT = 1L # Variable c_uint '1u'
GLUT_VERSION = 508L # Variable c_uint '508u'
GLUT_VIDEO_RESIZE_HEIGHT = 909L # Variable c_uint '909u'
GLUT_VIDEO_RESIZE_HEIGHT_DELTA = 905L # Variable c_uint '905u'
GLUT_VIDEO_RESIZE_IN_USE = 901L # Variable c_uint '901u'
GLUT_VIDEO_RESIZE_POSSIBLE = 900L # Variable c_uint '900u'
GLUT_VIDEO_RESIZE_WIDTH = 908L # Variable c_uint '908u'
GLUT_VIDEO_RESIZE_WIDTH_DELTA = 904L # Variable c_uint '904u'
GLUT_VIDEO_RESIZE_X = 906L # Variable c_uint '906u'
GLUT_VIDEO_RESIZE_X_DELTA = 902L # Variable c_uint '902u'
GLUT_VIDEO_RESIZE_Y = 907L # Variable c_uint '907u'
GLUT_VIDEO_RESIZE_Y_DELTA = 903L # Variable c_uint '903u'
GLUT_VISIBLE = 1L # Variable c_uint '1u'
GLUT_WINDOW_ACCUM_ALPHA_SIZE = 114L # Variable c_uint '114u'
GLUT_WINDOW_ACCUM_BLUE_SIZE = 113L # Variable c_uint '113u'
GLUT_WINDOW_ACCUM_GREEN_SIZE = 112L # Variable c_uint '112u'
GLUT_WINDOW_ACCUM_RED_SIZE = 111L # Variable c_uint '111u'
GLUT_WINDOW_ALPHA_SIZE = 110L # Variable c_uint '110u'
GLUT_WINDOW_BLUE_SIZE = 109L # Variable c_uint '109u'
GLUT_WINDOW_BORDER_WIDTH = 506L # Variable c_uint '506u'
GLUT_WINDOW_BUFFER_SIZE = 104L # Variable c_uint '104u'
GLUT_WINDOW_COLORMAP_SIZE = 119L # Variable c_uint '119u'
GLUT_WINDOW_CURSOR = 122L # Variable c_uint '122u'
GLUT_WINDOW_DEPTH_SIZE = 106L # Variable c_uint '106u'
GLUT_WINDOW_DOUBLEBUFFER = 115L # Variable c_uint '115u'
GLUT_WINDOW_FORMAT_ID = 123L # Variable c_uint '123u'
GLUT_WINDOW_GREEN_SIZE = 108L # Variable c_uint '108u'
GLUT_WINDOW_HEADER_HEIGHT = 507L # Variable c_uint '507u'
GLUT_WINDOW_HEIGHT = 103L # Variable c_uint '103u'
GLUT_WINDOW_NUM_CHILDREN = 118L # Variable c_uint '118u'
GLUT_WINDOW_NUM_SAMPLES = 120L # Variable c_uint '120u'
GLUT_WINDOW_PARENT = 117L # Variable c_uint '117u'
GLUT_WINDOW_RED_SIZE = 107L # Variable c_uint '107u'
GLUT_WINDOW_RGBA = 116L # Variable c_uint '116u'
GLUT_WINDOW_STENCIL_SIZE = 105L # Variable c_uint '105u'
GLUT_WINDOW_STEREO = 121L # Variable c_uint '121u'
GLUT_WINDOW_WIDTH = 102L # Variable c_uint '102u'
GLUT_WINDOW_X = 100L # Variable c_uint '100u'
GLUT_WINDOW_Y = 101L # Variable c_uint '101u'
GLUT_XLIB_IMPLEMENTATION = 13L # Variable c_uint '13u'
GLU_UNKNOWN = 100124L # Variable c_uint '100124u'
GLU_U_STEP = 100206L # Variable c_uint '100206u'
GLU_VERSION = 100800L # Variable c_uint '100800u'
GLU_VERSION_1_1 = 1L # Variable c_uint '1u'
GLU_VERSION_1_2 = 1L # Variable c_uint '1u'
GLU_VERSION_1_3 = 1L # Variable c_uint '1u'
GLU_VERTEX = 100101L # Variable c_uint '100101u'
GLU_V_STEP = 100207L # Variable c_uint '100207u'
GL_V2F = 10784L # Variable c_uint '10784u'
GL_V3F = 10785L # Variable c_uint '10785u'
GL_VALIDATE_STATUS = 35715L # Variable c_uint '35715u'
GL_VARIABLE_A_NV = 34083L # Variable c_uint '34083u'
GL_VARIABLE_B_NV = 34084L # Variable c_uint '34084u'
GL_VARIABLE_C_NV = 34085L # Variable c_uint '34085u'
GL_VARIABLE_D_NV = 34086L # Variable c_uint '34086u'
GL_VARIABLE_E_NV = 34087L # Variable c_uint '34087u'
GL_VARIABLE_F_NV = 34088L # Variable c_uint '34088u'
GL_VARIABLE_G_NV = 34089L # Variable c_uint '34089u'
GL_VARIANT_ARRAY_EXT = 34792L # Variable c_uint '34792u'
GL_VARIANT_ARRAY_POINTER_EXT = 34793L # Variable c_uint '34793u'
GL_VARIANT_ARRAY_STRIDE_EXT = 34790L # Variable c_uint '34790u'
GL_VARIANT_ARRAY_TYPE_EXT = 34791L # Variable c_uint '34791u'
GL_VARIANT_DATATYPE_EXT = 34789L # Variable c_uint '34789u'
GL_VARIANT_EXT = 34753L # Variable c_uint '34753u'
GL_VARIANT_VALUE_EXT = 34788L # Variable c_uint '34788u'
GL_VBO_FREE_MEMORY_ATI = 34811L # Variable c_uint '34811u'
GL_VECTOR_EXT = 34751L # Variable c_uint '34751u'
GL_VENDOR = 7936L # Variable c_uint '7936u'
GL_VERSION = 7938L # Variable c_uint '7938u'
GL_VERSION_1_1 = 1L # Variable c_uint '1u'
GL_VERSION_1_2 = 1L # Variable c_uint '1u'
GL_VERSION_1_2_DEPRECATED = 1L # Variable c_uint '1u'
GL_VERSION_1_3 = 1L # Variable c_uint '1u'
GL_VERSION_1_3_DEPRECATED = 1L # Variable c_uint '1u'
GL_VERSION_1_4 = 1L # Variable c_uint '1u'
GL_VERSION_1_4_DEPRECATED = 1L # Variable c_uint '1u'
GL_VERSION_1_5 = 1L # Variable c_uint '1u'
GL_VERSION_2_0 = 1L # Variable c_uint '1u'
GL_VERSION_2_1 = 1L # Variable c_uint '1u'
GL_VERSION_3_0 = 1L # Variable c_uint '1u'
GL_VERSION_3_1 = 1L # Variable c_uint '1u'
GL_VERSION_3_2 = 1L # Variable c_uint '1u'
GL_VERSION_3_3 = 1L # Variable c_uint '1u'
GL_VERSION_4_0 = 1L # Variable c_uint '1u'
GL_VERSION_4_1 = 1L # Variable c_uint '1u'
GL_VERTEX23_BIT_PGI = 4L # Variable c_uint '4u'
GL_VERTEX4_BIT_PGI = 8L # Variable c_uint '8u'
GL_VERTEX_ARRAY = 32884L # Variable c_uint '32884u'
GL_VERTEX_ARRAY_ADDRESS_NV = 36641L # Variable c_uint '36641u'
GL_VERTEX_ARRAY_BINDING = 34229L # Variable c_uint '34229u'
GL_VERTEX_ARRAY_BINDING_APPLE = 34229L # Variable c_uint '34229u'
GL_VERTEX_ARRAY_BUFFER_BINDING = 34966L # Variable c_uint '34966u'
GL_VERTEX_ARRAY_BUFFER_BINDING_ARB = 34966L # Variable c_uint '34966u'
GL_VERTEX_ARRAY_COUNT_EXT = 32893L # Variable c_uint '32893u'
GL_VERTEX_ARRAY_EXT = 32884L # Variable c_uint '32884u'
GL_VERTEX_ARRAY_LENGTH_NV = 36651L # Variable c_uint '36651u'
GL_VERTEX_ARRAY_LIST_IBM = 103070L # Variable c_uint '103070u'
GL_VERTEX_ARRAY_LIST_STRIDE_IBM = 103080L # Variable c_uint '103080u'
GL_VERTEX_ARRAY_OBJECT_AMD = 37204L # Variable c_uint '37204u'
GL_VERTEX_ARRAY_PARALLEL_POINTERS_INTEL = 33781L # Variable c_uint '33781u'
GL_VERTEX_ARRAY_POINTER = 32910L # Variable c_uint '32910u'
GL_VERTEX_ARRAY_POINTER_EXT = 32910L # Variable c_uint '32910u'
GL_VERTEX_ARRAY_RANGE_APPLE = 34077L # Variable c_uint '34077u'
GL_VERTEX_ARRAY_RANGE_LENGTH_APPLE = 34078L # Variable c_uint '34078u'
GL_VERTEX_ARRAY_RANGE_LENGTH_NV = 34078L # Variable c_uint '34078u'
GL_VERTEX_ARRAY_RANGE_NV = 34077L # Variable c_uint '34077u'
GL_VERTEX_ARRAY_RANGE_POINTER_APPLE = 34081L # Variable c_uint '34081u'
GL_VERTEX_ARRAY_RANGE_POINTER_NV = 34081L # Variable c_uint '34081u'
GL_VERTEX_ARRAY_RANGE_VALID_NV = 34079L # Variable c_uint '34079u'
GL_VERTEX_ARRAY_RANGE_WITHOUT_FLUSH_NV = 34099L # Variable c_uint '34099u'
GL_VERTEX_ARRAY_SIZE = 32890L # Variable c_uint '32890u'
GL_VERTEX_ARRAY_SIZE_EXT = 32890L # Variable c_uint '32890u'
GL_VERTEX_ARRAY_STORAGE_HINT_APPLE = 34079L # Variable c_uint '34079u'
GL_VERTEX_ARRAY_STRIDE = 32892L # Variable c_uint '32892u'
GL_VERTEX_ARRAY_STRIDE_EXT = 32892L # Variable c_uint '32892u'
GL_VERTEX_ARRAY_TYPE = 32891L # Variable c_uint '32891u'
GL_VERTEX_ARRAY_TYPE_EXT = 32891L # Variable c_uint '32891u'
GL_VERTEX_ATTRIB_ARRAY0_NV = 34384L # Variable c_uint '34384u'
GL_VERTEX_ATTRIB_ARRAY10_NV = 34394L # Variable c_uint '34394u'
GL_VERTEX_ATTRIB_ARRAY11_NV = 34395L # Variable c_uint '34395u'
GL_VERTEX_ATTRIB_ARRAY12_NV = 34396L # Variable c_uint '34396u'
GL_VERTEX_ATTRIB_ARRAY13_NV = 34397L # Variable c_uint '34397u'
GL_VERTEX_ATTRIB_ARRAY14_NV = 34398L # Variable c_uint '34398u'
GL_VERTEX_ATTRIB_ARRAY15_NV = 34399L # Variable c_uint '34399u'
GL_VERTEX_ATTRIB_ARRAY1_NV = 34385L # Variable c_uint '34385u'
GL_VERTEX_ATTRIB_ARRAY2_NV = 34386L # Variable c_uint '34386u'
GL_VERTEX_ATTRIB_ARRAY3_NV = 34387L # Variable c_uint '34387u'
GL_VERTEX_ATTRIB_ARRAY4_NV = 34388L # Variable c_uint '34388u'
GL_VERTEX_ATTRIB_ARRAY5_NV = 34389L # Variable c_uint '34389u'
GL_VERTEX_ATTRIB_ARRAY6_NV = 34390L # Variable c_uint '34390u'
GL_VERTEX_ATTRIB_ARRAY7_NV = 34391L # Variable c_uint '34391u'
GL_VERTEX_ATTRIB_ARRAY8_NV = 34392L # Variable c_uint '34392u'
GL_VERTEX_ATTRIB_ARRAY9_NV = 34393L # Variable c_uint '34393u'
GL_VERTEX_ATTRIB_ARRAY_ADDRESS_NV = 36640L # Variable c_uint '36640u'
GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT_EXT = 1L # Variable c_uint '1u'
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = 34975L # Variable c_uint '34975u'
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING_ARB = 34975L # Variable c_uint '34975u'
GL_VERTEX_ATTRIB_ARRAY_DIVISOR = 35070L # Variable c_uint '35070u'
GL_VERTEX_ATTRIB_ARRAY_DIVISOR_ARB = 35070L # Variable c_uint '35070u'
GL_VERTEX_ATTRIB_ARRAY_ENABLED = 34338L # Variable c_uint '34338u'
GL_VERTEX_ATTRIB_ARRAY_ENABLED_ARB = 34338L # Variable c_uint '34338u'
GL_VERTEX_ATTRIB_ARRAY_INTEGER = 35069L # Variable c_uint '35069u'
GL_VERTEX_ATTRIB_ARRAY_INTEGER_NV = 35069L # Variable c_uint '35069u'
GL_VERTEX_ATTRIB_ARRAY_LENGTH_NV = 36650L # Variable c_uint '36650u'
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED = 34922L # Variable c_uint '34922u'
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED_ARB = 34922L # Variable c_uint '34922u'
GL_VERTEX_ATTRIB_ARRAY_POINTER = 34373L # Variable c_uint '34373u'
GL_VERTEX_ATTRIB_ARRAY_POINTER_ARB = 34373L # Variable c_uint '34373u'
GL_VERTEX_ATTRIB_ARRAY_SIZE = 34339L # Variable c_uint '34339u'
GL_VERTEX_ATTRIB_ARRAY_SIZE_ARB = 34339L # Variable c_uint '34339u'
GL_VERTEX_ATTRIB_ARRAY_STRIDE = 34340L # Variable c_uint '34340u'
GL_VERTEX_ATTRIB_ARRAY_STRIDE_ARB = 34340L # Variable c_uint '34340u'
GL_VERTEX_ATTRIB_ARRAY_TYPE = 34341L # Variable c_uint '34341u'
GL_VERTEX_ATTRIB_ARRAY_TYPE_ARB = 34341L # Variable c_uint '34341u'
GL_VERTEX_ATTRIB_ARRAY_UNIFIED_NV = 36638L # Variable c_uint '36638u'
GL_VERTEX_ATTRIB_MAP1_APPLE = 35328L # Variable c_uint '35328u'
GL_VERTEX_ATTRIB_MAP1_COEFF_APPLE = 35331L # Variable c_uint '35331u'
GL_VERTEX_ATTRIB_MAP1_DOMAIN_APPLE = 35333L # Variable c_uint '35333u'
GL_VERTEX_ATTRIB_MAP1_ORDER_APPLE = 35332L # Variable c_uint '35332u'
GL_VERTEX_ATTRIB_MAP1_SIZE_APPLE = 35330L # Variable c_uint '35330u'
GL_VERTEX_ATTRIB_MAP2_APPLE = 35329L # Variable c_uint '35329u'
GL_VERTEX_ATTRIB_MAP2_COEFF_APPLE = 35335L # Variable c_uint '35335u'
GL_VERTEX_ATTRIB_MAP2_DOMAIN_APPLE = 35337L # Variable c_uint '35337u'
GL_VERTEX_ATTRIB_MAP2_ORDER_APPLE = 35336L # Variable c_uint '35336u'
GL_VERTEX_ATTRIB_MAP2_SIZE_APPLE = 35334L # Variable c_uint '35334u'
GL_VERTEX_BLEND_ARB = 34471L # Variable c_uint '34471u'
GL_VERTEX_CONSISTENT_HINT_PGI = 107051L # Variable c_uint '107051u'
GL_VERTEX_DATA_HINT_PGI = 107050L # Variable c_uint '107050u'
GL_VERTEX_ID_NV = 35963L # Variable c_uint '35963u'
GL_VERTEX_PRECLIP_HINT_SGIX = 33775L # Variable c_uint '33775u'
GL_VERTEX_PRECLIP_SGIX = 33774L # Variable c_uint '33774u'
GL_VERTEX_PROGRAM_ARB = 34336L # Variable c_uint '34336u'
GL_VERTEX_PROGRAM_BINDING_NV = 34378L # Variable c_uint '34378u'
GL_VERTEX_PROGRAM_CALLBACK_DATA_MESA = 35767L # Variable c_uint '35767u'
GL_VERTEX_PROGRAM_CALLBACK_FUNC_MESA = 35766L # Variable c_uint '35766u'
GL_VERTEX_PROGRAM_CALLBACK_MESA = 35765L # Variable c_uint '35765u'
GL_VERTEX_PROGRAM_NV = 34336L # Variable c_uint '34336u'
GL_VERTEX_PROGRAM_PARAMETER_BUFFER_NV = 36258L # Variable c_uint '36258u'
GL_VERTEX_PROGRAM_POINT_SIZE = 34370L # Variable c_uint '34370u'
GL_VERTEX_PROGRAM_POINT_SIZE_ARB = 34370L # Variable c_uint '34370u'
GL_VERTEX_PROGRAM_POINT_SIZE_NV = 34370L # Variable c_uint '34370u'
GL_VERTEX_PROGRAM_POSITION_MESA = 35764L # Variable c_uint '35764u'
GL_VERTEX_PROGRAM_TWO_SIDE = 34371L # Variable c_uint '34371u'
GL_VERTEX_PROGRAM_TWO_SIDE_ARB = 34371L # Variable c_uint '34371u'
GL_VERTEX_PROGRAM_TWO_SIDE_NV = 34371L # Variable c_uint '34371u'
GL_VERTEX_SHADER = 35633L # Variable c_uint '35633u'
GL_VERTEX_SHADER_ARB = 35633L # Variable c_uint '35633u'
GL_VERTEX_SHADER_BINDING_EXT = 34689L # Variable c_uint '34689u'
GL_VERTEX_SHADER_BIT = 1L # Variable c_uint '1u'
GL_VERTEX_SHADER_EXT = 34688L # Variable c_uint '34688u'
GL_VERTEX_SHADER_INSTRUCTIONS_EXT = 34767L # Variable c_uint '34767u'
GL_VERTEX_SHADER_INVARIANTS_EXT = 34769L # Variable c_uint '34769u'
GL_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = 34770L # Variable c_uint '34770u'
GL_VERTEX_SHADER_LOCALS_EXT = 34771L # Variable c_uint '34771u'
GL_VERTEX_SHADER_OPTIMIZED_EXT = 34772L # Variable c_uint '34772u'
GL_VERTEX_SHADER_VARIANTS_EXT = 34768L # Variable c_uint '34768u'
GL_VERTEX_SOURCE_ATI = 34676L # Variable c_uint '34676u'
GL_VERTEX_STATE_PROGRAM_NV = 34337L # Variable c_uint '34337u'
GL_VERTEX_STREAM0_ATI = 34668L # Variable c_uint '34668u'
GL_VERTEX_STREAM1_ATI = 34669L # Variable c_uint '34669u'
GL_VERTEX_STREAM2_ATI = 34670L # Variable c_uint '34670u'
GL_VERTEX_STREAM3_ATI = 34671L # Variable c_uint '34671u'
GL_VERTEX_STREAM4_ATI = 34672L # Variable c_uint '34672u'
GL_VERTEX_STREAM5_ATI = 34673L # Variable c_uint '34673u'
GL_VERTEX_STREAM6_ATI = 34674L # Variable c_uint '34674u'
GL_VERTEX_STREAM7_ATI = 34675L # Variable c_uint '34675u'
GL_VERTEX_WEIGHT_ARRAY_EXT = 34060L # Variable c_uint '34060u'
GL_VERTEX_WEIGHT_ARRAY_POINTER_EXT = 34064L # Variable c_uint '34064u'
GL_VERTEX_WEIGHT_ARRAY_SIZE_EXT = 34061L # Variable c_uint '34061u'
GL_VERTEX_WEIGHT_ARRAY_STRIDE_EXT = 34063L # Variable c_uint '34063u'
GL_VERTEX_WEIGHT_ARRAY_TYPE_EXT = 34062L # Variable c_uint '34062u'
GL_VERTEX_WEIGHTING_EXT = 34057L # Variable c_uint '34057u'
GL_VIBRANCE_BIAS_NV = 34585L # Variable c_uint '34585u'
GL_VIBRANCE_SCALE_NV = 34579L # Variable c_uint '34579u'
GL_VIDEO_BUFFER_BINDING_NV = 36897L # Variable c_uint '36897u'
GL_VIDEO_BUFFER_INTERNAL_FORMAT_NV = 36909L # Variable c_uint '36909u'
GL_VIDEO_BUFFER_NV = 36896L # Variable c_uint '36896u'
GL_VIDEO_BUFFER_PITCH_NV = 36904L # Variable c_uint '36904u'
GL_VIDEO_CAPTURE_FIELD_LOWER_HEIGHT_NV = 36923L # Variable c_uint '36923u'
GL_VIDEO_CAPTURE_FIELD_UPPER_HEIGHT_NV = 36922L # Variable c_uint '36922u'
GL_VIDEO_CAPTURE_FRAME_HEIGHT_NV = 36921L # Variable c_uint '36921u'
GL_VIDEO_CAPTURE_FRAME_WIDTH_NV = 36920L # Variable c_uint '36920u'
GL_VIDEO_CAPTURE_SURFACE_ORIGIN_NV = 36924L # Variable c_uint '36924u'
GL_VIDEO_CAPTURE_TO_422_SUPPORTED_NV = 36902L # Variable c_uint '36902u'
GL_VIDEO_COLOR_CONVERSION_MATRIX_NV = 36905L # Variable c_uint '36905u'
GL_VIDEO_COLOR_CONVERSION_MAX_NV = 36906L # Variable c_uint '36906u'
GL_VIDEO_COLOR_CONVERSION_MIN_NV = 36907L # Variable c_uint '36907u'
GL_VIDEO_COLOR_CONVERSION_OFFSET_NV = 36908L # Variable c_uint '36908u'
GL_VIEWPORT = 2978L # Variable c_uint '2978u'
GL_VIEWPORT_BIT = 2048L # Variable c_uint '2048u'
GL_VIEWPORT_BOUNDS_RANGE = 33373L # Variable c_uint '33373u'
GL_VIEWPORT_INDEX_PROVOKING_VERTEX = 33375L # Variable c_uint '33375u'
GL_VIEWPORT_SUBPIXEL_BITS = 33372L # Variable c_uint '33372u'
GL_VOLATILE_APPLE = 35354L # Variable c_uint '35354u'
GL_WAIT_FAILED = 37149L # Variable c_uint '37149u'
GL_WEIGHT_ARRAY_ARB = 34477L # Variable c_uint '34477u'
GL_WEIGHT_ARRAY_BUFFER_BINDING = 34974L # Variable c_uint '34974u'
GL_WEIGHT_ARRAY_BUFFER_BINDING_ARB = 34974L # Variable c_uint '34974u'
GL_WEIGHT_ARRAY_POINTER_ARB = 34476L # Variable c_uint '34476u'
GL_WEIGHT_ARRAY_SIZE_ARB = 34475L # Variable c_uint '34475u'
GL_WEIGHT_ARRAY_STRIDE_ARB = 34474L # Variable c_uint '34474u'
GL_WEIGHT_ARRAY_TYPE_ARB = 34473L # Variable c_uint '34473u'
GL_WEIGHT_SUM_UNITY_ARB = 34470L # Variable c_uint '34470u'
GL_W_EXT = 34776L # Variable c_uint '34776u'
GL_WIDE_LINE_HINT_PGI = 107042L # Variable c_uint '107042u'
GL_WRAP_BORDER_SUN = 33236L # Variable c_uint '33236u'
GL_WRITE_DISCARD_NV = 35006L # Variable c_uint '35006u'
GL_WRITE_ONLY = 35001L # Variable c_uint '35001u'
GL_WRITE_ONLY_ARB = 35001L # Variable c_uint '35001u'
GL_WRITE_PIXEL_DATA_RANGE_LENGTH_NV = 34938L # Variable c_uint '34938u'
GL_WRITE_PIXEL_DATA_RANGE_NV = 34936L # Variable c_uint '34936u'
GL_WRITE_PIXEL_DATA_RANGE_POINTER_NV = 34940L # Variable c_uint '34940u'
GL_X_EXT = 34773L # Variable c_uint '34773u'
GL_XOR = 5382L # Variable c_uint '5382u'
GL_YCBAYCR8A_4224_NV = 36914L # Variable c_uint '36914u'
GL_YCBCR_422_APPLE = 34233L # Variable c_uint '34233u'
GL_YCBCR_MESA = 34647L # Variable c_uint '34647u'
GL_YCBYCR8_422_NV = 36913L # Variable c_uint '36913u'
GL_YCRCB_422_SGIX = 33211L # Variable c_uint '33211u'
GL_YCRCB_444_SGIX = 33212L # Variable c_uint '33212u'
GL_YCRCBA_SGIX = 33561L # Variable c_uint '33561u'
GL_YCRCB_SGIX = 33560L # Variable c_uint '33560u'
GL_Y_EXT = 34774L # Variable c_uint '34774u'
GL_Z4Y12Z4CB12Z4A12Z4Y12Z4CR12Z4A12_4224_NV = 36918L # Variable c_uint '36918u'
GL_Z4Y12Z4CB12Z4CR12_444_NV = 36919L # Variable c_uint '36919u'
GL_Z4Y12Z4CB12Z4Y12Z4CR12_422_NV = 36917L # Variable c_uint '36917u'
GL_Z6Y10Z6CB10Z6A10Z6Y10Z6CR10Z6A10_4224_NV = 36916L # Variable c_uint '36916u'
GL_Z6Y10Z6CB10Z6Y10Z6CR10_422_NV = 36915L # Variable c_uint '36915u'
GL_ZERO = 0L # Variable c_uint '0u'
GL_ZERO_EXT = 34781L # Variable c_uint '34781u'
GL_Z_EXT = 34775L # Variable c_uint '34775u'
GL_ZOOM_X = 3350L # Variable c_uint '3350u'
GL_ZOOM_Y = 3351L # Variable c_uint '3351u'
__GLsync._fields_ = [
]
__all__ = ['GL_INDEX_ARRAY_TYPE', 'GL_INDEX_CLEAR_VALUE',
           'GLUT_NUM_MOUSE_BUTTONS', 'glCopyTexImage1D', 'GLsizei',
           'GL_OUTPUT_TEXTURE_COORD20_EXT', 'GL_TEXCOORD2_BIT_PGI',
           'GL_BACK_NORMALS_HINT_PGI', 'GL_PIXEL_TILE_HEIGHT_SGIX',
           'GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY',
           'GLUT_HAS_OVERLAY', 'GL_SAMPLE_ALPHA_TO_ONE_SGIS',
           'GL_FLOAT_VEC3', 'glutGameModeString', 'GL_SOURCE1_ALPHA',
           'GL_DITHER', 'GL_SHADING_LANGUAGE_VERSION_ARB', 'glIndexi',
           'GL_DST_ALPHA', 'glMultiTexCoord2sARB',
           'glCompressedTexSubImage3D', 'glEvalCoord2d', 'GLboolean',
           'glEvalCoord2f', 'GL_TEXTURE13_ARB', 'glIndexd',
           'GL_COORD_REPLACE_NV', 'glIndexf', 'GLU_TRUE',
           'GL_ALPHA_TEST_FUNC', 'GL_INT_2_10_10_10_REV',
           'GL_PROXY_TEXTURE_2D_MULTISAMPLE',
           'GL_PROVOKING_VERTEX_EXT', 'GL_TEXTURE_MAX_LOD',
           'GL_LINE_STRIP_ADJACENCY_ARB', 'glIndexs',
           'GLU_OUTLINE_PATCH', 'GL_OBJECT_SUBTYPE_ARB',
           'GL_RGBA_INTEGER_EXT', 'GL_SRGB8_EXT',
           'GL_ALPHA_FLOAT32_ATI', 'GL_MIRROR_CLAMP_TO_EDGE_EXT',
           'GLchar', 'GL_LUMINANCE16F_ARB', 'GL_RGB9_E5',
           'GLUT_FULLY_COVERED', 'GLU_NURBS_NORMAL_EXT',
           'GL_NUM_FRAGMENT_CONSTANTS_ATI', 'GL_PROXY_TEXTURE_2D_EXT',
           'GL_PIXEL_PACK_BUFFER_BINDING_EXT', 'GL_TEXTURE18_ARB',
           'GL_IMAGE_1D_EXT', 'GL_TRANSPOSE_PROGRAM_MATRIX_EXT',
           'GL_RGBA32UI', 'GL_SOURCE2_ALPHA_EXT',
           'GL_SECONDARY_COLOR_ARRAY_STRIDE_EXT', 'GLUT_KEY_F9',
           'GL_TEXTURE_MIN_LOD', 'glFogfv',
           'GL_MAX_GEOMETRY_VARYING_COMPONENTS_ARB',
           'GL_MODELVIEW6_ARB', 'GL_FRAGMENT_LIGHTING_SGIX',
           'glVertex4iv', 'GL_HISTOGRAM_LUMINANCE_SIZE_EXT',
           'GL_SOURCE0_ALPHA', 'GL_RGB_FLOAT32_APPLE',
           'GL_BLEND_EQUATION', 'GL_VIDEO_CAPTURE_FRAME_HEIGHT_NV',
           'GL_BYTE', 'GL_EYE_DISTANCE_TO_LINE_SGIS', 'GL_R32UI',
           'GL_MAX_ASYNC_READ_PIXELS_SGIX', 'GL_PACK_RESAMPLE_OML',
           'GL_SAMPLER_1D_ARRAY_EXT', 'GL_PROXY_HISTOGRAM',
           'GL_DETAIL_TEXTURE_LEVEL_SGIS',
           'GL_BUFFER_MAP_POINTER_ARB', 'GL_DEPTH_BIAS',
           'GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH_ARB',
           'GL_COLOR_CLEAR_VALUE', 'GL_TEXTURE_DEPTH_TYPE_ARB',
           'GL_BUFFER_USAGE', 'GL_FRAMEBUFFER_SRGB',
           'GL_DEPTH32F_STENCIL8_NV',
           'GL_MAX_PROGRAM_TEX_INDIRECTIONS_ARB',
           'GL_PIXEL_MAP_G_TO_G', 'GL_PIXEL_TEX_GEN_Q_ROUND_SGIX',
           'GL_MATRIX_INDEX_ARRAY_STRIDE_ARB', 'GL_RENDER',
           'GL_MAX_MAP_TESSELLATION_NV', 'GL_INT8_NV', 'GL_RGBA2_EXT',
           'GL_SECONDARY_COLOR_ARRAY_TYPE', 'GL_MATRIX_PALETTE_ARB',
           'glColor4uiv', 'GL_MAX_GENERAL_COMBINERS_NV',
           'GLU_NURBS_ERROR1', 'GL_ATTRIB_ARRAY_POINTER_NV',
           'GL_TRIANGLE_STRIP_ADJACENCY', 'glLoadTransposeMatrixd',
           'GL_TRANSFORM_FEEDBACK_BUFFER', 'glPopAttrib',
           'glutBitmapWidth', 'GL_PROXY_TEXTURE_3D_EXT',
           'GLU_TESS_END', 'glutDestroyWindow', 'glColorMaterial',
           'GL_BGRA_EXT', 'GL_MATRIX19_ARB',
           'GL_RENDERBUFFER_INTERNAL_FORMAT_EXT', 'glColor3b',
           'GL_FLOAT_RGBA32_NV', 'GLUT_GAME_MODE_HEIGHT', 'glColor3f',
           'GL_MAX_FRAGMENT_PROGRAM_LOCAL_PARAMETERS_NV', 'glColor3d',
           'GL_OUTPUT_TEXTURE_COORD22_EXT',
           'GL_COLOR_ATTACHMENT15_EXT', 'GL_ALLOW_DRAW_FRG_HINT_PGI',
           'GL_CURRENT_RASTER_TEXTURE_COORDS', 'glColor3i',
           'GL_SHARPEN_TEXTURE_FUNC_POINTS_SGIS',
           'GL_RENDERBUFFER_FREE_MEMORY_ATI', 'GL_EXP',
           'GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING_ARB', 'glColor3s',
           'GL_SCISSOR_BIT', 'glutJoystickNotWorking',
           'GL_HISTOGRAM_FORMAT',
           'GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE',
           'GL_SAMPLE_ALPHA_TO_COVERAGE_ARB', 'GLU_NURBS_ERROR9',
           'GL_GEOMETRY_SHADER_ARB', 'GL_CMYK_EXT', 'GL_RGB12',
           'GL_TIME_ELAPSED_EXT', 'GL_BLEND_DST_ALPHA_EXT',
           'GL_CON_26_ATI', 'GL_IUI_V3F_EXT',
           'GL_TEXTURE_COMPARE_FAIL_VALUE_ARB',
           'GL_SAMPLE_SHADING_ARB', 'GL_POLYGON_OFFSET_FILL',
           'glutBitmapTimesRoman10', 'GL_TRACK_MATRIX_NV',
           'GL_FIRST_VERTEX_CONVENTION',
           'GL_INT_IMAGE_2D_MULTISAMPLE_ARRAY_EXT', 'glVertex2iv',
           'GLfloat', 'GL_MINMAX_FORMAT', 'GL_MAX_CLIP_PLANES',
           'GL_COLOR_TABLE_BLUE_SIZE_SGI', 'GL_VERSION_1_4',
           'GL_ALL_COMPLETED_NV', 'GL_FRAGMENT_SHADER_BIT',
           'GL_PN_TRIANGLES_NORMAL_MODE_LINEAR_ATI', 'GL_RGB9_E5_EXT',
           'GL_VERTEX_ATTRIB_MAP1_ORDER_APPLE', 'GLU_SMOOTH',
           'GL_TEXTURE_SWIZZLE_G_EXT',
           'GL_PROGRAM_TEX_INSTRUCTIONS_ARB', 'GL_DOUBLE_MAT4',
           'GL_IMAGE_2D_ARRAY_EXT', 'GL_DOUBLE_MAT2',
           'GL_DOUBLE_MAT3', 'GL_DEBUG_OBJECT_MESA',
           'GL_COMPILE_AND_EXECUTE', 'GL_DRAW_BUFFER0_ARB',
           'GL_GREEN_BITS', 'GL_FENCE_CONDITION_NV',
           'GL_TEXTURE_GREEN_TYPE', 'glFogi', 'GL_FOG_COORD_ARRAY',
           'GL_MIN_SAMPLE_SHADING_VALUE', 'GL_R1UI_T2F_N3F_V3F_SUN',
           'glVertexPointer', 'GL_HISTOGRAM_FORMAT_EXT', 'glFogf',
           'GL_COMBINE_ALPHA_EXT', 'glMultiTexCoord1d',
           'GL_RGB5_A1_EXT', 'glMultiTexCoord1f',
           'GL_LUMINANCE_ALPHA32I_EXT', 'GL_READ_WRITE_ARB',
           'GL_VERTEX_ATTRIB_ARRAY_POINTER_ARB', 'glutGetModifiers',
           'GL_QUAD_MESH_SUN', 'glMultiTexCoord1i',
           'GL_FRAGMENT_SHADER_DERIVATIVE_HINT', 'GL_TEXTURE_DEPTH',
           'GL_STORAGE_CLIENT_APPLE', 'GLU_NURBS_ERROR6',
           'GL_NORMAL_MAP_ARB', 'glMultiTexCoord1s', 'glStencilOp',
           'GL_RGB_FLOAT16_APPLE', 'GL_DUAL_ALPHA4_SGIS',
           'GL_PIXEL_MAP_I_TO_I', 'GL_DRAW_BUFFER6',
           'GL_DRAW_BUFFER7', 'GL_DRAW_BUFFER4', 'GL_DRAW_BUFFER5',
           'glTexCoord3sv', 'GL_DRAW_BUFFER3', 'GL_DRAW_BUFFER0',
           'GL_DRAW_BUFFER1', 'GL_LIGHT1', 'GL_LIGHT0', 'GL_LIGHT3',
           'GL_LIGHT2', 'GL_COPY', 'GL_LIGHT4', 'GL_DRAW_BUFFER8',
           'GL_DRAW_BUFFER9', 'GL_MAP_STENCIL',
           'GL_PN_TRIANGLES_NORMAL_MODE_ATI',
           'GL_QUADRATIC_ATTENUATION', 'GL_SMOOTH_LINE_WIDTH_RANGE',
           'GL_TEXTURE20', 'GL_TEXTURE_RECTANGLE',
           'GL_PROXY_TEXTURE_2D_ARRAY_EXT',
           'GL_MAX_GEOMETRY_VARYING_COMPONENTS_EXT', 'GL_FILL',
           'GL_LUMINANCE_ALPHA32UI_EXT', 'GL_DEPTH_BUFFER',
           'GL_SRC_COLOR', 'GL_COVERAGE_SAMPLES_NV',
           'GL_SAMPLER_BINDING', 'glutEstablishOverlay',
           'GL_FLOAT_RGB_NV', 'GLU_NURBS_ERROR36',
           'glutStrokeMonoRoman', 'GL_SAMPLE_BUFFERS',
           'GL_MATRIX28_ARB', 'GL_DEPENDENT_AR_TEXTURE_2D_NV',
           'GL_ACTIVE_ATTRIBUTE_MAX_LENGTH',
           'GL_MATRIX_INDEX_ARRAY_SIZE_ARB', 'GL_EXTENSIONS',
           'GL_COLOR_MATRIX', 'GL_VERTEX_WEIGHT_ARRAY_EXT',
           'GL_PASS_THROUGH_TOKEN', 'GL_UPPER_LEFT',
           'GL_MAP1_VERTEX_ATTRIB2_4_NV', 'GL_INT_IMAGE_2D_ARRAY_EXT',
           'GL_PROGRAM_MATRIX_STACK_DEPTH_EXT', 'GL_CON_2_ATI',
           'GL_LAST_VERTEX_CONVENTION',
           'GL_NUM_INPUT_INTERPOLATOR_COMPONENTS_ATI',
           'GL_COUNTER_RANGE_AMD',
           'GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_EXT',
           'glVertex3dv', 'GL_STENCIL_BACK_PASS_DEPTH_FAIL',
           'GL_INT_SAMPLER_CUBE_MAP_ARRAY', 'GL_UNIFORM_BUFFER',
           'glutForceJoystickFunc', 'GLUT_INIT_STATE',
           'GL_SAMPLE_MASK', 'glutDestroyMenu', 'GL_MULTISAMPLE_ARB',
           'glColor4fv', 'GL_CCW', 'glConvolutionFilter2D',
           'GL_TEXTURE_1D', 'GL_DEPTH_COMPONENT24',
           'GL_VERTEX_ATTRIB_MAP1_SIZE_APPLE', 'glTexCoord2sv',
           'glutUseLayer', 'GL_INTERLEAVED_ATTRIBS_EXT',
           'GL_RG_SNORM', 'GL_OUTPUT_TEXTURE_COORD26_EXT',
           'GL_VERTEX_ATTRIB_ARRAY_INTEGER', 'glGetPixelMapuiv',
           'GL_MODELVIEW18_ARB',
           'GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE', 'GL_R32I',
           'GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_EXT', 'GL_R32F',
           'GL_PRIMITIVES_GENERATED_NV', 'GL_DRAW_BUFFER15_ARB',
           'glGetPointerv', 'GL_INT_VEC4',
           'GL_VERTEX_ARRAY_BUFFER_BINDING',
           'GLUT_WINDOW_COLORMAP_SIZE', 'GL_OPERAND0_RGB_EXT',
           'GL_FEEDBACK_BUFFER_TYPE', 'GL_PIXEL_MAP_R_TO_R',
           'GL_TEXTURE_MAX_CLAMP_S_SGIX',
           'GLUT_WINDOW_ACCUM_RED_SIZE',
           'GL_EDGE_FLAG_ARRAY_LIST_IBM', 'glFrustum',
           'glMultiTexCoord4sv', 'GL_REPLICATE_BORDER',
           'GL_ELEMENT_ARRAY_ATI', 'GL_CMYKA_EXT',
           'GL_VERTEX_BLEND_ARB', 'GL_TEXTURE_COMPRESSED',
           'GL_MATRIX20_ARB', 'GL_RGB32F', 'GL_FLOAT_MAT2',
           'GL_FLOAT_MAT3', 'GL_DEPTH', 'glMultiTexCoord4iARB',
           'GL_FLOAT_MAT4', 'GL_RGB16F', 'GLUT_HAS_MOUSE',
           'GLUT_KEY_F11', 'GL_MAP2_VERTEX_ATTRIB9_4_NV',
           'GL_POST_COLOR_MATRIX_ALPHA_SCALE_SGI', 'GL_OPERAND1_RGB',
           'GL_OBJECT_LINK_STATUS_ARB', 'GL_COLOR_ATTACHMENT8_EXT',
           'GL_ONE_MINUS_SRC_ALPHA',
           'GL_COLOR_CLEAR_UNCLAMPED_VALUE_ATI', 'GL_BUMP_TARGET_ATI',
           'GL_MAX_TESS_PATCH_COMPONENTS', 'GL_MAX_VERTEX_HINT_PGI',
           'GL_COLOR_ARRAY_LIST_STRIDE_IBM', 'GL_T2F_C4UB_V3F',
           'GL_DOT_PRODUCT_TEXTURE_1D_NV', 'GL_NAME_STACK_DEPTH',
           'GL_RGBA8I', 'GL_PROGRAM_PARAMETERS_ARB', 'GL_SRC1_ALPHA',
           'GL_MATRIX12_ARB', 'GL_CURRENT_TANGENT_EXT',
           'GL_SIGNED_ALPHA_NV', 'GL_R3_G3_B2',
           'GL_STENCIL_TAG_BITS_EXT', 'GL_SAMPLE_PATTERN_SGIS',
           'GL_ALPHA_BIAS', 'GL_TRANSFORM_FEEDBACK_BUFFER_ACTIVE',
           'GL_PROGRAM_NATIVE_TEX_INSTRUCTIONS_ARB',
           'GL_TEXTURE_LIGHTING_MODE_HP', 'GL_HILO16_NV',
           'GL_TRANSFORM_FEEDBACK_NV', 'GL_IMAGE_ROTATE_ANGLE_HP',
           'GL_MULTISAMPLE_EXT', 'GL_FOG_COORDINATE_ARRAY',
           'GL_RASTERIZER_DISCARD_EXT', 'GL_MATRIX1_NV',
           'GL_SAMPLER_CUBE_SHADOW', 'GL_TEXTURE_BINDING_3D',
           'GL_TEXTURE_BORDER', 'GLUT_WINDOW_ALPHA_SIZE', 'glutInit',
           'GL_PACK_IMAGE_HEIGHT_EXT', 'glutInitContextFlags',
           'GL_TEXTURE_4DSIZE_SGIS', 'GLUT_INIT_MINOR_VERSION',
           'GL_FOG_COORDINATE_SOURCE_EXT',
           'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_3D_ZOFFSET_EXT',
           'GL_TEXTURE', 'GL_BLUE_MAX_CLAMP_INGR',
           'glutGetWindowData', 'GL_MAX_PROJECTION_STACK_DEPTH',
           'GL_MIN_PROGRAM_TEXEL_OFFSET_NV', 'GL_CND_ATI',
           'GL_MAX_CLIP_DISTANCES', 'GL_CULL_MODES_NV',
           'GL_T2F_IUI_N3F_V2F_EXT', 'GL_CLIP_DISTANCE_NV',
           'GLsizeiptr', 'glTexCoord4iv', 'GL_ACTIVE_UNIFORMS',
           'GL_TEXTURE24_ARB', 'glTexCoord2dv',
           'GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET', 'GLU_NURBS_ERROR3',
           'GL_DOT2_ADD_ATI', 'glIndexPointer',
           'GL_EVAL_VERTEX_ATTRIB3_NV', 'GL_TEXTURE_BINDING_CUBE_MAP',
           'GL_MAX_TEXTURE_IMAGE_UNITS',
           'GL_PIXEL_TRANSFORM_2D_MATRIX_EXT',
           'GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_EXT',
           'GL_PIXEL_UNPACK_BUFFER_BINDING_ARB',
           'GL_PARTIAL_SUCCESS_NV', 'GLUT_INIT_DISPLAY_MODE',
           'GLU_OBJECT_PATH_LENGTH_EXT',
           'GL_NUM_COMPRESSED_TEXTURE_FORMATS',
           'GL_YCBAYCR8A_4224_NV', 'GL_INDEX_MATERIAL_EXT',
           'GL_NORMAL_ARRAY_BUFFER_BINDING_ARB', 'GLU_NURBS_ERROR32',
           'GL_SECONDARY_COLOR_ARRAY_EXT', 'GL_UNPACK_RESAMPLE_OML',
           'GL_CURRENT_VERTEX_EXT', 'GL_BLEND_EQUATION_RGB',
           'GL_UNSIGNED_INT_8_8_8_8_EXT', 'GL_ALPHA_FLOAT16_APPLE',
           'GLUT_CURSOR_TOP_SIDE', 'glMultiTexCoord1fARB',
           'GL_RASTERIZER_DISCARD_NV', 'GL_TEXTURE_MAX_LEVEL',
           'GL_ACCUM_RED_BITS', 'glutGetWindow',
           'GL_TEXTURE_COMPARE_FUNC_ARB', 'glCopyColorSubTable',
           'GL_TEXTURE_CUBE_MAP_POSITIVE_X',
           'GL_UNSIGNED_INT_SAMPLER_2D_ARRAY_EXT', 'glutDisplayFunc',
           'GL_CLAMP_VERTEX_COLOR_ARB', 'GL_STENCIL_BUFFER',
           'GL_ALPHA8', 'GL_GEOMETRY_PROGRAM_PARAMETER_BUFFER_NV',
           'GL_TEXTURE_CUBE_MAP_POSITIVE_Z', 'GLUT_KEY_F5',
           'GL_FRAGMENT_COLOR_EXT', 'GLU_UNKNOWN',
           'GL_TEXTURE_APPLICATION_MODE_EXT',
           'GL_PROGRAM_ATTRIBS_ARB',
           'GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY',
           'GL_STENCIL_CLEAR_TAG_VALUE_EXT', 'GL_MODELVIEW28_ARB',
           'GL_ALPHA4', 'GL_MAX_GEOMETRY_OUTPUT_COMPONENTS',
           'glutGetModeValues', 'GL_R1UI_C4F_N3F_V3F_SUN',
           'GL_CONSTANT_COLOR1_NV', 'GL_RENDER_MODE',
           'GL_UNPACK_CONSTANT_DATA_SUNX', 'GL_LINE',
           'glCopyTexImage2D',
           'GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT5_EXT',
           'GL_LUMINANCE16_EXT', 'GL_DRAW_BUFFER4_ATI',
           'GL_SAMPLER_2D_MULTISAMPLE', 'GL_TEXTURE21_ARB',
           'GL_MATRIX3_NV', 'GLU_OBJECT_PARAMETRIC_ERROR_EXT',
           'GL_REG_5_ATI', 'GL_OUTPUT_TEXTURE_COORD19_EXT',
           'GL_YCBCR_422_APPLE', 'GL_POINT_FADE_THRESHOLD_SIZE_ARB',
           'GL_RGBA32UI_EXT', 'GLUT_VIDEO_RESIZE_X_DELTA',
           'GL_CONVOLUTION_FILTER_SCALE', 'GL_BLUE_INTEGER',
           'GL_OUTPUT_TEXTURE_COORD18_EXT', 'GL_CONVOLUTION_2D',
           'GL_DYNAMIC_COPY', 'GL_GEOMETRY_PROGRAM_NV',
           'GL_SYNC_FLAGS', 'GL_SAMPLE_MASK_VALUE_NV',
           'GL_PATCH_DEFAULT_OUTER_LEVEL', 'GL_SHADER_CONSISTENT_NV',
           'GL_ZOOM_Y', 'GL_MAX_TEXTURE_IMAGE_UNITS_ARB',
           'GL_STENCIL_PASS_DEPTH_FAIL',
           'GL_POST_TEXTURE_FILTER_BIAS_SGIX',
           'GL_UNSIGNED_BYTE_2_3_3_REV', 'GL_PROXY_COLOR_TABLE_SGI',
           'GL_COLOR_ARRAY_TYPE_EXT', 'GL_BOOL_VEC2_ARB',
           'GL_CLIENT_ACTIVE_TEXTURE', 'GL_RGBA_FLOAT16_APPLE',
           'GLUtriangulatorObj', 'GLubyte',
           'GL_BUFFER_FLUSHING_UNMAP_APPLE', 'GL_BUFFER_MAPPED_ARB',
           'GL_OPERAND2_ALPHA', 'GL_SAMPLE_ALPHA_TO_COVERAGE',
           'GL_FOG_DENSITY', 'GL_TEXTURE_CONSTANT_DATA_SUNX',
           'GL_CONSTANT_ATTENUATION', 'GL_EVAL_VERTEX_ATTRIB5_NV',
           'GL_DRAW_INDIRECT_BUFFER_BINDING',
           'GL_UNPACK_ROW_BYTES_APPLE', 'GL_CONVOLUTION_HINT_SGIX',
           'GL_ADD_SIGNED_ARB', 'GL_VERTEX_STREAM2_ATI',
           'GL_LUMINANCE_FLOAT32_APPLE', 'GL_HI_BIAS_NV',
           'GL_RESAMPLE_ZERO_FILL_OML',
           'GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING_ARB',
           'GL_EVAL_VERTEX_ATTRIB7_NV', 'GL_INT_VEC4_ARB',
           'GL_SAMPLES_SGIS', 'GL_DOT3_RGB', 'GL_HILO8_NV',
           'GL_CLAMP_READ_COLOR', 'GL_RED_INTEGER',
           'GL_VERTEX_ARRAY_STRIDE_EXT',
           'GL_DISTANCE_ATTENUATION_EXT', 'GL_COLOR_ATTACHMENT5',
           'GL_COLOR_ATTACHMENT4', 'GL_COLOR_ATTACHMENT7',
           'GL_COLOR_ATTACHMENT6', 'GL_COLOR_ATTACHMENT1',
           'GL_COLOR_ATTACHMENT0', 'GL_COLOR_ATTACHMENT3',
           'GL_COLOR_ATTACHMENT2',
           'GL_POST_COLOR_MATRIX_ALPHA_BIAS_SGI',
           'GLUT_JOYSTICK_BUTTONS', 'GL_COLOR_ATTACHMENT9',
           'GL_COLOR_ATTACHMENT8', 'GL_SOURCE1_RGB_ARB',
           'GL_MIRROR_CLAMP_ATI', 'glPolygonMode', 'GL_MATRIX5_NV',
           'GLU_TESS_WINDING_NEGATIVE', 'GL_INT_VEC2_ARB',
           'GL_READ_PIXEL_DATA_RANGE_LENGTH_NV', 'GL_DEPTH_WRITEMASK',
           'GL_PATCH_VERTICES', 'GL_CULL_FACE_MODE',
           'GL_POST_CONVOLUTION_COLOR_TABLE',
           'GL_TRANSFORM_FEEDBACK_BUFFER_BINDING',
           'GL_SAMPLER_1D_ARB', 'GL_PROGRAM_TARGET_NV',
           'GL_VERTEX_PROGRAM_PARAMETER_BUFFER_NV',
           'GL_POST_TEXTURE_FILTER_SCALE_RANGE_SGIX',
           'GL_MAX_PROGRAM_GENERIC_RESULTS_NV', 'GL_BOOL',
           'GL_PIXEL_TILE_CACHE_INCREMENT_SGIX',
           'GL_RGBA_INTEGER_MODE_EXT',
           'GL_POST_CONVOLUTION_BLUE_SCALE', 'GLUT_CURSOR_RIGHT_SIDE',
           'glLineStipple', 'GL_MODELVIEW25_ARB',
           'glMultiTexCoord4fvARB', 'GL_SIGNED_HILO8_NV',
           'GL_FRAGMENT_COLOR_MATERIAL_SGIX',
           'GL_QUAD_TEXTURE_SELECT_SGIS', 'GL_DOT3_RGB_EXT',
           'GL_TEXTURE_PRE_SPECULAR_HP', 'GLsizeiptrARB',
           'GL_COMBINE_RGB_EXT', 'GL_T2F_V3F', 'GL_STACK_OVERFLOW',
           'GL_MAX_PROGRAM_ALU_INSTRUCTIONS_ARB',
           'GL_FRAMEBUFFER_EXT', 'GL_MAX_PROGRAM_MATRICES_ARB',
           'GL_ALWAYS', 'GL_NORMAL_MAP',
           'GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT_ARB',
           'GL_MAP2_BINORMAL_EXT', 'glMultiTexCoord3dARB', 'GL_RGBA2',
           'GLU_NURBS_BEGIN_DATA_EXT', 'GL_SPRITE_AXIS_SGIX',
           'GL_TEXTURE_FILTER_CONTROL', 'GL_FLOAT_MAT3_ARB',
           'GLUT_WINDOW_DEPTH_SIZE', 'GL_POINT_SPRITE_COORD_ORIGIN',
           'GL_INTERLACE_SGIX', 'GL_POINT_SIZE_RANGE',
           'GL_HISTOGRAM_WIDTH', 'glutPostRedisplay',
           'glutSpaceballRotateFunc', 'GL_BLUE_BIAS', 'GL_GREEN_BIAS',
           'GL_IMAGE_SCALE_X_HP', 'GL_MAX_TEXTURE_COORDS',
           'GLU_NURBS_ERROR30', 'GL_DEBUG_TYPE_ERROR_ARB',
           'GL_DRAW_BUFFER10_ARB', 'GL_FIXED_ONLY',
           'GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE', 'glGetMapdv',
           'glutSolidCube', 'GL_DEBUG_SEVERITY_MEDIUM_AMD',
           'GL_RGBA32I_EXT', 'GL_MULTISAMPLE_BIT',
           'GL_MAX_PROGRAM_NATIVE_TEX_INDIRECTIONS_ARB',
           'GL_FRAGMENT_COLOR_MATERIAL_FACE_SGIX',
           'glGetConvolutionParameterfv',
           'GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_CONTROL_SHADER',
           'GL_FOG_COLOR', 'GL_MATRIX7_NV', 'glCopyTexSubImage3D',
           'GL_TEXTURE_LUMINANCE_TYPE', 'GL_RG16UI',
           'GL_SWIZZLE_STRQ_DQ_ATI', 'GL_DRAW_BUFFER12',
           'glutEnterGameMode', 'GL_SIGNED_INTENSITY_NV',
           'GLUT_CURSOR_BOTTOM_RIGHT_CORNER', 'glTexParameterf',
           'GL_COUNTER_TYPE_AMD', 'glGetHistogramParameteriv',
           'glTexParameteri', 'GL_PIXEL_TILE_CACHE_SIZE_SGIX',
           'GL_FOG_COORD_ARRAY_STRIDE', 'GL_VERTEX_STREAM0_ATI',
           'GL_PIXEL_GROUP_COLOR_SGIS', 'GL_STENCIL_BACK_REF',
           'GLclampf', 'GLbyte', 'GLclampd', 'GL_LINE_RESET_TOKEN',
           'GL_CON_9_ATI', 'GL_COMBINE_RGB',
           'GL_DEPTH_PASS_INSTRUMENT_COUNTERS_SGIX',
           'GL_TEXTURE0_ARB', 'GL_STEREO', 'GLUT_OVERLAY',
           'GL_ALREADY_SIGNALED', 'GL_STATIC_COPY_ARB', 'glColor4ub',
           'GL_VERTEX_PROGRAM_CALLBACK_FUNC_MESA',
           'GL_LIGHT_MODEL_LOCAL_VIEWER', 'GL_LINEAR_DETAIL_SGIS',
           'GL_VERTEX_STREAM3_ATI', 'glColor4ui',
           'GL_PROGRAM_STRING_ARB', 'GL_DISCARD_ATI', 'GL_MEDIUM_INT',
           'GL_LUMINANCE6_ALPHA2', 'glColor4us',
           'GL_PROXY_TEXTURE_2D_MULTISAMPLE_ARRAY',
           'GL_FRAMEBUFFER_DEFAULT', 'GL_CLIP_PLANE1',
           'GL_CLIP_PLANE0', 'GL_CLIP_PLANE3', 'GL_CLIP_PLANE2',
           'GL_CLIP_PLANE5', 'GL_CLIP_PLANE4',
           'GL_VERTEX_STREAM6_ATI',
           'GL_VIDEO_CAPTURE_SURFACE_ORIGIN_NV',
           'GL_UNPACK_IMAGE_HEIGHT', 'glGetString',
           'GL_PROXY_POST_CONVOLUTION_COLOR_TABLE_SGI',
           'GL_COLOR_INDEX16_EXT', 'GL_NORMAL_ARRAY_TYPE',
           'GL_TEXTURE_BUFFER', 'GL_OUTPUT_TEXTURE_COORD4_EXT',
           'GL_SAMPLER_CUBE_MAP_ARRAY_ARB',
           'GL_COLOR_ATTACHMENT10_EXT',
           'GL_TEXTURE_BINDING_RECTANGLE', 'glEdgeFlagPointer',
           'GL_CON_4_ATI', 'GL_POINTS', 'glCopyPixels',
           'GL_RENDERBUFFER_DEPTH_SIZE_EXT', 'GL_FRAMEZOOM_SGIX',
           'GL_LINEAR_CLIPMAP_NEAREST_SGIX', 'glDeleteTextures',
           'GL_RENDERBUFFER_BLUE_SIZE', 'GL_UNIFORM_NAME_LENGTH',
           'GLUT_CURSOR_UP_DOWN', 'GL_POLYGON', 'GL_SCISSOR_BOX',
           'GL_MAP1_INDEX', 'GL_COMBINER_SUM_OUTPUT_NV',
           'GL_LINE_WIDTH_GRANULARITY',
           'GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS_ARB',
           'GL_SAMPLES_PASSED_ARB', 'GL_VERTEX_ARRAY_BINDING_APPLE',
           'GL_OP_MUL_EXT', 'GL_SECONDARY_COLOR_ARRAY_ADDRESS_NV',
           'GL_ADD_SIGNED', 'GL_MAX_3D_TEXTURE_SIZE', 'GL_SELECT',
           'GL_PIXEL_FRAGMENT_RGB_SOURCE_SGIS', 'GLU_NURBS_ERROR15',
           'glMultiTexCoord3fARB',
           'GL_FRAGMENT_LIGHT_MODEL_LOCAL_VIEWER_SGIX',
           'GL_TEXTURE_CLIPMAP_LOD_OFFSET_SGIX', 'GLU_NURBS_ERROR11',
           'glutMenuDestroyFunc', 'GL_DONT_CARE',
           'GL_MODELVIEW17_ARB', 'GL_LUMINANCE_ALPHA_FLOAT32_APPLE',
           'GL_REG_18_ATI', 'GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING',
           'GLU_NURBS_ERROR19', 'GL_DEBUG_ASSERT_MESA',
           'GL_MAP_FLUSH_EXPLICIT_BIT', 'GL_UNSIGNED_SHORT',
           'GL_POST_COLOR_MATRIX_GREEN_SCALE_SGI', 'glRenderMode',
           'GL_CURRENT_VERTEX_WEIGHT_EXT', 'GL_QUAD_STRIP',
           'glGetCompressedTexImage', 'GL_UNSIGNED_INT_VEC3_EXT',
           'GL_MAX_EXT', 'GL_SAMPLER_RENDERBUFFER_NV',
           'GL_RENDERBUFFER_STENCIL_SIZE', 'GL_TRIANGLE_MESH_SUN',
           'GL_UNIFORM_BLOCK_BINDING',
           'GL_LOCAL_CONSTANT_DATATYPE_EXT', 'GL_Z_EXT',
           'GL_FLOAT_MAT4_ARB', 'GLint64EXT', 'GL_RGBA_FLOAT32_APPLE',
           'GL_RETURN', 'GL_DYNAMIC_READ_ARB', 'GL_LEQUAL',
           'GL_INTENSITY16F_ARB',
           'GL_FRAMEBUFFER_INCOMPLETE_FORMATS_EXT',
           'GL_DISTANCE_ATTENUATION_SGIS',
           'GL_NEAREST_CLIPMAP_NEAREST_SGIX',
           'GL_MAX_CONVOLUTION_HEIGHT', 'GL_COMBINE_ARB',
           'GL_UNSIGNED_INVERT_NV', 'GL_PIXEL_MAP_A_TO_A_SIZE',
           'GL_RGBA_S3TC', 'GL_LIGHT_MODEL_AMBIENT', 'glGetTexEnvfv',
           'GL_INTERPOLATE_ARB', 'glCullFace',
           'GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_EXT',
           'GL_VERTEX_ARRAY_SIZE_EXT', 'GL_GEOMETRY_SHADER_EXT',
           'GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_ARB',
           'GL_TEXTURE_COMPRESSION_HINT',
           'GL_TEXTURE_COORD_ARRAY_LENGTH_NV',
           'GL_WIDE_LINE_HINT_PGI',
           'GL_FRAGMENT_COLOR_MATERIAL_PARAMETER_SGIX',
           'GL_REPLACEMENT_CODE_ARRAY_TYPE_SUN', 'GL_FLOAT16_VEC4_NV',
           'GL_CURRENT_VERTEX_ATTRIB', 'GL_MAP1_VERTEX_ATTRIB0_4_NV',
           'GL_OP_FRAC_EXT', 'GL_SPARE1_NV', 'glutStrokeWidth',
           'GL_SCALE_BY_TWO_NV', 'GL_MATRIX10_ARB',
           'GL_PRIMARY_COLOR', 'GL_C3F_V3F',
           'GL_TRANSFORM_FEEDBACK_BUFFER_PAUSED_NV',
           'GL_OP_EXP_BASE_2_EXT', 'GL_COMBINER_BIAS_NV',
           'glutVideoPan', 'GLU_PARAMETRIC_ERROR', 'GL_AUX_BUFFERS',
           'GL_UNSIGNED_INT_10_10_10_2', 'GL_CON_17_ATI',
           'GL_OPERAND2_RGB_ARB', 'GL_IMPLEMENTATION_COLOR_READ_TYPE',
           'GL_IMAGE_3D_EXT', 'GL_UNSIGNED_SHORT_4_4_4_4_REV',
           'GL_CON_24_ATI', 'GL_INT_SAMPLER_2D_EXT', 'GL_SMOOTH',
           'GL_REG_16_ATI', 'GL_FLOAT16_VEC2_NV', 'GL_DISCARD_NV',
           'GL_MAX_UNIFORM_BLOCK_SIZE', 'GLUT_RENDERING_CONTEXT',
           'GL_MODELVIEW27_ARB', 'GL_FRAGMENT_PROGRAM_ARB',
           'GL_VIBRANCE_SCALE_NV', 'glTexEnvfv',
           'GL_CURRENT_TEXTURE_COORDS', 'GL_STATIC_READ',
           'GL_LUMINANCE8I_EXT', 'GL_VERTEX_ATTRIB_MAP2_APPLE',
           'glutGetColor', 'GL_SHADOW_AMBIENT_SGIX',
           'GLUT_GAME_MODE_PIXEL_DEPTH',
           'GL_TEXTURE_DEFORMATION_SGIX',
           'GL_STRICT_DEPTHFUNC_HINT_PGI',
           'GL_MAX_COLOR_ATTACHMENTS_EXT', 'GL_VERSION_2_1',
           'GL_IMAGE_BINDING_LEVEL_EXT', 'glLightModelfv',
           'GLUT_VIDEO_RESIZE_Y', 'GL_BOOL_VEC3_ARB',
           'GL_MATRIX25_ARB', 'GL_ASYNC_HISTOGRAM_SGIX',
           'GL_CONVOLUTION_2D_EXT', 'glConvolutionParameteri',
           'GLhalfARB', 'GL_VERTEX_PROGRAM_TWO_SIDE_NV',
           'GL_VIEWPORT_BOUNDS_RANGE', 'GLU_NURBS_ERROR5',
           'GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION',
           'glConvolutionParameterf', 'GLUT_KEY_F1',
           'GL_LUMINANCE_ALPHA16F_ARB',
           'GL_SHARED_TEXTURE_PALETTE_EXT',
           'GL_ACTIVE_STENCIL_FACE_EXT', 'GL_LUMINANCE_ALPHA',
           'GL_MAX_CONVOLUTION_WIDTH',
           'GL_MAX_TRACK_MATRIX_STACK_DEPTH_NV',
           'GL_PIXEL_UNPACK_BUFFER_BINDING', 'GL_HILO_NV',
           'GL_DRAW_BUFFER9_ATI', 'GLUT_VIDEO_RESIZE_X',
           'GL_COMPRESSED_INTENSITY', 'GLUT_CURSOR_RIGHT_ARROW',
           'glVertex4s', 'GL_SCREEN_COORDINATES_REND',
           'GL_PIXEL_PACK_BUFFER_BINDING_ARB',
           'GL_ELEMENT_ARRAY_LENGTH_NV', 'GL_TRANSPOSE_NV',
           'GL_VERTEX_STREAM5_ATI',
           'GL_TRANSFORM_FEEDBACK_BUFFER_BINDING_NV',
           'GL_MAT_EMISSION_BIT_PGI', 'GL_TEXTURE_COMPARE_FUNC',
           'glGetMinmaxParameterfv', 'GL_SPOT_DIRECTION',
           'GL_COMPRESSED_SIGNED_RG_RGTC2', 'glVertex4d',
           'GL_VERTEX_ATTRIB_ARRAY_STRIDE_ARB', 'GL_CURRENT_COLOR',
           'glVertex4i', 'GL_PIXEL_TEX_GEN_ALPHA_MS_SGIX',
           'GL_DSDT8_MAG8_NV', 'GL_SAMPLER_2D_ARB',
           'GL_COMPRESSED_RED_RGTC1_EXT',
           'GL_INVALID_FRAMEBUFFER_OPERATION', 'GLintptr',
           'GL_RGB_INTEGER_EXT', 'GL_MAX_TRANSFORM_FEEDBACK_BUFFERS',
           'GL_INT_IMAGE_2D_MULTISAMPLE_EXT',
           'GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING',
           'GL_DEPTH32F_STENCIL8', 'GL_MAX_ARRAY_TEXTURE_LAYERS',
           'GL_DT_BIAS_NV', 'GL_UNIFORM_IS_ROW_MAJOR',
           'GL_IMAGE_MAG_FILTER_HP', 'GL_MAX_SERVER_WAIT_TIMEOUT',
           'GL_POST_COLOR_MATRIX_ALPHA_SCALE',
           'GL_UNSIGNED_INT_2_10_10_10_REV',
           'GL_MODULATE_SUBTRACT_ATI', 'glAlphaFunc', 'GL_NOR',
           'GL_DEPENDENT_RGB_TEXTURE_3D_NV', 'GL_FLAT',
           'GL_DU8DV8_ATI', 'GL_PACK_ALIGNMENT',
           'GL_DRAW_BUFFER6_ATI', 'GL_RGBA8UI_EXT', 'glStencilFunc',
           'GLU_NURBS_VERTEX_EXT', 'glTexCoord3dv',
           'GLUT_CURSOR_LEFT_SIDE',
           'GL_VERTEX_ARRAY_STORAGE_HINT_APPLE', 'GL_RGB2_EXT',
           'GL_UNPACK_LSB_FIRST', 'glutSetIconTitle',
           'GL_QUAD_LUMINANCE4_SGIS', 'GLU_NURBS_END',
           'GL_SAMPLE_MASK_VALUE', 'GL_SOURCE1_RGB',
           'GL_CONSTANT_BORDER', 'GL_STRICT_LIGHTING_HINT_PGI',
           'GL_UNSIGNED_INT_VEC4_EXT',
           'GL_CURRENT_FOG_COORDINATE_EXT', 'GL_ACTIVE_TEXTURE',
           'GL_POST_CONVOLUTION_BLUE_BIAS_EXT', 'GLUT_ACTIVE_SHIFT',
           'GL_ALPHA_INTEGER', 'GL_GREEN_SCALE', 'GL_OR_REVERSE',
           'GL_MATRIX17_ARB', 'GL_PROJECTION', 'GL_DEPTH_FUNC',
           'GL_UNSIGNED_INT_SAMPLER_3D', 'glRasterPos2iv', 'GL_RGBA',
           'GLUT_KEY_F2', 'GL_COLOR_INDEX4_EXT', 'GL_INT_VEC3',
           'GL_ELEMENT_ARRAY_ADDRESS_NV', 'GLUT_WINDOW_FORMAT_ID',
           'GLU_TESS_WINDING_NONZERO', 'GL_STENCIL_FAIL',
           'GL_DOUBLEBUFFER', 'GL_VERSION_4_0', 'GL_VERSION_4_1',
           'GLU_TESS_COMBINE_DATA', 'GL_COLOR_TABLE',
           'GL_SAMPLE_MASK_INVERT_SGIS',
           'GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER_EXT',
           'GL_PACK_SKIP_IMAGES_EXT', 'glPushAttrib',
           'GL_FRAMEBUFFER_UNSUPPORTED', 'GL_RED_BIAS',
           'GL_COMBINER_INPUT_NV',
           'GL_MAX_PROGRAM_NATIVE_INSTRUCTIONS_ARB',
           'GL_SOURCE3_ALPHA_NV', 'GL_SRC0_RGB',
           'GL_MAX_PROGRAM_LOOP_COUNT_NV', 'GL_PROGRAM_LENGTH_ARB',
           'glLightiv', 'GLushort',
           'GL_EDGE_FLAG_ARRAY_BUFFER_BINDING',
           'GL_MAX_CUBE_MAP_TEXTURE_SIZE',
           'GL_OFFSET_HILO_TEXTURE_RECTANGLE_NV',
           'GL_CONSTANT_COLOR_EXT', 'GL_RENDERBUFFER_WIDTH',
           'GLUT_NORMAL_DAMAGED', 'GL_DUAL_LUMINANCE12_SGIS',
           'GL_STENCIL_BACK_VALUE_MASK',
           'GL_MAP2_VERTEX_ATTRIB13_4_NV', 'GL_STORAGE_CACHED_APPLE',
           'GL_TEXTURE_BLUE_SIZE', 'GL_HISTOGRAM_GREEN_SIZE',
           'GL_FLOAT16_NV', 'GL_OFFSET_TEXTURE_RECTANGLE_SCALE_NV',
           'GL_RESTART_SUN', 'glutReshapeFunc',
           'GL_POINT_SIZE_MIN_SGIS',
           'GL_COLOR_ARRAY_PARALLEL_POINTERS_INTEL', 'glScissor',
           'GL_REG_19_ATI', 'glGetBooleanv', 'GL_VERTEX_SHADER',
           'glMaterialfv', 'GL_DOT_PRODUCT_AFFINE_DEPTH_REPLACE_NV',
           'GL_DRAW_BUFFER10', 'GL_DRAW_BUFFER11', 'GLUTproc',
           'GL_DRAW_BUFFER13', 'GL_DRAW_BUFFER14', 'GL_DRAW_BUFFER15',
           'GL_RGB12_EXT', 'GL_RGB_INTEGER',
           'GL_TEXTURE_LOD_BIAS_S_SGIX', 'GL_SUBTRACT_ARB',
           'GL_TEXTURE_COORD_ARRAY_POINTER_EXT',
           'glutPassiveMotionFunc', 'GL_EDGEFLAG_BIT_PGI',
           'GLUT_DOUBLE', 'GL_BLUE_INTEGER_EXT', 'GLUT_WINDOW_STEREO',
           'GL_CONSTANT_ALPHA', 'GL_MAX_VERTEX_SHADER_INVARIANTS_EXT',
           'GL_VERTEX_ARRAY_RANGE_VALID_NV', 'GL_R16I',
           'GL_ASYNC_READ_PIXELS_SGIX', 'GL_IMAGE_BINDING_ACCESS_EXT',
           'GLU_TESS_WINDING_POSITIVE', 'GL_YCRCB_444_SGIX',
           'GL_RGB32F_ARB', 'glColor4dv', 'GL_DUDV_ATI',
           'GL_TEXTURE_RED_SIZE_EXT', 'GL_PIXEL_MAP_A_TO_A',
           'GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER',
           'GL_COMPARE_R_TO_TEXTURE', 'GL_DEPTH_BOUNDS_EXT',
           'GL_PREVIOUS', 'GL_ACTIVE_VARYING_MAX_LENGTH_NV',
           'GL_ALPHA_SNORM', 'GL_MAX_IMAGE_SAMPLES_EXT',
           'GL_PROXY_COLOR_TABLE', 'GL_TEXTURE_DEFORMATION_BIT_SGIX',
           'GL_PIXEL_UNPACK_BUFFER_ARB', 'GL_PIXEL_COUNT_NV',
           'GL_MATRIX9_ARB', 'GL_INTENSITY_FLOAT16_APPLE',
           'GL_IMAGE_CUBE_MAP_ARRAY_EXT', 'GL_DIFFUSE',
           'GL_TEXTURE_CLIPMAP_OFFSET_SGIX',
           'GL_OUTPUT_TEXTURE_COORD15_EXT', 'GL_SOURCE2_RGB',
           'GL_QUERY_NO_WAIT', 'glNormal3iv',
           'GL_EYE_DISTANCE_TO_POINT_SGIS', 'GL_TEXTURE_3D_EXT',
           'GL_READ_PIXEL_DATA_RANGE_POINTER_NV', 'GL_TEXTURE_GEN_T',
           'GL_MAX_VERTEX_SHADER_VARIANTS_EXT',
           'GL_MAX_ELEMENTS_VERTICES_EXT',
           'GL_OBJECT_INFO_LOG_LENGTH_ARB',
           'GL_VERTEX_ATTRIB_ARRAY4_NV', 'GL_TEXTURE_GEN_R',
           'GL_MODELVIEW23_ARB', 'GL_MAX_RENDERBUFFER_SIZE',
           'GL_FRAGMENT_PROGRAM_PARAMETER_BUFFER_NV',
           'GL_NEXT_VIDEO_CAPTURE_BUFFER_STATUS_NV', 'glColor3uiv',
           'GL_INCR_WRAP', 'GL_RENDERBUFFER_ALPHA_SIZE',
           'GLU_TESS_TOLERANCE', 'GL_HIGH_INT', 'GL_TEXTURE16',
           'GL_MODELVIEW15_ARB', 'GL_TEXTURE_GREEN_TYPE_ARB',
           'GL_LIGHT_MODEL_TWO_SIDE', 'glListBase',
           'glMultiTexCoord1iARB', 'GL_OP_SET_LT_EXT',
           'GL_MAP2_VERTEX_ATTRIB6_4_NV', 'GL_TEXTURE_2D_BINDING_EXT',
           'GL_MAX_CONVOLUTION_WIDTH_EXT', 'GL_COMPILE',
           'GL_SAMPLE_POSITION', 'GL_STORAGE_PRIVATE_APPLE',
           'GL_SHADING_LANGUAGE_VERSION',
           'GL_GUILTY_CONTEXT_RESET_ARB',
           'GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS_NV',
           'GL_INCR', 'GL_MAX_RECTANGLE_TEXTURE_SIZE',
           'GL_T2F_IUI_V2F_EXT', 'GL_ALPHA_TEST_REF',
           'GL_MAP_ATTRIB_V_ORDER_NV', 'GL_UNPACK_SKIP_ROWS',
           'GL_TRUE', 'GL_PROGRAM_ERROR_STRING_ARB',
           'GL_COLOR_ALPHA_PAIRING_ATI', 'GLUT_JOYSTICK_POLL_RATE',
           'GL_UNPACK_SUBSAMPLE_RATE_SGIX',
           'GL_EVAL_VERTEX_ATTRIB12_NV', 'GL_DEPTH_CLAMP',
           'GL_DRAW_BUFFER13_ATI', 'GL_RGB4_EXT',
           'GL_BLEND_DST_ALPHA', 'GL_VERSION_3_2',
           'GL_INT_SAMPLER_CUBE', 'GL_DECR_WRAP',
           'GL_POINT_SPRITE_R_MODE_NV', 'GL_CURRENT_QUERY',
           'GL_COLOR_ATTACHMENT10', 'GL_DRAW_BUFFER3_ATI', 'GL_EXP2',
           'GL_MAX_PROGRAM_ATTRIB_COMPONENTS_NV', 'GL_RGB16UI',
           'GL_COPY_INVERTED', 'GL_DEPTH_CLAMP_NV',
           'GLUT_KEY_REPEAT_ON', 'GL_FRAGMENT_LIGHT6_SGIX',
           'GL_MATRIX8_ARB', 'GL_LOWER_LEFT',
           'GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT3_EXT',
           'GL_SECONDARY_COLOR_ARRAY_TYPE_EXT',
           'GL_DEBUG_CATEGORY_API_ERROR_AMD',
           'GL_VERTEX_ATTRIB_ARRAY_LENGTH_NV', 'GL_INDEX_ARRAY_EXT',
           'glFeedbackBuffer', 'glCopyTexSubImage1D', 'glTexCoord1i',
           'glTexCoord1d', 'GL_FOG_COORDINATE_ARRAY_EXT',
           'glTexCoord1f', 'GL_UNDEFINED_VERTEX',
           'GL_NATIVE_GRAPHICS_HANDLE_PGI', 'GL_MATRIX1_ARB',
           'GL_PIXEL_MAP_G_TO_G_SIZE', 'GL_PIXEL_UNPACK_BUFFER',
           'GL_CONSTANT_COLOR0_NV', 'GL_TEXTURE_FILTER4_SIZE_SGIS',
           'GL_REG_20_ATI', 'glutGet', 'GL_INT8_VEC3_NV',
           'GL_LOCAL_CONSTANT_VALUE_EXT',
           'GL_POINT_DISTANCE_ATTENUATION',
           'GL_TEXTURE_BUFFER_DATA_STORE_BINDING',
           'GL_UNSIGNED_BYTE_3_3_2_EXT', 'GL_OPERAND0_ALPHA_ARB',
           'glDrawRangeElements', 'glTexCoord1s',
           'GL_REPLACE_OLDEST_SUN', 'GL_MATRIX0_NV',
           'GL_MAX_VERTEX_SHADER_LOCAL_CONSTANTS_EXT',
           'GL_AMBIENT_AND_DIFFUSE', 'GL_TEXTURE_1D_BINDING_EXT',
           'GL_FRAGMENT_SHADER', 'GL_TRIANGLES_ADJACENCY_ARB',
           'glColor3bv', 'GL_MATRIX7_ARB', 'GL_CON_27_ATI',
           'GL_UNSIGNED_INT_24_8_MESA', 'GL_ZERO',
           'GL_TRANSPOSE_MODELVIEW_MATRIX', 'GL_ELEMENT_ARRAY_BUFFER',
           'GL_CONTEXT_CORE_PROFILE_BIT', 'GLU_FALSE',
           'GL_BUFFER_MAP_LENGTH', 'GL_TRANSFORM_FEEDBACK_ATTRIBS_NV',
           'GL_IMAGE_MIN_FILTER_HP',
           'GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCALS_EXT',
           'GL_MAP1_GRID_DOMAIN', 'GL_RETAINED_APPLE',
           'glutVideoResizeGet', 'GL_INVARIANT_EXT',
           'GL_HALF_BIAS_NORMAL_NV', 'GL_FIXED',
           'GL_DEBUG_SOURCE_THIRD_PARTY_ARB',
           'GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS',
           'GL_TEXTURE_CUBE_MAP_POSITIVE_Y_ARB', 'GL_CON_16_ATI',
           'GLUT_OVERLAY_DAMAGED', 'GL_FLOAT_RGB16_NV',
           'GL_SAMPLE_COVERAGE_VALUE_ARB', 'GL_OPERAND1_ALPHA_ARB',
           'GL_T2F_C3F_V3F', 'GL_TEXTURE10', 'GL_FLOAT_RGBA16_NV',
           'glClearAccum', 'GL_COMPRESSED_RED', 'GL_BGR',
           'GL_RESAMPLE_REPLICATE_SGIX', 'GL_TEXTURE_2D',
           'GL_MAX_LIGHTS', 'GL_RGBA16_SNORM',
           'GL_TEXTURE_BINDING_1D_ARRAY', 'GL_SAMPLER_2D_ARRAY_EXT',
           'GL_RGB16F_ARB', 'GL_COMBINER_MUX_SUM_NV',
           'GL_MAX_VIEWPORT_DIMS', 'GL_LIST_INDEX', 'GL_OP_RECIP_EXT',
           'GL_FRAGMENT_NORMAL_EXT', 'GL_FOG_COORDINATE_SOURCE',
           'GL_TEXTURE_BORDER_COLOR', 'glMap2d', 'glMap2f',
           'GL_PROXY_TEXTURE_1D_EXT', 'GL_MATRIX31_ARB',
           'GL_RGB_FLOAT32_ATI',
           'GL_MAX_GEOMETRY_OUTPUT_VERTICES_EXT',
           'GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY',
           'GL_TABLE_TOO_LARGE_EXT',
           'GL_TRANSPOSE_TEXTURE_MATRIX_ARB',
           'GL_TEXTURE_BUFFER_FORMAT_ARB',
           'GL_MAX_PROGRAM_NATIVE_PARAMETERS_ARB', 'glIsEnabled',
           'GL_ALPHA_MIN_CLAMP_INGR', 'glGetError', 'glGetTexEnviv',
           'GL_COMPILE_STATUS', 'GL_LOGIC_OP_MODE',
           'GLUT_WINDOW_RED_SIZE', 'GL_PREVIOUS_TEXTURE_INPUT_NV',
           'glEvalCoord1d', 'glGetTexLevelParameterfv',
           'glEvalCoord1f', 'GL_ALPHA_FLOAT32_APPLE',
           'glutBitmapString', 'GL_DUAL_INTENSITY4_SGIS',
           'GL_SIGNED_RGB_UNSIGNED_ALPHA_NV',
           'GL_OBJECT_ACTIVE_UNIFORM_MAX_LENGTH_ARB',
           'glGetPixelMapusv', 'GLUquadricObj', 'glutVideoResize',
           'glAccum', 'GL_UNSIGNED_BYTE', 'GLuint64EXT',
           'GL_TESSELLATION_MODE_AMD', 'GL_INT_SAMPLER_BUFFER_EXT',
           'GL_OUTPUT_TEXTURE_COORD7_EXT',
           'GL_TEXTURE_MATERIAL_PARAMETER_EXT',
           'GL_UNSIGNED_INT_5_9_9_9_REV', 'glTexCoord2iv',
           'GLUT_FORCE_INDIRECT_CONTEXT', 'GL_R16',
           'GL_DRAW_BUFFER0_ATI', 'GL_SIGNED_RGBA_NV', 'GL_RGB16_EXT',
           'GL_PIXEL_PACK_BUFFER', 'glStencilMask',
           'GL_PACK_LSB_FIRST', 'GL_VERSION_1_3', 'GL_VERSION_1_2',
           'GL_TEXTURE_LOD_BIAS_T_SGIX', 'GL_OUTPUT_FOG_EXT',
           'GLUT_VISIBLE', 'glPointSize',
           'GL_HISTOGRAM_ALPHA_SIZE_EXT', 'GL_UNSIGNED_BYTE_3_3_2',
           'GL_IMAGE_ROTATE_ORIGIN_Y_HP', 'GLU_NURBS_TESSELLATOR_EXT',
           'GL_PROXY_TEXTURE_CUBE_MAP_ARRAY_ARB',
           'GL_CURRENT_MATRIX_NV', 'GL_DRAW_BUFFER2',
           'GL_MAX_VERTEX_BINDABLE_UNIFORMS_EXT',
           'GL_TEXTURE_WRAP_R_EXT',
           'GL_TRANSFORM_FEEDBACK_BUFFER_SIZE', 'GL_DRAW_BUFFER',
           'glutExit', 'glMultiTexCoord1dvARB',
           'GLU_NURBS_NORMAL_DATA_EXT', 'GL_VERSION_3_0',
           'GL_VERSION_3_3', 'GL_COPY_PIXEL_TOKEN', 'glRectsv',
           'GL_STENCIL_INDEX4', 'GL_POINT_FADE_THRESHOLD_SIZE',
           'GL_PIXEL_FRAGMENT_ALPHA_SOURCE_SGIS',
           'GL_PROGRAM_RESIDENT_NV',
           'GL_MAX_COLOR_MATRIX_STACK_DEPTH', 'GL_DEPTH_BITS',
           'GL_RASTER_POSITION_UNCLIPPED_IBM', 'GL_RGB8UI',
           'GL_TEXTURE27_ARB', 'GL_STENCIL_INDEX16',
           'GL_POINT_SIZE_GRANULARITY', 'glMultiTexCoord1fvARB',
           'GL_ATOMIC_COUNTER_BARRIER_BIT_EXT', 'glutStrokeCharacter',
           'GL_POST_COLOR_MATRIX_COLOR_TABLE', 'GLUT_CURSOR_INHERIT',
           'GL_DOT_PRODUCT_TEXTURE_2D_NV', 'GL_MATRIX6_NV',
           'GL_OP_DOT4_EXT', 'GLUT_WINDOW_RGBA', 'GLUT_LEFT',
           'glGetTexGeniv', 'GL_BLEND_DST_RGB', 'GL_EQUIV',
           'GL_MIRROR_CLAMP_TO_EDGE_ATI', 'GL_MAP1_VERTEX_3',
           'GL_VERTEX_ARRAY_COUNT_EXT', 'GL_RED_INTEGER_EXT',
           'GL_CLEAR', 'GLU_TESS_WINDING_ABS_GEQ_TWO', 'GL_LIGHT7',
           'GL_CURRENT_RASTER_POSITION_VALID',
           'GL_BUMP_NUM_TEX_UNITS_ATI', 'GL_HISTOGRAM_LUMINANCE_SIZE',
           'GL_MATRIX_MODE', 'GL_COLOR_ATTACHMENT3_EXT', 'GL_LIGHT6',
           'GL_PACK_IMAGE_DEPTH_SGIS', 'GL_PIXEL_PACK_BUFFER_BINDING',
           'GLUT_AUX1', 'GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT_ARB',
           'GL_UNPACK_ALIGNMENT', 'GL_INT_IMAGE_1D_ARRAY_EXT',
           'GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS',
           'GL_TEXTURE_BINDING_2D_MULTISAMPLE', 'GL_VARIABLE_E_NV',
           'GL_POINT_SIZE_MAX_ARB', 'GLUT_KEY_RIGHT',
           'GL_FLOAT16_VEC3_NV', 'GL_UNSIGNED_INT_IMAGE_2D_EXT',
           'GL_IMAGE_BINDING_FORMAT_EXT', 'GL_TEXTURE_BINDING_2D',
           'GL_TEXTURE_BUFFER_DATA_STORE_BINDING_EXT',
           'GL_VARIABLE_B_NV', 'GLU_VERSION_1_1',
           'GL_PROXY_POST_CONVOLUTION_COLOR_TABLE', 'GLU_VERSION_1_3',
           'GL_MAP2_VERTEX_ATTRIB14_4_NV', 'GL_RED_MIN_CLAMP_INGR',
           'GL_VIEWPORT_SUBPIXEL_BITS',
           'GLU_TESS_NEED_COMBINE_CALLBACK',
           'GL_VERTEX_ATTRIB_ARRAY_SIZE_ARB', 'GLU_TESS_ERROR1',
           'GL_RGBA16_EXT', 'GL_MODELVIEW1_MATRIX_EXT',
           'GL_UNSIGNED_INT_10F_11F_11F_REV_EXT',
           'GL_TEXTURE_CUBE_MAP_SEAMLESS', 'GLU_TESS_ERROR6',
           'GLU_TESS_ERROR7', 'GL_TEXTURE15_ARB',
           'GL_CALLIGRAPHIC_FRAGMENT_SGIX',
           'GL_OUTPUT_TEXTURE_COORD24_EXT',
           'GL_CURRENT_RASTER_POSITION', 'GLUT_XLIB_IMPLEMENTATION',
           'GL_VERTEX_ATTRIB_ARRAY_SIZE', 'GLU_INTERIOR',
           'GL_EVAL_VERTEX_ATTRIB15_NV',
           'GL_PROGRAM_NATIVE_ALU_INSTRUCTIONS_ARB', 'GLUT_RGB',
           'GL_TEXTURE28_ARB', 'GL_MATRIX6_ARB', 'GL_LINE_STIPPLE',
           'GL_CURRENT_WEIGHT_ARB', 'GL_SHADOW_ATTENUATION_EXT',
           'GL_TRIANGLE_LIST_SUN', 'GL_INVERSE_NV',
           'GL_POINT_FADE_THRESHOLD_SIZE_SGIS',
           'GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN_EXT',
           'GL_DOT_PRODUCT_DEPTH_REPLACE_NV', 'GL_FLOAT_VEC2',
           'glGetTexImage', 'GL_DRAW_INDIRECT_LENGTH_NV',
           'GL_FLOAT_VEC4', 'GL_R11F_G11F_B10F_EXT',
           'GL_FLOAT_RGB32_NV', 'GL_COEFF', 'GL_VERTEX_PROGRAM_ARB',
           'GL_SOURCE2_ALPHA', 'glGetMapfv',
           'GL_INSTRUMENT_MEASUREMENTS_SGIX',
           'GL_VERTEX_ATTRIB_MAP1_APPLE',
           'GL_MIN_PROGRAM_TEXEL_OFFSET', 'GL_BUFFER_SIZE',
           'GL_TRANSPOSE_PROJECTION_MATRIX_ARB',
           'GL_MAP1_VERTEX_ATTRIB9_4_NV', 'GL_STATIC_ATI',
           'GLUT_API_VERSION', 'GL_BUFFER_SIZE_ARB',
           'GL_COLOR_SUM_EXT', 'GL_MAX_GEOMETRY_INPUT_COMPONENTS',
           'GL_VARIABLE_D_NV', 'GL_RGBA4_S3TC',
           'GL_AUX_DEPTH_STENCIL_APPLE', 'GL_CLAMP_READ_COLOR_ARB',
           'glRasterPos2fv', 'GL_PROXY_HISTOGRAM_EXT',
           'GL_TEXTURE_DEPTH_EXT', 'GL_VARIABLE_C_NV',
           'GL_COLOR_MATERIAL', 'GL_MAX_TEXTURE_STACK_DEPTH',
           'GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_EXT',
           'GL_SEPARABLE_2D_EXT', 'GL_REG_21_ATI', 'GL_SLUMINANCE8',
           'GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_EXT',
           'GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS',
           'GL_LUMINANCE_ALPHA8I_EXT',
           'GL_MAX_DEFORMATION_ORDER_SGIX', 'GLUT_LAYER_IN_USE',
           'GL_TEXTURE_COORD_ARRAY_STRIDE',
           'GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER_EXT', 'GL_Q',
           'GL_R', 'GL_S', 'GL_T', 'GL_MAX_PROGRAM_LOOP_DEPTH_NV',
           'GL_VERTEX_ATTRIB_ARRAY_ENABLED', 'GL_DOUBLE',
           'GL_RG8_SNORM', 'GLeglImageOES', 'GL_STENCIL_BACK_FUNC',
           'GL_MATRIX26_ARB', 'GLUT_INDEX', 'glCopyTexSubImage2D',
           'GL_MAP_ATTRIB_U_ORDER_NV', 'glutReportErrors',
           'GL_INT_VEC2', 'GL_OP_RECIP_SQRT_EXT', 'GL_MAX_SAMPLES',
           'GL_CON_29_ATI', 'glTexCoord2fv', 'GL_COLOR',
           'GL_YCBYCR8_422_NV', 'GL_GEOMETRY_OUTPUT_TYPE_EXT',
           'GL_REG_14_ATI', 'GL_NOOP', 'GL_HISTOGRAM_ALPHA_SIZE',
           'GL_PIXEL_MIN_FILTER_EXT', 'glutSolidTorus',
           'GL_CONTEXT_FLAGS', 'GL_PROGRAM_LENGTH_NV',
           'GL_TEXCOORD3_BIT_PGI', 'GL_BLEND_DST_RGB_EXT',
           'GL_INTENSITY16_SNORM', 'GL_MATRIX24_ARB',
           'GL_ALL_SHADER_BITS', 'glutStrokeString',
           'GL_DRAW_BUFFER14_ARB', 'GL_TEXTURE_BINDING_1D',
           'GL_TABLE_TOO_LARGE', 'GL_SAMPLER_2D_MULTISAMPLE_ARRAY',
           'GLUT_JOYSTICK_BUTTON_B', 'GL_MATRIX27_ARB',
           'GL_POINT_SIZE_MAX', 'GL_POST_COLOR_MATRIX_GREEN_SCALE',
           'GL_MODELVIEW_MATRIX', 'GL_FIELD_LOWER_NV',
           'GL_QUERY_WAIT', 'GL_FOG_FUNC_SGIS',
           'GL_PROGRAM_OBJECT_ARB', 'GL_OUTPUT_TEXTURE_COORD2_EXT',
           'GL_VERTEX_SHADER_LOCALS_EXT', 'GL_LO_SCALE_NV',
           'GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_ARB',
           'GL_MULTISAMPLE_BIT_3DFX',
           'GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_ARB',
           'GL_TEXTURE_BINDING_1D_ARRAY_EXT',
           'GL_MAX_TEXTURE_LOD_BIAS', 'GL_FRAGMENT_LIGHT1_SGIX',
           'GL_ALIASED_LINE_WIDTH_RANGE',
           'GL_MAX_CUBE_MAP_TEXTURE_SIZE_EXT',
           'GL_SURFACE_REGISTERED_NV', 'GL_RGBA_INTEGER',
           'GL_FRAGMENT_MATERIAL_EXT',
           'GL_VIDEO_COLOR_CONVERSION_MATRIX_NV', 'GL_HISTOGRAM_EXT',
           'GLint', 'GL_TEXTURE_COORD_ARRAY_TYPE',
           'GL_TEXTURE_BINDING_CUBE_MAP_ARB',
           'GL_MAX_GEOMETRY_SHADER_INVOCATIONS',
           'GL_RENDERBUFFER_WIDTH_EXT', 'glutCloseFunc',
           'GL_IGNORE_BORDER_HP', 'GL_EDGE_FLAG_ARRAY_ADDRESS_NV',
           'glColor3sv', 'GL_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP',
           'GL_TEXTURE_FREE_MEMORY_ATI', 'GLU_OUTSIDE', 'GL_POINT',
           'GL_ALPHA16UI_EXT', 'GL_RESET_NOTIFICATION_STRATEGY_ARB',
           'GL_PIXEL_SUBSAMPLE_4242_SGIX', 'GL_POLYGON_TOKEN',
           'glVertex4sv', 'GL_SMOOTH_LINE_WIDTH_GRANULARITY',
           'GL_COMPRESSED_RGBA_FXT1_3DFX',
           'GL_BUFFER_UPDATE_BARRIER_BIT_EXT', 'GL_SRGB',
           'GL_NORMAL_ARRAY_POINTER', 'GL_LUMINANCE12_ALPHA12',
           'GL_MAX_COLOR_MATRIX_STACK_DEPTH_SGI',
           'GL_INT_IMAGE_CUBE_MAP_ARRAY_EXT',
           'GL_MAX_TESS_CONTROL_INPUT_COMPONENTS',
           'GL_EVAL_VERTEX_ATTRIB13_NV',
           'GL_POST_CONVOLUTION_ALPHA_BIAS', 'GL_REPLACE_MIDDLE_SUN',
           'GL_SCALE_BY_FOUR_NV', 'glDrawArrays', 'GLUT_MULTISAMPLE',
           'GL_UNSIGNED_INT_SAMPLER_2D_RECT',
           'GL_FOG_COORDINATE_ARRAY_POINTER_EXT', 'GLUT_AUX2',
           'GLUT_AUX3', 'GL_UNSIGNED_SHORT_8_8_MESA',
           'GL_REFERENCE_PLANE_SGIX', 'GL_LUMINANCE_ALPHA16UI_EXT',
           'glClear', 'glMultiTexCoord2dvARB',
           'GLUT_NUM_TABLET_BUTTONS', 'GL_ELEMENT_ARRAY_TYPE_APPLE',
           'GL_FOG_COORD_ARRAY_LENGTH_NV', 'GL_MUL_ATI',
           'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME',
           'GL_GEOMETRY_DEFORMATION_BIT_SGIX', 'GLUT_CURSOR_DESTROY',
           'GL_BLEND_SRC_ALPHA', 'GL_UNSIGNED_INT64_VEC2_NV',
           'GL_INTERPOLATE_EXT', 'GL_MAX_CLIPMAP_VIRTUAL_DEPTH_SGIX',
           'glTranslatef', 'glTranslated', 'GL_TEXTURE_GEN_MODE',
           'GL_AND_REVERSE', 'GL_MAX_INTEGER_SAMPLES',
           'GL_EVAL_VERTEX_ATTRIB11_NV', 'GL_CLAMP_FRAGMENT_COLOR',
           'glTexImage1D', 'GL_QUERY_RESULT_AVAILABLE',
           'GL_FORMAT_SUBSAMPLE_24_24_OML', 'GL_TEXTURE_RED_TYPE_ARB',
           'glutCreateMenu', 'GL_UNSIGNED_INT_24_8_EXT',
           'GL_FOG_MODE', 'GL_RGBA8_SNORM',
           'GL_POST_COLOR_MATRIX_RED_SCALE', 'GL_CLAMP_TO_EDGE_SGIS',
           'GL_COLOR3_BIT_PGI', 'glTexCoord4s',
           'GL_BUMP_TEX_UNITS_ATI', 'GLUT_CURSOR_FULL_CROSSHAIR',
           'GL_OBJECT_ACTIVE_ATTRIBUTES_ARB',
           'GL_MAX_COMBINED_IMAGE_UNITS_AND_FRAGMENT_OUTPUTS_EXT',
           'GL_AND', 'GL_ACTIVE_PROGRAM_EXT',
           'GL_IMAGE_2D_MULTISAMPLE_EXT', 'GL_BLUE_MIN_CLAMP_INGR',
           'GL_WRITE_DISCARD_NV', 'GL_PASS_THROUGH_NV',
           'GL_ACCUM_GREEN_BITS', 'glVertex3iv',
           'GL_LINE_STRIP_ADJACENCY_EXT', 'glTexGenfv',
           'GL_INT_SAMPLER_1D_ARRAY_EXT', 'glutTabletButtonFunc',
           'GL_COMPRESSED_SIGNED_RED_RGTC1_EXT', 'glMateriali',
           'glMultiTexCoord2svARB', 'GL_IUI_V2F_EXT',
           'GL_UNSIGNED_INT_10_10_10_2_EXT', 'GL_COORD_REPLACE_ARB',
           'GL_REG_26_ATI', 'GL_RGBA4',
           'GL_COMPRESSED_RED_GREEN_RGTC2_EXT', 'GL_INTENSITY12_EXT',
           'GL_ELEMENT_ARRAY_TYPE_ATI',
           'GL_EDGE_FLAG_ARRAY_POINTER_EXT', 'glMaterialf',
           'GL_FUNC_REVERSE_SUBTRACT_EXT', 'GL_RESAMPLE_AVERAGE_OML',
           'GL_VERTEX_ATTRIB_ARRAY_ADDRESS_NV',
           'GL_TEXTURE_CLIPMAP_FRAME_SGIX',
           'GL_TEXTURE_SHARED_SIZE_EXT',
           'GL_SYNC_GPU_COMMANDS_COMPLETE',
           'GL_SMOOTH_POINT_SIZE_RANGE', 'GL_MODELVIEW19_ARB',
           'GL_UNIFORM_BARRIER_BIT_EXT', 'GL_ALPHA_FLOAT16_ATI',
           'GL_ALIASED_POINT_SIZE_RANGE',
           'GL_TESS_CONTROL_SHADER_BIT', 'GL_COMPRESSED_SRGB_EXT',
           'GL_VERTEX_PROGRAM_TWO_SIDE_ARB', 'GLUT_WINDOW_PARENT',
           'GLU_NURBS_COLOR_EXT', 'GL_NEGATIVE_X_EXT',
           'GL_PRIMITIVE_ID_NV', 'GL_MAX_TEXTURE_IMAGE_UNITS_NV',
           'GL_MAX_NAME_STACK_DEPTH',
           'GL_MAX_PROGRAM_PARAMETER_BUFFER_SIZE_NV', 'GLUT_KEY_F3',
           'GL_ALPHA_MAX_SGIX', 'GL_GEOMETRY_VERTICES_OUT_EXT',
           'GL_MAX_GEOMETRY_OUTPUT_VERTICES', 'GL_MATRIX15_ARB',
           'GL_OPERAND1_RGB_EXT', 'GL_DEPTH_BUFFER_BIT',
           'glGetMinmaxParameteriv',
           'GL_VIDEO_COLOR_CONVERSION_OFFSET_NV',
           'GL_UNSIGNED_INT_SAMPLER_2D_RECT_EXT',
           'GL_MODELVIEW29_ARB',
           'GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING',
           'GL_DRAW_BUFFER12_ATI', 'GL_MATRIX_INDEX_ARRAY_ARB',
           'GL_PERTURB_EXT', 'GL_TEXTURE1_ARB',
           'GLUT_VIDEO_RESIZE_WIDTH', 'GL_FLOAT_CLEAR_COLOR_VALUE_NV',
           'GL_TANGENT_ARRAY_EXT',
           'GL_IMPLEMENTATION_COLOR_READ_FORMAT', 'glPolygonOffset',
           'GL_MAP2_VERTEX_ATTRIB10_4_NV', 'GL_MAX_SPOT_EXPONENT_NV',
           'GL_ARRAY_BUFFER_BINDING_ARB', 'GL_COLOR_TABLE_BIAS',
           'glutInitDisplayString', 'GL_FEEDBACK_BUFFER_SIZE',
           'GL_VARIANT_ARRAY_TYPE_EXT',
           'GL_TEXTURE_RENDERBUFFER_DATA_STORE_BINDING_NV',
           'GL_DEPTH_STENCIL_NV', 'GL_COMPRESSED_TEXTURE_FORMATS',
           'GL_PERFMON_RESULT_SIZE_AMD', 'GL_PROGRAM_SEPARABLE',
           'GL_DEBUG_SEVERITY_HIGH_ARB', 'GL_MODULATE_SIGNED_ADD_ATI',
           'GL_PIXEL_COUNT_AVAILABLE_NV', 'GL_DEPTH_COMPONENT24_ARB',
           'GL_MAT_COLOR_INDEXES_BIT_PGI',
           'GL_PRIMITIVES_GENERATED_EXT',
           'GL_TESS_CONTROL_OUTPUT_VERTICES', 'glMap1d', 'glMap1f',
           'GL_RGBA8', 'glMultiTexCoord3svARB',
           'GL_IMPLEMENTATION_COLOR_READ_TYPE_OES',
           'GL_QUAD_INTENSITY8_SGIS', 'glGetConvolutionParameteriv',
           'GL_STENCIL_INDEX1_EXT', 'GL_SAMPLER_2D_RECT_SHADOW',
           'GLU_NURBS_BEGIN_EXT', 'GL_POINT_TOKEN',
           'GL_T4F_C4F_N3F_V4F', 'glRasterPos3sv', 'GL_TEXTURE30',
           'GL_TEXTURE31', 'glutAttachMenu',
           'GL_UNSIGNED_INT_SAMPLER_1D', 'GL_VERTEX_ATTRIB_ARRAY9_NV',
           'GLUT_KEY_REPEAT_OFF', 'GLUT_RIGHT_BUTTON', 'GL_BACK_LEFT',
           'GLenum', 'GL_TEXTURE_ENV_COLOR', 'GL_BUFFER_MAP_POINTER',
           'GL_MAP1_VERTEX_ATTRIB11_4_NV', 'GLUT_SRGB',
           'GL_LINE_SMOOTH', 'GL_MAT_AMBIENT_AND_DIFFUSE_BIT_PGI',
           'GL_VARIABLE_G_NV', 'GL_OBJECT_ATTACHED_OBJECTS_ARB',
           'GLbitfield', 'GL_STENCIL_ATTACHMENT_EXT',
           'GL_STENCIL_REF', 'GL_LUMINANCE_ALPHA8UI_EXT',
           'GL_NORMAL_MAP_EXT', 'glLighti',
           'GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING_ARB',
           'GL_ALWAYS_FAST_HINT_PGI', 'GL_BLEND_EQUATION_RGB_EXT',
           'GLUT_WINDOW_NUM_CHILDREN', 'glLightf',
           'GL_COPY_WRITE_BUFFER', 'glutChangeToMenuEntry',
           'GL_INDEX_ARRAY_COUNT_EXT', 'GLU_INSIDE',
           'GL_OPERAND0_RGB', 'GL_MAX_TEXTURE_BUFFER_SIZE_ARB',
           'GL_NATIVE_GRAPHICS_BEGIN_HINT_PGI',
           'GL_LIGHT_MODEL_COLOR_CONTROL', 'GL_FEEDBACK',
           'GL_TEXCOORD1_BIT_PGI',
           'GL_WEIGHT_ARRAY_BUFFER_BINDING_ARB',
           'GL_UNSIGNED_INT8_NV', 'GL_MAX_ATTRIB_STACK_DEPTH',
           'GL_PIXEL_UNPACK_BUFFER_BINDING_EXT', 'GL_MODELVIEW13_ARB',
           'GL_FORCE_BLUE_TO_ONE_NV', 'glutGetMenuData',
           'GL_DUAL_LUMINANCE4_SGIS', 'GL_PIXEL_MAP_I_TO_G',
           'glutWireTorus', 'GL_TEXTURE29_ARB',
           'GL_REPLICATE_BORDER_HP', 'GL_DUAL_LUMINANCE_ALPHA8_SGIS',
           'GLint64', 'GL_PIXEL_MAP_I_TO_A', 'GLU_NURBS_ERROR34',
           'GL_OUTPUT_TEXTURE_COORD10_EXT',
           'GL_ACTIVE_SUBROUTINE_UNIFORM_LOCATIONS',
           'GL_FORMAT_SUBSAMPLE_244_244_OML', 'GL_OPERAND3_RGB_NV',
           'GL_POINT_SPRITE_NV', 'GLvdpauSurfaceNV',
           'GL_LINEAR_DETAIL_ALPHA_SGIS',
           'GL_MAX_3D_TEXTURE_SIZE_EXT',
           'GL_COLOR_ARRAY_BUFFER_BINDING', 'GL_R16F',
           'GL_QUAD_INTENSITY4_SGIS', 'GL_TEXTURE_MIN_LOD_SGIS',
           'GL_VERTEX_ARRAY_RANGE_LENGTH_APPLE', 'GL_MODELVIEW1_ARB',
           'GL_INT64_NV', 'GL_OP_LOG_BASE_2_EXT', 'GL_REG_9_ATI',
           'GLUT_TRY_DIRECT_CONTEXT', 'GL_SOURCE2_ALPHA_ARB',
           'GL_EDGE_FLAG_ARRAY_STRIDE', 'glMapGrid2d',
           'glutJoystickGetSaturation', 'glMapGrid2f',
           'GL_TEXTURE_MAG_FILTER',
           'GL_MAX_VERTEX_SHADER_INSTRUCTIONS_EXT',
           'GL_CONVOLUTION_FILTER_BIAS', 'GL_WEIGHT_ARRAY_ARB',
           'GL_COLOR_MATERIAL_FACE', 'GL_TEXTURE_LIGHT_EXT',
           'glutInitContextVersion', 'GL_PROGRAM_POINT_SIZE_ARB',
           'GL_VERSION', 'GL_TESS_GEN_SPACING', 'GL_SAMPLER_CUBE',
           'GL_EVAL_FRACTIONAL_TESSELLATION_NV',
           'GL_OBJECT_ACTIVE_UNIFORMS_ARB',
           'GL_MAX_PROGRAM_EXEC_INSTRUCTIONS_NV', 'glutPopWindow',
           'glutLeaveMainLoop', 'GL_INDEX_MATERIAL_PARAMETER_EXT',
           'GL_TANGENT_ARRAY_STRIDE_EXT', 'GL_FRAGMENT_LIGHT5_SGIX',
           'GL_LEFT', 'GL_TEXTURE_ALPHA_TYPE_ARB',
           'GLU_NURBS_RENDERER_EXT',
           'GL_MAX_PROGRAM_NATIVE_ATTRIBS_ARB',
           'GL_POST_COLOR_MATRIX_BLUE_BIAS',
           'GL_LUMINANCE_ALPHA_INTEGER_EXT',
           'GL_DEPTH24_STENCIL8_EXT', 'glTexEnvf', 'GLU_NURBS_ERROR7',
           'GLU_NURBS_ERROR4', 'GL_INT_IMAGE_2D_RECT_EXT',
           'GLU_NURBS_ERROR2', 'GL_MIRRORED_REPEAT_IBM',
           'GL_COMPRESSED_SRGB_S3TC_DXT1_EXT', 'glutLayerGet',
           'glGetHistogramParameterfv', 'GL_PROJECTION_MATRIX',
           'GL_MATRIX4_ARB', 'GL_PN_TRIANGLES_TESSELATION_LEVEL_ATI',
           'GLU_NURBS_ERROR8', 'glTexEnvi', 'glMultiTexCoord1iv',
           'GL_INVERTED_SCREEN_W_REND', 'GL_MAX_TEXTURE_SIZE',
           'GL_Z4Y12Z4CB12Z4A12Z4Y12Z4CR12Z4A12_4224_NV',
           'glutDialsFunc', 'GL_ALPHA8_SNORM', 'GL_ALPHA32F_ARB',
           'GL_PIXEL_MAP_I_TO_B', 'GLUT_ACTION_EXIT',
           'GL_ARRAY_BUFFER', 'GLintptrARB', 'GL_COMPRESSED_ALPHA',
           'GL_MAX_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT',
           'GL_INVARIANT_VALUE_EXT', 'GL_SIGNED_RGB_NV',
           'GL_TEXTURE_COMPRESSED_IMAGE_SIZE', 'GLU_SILHOUETTE',
           'GL_UNPACK_SKIP_IMAGES_EXT', 'GL_SPARE0_NV',
           'GL_LUMINANCE12_ALPHA4', 'glGetMapiv',
           'GL_MAP2_GRID_SEGMENTS', 'GL_BLEND_SRC_RGB',
           'GL_MATRIX14_ARB', 'GL_MAX_SAMPLE_MASK_WORDS_NV',
           'GL_ALPHA8I_EXT',
           'GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS',
           'GL_TRIANGLE_STRIP_ADJACENCY_EXT',
           'GL_TEXTURE_LOD_BIAS_EXT',
           'GL_CURRENT_MATRIX_STACK_DEPTH_NV',
           'GL_SAMPLE_ALPHA_TO_ONE', 'GL_WEIGHT_ARRAY_BUFFER_BINDING',
           'GL_SPRITE_OBJECT_ALIGNED_SGIX',
           'GL_PROGRAM_POINT_SIZE_EXT',
           'GL_NUM_SHADER_BINARY_FORMATS',
           'GL_CLAMP_FRAGMENT_COLOR_ARB', 'GL_ATTRIB_ARRAY_STRIDE_NV',
           'GL_STENCIL_BACK_PASS_DEPTH_PASS', 'glMultiTexCoord3iv',
           'GL_MULTISAMPLE_FILTER_HINT_NV',
           'GL_TRANSFORM_FEEDBACK_BUFFER_ACTIVE_NV', 'glutHideWindow',
           'GL_SECONDARY_COLOR_ARRAY_SIZE_EXT',
           'GL_TEXTURE_COMPARE_SGIX', 'GL_DRAW_BUFFER13_ARB',
           'glLightModelf', 'GL_INT_SAMPLER_2D',
           'GL_DUAL_ALPHA12_SGIS', 'GL_RG32F',
           'GL_UNSIGNED_INT_SAMPLER_BUFFER_AMD',
           'GL_VERTEX_ARRAY_RANGE_LENGTH_NV',
           'GL_PIXEL_TILE_GRID_HEIGHT_SGIX',
           'GL_MAP1_VERTEX_ATTRIB6_4_NV', 'GL_RG32I',
           'GL_DRAW_BUFFER3_ARB', 'glLightModeli',
           'GL_MAX_CONVOLUTION_HEIGHT_EXT',
           'GL_UNSIGNED_INT_IMAGE_2D_ARRAY_EXT',
           'GL_TEXTURE_ALPHA_SIZE_EXT',
           'GL_MAX_GEOMETRY_UNIFORM_BLOCKS', 'GL_LUMINANCE8_SNORM',
           'glCallLists', 'GL_RGBA8UI', 'GLUT_VIDEO_RESIZE_POSSIBLE',
           'GL_MAT_SPECULAR_BIT_PGI', 'GL_UNSIGNED_SHORT_5_6_5_REV',
           'glTexCoord3i', 'GL_MAX_PROGRAM_IF_DEPTH_NV',
           'GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_ARB',
           'GL_POINT_FADE_THRESHOLD_SIZE_EXT', 'GL_DOUBLE_MAT4_EXT',
           'GL_OP_MAX_EXT', 'glTexCoord3f', 'GL_NONE', 'glTexCoord3d',
           'GL_POLYGON_MODE', 'GL_PROXY_TEXTURE_RECTANGLE_ARB',
           'GL_HALF_FLOAT', 'GL_RGBA_SNORM',
           'GL_LINEAR_CLIPMAP_LINEAR_SGIX', 'glutMainLoopEvent',
           'glTexCoord3s', 'GLUT_CURSOR_CROSSHAIR', 'GL_LIGHTING_BIT',
           'GL_DEBUG_CATEGORY_WINDOW_SYSTEM_AMD', 'GL_NAND',
           'GL_MAX_SHININESS_NV', 'GLU_OBJECT_PATH_LENGTH',
           'glAreTexturesResident', 'GL_REG_15_ATI',
           'GLU_TESS_BOUNDARY_ONLY', 'GL_MAX_4D_TEXTURE_SIZE_SGIS',
           'GLUT_VERSION', 'GL_MAX_GEOMETRY_UNIFORM_COMPONENTS',
           'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER_EXT',
           'GL_INDEX_ARRAY', 'glRasterPos4sv', 'GL_V2F',
           'GL_CONVOLUTION_1D_EXT', 'glColor4s',
           'GL_SLUMINANCE_ALPHA_EXT',
           'GL_INDEX_ARRAY_LIST_STRIDE_IBM', 'GLUT_KEY_F7',
           'glutBitmap9By15', 'GL_TEXTURE_BINDING_CUBE_MAP_ARRAY',
           'GL_ALPHA', 'GL_RGB10', 'GL_TEXTURE_RESIDENT_EXT',
           'glClientActiveTextureARB',
           'GL_INT_SAMPLER_CUBE_MAP_ARRAY_ARB', 'GL_COLOR_WRITEMASK',
           'GL_MATRIX23_ARB', 'glColor4b', 'glColor4f', 'glColor4d',
           'GL_PROGRAM_NATIVE_PARAMETERS_ARB', 'glColor4i',
           'GL_PACK_SKIP_IMAGES', 'GL_TEXTURE_WRAP_T',
           'GL_UNSIGNED_INT_SAMPLER_CUBE',
           'GLUT_FORCE_DIRECT_CONTEXT',
           'GL_CONVOLUTION_BORDER_COLOR_HP', 'GL_INT_SAMPLER_3D_EXT',
           'GL_PROGRAM_BINARY_LENGTH', 'GL_EVAL_BIT', 'glVertex2dv',
           'GL_TEXTURE_BLUE_TYPE_ARB', 'GL_SAMPLER_BUFFER',
           'GL_COMPRESSED_RGB', 'GL_TIME_ELAPSED', 'GL_REG_27_ATI',
           'GL_CONVOLUTION_BORDER_COLOR', 'GL_MAX_TEXTURE_COORDS_ARB',
           'GL_POST_COLOR_MATRIX_GREEN_BIAS_SGI',
           'GL_COLOR_ARRAY_STRIDE_EXT',
           'GL_OUTPUT_TEXTURE_COORD11_EXT',
           'GL_CULL_VERTEX_OBJECT_POSITION_EXT', 'GL_TEXTURE12_ARB',
           'GLUT_JOYSTICK_BUTTON_D', 'GL_UNSIGNED_NORMALIZED',
           'GL_GLEXT_VERSION', 'GLUT_JOYSTICK_BUTTON_A',
           'GL_RESAMPLE_ZERO_FILL_SGIX', 'GLUT_JOYSTICK_BUTTON_C',
           'GL_BLUE_BITS', 'glViewport', 'GLUT_OVERLAY_POSSIBLE',
           'GL_INVALID_FRAMEBUFFER_OPERATION_EXT',
           'GL_SAMPLE_MASK_NV', 'GL_FLOAT_RG32_NV',
           'GL_LUMINANCE16_ALPHA16', 'GL_PACK_SWAP_BYTES', 'GL_EQUAL',
           'GLUT_WINDOW_HEADER_HEIGHT',
           'GL_PROGRAM_ATTRIB_COMPONENTS_NV',
           'GL_PROGRAM_PIPELINE_BINDING', 'GL_SAMPLES_3DFX',
           'GL_MIN_SAMPLE_SHADING_VALUE_ARB', 'GL_INTENSITY8UI_EXT',
           'GL_TEXTURE_SWIZZLE_B', 'GL_TEXTURE_SWIZZLE_A',
           'GL_POLYGON_OFFSET_UNITS', 'GL_LOW_FLOAT',
           'GL_FRAGMENT_SHADER_DERIVATIVE_HINT_ARB', 'GL_CUBIC_HP',
           'GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_ARRAY_EXT',
           'GL_PIXEL_TILE_GRID_DEPTH_SGIX', 'glutBitmapCharacter',
           'GL_RENDERBUFFER_INTERNAL_FORMAT',
           'GL_MIRROR_CLAMP_TO_BORDER_EXT', 'GL_INT_SAMPLER_BUFFER',
           'GL_INT_SAMPLER_1D_EXT',
           'GL_MAX_GEOMETRY_OUTPUT_VERTICES_ARB', 'glPixelStorei',
           'glutMainLoop', 'glPixelStoref',
           'GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_ARB',
           'GL_CURRENT_MATRIX_STACK_DEPTH_ARB',
           'GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW',
           'GL_VERTEX_ARRAY_LENGTH_NV', 'glEvalCoord1dv',
           'GL_TEXTURE_COORD_ARRAY_EXT', 'glRecti', 'GL_LINE_STRIP',
           'GL_ASYNC_TEX_IMAGE_SGIX', 'GL_PACK_ROW_LENGTH',
           'GL_LIGHT_MODEL_COLOR_CONTROL_EXT', 'glRectf',
           'GLUT_STEREO', 'glRectd', 'GL_MAP2_VERTEX_ATTRIB4_4_NV',
           'GL_GREEN_MIN_CLAMP_INGR', 'GL_LUMINANCE8_ALPHA8',
           'glBindTexture', 'glRects', 'glutSetKeyRepeat',
           'GL_INT16_VEC3_NV', 'GL_RENDERBUFFER_DEPTH_SIZE',
           'GL_REG_31_ATI', 'GL_INTENSITY_FLOAT16_ATI', 'GL_BITMAP',
           'GL_DYNAMIC_READ', 'GL_COMPRESSED_LUMINANCE',
           'GL_VERTEX_WEIGHT_ARRAY_STRIDE_EXT',
           'GL_Z6Y10Z6CB10Z6A10Z6Y10Z6CR10Z6A10_4224_NV',
           'GL_VERTEX_ARRAY', 'glGetColorTableParameteriv',
           'GL_SLUMINANCE_ALPHA', 'GL_INDEX_ARRAY_LENGTH_NV',
           'GL_LUMINANCE6_ALPHA2_EXT', 'GL_DEPTH_STENCIL',
           'GL_CONSTANT_EXT', 'GL_DUAL_ALPHA8_SGIS',
           'GL_SAMPLER_OBJECT_AMD', 'GL_PROGRAM_NATIVE_ATTRIBS_ARB',
           'glutMotionFunc', 'GL_UNIFORM_BUFFER_BINDING_EXT',
           'GL_POINT_SIZE', 'GL_TEXTURE_INTENSITY_SIZE',
           'GL_OUTPUT_TEXTURE_COORD17_EXT', 'GL_REDUCE_EXT',
           'GL_REG_22_ATI', 'GL_SYNC_CONDITION', 'GL_MATRIX16_ARB',
           'GL_VERTEX_ATTRIB_ARRAY10_NV',
           'GL_ACTIVE_UNIFORM_MAX_LENGTH', 'GL_HISTOGRAM_SINK',
           'GL_TEXTURE_DT_SIZE_NV', 'GL_MAP_INVALIDATE_RANGE_BIT',
           'GL_TEXTURE23', 'GL_TEXTURE22', 'GL_TEXTURE21',
           'glPixelMapfv', 'GL_TEXTURE27', 'GL_TEXTURE26',
           'GL_TEXTURE25', 'GL_TEXTURE24', 'GL_DOUBLE_MAT2_EXT',
           'GL_R8_SNORM', 'GL_TEXTURE29', 'GL_TEXTURE28',
           'GLUT_ACTION_GLUTMAINLOOP_RETURNS',
           'GL_ELEMENT_ARRAY_BUFFER_BINDING',
           'GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER',
           'GL_TRIANGLES_ADJACENCY', 'GL_PIXEL_MODE_BIT',
           'glSampleCoverage', 'GL_INT_VEC3_ARB',
           'GL_TEXTURE_1D_STACK_BINDING_MESAX', 'GL_ALPHA_SCALE',
           'GLUT_KEY_NUM_LOCK', 'GL_READ_BUFFER',
           'GL_ELEMENT_ARRAY_APPLE', 'GL_PACK_SKIP_PIXELS', 'GL_RG8I',
           'GL_BLEND_EQUATION_EXT', 'GL_TESS_CONTROL_SHADER',
           'GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS',
           'GL_FIXED_ONLY_ARB', 'GL_IMAGE_ROTATE_ORIGIN_X_HP',
           'GL_GEQUAL', 'GL_FRAMEBUFFER_SRGB_EXT',
           'GL_MODELVIEW8_ARB', 'GL_COLOR_ATTACHMENT5_EXT',
           'GLUT_WINDOW_DOUBLEBUFFER', 'GL_EXPAND_NORMAL_NV',
           'GL_DSDT8_NV', 'GL_NEGATE_BIT_ATI', 'GLUT_HAS_KEYBOARD',
           'GL_INTENSITY32UI_EXT', 'GL_INVALID_OPERATION',
           'GLUT_RGBA', 'GL_VARIANT_EXT',
           'GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION_EXT',
           'GL_PERFMON_RESULT_AVAILABLE_AMD',
           'GL_EDGE_FLAG_ARRAY_EXT', 'glTexGenf',
           'GL_COMPRESSED_RED_RGTC1', 'glTexGend',
           'GL_BINORMAL_ARRAY_STRIDE_EXT',
           'GL_FRAGMENT_PROGRAM_CALLBACK_FUNC_MESA', 'glTexGeni',
           'GL_TEXTURE_BUFFER_ARB', 'GL_POLYGON_OFFSET_EXT',
           'GL_RGB10_A2_EXT', 'GL_ARRAY_BUFFER_BINDING',
           'GL_INDEX_WRITEMASK', 'GL_INTERPOLATE',
           'GLUT_KEY_REPEAT_DEFAULT',
           'GL_MAX_BINDABLE_UNIFORM_SIZE_EXT', 'GL_STREAM_DRAW',
           'GL_DYNAMIC_DRAW', 'GL_SPRITE_AXIAL_SGIX', 'GL_RGB8_EXT',
           'GL_DOT_PRODUCT_DIFFUSE_CUBE_MAP_NV', 'GLU_NURBS_MODE_EXT',
           'glMultiTexCoord3ivARB', 'GL_MULTISAMPLE_SGIS',
           'GL_CON_12_ATI', 'GL_EDGE_FLAG_ARRAY_BUFFER_BINDING_ARB',
           'GL_QUADS', 'GL_UNPACK_ROW_LENGTH', 'GL_MODELVIEW30_ARB',
           'GL_CURRENT_PROGRAM',
           'GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS',
           'glRasterPos2dv', 'GL_BUFFER_MAPPED',
           'GL_DEBUG_CATEGORY_PERFORMANCE_AMD', 'GL_EYE_LINEAR',
           'GL_IMAGE_1D_ARRAY_EXT', 'GL_REG_24_ATI',
           'GL_VERTEX_ATTRIB_ARRAY6_NV',
           'GL_TEXTURE_INTENSITY_SIZE_EXT',
           'GL_EVAL_VERTEX_ATTRIB14_NV', 'GLUT_INIT_WINDOW_WIDTH',
           'GL_INTENSITY8I_EXT', 'GL_REG_28_ATI', 'GL_ALPHA4_EXT',
           'GL_OBJECT_POINT_SGIS', 'glMultiTexCoord3sARB',
           'GL_MAX_UNIFORM_BUFFER_BINDINGS', 'GLU_NURBS_ERROR',
           'GL_IUI_N3F_V2F_EXT', 'GL_COMPRESSED_LUMINANCE_LATC1_EXT',
           'GL_COMBINER_CD_OUTPUT_NV', 'GL_BOOL_VEC4_ARB',
           'GL_OFFSET_TEXTURE_2D_NV', 'GL_FRAMEBUFFER', 'GL_SPECULAR',
           'GLUT_KEY_PAGE_DOWN', 'GL_ALLOW_DRAW_WIN_HINT_PGI',
           'GL_COLOR_TABLE_FORMAT_SGI', 'glTexCoord2f',
           'GL_VERTEX_SHADER_VARIANTS_EXT', 'glColor4iv',
           'GL_RGB32I_EXT', 'GL_OPERAND1_RGB_ARB', 'glTexCoord2i',
           'GL_GENERATE_MIPMAP', 'GLU_OBJECT_PARAMETRIC_ERROR',
           'GL_NEGATIVE_ONE_EXT', 'GL_PROGRAM_PARAMETER_NV',
           'GL_FOG_COORDINATE_ARRAY_LIST_STRIDE_IBM',
           'GL_OP_INDEX_EXT', 'GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR_ARB',
           'GL_PN_TRIANGLES_NORMAL_MODE_QUADRATIC_ATI',
           'glTexCoord2s', 'GL_COLOR_ARRAY_SIZE',
           'GL_OUTPUT_COLOR0_EXT', 'GL_POLYGON_OFFSET_FACTOR',
           'GL_TEXTURE_STACK_DEPTH',
           'GL_COMPRESSED_RGBA_S3TC_DXT3_EXT', 'GL_Y_EXT',
           'GL_GENERATE_MIPMAP_SGIS', 'GL_STENCIL_PASS_DEPTH_PASS',
           'GL_SYNC_FLUSH_COMMANDS_BIT', 'glNormal3dv',
           'GL_QUERY_WAIT_NV', 'GL_DRAW_BUFFER14_ATI',
           'GL_NORMAL_ARRAY_EXT', 'GL_FRAGMENT_PROGRAM_CALLBACK_MESA',
           'GL_ZOOM_X', 'glutSpecialFunc', 'glTexCoord1dv',
           'GL_SAMPLE_ALPHA_TO_ONE_EXT', 'glArrayElement',
           'glReadPixels', 'GL_VERTEX_ATTRIB_ARRAY7_NV',
           'GL_VERSION_1_5', 'GL_EDGE_FLAG', 'GL_REG_7_ATI',
           'GL_PIXEL_MAP_I_TO_B_SIZE', 'glShadeModel',
           'GL_MULTISAMPLE_3DFX', 'GL_BINORMAL_ARRAY_TYPE_EXT',
           'GL_RGBA16I_EXT', 'glMapGrid1f', 'GLU_NURBS_ERROR10',
           'GLU_NURBS_VERTEX', 'GLUT_TRANSPARENT_INDEX',
           'GL_TEXTURE_BIT', 'GL_CLIP_VOLUME_CLIPPING_HINT_EXT',
           'GL_DEBUG_CATEGORY_UNDEFINED_BEHAVIOR_AMD',
           'GL_VERTEX_PRECLIP_HINT_SGIX',
           'GL_MAX_DEPTH_TEXTURE_SAMPLES',
           'GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN_NV', 'GL_MINMAX',
           'GL_QUERY_BY_REGION_WAIT', 'GL_TEXTURE_RESIDENT',
           'GL_TESS_GEN_VERTEX_ORDER',
           'GL_REPLACEMENT_CODE_ARRAY_POINTER_SUN', 'GL_OP_MOV_EXT',
           'GL_QUERY_RESULT_AVAILABLE_ARB', 'GL_FOG',
           'glMultiTexCoord4dARB', 'GLU_TESS_COORD_TOO_LARGE',
           'GL_PACK_CMYK_HINT_EXT', 'GL_FOG_COORD',
           'GL_FIELD_UPPER_NV', 'GL_POSITION',
           'GL_RESAMPLE_DECIMATE_OML',
           'GL_VIDEO_BUFFER_INTERNAL_FORMAT_NV', 'glRectiv',
           'GL_CONVOLUTION_BORDER_MODE', 'GL_INT_IMAGE_3D_EXT',
           'glRasterPos3dv', 'GL_SPRITE_EYE_ALIGNED_SGIX', 'GL_RG',
           'GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_EXT',
           'GL_PROXY_TEXTURE_CUBE_MAP_ARB',
           'GL_VERTEX_ATTRIB_ARRAY1_NV',
           'GL_VERTEX_CONSISTENT_HINT_PGI',
           'GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE',
           'GL_LINE_STIPPLE_PATTERN', 'GL_VERTEX_ARRAY_RANGE_NV',
           'GL_COMPATIBLE_SUBROUTINES', 'GL_VARIANT_ARRAY_EXT',
           'GL_MAP1_TEXTURE_COORD_2', 'GL_LAST_VERTEX_CONVENTION_EXT',
           'GL_STENCIL_INDEX4_EXT', 'GL_ONE_MINUS_CONSTANT_ALPHA_EXT',
           'glColor4ubv', 'GL_TRANSPOSE_MODELVIEW_MATRIX_ARB',
           'GL_INDEX_ARRAY_STRIDE_EXT',
           'GL_PROGRAM_NATIVE_INSTRUCTIONS_ARB', 'GL_RED_BIT_ATI',
           'GLUT_OWNS_JOYSTICK', 'GL_POST_CONVOLUTION_RED_BIAS',
           'GL_DEBUG_TYPE_PERFORMANCE_ARB', 'GL_COLOR_INDEX8_EXT',
           'GL_ENABLE_BIT', 'GL_RENDERBUFFER_BINDING',
           'GL_VERTEX_WEIGHT_ARRAY_TYPE_EXT',
           'GL_PARALLEL_ARRAYS_INTEL', 'glutFullScreenToggle',
           'GL_VERTEX_ATTRIB_ARRAY_DIVISOR_ARB', 'GL_DOT3_RGBA_ARB',
           'GL_UNSIGNED_INT_5_9_9_9_REV_EXT',
           'GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS',
           'GL_VERTEX_PROGRAM_POSITION_MESA', 'GL_SWIZZLE_STQ_DQ_ATI',
           'GL_MAP_COLOR', 'GL_OUTPUT_TEXTURE_COORD8_EXT',
           'GL_MAX_VERTEX_ATTRIBS',
           'GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS', 'GL_CONSTANT',
           'GL_WRITE_ONLY_ARB', 'GL_OUTPUT_TEXTURE_COORD21_EXT',
           'GL_VERTEX_ATTRIB_MAP2_SIZE_APPLE', 'GL_LINE_WIDTH_RANGE',
           'GL_OP_CLAMP_EXT', 'GL_BLUE_BIT_ATI',
           'GL_VERTEX_ATTRIB_ARRAY15_NV', 'GL_VERSION_3_1',
           'glHistogram', 'glutSpecialUpFunc',
           'GL_VERTEX_ATTRIB_ARRAY3_NV', 'GL_ALLOW_DRAW_MEM_HINT_PGI',
           'GLU_SAMPLING_METHOD', 'GL_LESS', 'GL_SIGNALED',
           'GL_MAX_OPTIMIZED_VERTEX_SHADER_INSTRUCTIONS_EXT',
           'GL_STENCIL_INDEX1', 'GL_DEPTH_BOUNDS_TEST_EXT',
           'GL_COMBINE_EXT', 'GL_TEXTURE_STENCIL_SIZE',
           'GLUT_SCREEN_WIDTH_MM',
           'GL_TRANSFORM_FEEDBACK_BARRIER_BIT_EXT',
           'GL_UNSIGNED_INT_IMAGE_BUFFER_EXT', 'GLUT_NUM_DIALS',
           'GL_EMISSION', 'GL_UNSIGNED_INT16_VEC4_NV',
           'GL_SAMPLER_3D', 'GL_COMPRESSED_LUMINANCE_ALPHA',
           'GL_MAX_PROGRAM_INSTRUCTIONS_ARB', 'GL_INT_SAMPLER_1D',
           'GL_EDGE_FLAG_ARRAY_LIST_STRIDE_IBM',
           'GL_OP_CROSS_PRODUCT_EXT', 'glDeleteLists', 'glTexGendv',
           'GL_RENDERBUFFER_RED_SIZE', 'GL_LIGHT5',
           'GL_TEXTURE_CLIPMAP_VIRTUAL_DEPTH_SGIX',
           'GL_SAMPLER_3D_ARB', 'GL_PHONG_WIN', 'glutVisibilityFunc',
           'glutKeyboardFunc', 'glRasterPos4i',
           'GL_MAX_DRAW_BUFFERS_ARB', 'GL_ADD_SIGNED_EXT',
           'glTexCoord2d', 'GL_MAX_PROGRAM_SUBROUTINE_NUM_NV',
           'GL_PN_TRIANGLES_POINT_MODE_CUBIC_ATI',
           'GL_TEXTURE_SWIZZLE_R', 'GL_PACK_SKIP_VOLUMES_SGIS',
           'GL_UNSIGNED_SHORT_8_8_REV_MESA',
           'GL_DEBUG_SEVERITY_LOW_ARB', 'GL_CON_18_ATI',
           'GLU_NURBS_TEXTURE_COORD', 'GL_STENCIL_INDEX16_EXT',
           'glutDeviceGet', 'GL_FUNC_SUBTRACT_EXT', 'GL_REPEAT',
           'GLUT_ACTION_CONTINUE_EXECUTION', 'glMultiTexCoord2fvARB',
           'GL_T2F_C4F_N3F_V3F', 'GL_HALF_FLOAT_ARB',
           'GL_WEIGHT_ARRAY_STRIDE_ARB',
           'GL_OBJECT_DELETE_STATUS_ARB', 'GLUT_SCREEN_WIDTH',
           'GL_INT64_VEC4_NV', 'GL_MAP2_VERTEX_ATTRIB11_4_NV',
           'GL_FOG_FUNC_POINTS_SGIS', 'GL_MAX_FRAGMENT_LIGHTS_SGIX',
           'GL_DEBUG_SOURCE_OTHER_ARB', 'GL_MAP1_VERTEX_ATTRIB8_4_NV',
           'GL_VERTEX_SHADER_EXT', 'GL_CLIENT_ALL_ATTRIB_BITS',
           'GL_VALIDATE_STATUS', 'GL_RG16', 'GL_REG_25_ATI',
           'glMultiTexCoord1sARB', 'GLUT_CURSOR_WAIT',
           'glConvolutionParameterfv', 'GL_OP_ROUND_EXT',
           'GLUT_HIDDEN', 'GL_MAX_VERTEX_UNIFORM_COMPONENTS_ARB',
           'GL_UNPACK_SKIP_IMAGES', 'GLUT_USE_CURRENT_CONTEXT',
           'GL_RGB_SCALE_ARB',
           'GL_MAX_PROGRAM_NATIVE_TEX_INSTRUCTIONS_ARB',
           'GL_SAMPLER_1D_ARRAY_SHADOW',
           'GL_UNSIGNED_INT_SAMPLER_1D_EXT', 'GL_DRAW_BUFFER12_ARB',
           'glutWireDodecahedron',
           'GL_TEXTURE_CUBE_MAP_POSITIVE_X_EXT',
           'glCopyConvolutionFilter2D',
           'GL_VERTEX_PROGRAM_POINT_SIZE_NV',
           'GL_REPLACEMENT_CODE_ARRAY_STRIDE_SUN',
           'GL_TEXTURE_CLIPMAP_DEPTH_SGIX', 'GL_BLEND_EQUATION_ALPHA',
           'glutBitmap8By13', 'GL_INDEX_TEST_FUNC_EXT',
           'glRasterPos4f', 'GL_POST_CONVOLUTION_COLOR_TABLE_SGI',
           'GL_ACTIVE_ATTRIBUTES', 'GL_ONE_MINUS_CONSTANT_COLOR_EXT',
           'GLUT_HAS_DIAL_AND_BUTTON_BOX',
           'GL_SHADER_GLOBAL_ACCESS_BARRIER_BIT_NV',
           'GL_SLUMINANCE8_ALPHA8_EXT', 'GL_VIEWPORT_BIT',
           'GL_NORMAL_ARRAY_POINTER_EXT',
           'GL_MAX_ASYNC_DRAW_PIXELS_SGIX', 'glColorMask',
           'GL_CONVOLUTION_WIDTH_EXT', 'GL_IMAGE_CUBE_EXT',
           'GL_READ_FRAMEBUFFER_BINDING_EXT', 'GL_LOCAL_EXT',
           'GL_DETAIL_TEXTURE_2D_BINDING_SGIS',
           'GL_VERTEX_PROGRAM_CALLBACK_DATA_MESA', 'glutSetOption',
           'GL_POST_CONVOLUTION_GREEN_BIAS_EXT',
           'GL_UNSIGNED_INT_SAMPLER_3D_EXT',
           'GL_QUERY_BY_REGION_NO_WAIT',
           'GL_MAP1_VERTEX_ATTRIB12_4_NV',
           'GL_SAMPLE_COVERAGE_INVERT', 'GLU_POINT',
           'GL_COMPRESSED_ALPHA_ARB', 'GL_TEXTURE18', 'GL_TEXTURE19',
           'GL_MODELVIEW11_ARB', 'GL_TEXTURE17',
           'GL_NORMAL_ARRAY_TYPE_EXT', 'GL_NORMAL_ARRAY_ADDRESS_NV',
           'GL_TEXTURE12', 'glutPositionWindow',
           'GL_OUTPUT_TEXTURE_COORD28_EXT', 'GL_TEXTURE11',
           'GL_PROGRAM_NATIVE_TEX_INDIRECTIONS_ARB',
           'GL_QUERY_OBJECT_AMD', 'glutKeyboardUpFunc',
           'GL_TEXTURE_SWIZZLE_A_EXT', 'GLUT_VIDEO_RESIZE_IN_USE',
           'GL_NEGATIVE_W_EXT', 'GL_MAX_PROGRAM_CALL_DEPTH_NV',
           'glTexCoord4dv', 'GL_TEXTURE_COMPARE_MODE',
           'GL_MAX_ASYNC_TEX_IMAGE_SGIX', 'GL_RGB',
           'GL_MAP2_VERTEX_ATTRIB7_4_NV',
           'GL_TEXTURE_BASE_LEVEL_SGIS', 'GL_TEXTURE_DS_SIZE_NV',
           'GL_POST_CONVOLUTION_ALPHA_BIAS_EXT', 'glutPushWindow',
           'GL_HISTOGRAM', 'GL_STENCIL_BACK_FAIL',
           'GL_TRANSFORM_FEEDBACK_BUFFER_START',
           'GL_MAX_PROGRAM_TEXEL_OFFSET', 'GL_OBJECT_LINE_SGIS',
           'GL_COMPARE_R_TO_TEXTURE_ARB', 'glutStrokeRoman',
           'GL_MAP1_VERTEX_4', 'GL_BIAS_BY_NEGATIVE_ONE_HALF_NV',
           'GL_FLOAT_RGBA_NV', 'GLUT_CURSOR_LEFT_ARROW',
           'glutBitmapLength', 'GL_REG_30_ATI', 'GL_RGBA32F',
           'GL_RGBA32I', 'GL_POST_COLOR_MATRIX_BLUE_SCALE_SGI',
           'GL_VERTEX_ATTRIB_ARRAY_TYPE', 'glEnableClientState',
           'glResetHistogram', 'GL_SIGNED_RGB8_NV',
           'GL_NORMAL_ARRAY_LENGTH_NV', 'GL_COLOR_TABLE_BLUE_SIZE',
           'GL_STENCIL_WRITEMASK', 'GL_CON_28_ATI',
           'GL_TEXTURE_BINDING_BUFFER_EXT',
           'GL_FRAGMENT_PROGRAM_POSITION_MESA',
           'GL_PERFMON_RESULT_AMD', 'glMultiTexCoord2iARB',
           'GL_EIGHTH_BIT_ATI',
           'GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS_ARB',
           'GL_SAMPLE_PATTERN_EXT', 'GL_VERTEX_ATTRIB_ARRAY8_NV',
           'GL_VARIANT_VALUE_EXT', 'GL_PN_TRIANGLES_POINT_MODE_ATI',
           'GL_VERSION_1_3_DEPRECATED', 'GL_TEXTURE_LOD_BIAS_R_SGIX',
           'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE',
           'GL_MAP_UNSYNCHRONIZED_BIT', 'glNormal3d',
           'GL_PRIMITIVE_RESTART',
           'GL_VERTEX_ATTRIB_ARRAY_INTEGER_NV', 'glGetTexGendv',
           'GLU_CW', 'GL_UNSIGNED_IDENTITY_NV',
           'GL_PIXEL_MAP_B_TO_B_SIZE',
           'GL_UNSIGNED_SHORT_1_5_5_5_REV',
           'GL_TEXTURE_BINDING_RENDERBUFFER_NV', 'GL_MATRIX4_NV',
           'GLUT_DEBUG', 'GL_OP_MULTIPLY_MATRIX_EXT', 'glColor3usv',
           'GL_SRC_ALPHA', 'GL_TEXTURE_3D', 'glDepthMask',
           'GL_VIDEO_BUFFER_BINDING_NV',
           'GL_TEXTURE_COORD_ARRAY_PARALLEL_POINTERS_INTEL',
           'GLU_NURBS_BEGIN', 'GL_VIDEO_COLOR_CONVERSION_MAX_NV',
           'GL_DRAW_BUFFER9_ARB', 'GL_VERTEX_ATTRIB_ARRAY5_NV',
           'glColorTable', 'GL_DRAW_BUFFER5_ARB',
           'GL_BLEND_SRC_RGB_EXT', 'GLUT_DEVICE_KEY_REPEAT',
           'GL_COMBINER_SCALE_NV', 'GL_FRAGMENT_LIGHT0_SGIX',
           'GL_TANGENT_ARRAY_POINTER_EXT', 'GL_PIXEL_TEX_GEN_SGIX',
           'GL_DOT4_ATI', 'GL_VERTEX_ATTRIB_ARRAY12_NV',
           'GL_YCBCR_MESA', 'GL_SIGNED_INTENSITY8_NV', 'GL_MIN_EXT',
           'GL_TEXTURE_UNSIGNED_REMAP_MODE_NV',
           'GL_POLYGON_OFFSET_BIAS_EXT',
           'GL_SECONDARY_COLOR_ARRAY_STRIDE',
           'GLUT_GAME_MODE_POSSIBLE', 'GL_SAMPLE_SHADING',
           'glutMouseFunc', 'GL_RG32UI', 'GL_ALL_CLIENT_ATTRIB_BITS',
           'glRasterPos2sv', 'GL_NORMALIZE', 'glTexCoord1sv',
           'GL_GEOMETRY_OUTPUT_TYPE_ARB', 'GL_TEXTURE_LO_SIZE_NV',
           'GL_SAMPLE_BUFFERS_SGIS', 'GL_LINEAR_ATTENUATION',
           'GL_BLUE_SCALE', 'GL_MODELVIEW16_ARB',
           'GL_INTERLACE_READ_INGR', 'GL_TRANSFORM_HINT_APPLE',
           'GL_INTERLEAVED_ATTRIBS_NV', 'GL_MAX_TEXTURE_UNITS',
           'GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS_EXT',
           'glGetFloatv', 'GL_FRAMEBUFFER_COMPLETE',
           'GL_DEPENDENT_RGB_TEXTURE_CUBE_MAP_NV',
           'GL_COPY_READ_BUFFER', 'GL_SHADER_COMPILER',
           'GL_FOG_COORD_ARRAY_POINTER',
           'GL_POST_COLOR_MATRIX_RED_BIAS_SGI',
           'GL_FOG_COORDINATE_ARRAY_TYPE_EXT',
           'GL_NUM_FRAGMENT_REGISTERS_ATI', 'GL_MATRIX11_ARB',
           'glutMenuStateFunc', 'glGetIntegerv',
           'GL_FOG_COORD_ARRAY_ADDRESS_NV',
           'GL_TEXTURE_RANGE_LENGTH_APPLE', 'GL_LOGIC_OP',
           'GL_MAX_PATCH_VERTICES',
           'GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET_ARB', 'GL_NICEST',
           'GL_VERTEX_PROGRAM_BINDING_NV', 'GL_DRAW_BUFFER6_ARB',
           'GLUT_WINDOW_HEIGHT', 'GL_PROXY_TEXTURE_RECTANGLE_NV',
           'GL_MODELVIEW', 'GL_OBJECT_TYPE', 'GL_C4UB_V3F',
           'glTexImage2D', 'GL_RGBA_FLOAT32_ATI', 'GL_COLOR4_BIT_PGI',
           'glDrawPixels', 'glMultMatrixd', 'GL_DEPTH_ATTACHMENT_EXT',
           'glMultMatrixf', 'glIsTexture', 'GL_CLAMP_TO_BORDER_ARB',
           'GL_VERTEX_ATTRIB_ARRAY_ENABLED_ARB', 'GL_COMBINE',
           'GL_VIDEO_COLOR_CONVERSION_MIN_NV',
           'GL_MAX_ASYNC_HISTOGRAM_SGIX', 'GL_SWIZZLE_STR_DR_ATI',
           'GL_BIAS_BIT_ATI', 'GL_INDEX_LOGIC_OP', 'glMapGrid1d',
           'GL_SRC1_COLOR',
           'GL_OFFSET_PROJECTIVE_TEXTURE_RECTANGLE_SCALE_NV',
           'GL_OFFSET_TEXTURE_SCALE_NV', 'GL_TRANSFORM_FEEDBACK',
           'GL_TEXTURE_CUBE_MAP_NEGATIVE_X_EXT', 'glColor4usv',
           'glPolygonStipple', 'GL_BACK_PRIMARY_COLOR_NV',
           'glInterleavedArrays', 'GL_MATRIX0_ARB', 'GL_RED_SNORM',
           'GL_PROGRAM_ERROR_POSITION_ARB',
           'GL_DOT_PRODUCT_REFLECT_CUBE_MAP_NV',
           'GL_NUM_COMPATIBLE_SUBROUTINES', 'GL_QUAD_LUMINANCE8_SGIS',
           'GL_UNSIGNED_INT_S8_S8_8_8_NV', 'GL_SCISSOR_TEST',
           'GL_TEXTURE_RECTANGLE_ARB',
           'GL_CURRENT_RASTER_SECONDARY_COLOR',
           'GL_ARRAY_OBJECT_OFFSET_ATI', 'GL_VERTEX_ARRAY_LIST_IBM',
           'glPixelMapusv', 'GL_MAT_DIFFUSE_BIT_PGI',
           'glutJoystickGetNumButtons', 'GLUT_KEY_HOME',
           'glSeparableFilter2D', 'GL_TRANSPOSE_PROJECTION_MATRIX',
           'GL_TEXTURE_MAX_ANISOTROPY_EXT', 'GL_SUBPIXEL_BITS',
           'GL_INTENSITY16UI_EXT', 'GLU_CCW', 'glutSolidOctahedron',
           'GL_ACTIVE_SUBROUTINE_UNIFORM_MAX_LENGTH', 'GLUT_KEY_F6',
           'GL_TEXTURE_CUBE_MAP_POSITIVE_Z_EXT',
           'GL_UNIFORM_MATRIX_STRIDE', 'GL_DUAL_INTENSITY8_SGIS',
           'GL_TEXTURE_GEN_S', 'GL_NORMALIZED_RANGE_EXT',
           'GL_CLIENT_VERTEX_ARRAY_BIT', 'GL_CONVOLUTION_FORMAT_EXT',
           'GL_TEXTURE_NORMAL_EXT', 'GL_BGR_EXT',
           'GL_TEXTURE_MULTI_BUFFER_HINT_SGIX',
           'GL_VERTEX_ATTRIB_MAP2_COEFF_APPLE',
           'GL_INDEX_ARRAY_BUFFER_BINDING',
           'GL_DEPTH_COMPONENT16_SGIX', 'GL_SLUMINANCE_EXT',
           'GL_POLYGON_SMOOTH', 'GL_MAX_PROGRAM_TEXEL_OFFSET_NV',
           'GL_SELECTION_BUFFER_SIZE', 'GL_TEXTURE_LOD_BIAS',
           'GL_INDEX_ARRAY_POINTER_EXT', 'GLU_NURBS_ERROR28',
           'GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_EXT',
           'GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_ARB',
           'GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER',
           'GL_POST_CONVOLUTION_RED_SCALE',
           'GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE',
           'GL_TRANSFORM_FEEDBACK_BUFFER_START_NV', 'GL_XOR',
           'GL_POINT_DISTANCE_ATTENUATION_ARB', 'GLU_TESS_ERROR2',
           'GL_SINGLE_COLOR_EXT', 'GL_TEXTURE_ENV_BIAS_SGIX',
           'GL_TEXTURE_CUBE_MAP_POSITIVE_Y_EXT',
           'GL_VERTEX_ARRAY_POINTER', 'GL_TEXTURE_1D_ARRAY_EXT',
           'GLU_TESS_ERROR4', 'GL_NEAREST_MIPMAP_LINEAR',
           'glVertex2fv', 'GL_TEXTURE_MAX_LEVEL_SGIS',
           'GL_MAX_OPTIMIZED_VERTEX_SHADER_INVARIANTS_EXT',
           'GL_TRANSFORM_FEEDBACK_BUFFER_NV', 'GL_EMBOSS_CONSTANT_NV',
           'GL_QUERY_RESULT', 'GL_VARIABLE_F_NV',
           'GL_SIGNED_NORMALIZED',
           'GL_PROGRAM_NATIVE_TEMPORARIES_ARB', 'GL_R16_SNORM',
           'GL_TEXTURE_BLUE_SIZE_EXT', 'GL_DEBUG_SEVERITY_HIGH_AMD',
           'GL_COLOR_ARRAY_LIST_IBM', 'GL_DOUBLE_VEC2_EXT',
           'GLU_TESS_ERROR8', 'glLineWidth', 'GL_POINT_SIZE_MIN_ARB',
           'GL_SOURCE2_RGB_ARB', 'GL_TEXTURE10_ARB', 'GL_OP_SUB_EXT',
           'GLU_NURBS_ERROR22', 'GL_COLOR_ATTACHMENT1_EXT',
           'GL_R1UI_T2F_V3F_SUN', 'GL_CONVOLUTION_FILTER_SCALE_EXT',
           'GL_COLOR_ARRAY_LENGTH_NV', 'GL_RGB16_SNORM',
           'GL_PROGRAM_BINARY_RETRIEVABLE_HINT',
           'GL_VARIANT_ARRAY_POINTER_EXT', 'GL_UNSIGNED_INT_VEC4',
           'GL_MAP2_VERTEX_ATTRIB1_4_NV',
           'GL_MAX_VERTEX_UNIFORM_BLOCKS', 'glFogiv',
           'GL_MODELVIEW26_ARB', 'glLightModeliv',
           'GL_COLOR_TABLE_FORMAT', 'GL_OUTPUT_TEXTURE_COORD1_EXT',
           'GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY_EXT',
           'GL_ELEMENT_ARRAY_UNIFIED_NV', 'GL_COLOR_ARRAY_ADDRESS_NV',
           'GL_FRACTIONAL_EVEN', 'GL_EDGE_FLAG_ARRAY_POINTER',
           'GL_MAP1_VERTEX_ATTRIB5_4_NV', 'GLUT_ACCUM',
           'GL_ASYNC_DRAW_PIXELS_SGIX', 'GL_TEXTURE_MAX_CLAMP_T_SGIX',
           'GLUT_WINDOW_WIDTH', 'GL_MINMAX_EXT', 'glutGameModeGet',
           'GL_MAX_LIST_NESTING', 'GL_POINT_SIZE_MIN_EXT',
           'GLUT_PARTIALLY_RETAINED', 'GL_TEXTURE_WRAP_R',
           'GL_FLOAT_RG_NV', 'GL_INT64_VEC3_NV',
           'GL_LUMINANCE16_ALPHA16_EXT',
           'GL_MAX_PROGRAM_TEMPORARIES_ARB', 'glEvalCoord1fv',
           'GL_UNSIGNED_INT_IMAGE_1D_EXT', 'GL_DRAW_BUFFER2_ARB',
           'GL_TEXTURE_STENCIL_SIZE_EXT', 'GL_FOG_DISTANCE_MODE_NV',
           'GL_COLOR_ARRAY', 'glutWireRhombicDodecahedron',
           'GL_CON_0_ATI', 'GL_FOG_END', 'GL_ATTENUATION_EXT',
           'GL_COLOR_TABLE_ALPHA_SIZE_SGI',
           'GL_DRAW_INDIRECT_ADDRESS_NV',
           'GL_FIRST_VERTEX_CONVENTION_EXT', 'GL_HINT_BIT',
           'GL_DEBUG_CATEGORY_APPLICATION_AMD',
           'GL_MAX_PROGRAM_RESULT_COMPONENTS_NV',
           'GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS',
           'GL_TEXTURE_BINDING_BUFFER',
           'GL_MAX_PROGRAM_OUTPUT_VERTICES_NV', 'GL_DYNAMIC_ATI',
           'GL_OUTPUT_TEXTURE_COORD6_EXT', 'GL_GREEN_INTEGER',
           'GL_COLOR_ARRAY_POINTER', 'GL_TEXTURE_DEPTH_SIZE',
           'GL_STATIC_READ_ARB',
           'GL_OFFSET_PROJECTIVE_TEXTURE_RECTANGLE_NV',
           'GL_FENCE_STATUS_NV', 'GL_DRAW_BUFFER11_ATI',
           'GL_TEXTURE_UPDATE_BARRIER_BIT_EXT', 'GLUT_KEY_PAGE_UP',
           'GL_OP_FLOOR_EXT', 'GLU_FILL',
           'GLUT_WINDOW_ACCUM_BLUE_SIZE', 'GL_RENDERER',
           'GL_COMPRESSED_RGBA', 'GL_HALF_BIAS_NEGATE_NV',
           'GL_REPLACEMENT_CODE_SUN', 'GL_TEXTURE22_ARB',
           'GL_CLIENT_ATTRIB_STACK_DEPTH',
           'GL_SIGNED_LUMINANCE_ALPHA_NV', 'GL_SIGNED_HILO_NV',
           'GL_IMAGE_SCALE_Y_HP', 'GL_SUCCESS_NV',
           'GL_COLOR_ARRAY_COUNT_EXT',
           'GL_TRANSFORM_FEEDBACK_BUFFER_SIZE_EXT',
           'GL_TEXTURE19_ARB', 'GL_MAX_COLOR_ATTACHMENTS',
           'GL_TEXTURE_COMPONENTS', 'glEdgeFlag', 'GLUT_KEY_INSERT',
           'glVertex3d', 'GL_VERTEX_STREAM1_ATI', 'glVertex3f',
           'GL_MAX_CLIENT_ATTRIB_STACK_DEPTH', 'glVertex3i',
           'GL_COLOR_ARRAY_SIZE_EXT', 'glGetColorTable',
           'GL_SWIZZLE_STQ_ATI', 'GL_EDGE_FLAG_ARRAY_COUNT_EXT',
           'GL_DETAIL_TEXTURE_FUNC_POINTS_SGIS', 'GLU_DISPLAY_MODE',
           'glVertex3s', 'GL_UNSIGNED_INT_SAMPLER_BUFFER',
           'glutSolidCone', 'GL_TRANSFORM_FEEDBACK_BUFFER_MODE',
           'GL_BITMAP_TOKEN', 'glutEntryFunc',
           'GL_FEEDBACK_BUFFER_POINTER',
           'GL_COMPRESSED_SIGNED_LUMINANCE_ALPHA_LATC2_EXT',
           'GL_VERTEX_STREAM7_ATI', 'GLUT_CREATE_NEW_CONTEXT',
           'GL_SUBTRACT', 'GL_TEXTURE_CUBE_MAP_POSITIVE_X_ARB',
           'GL_INTENSITY_SNORM', 'GL_PRIMARY_COLOR_EXT',
           'GL_TRANSFORM_FEEDBACK_BINDING_NV',
           'GL_CURRENT_FOG_COORDINATE', 'GLUT_INIT_WINDOW_HEIGHT',
           'GL_CON_5_ATI', 'glMultiTexCoord3fvARB',
           'GL_NUM_LOOPBACK_COMPONENTS_ATI',
           'GL_TRANSFORM_FEEDBACK_BUFFER_START_EXT',
           'GL_VERTEX_ARRAY_STRIDE', 'GL_SAMPLER_CUBE_SHADOW_EXT',
           'GL_VERTEX_ARRAY_POINTER_EXT',
           'GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS',
           'glNormalPointer', 'GL_CON_23_ATI', 'glPassThrough',
           'GL_MULT', 'GL_STENCIL', 'GL_DOT3_RGB_ARB',
           'GL_POINT_SPRITE_ARB', 'GLshort',
           'GL_SYNC_CL_EVENT_COMPLETE_ARB',
           'GL_PIXEL_PACK_BUFFER_ARB', 'glBegin', 'glEvalCoord2dv',
           'glColor3ubv', 'GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_EXT',
           'GL_MODELVIEW24_ARB',
           'GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS_EXT',
           'GL_SRC2_RGB',
           'GL_MAX_PROGRAM_NATIVE_ADDRESS_REGISTERS_ARB',
           'GL_R1UI_C4UB_V3F_SUN', 'glLightfv',
           'GL_PIXEL_TEX_GEN_Q_FLOOR_SGIX', 'GL_SYNC_STATUS',
           'GL_MAX_IMAGE_UNITS_EXT', 'GL_ALPHA8_EXT',
           'GL_STREAM_DRAW_ARB', 'GL_UNIFORM_BLOCK_DATA_SIZE',
           'GL_VIEWPORT', 'GL_MAX_FRAGMENT_INTERPOLATION_OFFSET',
           'GL_DEPTH_TEXTURE_MODE_ARB', 'glutSolidTetrahedron',
           'GL_RGB8I', 'GL_ATTRIB_ARRAY_TYPE_NV',
           'GL_DRAW_BUFFER7_ARB', 'GL_COLOR_TABLE_LUMINANCE_SIZE',
           'GLU_TESS_WINDING_RULE', 'GL_BLEND_SRC', 'GL_DS_SCALE_NV',
           'GL_UNKNOWN_CONTEXT_RESET_ARB', 'glTexParameteriv',
           'GL_IMAGE_TRANSFORM_2D_HP', 'GL_BUFFER_MAP_OFFSET',
           'GL_FOG_SPECULAR_TEXTURE_WIN', 'GL_CON_14_ATI',
           'GL_PROGRAM_ERROR_POSITION_NV',
           'GL_TEXTURE_BINDING_RECTANGLE_ARB',
           'GL_PIXEL_SUBSAMPLE_2424_SGIX', 'GL_INT_SAMPLER_2D_RECT',
           'glIndexsv', 'glutAddMenuEntry', 'GL_INT_IMAGE_CUBE_EXT',
           'GL_ONE_EXT', 'GL_DEPTH24_STENCIL8', 'GL_MODELVIEW7_ARB',
           'GL_SAMPLE_BUFFERS_ARB',
           'GL_UNSIGNED_INT_SAMPLER_1D_ARRAY_EXT',
           'GL_MAX_TEXTURE_LOD_BIAS_EXT', 'GL_TEXTURE_COMPRESSED_ARB',
           'GLUT_CURSOR_TOP_RIGHT_CORNER', 'glBitmap',
           'GL_FUNC_ADD_EXT', 'GL_GEOMETRY_SHADER_INVOCATIONS',
           'glColorSubTable', 'GL_TEXTURE16_ARB', 'GL_COLOR_INDEX',
           'GL_PACK_IMAGE_HEIGHT', 'GL_MAP2_NORMAL',
           'GL_PIXEL_TILE_BEST_ALIGNMENT_SGIX', 'GL_COLOR_MATRIX_SGI',
           'GL_MAX_EVAL_ORDER', 'glTexCoord4f', 'glTexCoord4d',
           'GL_SAMPLER_2D_RECT_SHADOW_ARB', 'GLU_CULLING',
           'glTexCoord4i', 'GL_RGBA16F',
           'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_EXT',
           'GL_ANY_SAMPLES_PASSED', 'glColorTableParameteriv',
           'GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE',
           'GL_TEXTURE_COORD_ARRAY_LIST_STRIDE_IBM',
           'GL_COMPRESSED_RGB_S3TC_DXT1_EXT',
           'GL_COMPRESSED_LUMINANCE_ARB', 'GL_MAP_WRITE_BIT',
           'GL_SHADE_MODEL', 'GLUT_DOWN',
           'GL_GENERATE_MIPMAP_HINT_SGIS', 'glMultiTexCoord4svARB',
           'glNormal3fv', 'GL_COMPRESSED_SLUMINANCE',
           'GLU_TESS_MISSING_BEGIN_POLYGON', 'glTexCoord1fv',
           'glutWireCone', 'GL_RGBA16F_ARB', 'GL_UNIFORM_BLOCK_INDEX',
           'GL_PIXEL_TILE_WIDTH_SGIX', 'GL_MAP1_VERTEX_ATTRIB14_4_NV',
           'GL_INDEX_SHIFT', 'GL_LUMINANCE_ALPHA_SNORM',
           'glMultiTexCoord1dv', 'GL_TRIANGLES_ADJACENCY_EXT',
           'glTexCoord3fv', 'GLU_NURBS_VERTEX_DATA',
           'GL_TRANSFORM_FEEDBACK_BUFFER_MODE_NV', 'GLhalfNV',
           'GL_LIST_BIT', 'GLU_SAMPLING_TOLERANCE',
           'GL_BGRA_INTEGER_EXT', 'GL_UNIFORM_BUFFER_START',
           'GL_ONE_MINUS_SRC1_COLOR', 'GL_STREAM_READ', 'GL_LINEAR',
           'GLUT_INIT_WINDOW_Y', 'GLUT_INIT_WINDOW_X',
           'GL_MINMAX_SINK', 'glActiveTextureARB',
           'GL_PROXY_TEXTURE_CUBE_MAP_EXT', 'GL_STENCIL_INDEX',
           'GL_PROGRAM_TEMPORARIES_ARB', 'GL_TEXTURE_GREEN_SIZE_EXT',
           'GL_PROGRAM_TEX_INDIRECTIONS_ARB', 'GLUtesselatorObj',
           'GL_SEPARATE_ATTRIBS_NV', 'GLhandleARB', 'glDepthRange',
           'GLUT_INIT_FLAGS', 'GL_TRANSFORM_FEEDBACK_BUFFER_SIZE_NV',
           'GL_HIGH_FLOAT', 'glGetColorTableParameterfv',
           'GL_GREATER', 'GL_IUI_N3F_V3F_EXT', 'GLUT_KEY_F4',
           'glDrawBuffer', 'GL_PIXEL_SUBSAMPLE_4444_SGIX',
           'GL_SAMPLER_1D_ARRAY_SHADOW_EXT',
           'GL_GREEN_MAX_CLAMP_INGR', 'glRasterPos3fv',
           'GL_FRAMEBUFFER_SRGB_CAPABLE_EXT',
           'GL_LUMINANCE_ALPHA32F_ARB',
           'GL_TESS_EVALUATION_SHADER_BIT', 'GL_FRONT_FACE',
           'GL_POST_COLOR_MATRIX_COLOR_TABLE_SGI', 'GL_REPLACE',
           'GL_QUERY_RESULT_ARB', 'GL_VERTEX_ATTRIB_ARRAY_STRIDE',
           'GL_UNSIGNED_INT16_VEC3_NV', 'glClearIndex',
           'GL_OPERAND0_RGB_ARB',
           'GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE', 'GLUT_BLUE',
           'glFlush', 'GLUnurbsObj', 'GL_TEXTURE_LUMINANCE_SIZE_EXT',
           'GL_CONVOLUTION_BORDER_MODE_EXT',
           'GL_PIXEL_COUNTER_BITS_NV', 'GL_MINMAX_SINK_EXT',
           'GL_OPERAND2_ALPHA_ARB', 'GL_INTENSITY8_EXT',
           'GL_DUAL_LUMINANCE16_SGIS', 'GL_VERTEX_ARRAY_EXT',
           'GL_TANGENT_ARRAY_TYPE_EXT', 'GL_RG8UI',
           'GL_ACCUM_CLEAR_VALUE', 'GL_YCRCB_422_SGIX',
           'GL_RGB_SCALE_EXT', 'GL_PROXY_TEXTURE_1D_ARRAY_EXT',
           'GLUT_VIDEO_RESIZE_HEIGHT_DELTA', 'GLU_TESS_ERROR',
           'GL_PN_TRIANGLES_ATI', 'GL_SAMPLER_1D_SHADOW_ARB',
           'GL_MAX_PROGRAM_ATTRIBS_ARB', 'GL_TESS_EVALUATION_SHADER',
           'glGetTexLevelParameteriv', 'GL_RGB5_EXT',
           'GL_AVERAGE_EXT', 'GL_TRANSFORM_FEEDBACK_RECORD_NV',
           'GL_R16UI', 'GL_REG_8_ATI', 'GL_CONVOLUTION_1D',
           'GL_BLEND', 'GL_DEPENDENT_GB_TEXTURE_2D_NV',
           'GL_REGISTER_COMBINERS_NV', 'GL_MAP1_TEXTURE_COORD_3',
           'GL_COLOR_TABLE_GREEN_SIZE', 'GL_MAP1_TEXTURE_COORD_1',
           'glCallList', 'GL_DEPENDENT_HILO_TEXTURE_2D_NV', 'GL_MIN',
           'GL_MAP1_TEXTURE_COORD_4', 'GL_COMPRESSED_SRGB_ALPHA',
           'GL_INT_SAMPLER_BUFFER_AMD', 'GL_ONE_MINUS_SRC_COLOR',
           'GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET_ARB',
           'glutWarpPointer', 'glClearStencil',
           'GL_MAX_VERTEX_SHADER_LOCALS_EXT', 'GL_INTENSITY12',
           'GL_FRAGMENT_LIGHT7_SGIX', 'GL_PIXEL_MAP_I_TO_R_SIZE',
           'GL_C4UB_V2F', 'GL_OCCLUSION_TEST_HP',
           'glMultiTexCoord3fv', 'GL_LUMINANCE12_ALPHA12_EXT',
           'GL_DRAW_BUFFER1_ATI', 'GL_SAMPLE_MASK_EXT', 'GL_PATCHES',
           'GL_LIST_MODE', 'GL_MAP_TESSELLATION_NV', 'GL_TIMESTAMP',
           'GL_DEPTH_COMPONENT16_ARB', 'GL_IMAGE_2D_EXT',
           'GL_TEXTURE4', 'GL_TYPE_RGBA_FLOAT_ATI',
           'GL_VERTEX_PROGRAM_POINT_SIZE',
           'GL_UNSIGNED_SHORT_8_8_REV_APPLE',
           'GL_UNSIGNED_INT_IMAGE_3D_EXT', 'GL_OPERAND2_RGB',
           'GL_MAP2_VERTEX_ATTRIB2_4_NV',
           'GL_GEOMETRY_VERTICES_OUT_ARB',
           'GL_DEBUG_LOGGED_MESSAGES_ARB', 'GL_SRGB_ALPHA',
           'glVertex2f', 'glVertex2d', 'glMultiTexCoord4fARB',
           'GL_SLICE_ACCUM_SUN', 'GL_PACK_SKIP_ROWS',
           'GL_MAX_DRAW_BUFFERS_ATI', 'glTexImage3D', 'glVertex2i',
           'GL_LINEAR_MIPMAP_LINEAR', 'GL_RGBA_FLOAT16_ATI',
           'GL_LIGHTING', 'glVertex2s', 'GL_MAP1_COLOR_4',
           'GL_GEOMETRY_SHADER', 'GL_R8I', 'GL_COMBINER3_NV',
           'GL_LUMINANCE8_EXT', 'GL_SYNC_CL_EVENT_ARB',
           'GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS',
           'GL_TEXTURE_COORD_ARRAY_TYPE_EXT',
           'GL_TRANSFORM_FEEDBACK_VARYINGS_NV', 'glutIdleFunc',
           'GL_BLEND_COLOR', 'glutOverlayDisplayFunc',
           'GL_ALPHA_BITS', 'GL_FILTER4_SGIS',
           'GL_TEXTURE_COORD_ARRAY_STRIDE_EXT',
           'GL_BUFFER_OBJECT_APPLE', 'GL_SAMPLER_2D_ARRAY_SHADOW_EXT',
           'GL_ONE_MINUS_CONSTANT_ALPHA', 'GL_CON_22_ATI',
           'GLU_NURBS_NORMAL_DATA', 'GLU_END', 'GL_SRC2_ALPHA',
           'GL_UNSIGNED_INT_SAMPLER_2D', 'GL_MULTISAMPLE_BIT_EXT',
           'GL_CON_8_ATI', 'GL_MODELVIEW14_ARB', 'glGetPixelMapfv',
           'GL_ALPHA_MAX_CLAMP_INGR', 'glResetMinmax',
           'GL_ALWAYS_SOFT_HINT_PGI', 'GL_BLEND_SRC_ALPHA_EXT',
           'GL_TEXTURE3_ARB', 'GL_REG_10_ATI', 'glTexSubImage3D',
           'GL_VERSION_1_1', 'GL_INTENSITY32F_ARB',
           'GL_TESS_CONTROL_PROGRAM_NV',
           'GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE_SGI',
           'GL_VIDEO_BUFFER_PITCH_NV', 'GL_HISTOGRAM_WIDTH_EXT',
           'GL_SOURCE0_RGB_ARB', 'GL_TEXTURE_FETCH_BARRIER_BIT_EXT',
           'GL_MODELVIEW10_ARB', 'GL_MAP1_VERTEX_ATTRIB7_4_NV',
           'GL_NORMAL_ARRAY_LIST_STRIDE_IBM', 'GL_VARIABLE_A_NV',
           'GL_FOG_COORDINATE_ARRAY_TYPE',
           'GL_MAX_VERTEX_VARYING_COMPONENTS_ARB',
           'GL_ALPHA_MIN_SGIX', 'GL_SAMPLES_PASSED',
           'GL_PROVOKING_VERTEX', 'glGetHistogram',
           'GL_VERTEX_ATTRIB_ARRAY13_NV',
           'GL_STENCIL_TEST_TWO_SIDE_EXT', 'glMatrixMode',
           'GL_PACK_SUBSAMPLE_RATE_SGIX',
           'GLUT_GAME_MODE_REFRESH_RATE', 'GL_REG_12_ATI',
           'GLUT_FULLY_RETAINED', 'GL_LUMINANCE16I_EXT',
           'GL_COLOR_TABLE_INTENSITY_SIZE_SGI', 'GL_SEPARATE_ATTRIBS',
           'GL_CURRENT_FOG_COORD', 'GL_FRAMEBUFFER_UNDEFINED',
           'GL_TEXTURE_CUBE_MAP_POSITIVE_Z_ARB', 'GL_OBJECT_TYPE_ARB',
           'GLUT_MENU_NOT_IN_USE', 'GL_MAP2_VERTEX_ATTRIB0_4_NV',
           'GL_TEXTURE_COLOR_TABLE_SGI',
           'GL_OUTPUT_TEXTURE_COORD25_EXT', 'GL_CONVOLUTION_FORMAT',
           'glPrioritizeTextures', 'GL_MAP1_VERTEX_ATTRIB1_4_NV',
           'GL_PROXY_TEXTURE_2D_STACK_MESAX',
           'GL_PRIMITIVE_RESTART_NV', 'GL_FRAGMENT_DEPTH_EXT',
           'GL_TEXTURE_HEIGHT', 'glGetDoublev', 'GL_CULL_VERTEX_EXT',
           'GL_RGBA16I', 'GL_MAX_VARYING_VECTORS',
           'GL_FOG_SCALE_SGIX', 'GL_STENCIL_INDEX8',
           'GL_COMBINER_COMPONENT_USAGE_NV',
           'GL_POST_COLOR_MATRIX_RED_SCALE_SGI', 'GL_SAMPLER_1D',
           'GL_CULL_FRAGMENT_NV', 'GL_REPLACE_EXT',
           'GL_RGBA_FLOAT_MODE_ARB', 'glutSolidIcosahedron',
           'GL_INCR_WRAP_EXT', 'GL_COLOR_TABLE_LUMINANCE_SIZE_SGI',
           'GL_RED', 'GL_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT',
           'glutInitWindowSize', 'GL_DEPTH_STENCIL_EXT',
           'GL_POLYGON_OFFSET_LINE', 'GL_FUNC_REVERSE_SUBTRACT',
           'GL_NO_RESET_NOTIFICATION_ARB', 'GL_PRESERVE_ATI',
           'GL_LINE_TOKEN', 'GL_SRGB8_ALPHA8_EXT',
           'GL_DSDT_MAG_VIB_NV', 'GL_NEGATIVE_Y_EXT',
           'GL_MAX_PROGRAM_GENERIC_ATTRIBS_NV',
           'GL_COMPRESSED_RGBA_S3TC_DXT1_EXT', 'GL_GREEN',
           'GL_TEXTURE_4D_BINDING_SGIS', 'GL_MAGNITUDE_SCALE_NV',
           'GL_BACK_SECONDARY_COLOR_NV', 'GL_LUMINANCE_FLOAT32_ATI',
           'GL_OPERAND1_ALPHA_EXT', 'GL_MAP2_TEXTURE_COORD_1',
           'GL_MAP2_TEXTURE_COORD_2', 'GL_MAP2_TEXTURE_COORD_3',
           'GL_MAP2_TEXTURE_COORD_4', 'GLU_NURBS_BEGIN_DATA',
           'GL_MAX_MODELVIEW_STACK_DEPTH',
           'GL_TESSELLATION_FACTOR_AMD', 'GL_CONVOLUTION_WIDTH',
           'GL_CON_1_ATI', 'GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE',
           'GLU_NURBS_VERTEX_DATA_EXT', 'GL_TEXTURE_2D_MULTISAMPLE',
           'GL_VERTEX_SOURCE_ATI', 'GL_TEXTURE26_ARB',
           'GL_MATRIX29_ARB', 'GL_TEXTURE_BINDING_RECTANGLE_NV',
           'GLUT_WINDOW_ACCUM_GREEN_SIZE',
           'GL_OBJECT_SHADER_SOURCE_LENGTH_ARB',
           'GL_VERTEX_STREAM4_ATI', 'glGetTexGenfv',
           'GL_SAMPLER_2D_RECT', 'GL_LUMINANCE_SNORM',
           'GL_MAX_COMBINED_UNIFORM_BLOCKS', 'GL_FRAGMENT_PROGRAM_NV',
           'GL_INT16_VEC4_NV', 'GL_MAX_TEXTURE_UNITS_ARB',
           'GLUT_SINGLE', 'GL_TEXTURE_BUFFER_DATA_STORE_BINDING_ARB',
           'GLUT_UP', 'GL_LINE_STRIP_ADJACENCY', 'glMultiTexCoord2iv',
           'GL_INDEX_BITS', 'GL_LINEAR_SHARPEN_COLOR_SGIS',
           'GL_DST_COLOR', 'GL_DOT3_ATI', 'GL_MAX_SAMPLES_EXT',
           'GL_REG_4_ATI', 'GL_DRAW_BUFFER5_ATI', 'GL_STENCIL_BITS',
           'GL_UNSIGNED_INT', 'GL_PROGRAM_FORMAT_ARB',
           'GLU_NURBS_RENDERER', 'glRasterPos3iv', 'GL_CON_20_ATI',
           'glutSetupVideoResizing',
           'GL_TRANSPOSE_CURRENT_MATRIX_ARB', 'GL_V3F',
           'GL_DOUBLE_MAT3_EXT', 'GL_COLOR_SAMPLES_NV',
           'GL_FRAGMENT_PROGRAM_INTERPOLATION_OFFSET_BITS_NV',
           'GL_INT_SAMPLER_2D_RECT_EXT', 'glTexCoord4sv',
           'GL_LUMINANCE16', 'glutBitmapHeight',
           'GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES', 'glFinish',
           'glutMenuStatusFunc', 'GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT',
           'GL_ALPHA_BLEND_EQUATION_ATI', 'glColorTableParameterfv',
           'GL_RG16_SNORM', 'GL_DUAL_ALPHA16_SGIS',
           'GL_UNIFORM_BLOCK_REFERENCED_BY_GEOMETRY_SHADER',
           'glTexCoord4fv', 'GL_COLOR_TABLE_WIDTH_SGI',
           'GL_COLOR_ARRAY_TYPE',
           'GL_SHADER_IMAGE_ACCESS_BARRIER_BIT_EXT',
           'GL_MULTISAMPLE_BIT_ARB', 'GL_MODULATE', 'GL_RG_INTEGER',
           'glIndexdv', 'GL_FOG_COORD_ARRAY_BUFFER_BINDING',
           'GL_MAX_PROGRAM_SUBROUTINE_PARAMETERS_NV', 'glTexCoord3iv',
           'GL_Z4Y12Z4CB12Z4Y12Z4CR12_422_NV',
           'GL_RENDERBUFFER_HEIGHT', 'GL_RGB4_S3TC',
           'GL_INTERLEAVED_ATTRIBS', 'GL_TEXTURE_ALPHA_TYPE',
           'glClearDepth', 'GLUT_ACTIVE_CTRL',
           'GL_DEFORMATIONS_MASK_SGIX', 'GL_LIST_BASE',
           'GL_ELEMENT_ARRAY_BUFFER_BINDING_ARB', 'GL_BLUE',
           'GL_RGBA4_EXT', 'GL_COLOR_ATTACHMENT2_EXT',
           'GL_MAX_VARYING_FLOATS_ARB',
           'GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS',
           'GL_SRGB_EXT', 'GL_SOURCE3_RGB_NV', 'GL_COMBINE4_NV',
           'GL_COLOR_ATTACHMENT7_EXT',
           'GL_MAX_DEBUG_LOGGED_MESSAGES_AMD',
           'GLUT_VIDEO_RESIZE_Y_DELTA', 'GL_C4F_N3F_V3F',
           'GL_TEXTURE_POST_SPECULAR_HP', 'GL_CURRENT_BINORMAL_EXT',
           'GL_T4F_V4F', 'GL_STREAM_COPY', 'GL_INT64_VEC2_NV',
           'GL_FLOAT_RG16_NV', 'GL_SOURCE0_RGB', 'glNormal3sv',
           'GL_EYE_PLANE', 'GL_SAMPLER_2D_RECT_ARB',
           'GL_MAX_TEXTURE_COORDS_NV', 'GL_MATRIX18_ARB',
           'GL_SAMPLER_BUFFER_EXT',
           'GL_SIGNED_RGB8_UNSIGNED_ALPHA8_NV',
           'GL_TEXTURE_2D_MULTISAMPLE_ARRAY',
           'GL_DRAW_FRAMEBUFFER_EXT', 'GLUT_CURSOR_SPRAY',
           'GL_POINT_SMOOTH_HINT', 'GL_TEXTURE_SWIZZLE_R_EXT',
           'glRasterPos4iv', 'GL_RGB8UI_EXT',
           'GL_COMPRESSED_RGBA_BPTC_UNORM_ARB', 'GL_REG_0_ATI',
           'GL_TEXTURE_COMPRESSED_IMAGE_SIZE_ARB', 'GL_ORDER',
           'glEdgeFlagv', 'GL_VIBRANCE_BIAS_NV', 'GLUT_ACTIVE_ALT',
           'GL_INT8_VEC4_NV', 'GL_REFLECTION_MAP_ARB',
           'GL_STORAGE_SHARED_APPLE',
           'GL_TEXTURE_RANGE_POINTER_APPLE', 'GLU_VERSION_1_2',
           'GLUT_ALLOW_DIRECT_CONTEXT',
           'GL_MAX_PROGRAM_ADDRESS_REGISTERS_ARB',
           'GL_VERTEX23_BIT_PGI', 'GL_INT_SAMPLER_2D_ARRAY_EXT',
           'GL_MAP1_VERTEX_ATTRIB15_4_NV',
           'GL_OBJECT_COMPILE_STATUS_ARB',
           'GL_LAYER_PROVOKING_VERTEX', 'GL_TEXTURE11_ARB',
           'GL_FASTEST', 'GL_UNSIGNED_SHORT_5_5_5_1_EXT',
           'GL_ALPHA12_EXT', 'GL_LUMINANCE4', 'GL_SRGB8_ALPHA8',
           'glInitNames', 'GL_BUFFER_ACCESS_ARB',
           'GL_TRANSFORM_FEEDBACK_BUFFER_PAUSED', 'glColor3dv',
           'GL_OFFSET_TEXTURE_RECTANGLE_NV',
           'GL_TEXTURE_CUBE_MAP_NEGATIVE_X_ARB',
           'GLU_TESS_EDGE_FLAG_DATA', 'GL_INDEX_BIT_PGI',
           'GL_DRAW_BUFFER8_ATI', 'GL_INT16_VEC2_NV',
           'GL_SAMPLE_MASK_VALUE_SGIS', 'GL_CLIENT_PIXEL_STORE_BIT',
           'GL_PRIMITIVE_RESTART_INDEX', 'GL_DEBUG_SOURCE_API_ARB',
           'GL_INTERLACE_OML', 'GL_LINEAR_SHARPEN_ALPHA_SGIS',
           'GL_UNSIGNED_SHORT_4_4_4_4_EXT',
           'GL_VARIANT_ARRAY_STRIDE_EXT', 'GLUT_HAS_TABLET',
           'GL_POLYGON_BIT', 'GL_LERP_ATI',
           'GL_VERTEX_ARRAY_OBJECT_AMD',
           'GL_MAX_SUBROUTINE_UNIFORM_LOCATIONS',
           'GLU_INVALID_OPERATION', 'GL_PIXEL_TRANSFORM_2D_EXT',
           'GL_VERTEX_ARRAY_BINDING',
           'GL_PROGRAM_NATIVE_ADDRESS_REGISTERS_ARB',
           'glutJoystickGetMinRange', 'GL_ACCUM_BLUE_BITS',
           'GL_SAMPLER_CUBE_ARB',
           'GL_POST_CONVOLUTION_ALPHA_SCALE_EXT', 'GL_CURRENT_NORMAL',
           'GL_DEBUG_SOURCE_WINDOW_SYSTEM_ARB',
           'GL_INT_SAMPLER_RENDERBUFFER_NV', 'glutCopyColormap',
           'GL_COMPRESSED_SIGNED_RED_RGTC1', 'glPixelTransferi',
           'glTexSubImage2D', 'GL_MAX_SHADER_BUFFER_ADDRESS_NV',
           'GL_TIMEOUT_EXPIRED', 'glLogicOp', 'GL_SRC0_ALPHA',
           'glPixelTransferf', 'GL_PRESENT_TIME_NV',
           'GL_LUMINANCE_FLOAT16_ATI', 'GL_UNSIGNED_INT_8_8_8_8_REV',
           'GL_VERTEX_DATA_HINT_PGI', 'GLUT_RED',
           'GL_UNPACK_IMAGE_HEIGHT_EXT',
           'GL_VERTEX_WEIGHT_ARRAY_POINTER_EXT', 'GL_TEXTURE_WIDTH',
           'GL_UNIFORM_SIZE', 'GL_READ_ONLY_ARB',
           'GL_OFFSET_TEXTURE_MATRIX_NV', 'GL_IDENTITY_NV',
           'GL_UNPACK_IMAGE_DEPTH_SGIS', 'GL_DOT3_RGBA',
           'GL_DRAW_BUFFER4_ARB', 'glutFullScreen', 'GLUT_DEPTH',
           'GL_TEXTURE2_ARB', 'GL_COMPRESSED_RG',
           'GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_ARB',
           'GLUT_VIDEO_RESIZE_HEIGHT',
           'GL_FRAGMENT_PROGRAM_BINDING_NV', 'GL_CONSTANT_ARB',
           'GL_MATRIX_INDEX_ARRAY_POINTER_ARB',
           'GL_MAX_COLOR_TEXTURE_SAMPLES',
           'GL_TEXTURE_INTENSITY_TYPE', '__GLsync',
           'GL_RENDERBUFFER_COLOR_SAMPLES_NV',
           'GL_SAMPLE_MASK_INVERT_EXT', 'GL_OUT_OF_MEMORY',
           'GL_TEXTURE30_ARB', 'GL_MAX_TEXTURE_BUFFER_SIZE',
           'GL_COMPRESSED_INTENSITY_ARB',
           'GL_TEXTURE_CLIPMAP_CENTER_SGIX', 'GL_SOURCE1_RGB_EXT',
           'GL_NORMAL_ARRAY_STRIDE',
           'GL_MIN_FRAGMENT_INTERPOLATION_OFFSET',
           'GL_COMPRESSED_LUMINANCE_ALPHA_ARB', 'glTexGeniv',
           'glDrawElements', 'GL_VERTEX_SHADER_INSTRUCTIONS_EXT',
           'GL_PHONG_HINT_WIN', 'GL_CURRENT_TIME_NV',
           'glutSolidCylinder', 'glClientActiveTexture',
           'GL_EVAL_2D_NV', 'GL_GEOMETRY_OUTPUT_TYPE',
           'GL_RASTERIZER_DISCARD', 'uint64_t',
           'GL_WEIGHT_ARRAY_SIZE_ARB', 'GL_COLOR_INDEX1_EXT',
           'GL_R1UI_N3F_V3F_SUN', 'GLUT_GREEN',
           'GL_RENDERBUFFER_SAMPLES_EXT',
           'GL_TEXTURE_BINDING_CUBE_MAP_EXT', 'GL_MODELVIEW12_ARB',
           'GL_LINES_ADJACENCY_EXT',
           'GL_VERTEX_ATTRIB_ARRAY_TYPE_ARB',
           'GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER',
           'glutSetMenuData', 'GL_CON_19_ATI', 'GL_PRIMARY_COLOR_NV',
           'GL_TEXTURE_CUBE_MAP_EXT', 'GL_DRAW_BUFFER2_ATI',
           'GL_MAP2_VERTEX_ATTRIB12_4_NV', 'GL_TEXTURE_2D_ARRAY',
           'GLUT_CURSOR_CYCLE', 'GLU_TESS_VERTEX_DATA',
           'GL_VERTEX_SHADER_LOCAL_CONSTANTS_EXT',
           'GL_EDGE_FLAG_ARRAY', 'glMultiTexCoord2dARB',
           'GL_INT_SAMPLER_2D_MULTISAMPLE',
           'GL_COMPRESSED_SRGB_ALPHA_EXT', 'GL_STENCIL_TEST',
           'GL_ALPHA32UI_EXT', 'GL_OUTPUT_TEXTURE_COORD30_EXT',
           'GL_WEIGHT_ARRAY_TYPE_ARB', 'glMultiTexCoord4ivARB',
           'glutShowWindow', 'GL_QUAD_ALPHA4_SGIS',
           'GL_UNSIGNED_INT8_VEC2_NV', 'GL_UNSIGNED_INT64_NV',
           'GL_PROGRAM_RESULT_COMPONENTS_NV', 'GL_W_EXT', 'GL_INVERT',
           'GL_VERTEX_ATTRIB_MAP2_DOMAIN_APPLE', 'glMaterialiv',
           'GL_UNIFORM_BUFFER_EXT',
           'GL_OFFSET_PROJECTIVE_TEXTURE_2D_NV', 'GLUT_AUX4',
           'GL_DSDT_MAG_NV', 'GL_PIXEL_TILE_GRID_WIDTH_SGIX',
           'GL_DEPTH_COMPONENT32F', 'GL_DEPTH_STENCIL_TO_RGBA_NV',
           'GL_MAX_MATRIX_PALETTE_STACK_DEPTH_ARB',
           'GL_CLIENT_ACTIVE_TEXTURE_ARB', 'glutSolidSphere',
           'GL_PACK_ROW_BYTES_APPLE', 'GL_NORMAL_BIT_PGI',
           'GL_TEXTURE_MAX_CLAMP_R_SGIX',
           'GL_TEXTURE_FILTER_CONTROL_EXT',
           'GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS',
           'glutReshapeWindow', 'GL_MATRIX30_ARB',
           'GL_DEBUG_SOURCE_SHADER_COMPILER_ARB',
           'GL_SAMPLE_ALPHA_TO_MASK_EXT', 'GLUT_MENU_NUM_ITEMS',
           'GL_BUFFER_ACCESS_FLAGS', 'GL_PREVIOUS_EXT',
           'GL_UNIFORM_BUFFER_SIZE', 'glutJoystickSetMinRange',
           'GL_FRAME_NV', 'GL_VERSION_1_4_DEPRECATED',
           'glDisableClientState', 'GL_RED_BITS', 'GL_TEXTURE17_ARB',
           'GL_MAP2_VERTEX_ATTRIB5_4_NV', 'GL_TEXTURE_BUFFER_FORMAT',
           'GL_TEXTURE_LEQUAL_R_SGIX',
           'GL_TEXTURE_COORD_ARRAY_POINTER',
           'GL_TRACK_MATRIX_TRANSFORM_NV',
           'GL_TEXTURE_COMPRESSION_HINT_ARB',
           'GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS',
           'GL_MAX_SUBROUTINES',
           'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_EXT',
           'GLUT_NUM_BUTTON_BOX_BUTTONS', 'glutJoystickGetMaxRange',
           'GLU_INCOMPATIBLE_GL_VERSION', 'GL_MAGNITUDE_BIAS_NV',
           'GL_COMPARE_REF_DEPTH_TO_TEXTURE_EXT', 'GL_DOT3_RGBA_EXT',
           'GL_VERTEX_ARRAY_TYPE_EXT', 'GL_VARIANT_DATATYPE_EXT',
           'GL_BGRA', 'GL_ACTIVE_UNIFORM_BLOCKS', 'glEvalMesh2',
           'glEvalMesh1', 'GL_SHADER_OBJECT_ARB',
           'GL_COLOR_TABLE_BIAS_SGI', 'GL_REG_2_ATI', 'GL_RGB_SNORM',
           'GLUT_SCREEN_HEIGHT_MM', 'GL_RGB16I',
           'GL_LINEAR_SHARPEN_SGIS', 'GL_CURRENT_MATRIX_INDEX_ARB',
           'GL_TEXTURE_2D_STACK_BINDING_MESAX', 'glEvalCoord2fv',
           'GL_NUM_VIDEO_CAPTURE_STREAMS_NV',
           'GL_UNSIGNED_INT_IMAGE_2D_RECT_EXT', 'GL_MODELVIEW31_ARB',
           'GL_UNSIGNED_INT_SAMPLER_2D_EXT',
           'GL_FRAGMENT_LIGHT_MODEL_AMBIENT_SGIX',
           'GL_DEBUG_PRINT_MESA',
           'GL_VERTEX_ARRAY_RANGE_WITHOUT_FLUSH_NV',
           'glLoadTransposeMatrixf', 'GL_DEBUG_SEVERITY_LOW_AMD',
           'GL_MINOR_VERSION', 'GL_FOG_BIT', 'GL_OPERAND0_ALPHA',
           'GL_CURRENT_PALETTE_MATRIX_ARB',
           'GL_COLOR_ATTACHMENT4_EXT', 'GL_UNIFORM_BLOCK_NAME_LENGTH',
           'GL_EDGE_FLAG_ARRAY_STRIDE_EXT',
           'GL_MAX_RECTANGLE_TEXTURE_SIZE_ARB',
           'GL_FOG_COORDINATE_ARRAY_STRIDE_EXT', 'GLU_PATH_LENGTH',
           'GL_ALL_ATTRIB_BITS', 'GLUT_ALPHA',
           'GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_EVALUATION_SHADER',
           'GL_POST_TEXTURE_FILTER_SCALE_SGIX',
           'GL_IR_INSTRUMENT1_SGIX', 'GL_TEXTURE_GEN_Q',
           'GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW_ARB',
           'GL_POST_COLOR_MATRIX_RED_BIAS', 'GL_CONDITION_SATISFIED',
           'GL_SUB_ATI', 'GL_CONTEXT_FLAG_FORWARD_COMPATIBLE_BIT',
           'GL_SAMPLER_BUFFER_AMD', 'GL_CURRENT_MATRIX_ARB',
           'GL_GENERIC_ATTRIB_NV', 'GLUT_KEY_DELETE',
           'GL_SAMPLES_ARB', 'GL_MODELVIEW1_EXT',
           'GL_SECONDARY_COLOR_ARRAY_POINTER', 'GL_BGR_INTEGER_EXT',
           'GL_TEXTURE_COMPARE_MODE_ARB',
           'GL_VERTEX_PROGRAM_CALLBACK_MESA',
           'GLUT_DISPLAY_MODE_POSSIBLE', 'GL_MAX_VARYING_COMPONENTS',
           'GL_VIDEO_BUFFER_NV', 'GL_CLIP_NEAR_HINT_PGI',
           'GL_INTERLACE_READ_OML', 'GLuint64', 'GL_PREVIOUS_ARB',
           'GL_TEXTURE_1D_ARRAY', 'GL_CURRENT_VERTEX_ATTRIB_ARB',
           'GL_TEXTURE_2D_STACK_MESAX',
           'GL_VIDEO_CAPTURE_FRAME_WIDTH_NV',
           'GL_READ_FRAMEBUFFER_BINDING', 'GL_VERTEX_SHADER_ARB',
           'GL_FRAMEBUFFER_ATTACHMENT_LAYERED',
           'GL_PIXEL_PACK_BUFFER_EXT', 'GL_COORD_REPLACE',
           'GL_GEOMETRY_DEFORMATION_SGIX', 'GL_SAMPLE_BUFFERS_3DFX',
           'GL_UNIFORM_ARRAY_STRIDE', 'GL_SURFACE_STATE_NV',
           'GL_IMAGE_2D_MULTISAMPLE_ARRAY_EXT',
           'GL_POINT_SIZE_MAX_SGIS', 'glClipPlane',
           'GL_VERTEX_PROGRAM_NV', 'GL_DEPTH_STENCIL_MESA',
           'glIndexub', 'GL_MAX_VERTEX_ATTRIBS_ARB', 'GL_RGB16UI_EXT',
           'GL_LUMINANCE_ALPHA16I_EXT', 'GL_COMBINER_AB_OUTPUT_NV',
           'GLUT_AUX', 'GLUT_WINDOW_BLUE_SIZE', 'GL_INFO_LOG_LENGTH',
           'GL_EVAL_VERTEX_ATTRIB10_NV',
           'GL_COMPRESSED_SIGNED_RED_GREEN_RGTC2_EXT',
           'GLUT_WINDOW_CURSOR', 'GL_DRAW_BUFFER10_ATI',
           'GL_WEIGHT_SUM_UNITY_ARB',
           'GL_FRAGMENT_LIGHT_MODEL_TWO_SIDE_SGIX',
           'GL_COMPRESSED_LUMINANCE_ALPHA_LATC2_EXT',
           'GL_RENDERBUFFER_HEIGHT_EXT', 'GL_REFLECTION_MAP_EXT',
           'GL_COMBINE_RGB_ARB', 'GL_LUMINANCE_ALPHA_FLOAT16_ATI',
           'GL_DUAL_LUMINANCE8_SGIS', 'GL_FAILURE_NV',
           'GL_PIXEL_BUFFER_BARRIER_BIT_EXT', 'GL_SRGB_ALPHA_EXT',
           'GL_RGB16I_EXT', 'GL_RESCALE_NORMAL',
           'GL_DEBUG_SOURCE_APPLICATION_ARB',
           'GL_VERTEX_ATTRIB_MAP1_COEFF_APPLE', 'GL_FIELDS_NV',
           'glutInitContextProfile', 'GL_LOCAL_CONSTANT_EXT',
           'GL_DUAL_INTENSITY16_SGIS',
           'GL_PERSPECTIVE_CORRECTION_HINT', 'GL_VERSION_2_0',
           'GL_TEXTURE_CUBE_MAP_POSITIVE_Y', 'GL_GEOMETRY_SHADER_BIT',
           'GLUT_STENCIL', 'glutWireTeapot', 'GL_SAMPLE_POSITION_NV',
           'GL_MAP_READ_BIT', 'GL_ALPHA_INTEGER_EXT',
           'GLU_NURBS_COLOR_DATA', 'GL_COMBINER6_NV', 'GLuint',
           'GL_WRITE_PIXEL_DATA_RANGE_POINTER_NV',
           'GL_POST_CONVOLUTION_ALPHA_SCALE', 'glMultiTexCoord1fv',
           'GL_VERTEX_ARRAY_ADDRESS_NV', 'GL_LUMINANCE12',
           'GL_NUM_PASSES_ATI', 'GL_LINE_BIT',
           'GLUT_WINDOW_NUM_SAMPLES', 'GL_TEXTURE20_ARB',
           'GL_VERTEX_ATTRIB_ARRAY11_NV', 'GL_OP_NEGATE_EXT',
           'GL_DEBUG_TYPE_OTHER_ARB', 'GL_T2F_N3F_V3F',
           'GL_COMBINER4_NV', 'GL_TRANSFORM_BIT', 'GL_RELEASED_APPLE',
           'glutInitWindowPosition', 'GL_INTENSITY16I_EXT',
           'GL_MAP1_VERTEX_ATTRIB3_4_NV', 'GL_MODELVIEW9_ARB',
           'GL_TEXTURE_COLOR_WRITEMASK_SGIS',
           'GL_ONE_MINUS_CONSTANT_COLOR',
           'GL_CULL_VERTEX_EYE_POSITION_EXT',
           'GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT1_EXT',
           'GL_WRITE_PIXEL_DATA_RANGE_LENGTH_NV',
           'GL_UNSIGNED_INT_8_8_8_8', 'glColor3us',
           'glMultiTexCoord4s', 'GL_OBJECT_DISTANCE_TO_POINT_SGIS',
           'GL_RGB_S3TC', 'glutIgnoreKeyRepeat', 'glGetLightiv',
           'GL_ONE_MINUS_DST_ALPHA', 'GL_ALPHA12',
           'GL_INDEX_ARRAY_POINTER', 'GL_ALPHA16',
           'glMultiTexCoord4f', 'glColor3ub', 'glMultiTexCoord4d',
           'GL_FOG_OFFSET_SGIX', 'glColor3ui',
           'GL_PROGRAM_FORMAT_ASCII_ARB', 'glMultiTexCoord4i',
           'GL_FRAMEBUFFER_UNSUPPORTED_EXT',
           'GLUT_WINDOW_STENCIL_SIZE', 'glMultiTexCoord1ivARB',
           'GL_TEXTURE_PRIORITY', 'glGetPolygonStipple',
           'GL_POINT_SIZE_MIN', 'GL_LOSE_CONTEXT_ON_RESET_ARB',
           'GL_RGBA12', 'GL_GENERATE_MIPMAP_HINT',
           'GL_STREAM_COPY_ARB', 'GL_RGBA16', 'glDepthFunc',
           'GL_MAX_CLIPMAP_DEPTH_SGIX',
           'GL_FRAMEBUFFER_ATTACHMENT_LAYERED_EXT', 'GL_MAP1_NORMAL',
           'glBlendEquation', 'GL_COMBINER0_NV',
           'GL_DOT_PRODUCT_TEXTURE_RECTANGLE_NV',
           'glutSolidSierpinskiSponge', 'GL_COMPRESSED_RGB_FXT1_3DFX',
           'GL_HALF_BIT_ATI', 'GL_CON_31_ATI', 'glMultiTexCoord3dv',
           'glColor4sv', 'GL_LUMINANCE32I_EXT', 'glPopClientAttrib',
           'GL_PIXEL_TEX_GEN_ALPHA_LS_SGIX', 'GL_RGB5_A1',
           'GL_DEPTH_ATTACHMENT', 'GL_UNPACK_SKIP_PIXELS',
           'GL_SECONDARY_COLOR_NV', 'GL_QUERY_COUNTER_BITS',
           'GL_PERFORMANCE_MONITOR_AMD', 'glColor3iv',
           'glutSolidDodecahedron', 'GL_FOG_HINT',
           'glCompressedTexImage1D', 'GL_COMP_BIT_ATI',
           'GL_TEXTURE_GEQUAL_R_SGIX', 'GLUT_GAME_MODE_WIDTH',
           'GL_OFFSET_HILO_PROJECTIVE_TEXTURE_RECTANGLE_NV',
           'GL_VERTEX_SHADER_BIT', 'GL_DEPTH_COMPONENT32_SGIX',
           'GL_MAX_FRAGMENT_INTERPOLATION_OFFSET_NV',
           'GL_ATTACHED_SHADERS', 'GL_FRAMEBUFFER_COMPLETE_EXT',
           'GL_UNSIGNED_INT64_AMD', 'GL_LINEAR_MIPMAP_NEAREST',
           'GL_SECONDARY_INTERPOLATOR_ATI',
           'GL_VERTEX_ATTRIB_MAP2_ORDER_APPLE', 'GL_LAYER_NV',
           'GLdouble', 'GLU_TESS_ERROR5',
           'GL_DEBUG_CALLBACK_FUNCTION_ARB', 'GL_RGB10_A2',
           'GL_ACTIVE_SUBROUTINE_MAX_LENGTH', 'GL_SOURCE0_ALPHA_EXT',
           'GL_VERTEX_ARRAY_RANGE_POINTER_NV',
           'GL_LAST_VIDEO_CAPTURE_STATUS_NV',
           'GL_READ_FRAMEBUFFER_EXT',
           'GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS',
           'GL_RESAMPLE_REPLICATE_OML', 'GLU_VERSION',
           'GL_MAP1_VERTEX_ATTRIB13_4_NV', 'GLU_TESS_EDGE_FLAG',
           'GLUT_NORMAL', 'GL_FOG_COORD_ARRAY_TYPE',
           'GL_INTENSITY_EXT', 'ptrdiff_t', 'GL_MAX_VERTEX_STREAMS',
           'GL_SAMPLE_ALPHA_TO_ONE_ARB', 'GL_UNPACK_SWAP_BYTES',
           'GLUT_VIDEO_RESIZE_WIDTH_DELTA',
           'GL_DEBUG_OUTPUT_SYNCHRONOUS_ARB',
           'GL_PIXEL_MAP_I_TO_A_SIZE', 'GL_CONSTANT_BORDER_HP',
           'GL_SMOOTH_POINT_SIZE_GRANULARITY',
           'GL_CLAMP_VERTEX_COLOR', 'GL_DOUBLE_VEC2',
           'GL_INVARIANT_DATATYPE_EXT',
           'GL_TRANSPOSE_COLOR_MATRIX_ARB', 'GL_MAP2_INDEX',
           'GL_VIEWPORT_INDEX_PROVOKING_VERTEX',
           'GL_EVAL_TRIANGULAR_2D_NV', 'GL_LO_BIAS_NV',
           'GL_EDGE_FLAG_ARRAY_LENGTH_NV', 'GL_VERTEX4_BIT_PGI',
           'GL_CON_25_ATI', 'GL_IMAGE_BINDING_LAYER_EXT',
           'GL_NOTEQUAL', 'GL_TEXTURE_COORD_ARRAY',
           'GL_TEXTURE_SWIZZLE_RGBA_EXT',
           'GL_COLOR_TABLE_GREEN_SIZE_SGI',
           'GL_FLOAT_32_UNSIGNED_INT_24_8_REV', 'GL_LINES',
           'GL_MAP2_GRID_DOMAIN', 'GL_UNSIGNED_INT16_VEC2_NV',
           'GL_INT_SAMPLER_1D_ARRAY', 'GL_DATA_BUFFER_AMD',
           'GL_SEPARATE_SPECULAR_COLOR_EXT', 'GL_TEXTURE_RED_SIZE',
           'GL_VIDEO_CAPTURE_TO_422_SUPPORTED_NV',
           'GLU_NURBS_ERROR35', 'GL_OBJECT_LINEAR',
           'GL_OUTPUT_TEXTURE_COORD3_EXT', 'glutGetMenu',
           'GL_SIGNED_IDENTITY_NV', 'GL_CURRENT_ATTRIB_NV',
           'GL_COLOR_ATTACHMENT14_EXT', 'GL_CURRENT_QUERY_ARB',
           'GL_TEXTURE14', 'GL_RGBA12_EXT',
           'GL_FRAGMENT_INTERPOLATION_OFFSET_BITS', 'GL_COMBINER2_NV',
           'GL_OFFSET_PROJECTIVE_TEXTURE_2D_SCALE_NV',
           'GL_OPERAND2_ALPHA_EXT', 'GL_TEXTURE_FLOAT_COMPONENTS_NV',
           'GL_POST_CONVOLUTION_BLUE_BIAS', 'glEvalPoint1',
           'GL_FRAGMENT_SHADER_ARB', 'glEvalPoint2',
           'GL_SATURATE_BIT_ATI', 'GL_OBJECT_DISTANCE_TO_LINE_SGIS',
           'GL_TEXTURE13', 'glutJoystickSetMaxRange',
           'GL_TEXTURE_SHARED_SIZE', 'GL_POLYGON_STIPPLE_BIT',
           'glTexSubImage1D', 'GL_RED_MAX_CLAMP_INGR',
           'GL_MAX_FRAGMENT_UNIFORM_BLOCKS',
           'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_EXT',
           'GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS', 'GL_DOUBLE_VEC4_EXT',
           'GL_TESS_CONTROL_PROGRAM_PARAMETER_BUFFER_NV',
           'glutWireSierpinskiSponge', 'GL_MAP1_VERTEX_ATTRIB10_4_NV',
           'GL_SHORT', 'GL_TEXTURE_4D_SGIS', 'GLUT_CURSOR_INFO',
           'GL_CURRENT_SECONDARY_COLOR_EXT', 'GL_CW',
           'GL_STATIC_COPY', 'GL_LINEAR_DETAIL_COLOR_SGIS',
           'GL_STENCIL_BACK_FUNC_ATI',
           'GL_MAX_VERTEX_UNIFORM_COMPONENTS',
           'GL_RENDERBUFFER_RED_SIZE_EXT', 'GLcharARB',
           'glRasterPos4dv', 'GL_SAMPLE_ALPHA_TO_MASK_SGIS',
           'GL_DEPTH_TEXTURE_MODE',
           'GL_OFFSET_HILO_PROJECTIVE_TEXTURE_2D_NV',
           'GL_UNSIGNED_INT_10F_11F_11F_REV', 'GLprogramcallbackMESA',
           'GL_LUMINANCE16_SNORM', 'GL_TEXTURE_SHADER_NV',
           'GL_TEXTURE_COORD_ARRAY_LIST_IBM',
           'GLUT_WINDOW_GREEN_SIZE', 'GL_STATIC_DRAW', 'glLoadName',
           'GL_RENDERBUFFER', 'GL_FOG_SCALE_VALUE_SGIX',
           'GL_INT_IMAGE_2D_EXT', 'GL_TEXTURE_BORDER_VALUES_NV',
           'GL_VERTEX_STATE_PROGRAM_NV', 'glutSetMenu',
           'glLoadMatrixf', 'glLoadMatrixd', 'glTexParameterfv',
           'GL_INTENSITY16_EXT', 'GL_VBO_FREE_MEMORY_ATI',
           'GL_INDEX_ARRAY_TYPE_EXT',
           'GL_TRANSFORM_FEEDBACK_BUFFER_MODE_EXT',
           'GL_SOURCE0_ALPHA_ARB', 'GLU_NURBS_NORMAL',
           'GL_PER_STAGE_CONSTANTS_NV',
           'GL_OUTPUT_TEXTURE_COORD0_EXT',
           'GL_MAX_PROGRAM_NATIVE_ALU_INSTRUCTIONS_ARB',
           'GL_TEXTURE_CUBE_MAP_ARB', 'GLUT_CURSOR_LEFT_RIGHT',
           'GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET', 'GL_OR_INVERTED',
           'glMultiTexCoord1svARB', 'GL_TEXTURE_GREEN_SIZE',
           'GL_PIXEL_MAG_FILTER_EXT', 'GL_HISTOGRAM_GREEN_SIZE_EXT',
           'GL_BUFFER_USAGE_ARB', 'glGetConvolutionFilter',
           'GL_OUTPUT_TEXTURE_COORD5_EXT', 'GL_TEXTURE9_ARB',
           'GL_TEXTURE_MAX_LOD_SGIS', 'GL_FULL_STIPPLE_HINT_PGI',
           'GL_FRAGMENT_LIGHT_MODEL_NORMAL_INTERPOLATION_SGIX',
           'GL_INTENSITY4', 'glPopName', 'GL_MAX_ACTIVE_LIGHTS_SGIX',
           'GL_POLYGON_OFFSET_FACTOR_EXT', 'GL_INTENSITY8',
           'GL_DEPTH_STENCIL_TO_BGRA_NV',
           'GL_TEXTURE_COORD_ARRAY_ADDRESS_NV',
           'GL_TEXTURE_BLUE_TYPE', 'GL_REFLECTION_MAP_NV',
           'GL_SIGNED_LUMINANCE8_ALPHA8_NV',
           'GL_VERTEX_ATTRIB_ARRAY_DIVISOR', 'GL_LIST_PRIORITY_SGIX',
           'GL_COLOR_SUM_ARB', 'GL_FOG_COORD_SRC', 'GL_RGB8_SNORM',
           'GL_PIXEL_MAP_I_TO_I_SIZE',
           'GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET_NV',
           'GLUT_LUMINANCE', 'GL_UNSIGNED_SHORT_8_8_APPLE',
           'GL_SAMPLE_COVERAGE_ARB', 'GL_DECAL', 'GL_INTENSITY16',
           'GL_SELECTION_BUFFER_POINTER', 'GL_INT_IMAGE_BUFFER_EXT',
           'GL_MAX_MULTISAMPLE_COVERAGE_MODES_NV', 'GL_TRIANGLE_FAN',
           'GLU_NURBS_TEX_COORD_DATA_EXT', 'glutSetWindow',
           'GL_OBJECT_BUFFER_SIZE_ATI', 'GL_SAMPLES',
           'GL_LUMINANCE_ALPHA_FLOAT16_APPLE',
           'GL_FRAMEBUFFER_BINDING_EXT',
           'GL_VERTEX_PROGRAM_POINT_SIZE_ARB',
           'GL_DEBUG_LOGGED_MESSAGES_AMD', 'GL_UNSIGNED_INT_VEC3',
           'GL_INTENSITY_FLOAT32_APPLE', 'GL_UNSIGNED_SHORT_5_6_5',
           'GL_COLOR_ARRAY_EXT', 'GL_RGBA16UI_EXT', 'GL_MATRIX21_ARB',
           'GL_BUFFER_SERIALIZED_MODIFY_APPLE', 'GL_R1UI_V3F_SUN',
           'GL_MAX_VARYING_COMPONENTS_EXT',
           'GLUT_COMPATIBILITY_PROFILE',
           'GL_TEXTURE_BUFFER_FORMAT_EXT', 'GL_REG_11_ATI',
           'GL_LUMINANCE_INTEGER_EXT', 'GL_HISTOGRAM_RED_SIZE_EXT',
           'GL_RGBA_MODE', 'glRectdv',
           'GL_POST_COLOR_MATRIX_BLUE_SCALE', 'GL_AVERAGE_HP',
           'GLU_TESS_WINDING_ODD', 'GL_REG_1_ATI', 'GL_REG_29_ATI',
           'GL_NEGATIVE_Z_EXT', 'GL_SPRITE_MODE_SGIX',
           'GL_ELEMENT_ARRAY_POINTER_ATI', 'GL_SOURCE1_ALPHA_EXT',
           'GLUT_NOT_VISIBLE', 'GL_TEXTURE_LUMINANCE_TYPE_ARB',
           'GL_RGB32UI', 'GL_STENCIL_BACK_FAIL_ATI',
           'GL_MAX_PROGRAM_LOCAL_PARAMETERS_ARB',
           'GL_GREEN_INTEGER_EXT', 'GL_TEXTURE4_ARB', 'GL_READ_WRITE',
           'GL_INDEX_TEST_EXT', 'GLUT_MIDDLE_BUTTON',
           'GL_PROXY_TEXTURE_RECTANGLE',
           'GL_POST_COLOR_MATRIX_ALPHA_BIAS', 'GL_INT_SAMPLER_3D',
           'glutDetachMenu', 'GL_ALPHA16_SNORM', 'glIndexfv',
           'GL_MATRIX_INDEX_ARRAY_TYPE_ARB', 'GLUT_SCREEN_HEIGHT',
           'GL_QUERY_BY_REGION_NO_WAIT_NV',
           'GL_UNSIGNED_INT_SAMPLER_CUBE_EXT', 'GL_CON_13_ATI',
           'GL_PN_TRIANGLES_POINT_MODE_LINEAR_ATI', 'glutWMCloseFunc',
           'GL_UNSIGNED_SHORT_15_1_MESA', 'GL_RGB16', 'GL_TEXTURE8',
           'GL_MAP2_TANGENT_EXT', 'GL_DEBUG_CALLBACK_USER_PARAM_ARB',
           'GL_ACTIVE_VARYINGS_NV', 'GL_TEXTURE5', 'GL_TEXTURE6',
           'GL_TEXTURE7', 'GL_TEXTURE0', 'GL_CONTEXT_PROFILE_MASK',
           'GL_TEXTURE2', 'GL_TEXTURE3', 'GL_FLOAT_VEC2_ARB',
           'GL_BOOL_VEC4', 'GL_WRITE_PIXEL_DATA_RANGE_NV',
           'GL_RENDERBUFFER_BINDING_EXT', 'glutGetProcAddress',
           'GL_BOOL_VEC3', 'GL_BOOL_VEC2', 'GLU_NURBS_ERROR14',
           'glutWireTetrahedron', 'GL_STREAM_READ_ARB',
           'glutWireOctahedron',
           'GL_DEBUG_CATEGORY_SHADER_COMPILER_AMD',
           'GL_OBJECT_VALIDATE_STATUS_ARB',
           'GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS',
           'GL_COLOR_MATERIAL_PARAMETER', 'GL_INDEX_MODE',
           'glCompressedTexImage2D', 'GL_ONE',
           'glutPostOverlayRedisplay',
           'GL_OUTPUT_TEXTURE_COORD23_EXT', 'GL_FLOAT_MAT2_ARB',
           'glVertex4fv', 'GL_MAX_ELEMENTS_INDICES_EXT',
           'GL_NAMED_STRING_TYPE_ARB', 'GL_SRC_ALPHA_SATURATE',
           'GL_COLOR_ARRAY_POINTER_EXT', 'GL_VECTOR_EXT',
           'GL_R1UI_C3F_V3F_SUN', 'GL_SAMPLE_MASK_VALUE_EXT',
           'glMultiTexCoord4dvARB', 'glMultiTexCoord1sv',
           'GL_OUTPUT_VERTEX_EXT', 'GL_TRIANGLE_STRIP', 'GL_N3F_V3F',
           'GL_DEPTH_CLAMP_NEAR_AMD',
           'GL_TRANSFORM_FEEDBACK_VARYINGS_EXT', 'glRasterPos2s',
           'GL_UNSIGNED_INT8_VEC3_NV', 'GL_FRONT_LEFT',
           'GL_PIXEL_TEX_GEN_Q_CEILING_SGIX', 'GL_DRAW_PIXELS_APPLE',
           'GLU_TESS_COMBINE', 'GL_CLAMP', 'GL_PERCENTAGE_AMD',
           'GL_EMBOSS_LIGHT_NV', 'GL_RESCALE_NORMAL_EXT',
           'GL_OUTPUT_TEXTURE_COORD14_EXT',
           'GLU_TESS_MISSING_BEGIN_CONTOUR', 'GL_INDEX_OFFSET',
           'glGetSeparableFilter', 'GL_INTENSITY', 'glColor4bv',
           'glRasterPos2f', 'glutStrokeLength', 'glRasterPos2d',
           'glLoadIdentity', 'glRasterPos2i',
           'GL_DEBUG_CATEGORY_OTHER_AMD', 'GL_TEXCOORD4_BIT_PGI',
           'GL_NATIVE_GRAPHICS_END_HINT_PGI',
           'GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY', 'GL_CON_7_ATI',
           'glutPostWindowOverlayRedisplay', 'GL_CLIP_FAR_HINT_PGI',
           'GLU_VERTEX', 'GL_STENCIL_FUNC',
           'GL_MAX_FRAGMENT_BINDABLE_UNIFORMS_EXT',
           'GLU_TESS_MISSING_END_POLYGON', 'GL_TEXTURE_ENV',
           'GL_DRAW_BUFFER8_ARB', 'GL_INT_SAMPLER_2D_ARRAY',
           'GL_DECR', 'GL_BACK', 'GL_PRIMITIVE_RESTART_INDEX_NV',
           'GL_MAJOR_VERSION', 'glutJoystickFunc',
           'GL_LUMINANCE8UI_EXT', 'glTexCoord1iv', 'GL_INT',
           'GL_VERTEX_ATTRIB_ARRAY_POINTER', 'GL_MODELVIEW2_ARB',
           'GL_SAMPLE_COVERAGE_INVERT_ARB',
           'GL_LUMINANCE8_ALPHA8_EXT', 'GL_CLIP_DISTANCE1',
           'GL_CLIP_DISTANCE0', 'GL_CLIP_DISTANCE3',
           'GL_CLIP_DISTANCE2', 'GL_CLIP_DISTANCE5',
           'GL_CLIP_DISTANCE4', 'GL_CLIP_DISTANCE7',
           'GL_CLIP_DISTANCE6', 'GL_COMPRESSED_RGBA_S3TC_DXT5_EXT',
           'GL_UNSIGNED_INT_VEC2', 'GL_IMAGE_TRANSLATE_Y_HP',
           'GL_FRONT_AND_BACK', 'GL_VERTEX_ATTRIB_MAP1_DOMAIN_APPLE',
           'GL_COMPRESSED_RG_RGTC2',
           'GL_MAX_PROGRAM_TEX_INSTRUCTIONS_ARB',
           'GL_VERTEX_ATTRIB_ARRAY_UNIFIED_NV', 'GLUT_CAPTIONLESS',
           'GL_EXPAND_NEGATE_NV', 'GL_TEXTURE_COORD_ARRAY_SIZE_EXT',
           'GL_MAX_VERTEX_ARRAY_RANGE_ELEMENT_NV',
           'GL_PROXY_TEXTURE_1D_STACK_MESAX', 'GL_SYNC_FENCE',
           'GLU_FLAT', 'GL_SIGNED_ALPHA8_NV',
           'GLUT_WINDOW_ACCUM_ALPHA_SIZE', 'GL_MODELVIEW3_ARB',
           'GL_TEXTURE_SWIZZLE_RGBA', 'glMultiTexCoord2sv',
           'GL_SECONDARY_COLOR_ARRAY_LIST_IBM',
           'GL_NAMED_STRING_LENGTH_ARB', 'GL_UNSIGNED_SHORT_4_4_4_4',
           'GL_TEXTURE_ALPHA_SIZE', 'GL_PROXY_TEXTURE_3D',
           'GL_VERTEX_SHADER_BINDING_EXT', 'GLUT_HAS_SPACEBALL',
           'GL_DOUBLE_VEC4', 'GL_OFFSET_TEXTURE_BIAS_NV',
           'GL_DEPTH_COMPONENT32_ARB', 'GL_DOUBLE_VEC3',
           'GL_TRANSPOSE_TEXTURE_MATRIX', 'GL_TEXTURE_SWIZZLE_B_EXT',
           'GL_VERTEX_ATTRIB_ARRAY14_NV',
           'GL_UNSIGNED_INT_8_8_S8_S8_REV_NV',
           'glutJoystickGetCenter', 'GL_LINE_STIPPLE_REPEAT',
           'glutJoystickSetCenter', 'GL_MODULATE_ADD_ATI',
           'GL_EVAL_VERTEX_ATTRIB8_NV', 'GL_CURRENT_SECONDARY_COLOR',
           'GL_DEPTH_COMPONENT32F_NV', 'glutBitmapHelvetica18',
           'GL_TESS_EVALUATION_PROGRAM_NV', 'glutBitmapHelvetica12',
           'GL_SAMPLER_2D_SHADOW_ARB', 'glutBitmapHelvetica10',
           'GL_MAX_OPTIMIZED_VERTEX_SHADER_VARIANTS_EXT',
           'GL_TEXTURE_BINDING_2D_ARRAY',
           'GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT',
           'GL_MAX_DRAW_BUFFERS', 'GL_MODELVIEW21_ARB',
           'GL_MAX_DEBUG_MESSAGE_LENGTH_ARB', 'GL_RED_SCALE',
           'GL_LIGHT_MODEL_SPECULAR_VECTOR_APPLE',
           'GL_VERTEX_ARRAY_BUFFER_BINDING_ARB', 'glGetMaterialfv',
           'GL_SECONDARY_COLOR_ARRAY', 'GL_RGBA8_EXT',
           'GL_FLOAT_32_UNSIGNED_INT_24_8_REV_NV', 'glPixelMapuiv',
           'GL_TEXTURE_ENV_MODE', 'GL_CURRENT_INDEX',
           'GL_PATCH_DEFAULT_INNER_LEVEL', 'GL_TEXTURE15',
           'glutTabletMotionFunc',
           'GL_TESS_EVALUATION_PROGRAM_PARAMETER_BUFFER_NV',
           'GL_BLEND_EQUATION_ALPHA_EXT', 'GL_COLOR_TABLE_ALPHA_SIZE',
           'GL_E_TIMES_F_NV', 'GL_COLOR_ATTACHMENT9_EXT',
           'GL_TEXT_FRAGMENT_SHADER_ATI',
           'GL_MAX_PROGRAM_MATRIX_STACK_DEPTH_ARB',
           'glMultiTexCoord1dARB', 'GL_REFLECTION_MAP',
           'GL_LUMINANCE32UI_EXT', 'GL_BGR_INTEGER',
           'GL_CONVOLUTION_HEIGHT_EXT',
           'GL_COLOR_MATRIX_STACK_DEPTH_SGI',
           'GL_ALL_BARRIER_BITS_EXT',
           'GL_MAX_FRAGMENT_UNIFORM_COMPONENTS_ARB',
           'GL_UNIFORM_BUFFER_BINDING', 'GL_UNIFORM_TYPE',
           'GL_DELETE_STATUS', 'GL_MODELVIEW0_ARB',
           'GL_ONE_MINUS_SRC1_ALPHA', 'GL_TEXTURE_BASE_LEVEL',
           'GLU_NONE', 'GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT_EXT',
           'GL_STATIC_DRAW_ARB',
           'GL_RENDERBUFFER_COVERAGE_SAMPLES_NV',
           'glConvolutionParameteriv', 'GL_COMMAND_BARRIER_BIT_EXT',
           'GL_COLOR_ATTACHMENT13_EXT', 'GL_LUMINANCE8_ALPHA8_SNORM',
           'GL_STENCIL_INDEX8_EXT', 'GL_POINT_BIT',
           'GL_DRAW_BUFFER7_ATI', 'GL_SIGNED_LUMINANCE8_NV',
           'glEnable', 'GL_GLOBAL_ALPHA_SUN', 'GL_LUMINANCE8',
           'GL_FRONT_RIGHT', 'GLU_NURBS_COLOR',
           'GL_MAP_INVALIDATE_BUFFER_BIT', 'GL_MODELVIEW4_ARB',
           'GL_FRACTIONAL_ODD', 'GL_DEPTH_TEST', 'GLUT_KEY_END',
           'GL_OPERAND3_ALPHA_NV', 'GL_PIXEL_TEX_GEN_MODE_SGIX',
           'GL_IMAGE_BINDING_LAYERED_EXT', 'GL_MULTISAMPLE',
           'GL_COLOR_TABLE_WIDTH', 'GL_TEXTURE_RED_TYPE',
           'GL_FOG_INDEX', 'GLU_INVALID_ENUM',
           'GL_SECONDARY_COLOR_ARRAY_POINTER_EXT',
           'GL_FRAGMENT_PROGRAM_CALLBACK_DATA_MESA',
           'GL_CONSTANT_ALPHA_EXT', 'GL_FUNC_SUBTRACT',
           'GL_VERTEX_PROGRAM_TWO_SIDE', 'GL_MAX_TESS_GEN_LEVEL',
           'GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH',
           'GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING',
           'glutSolidRhombicDodecahedron',
           'GL_VIDEO_CAPTURE_FIELD_UPPER_HEIGHT_NV',
           'GL_CLAMP_TO_BORDER', 'GL_COLOR_ATTACHMENT15',
           'glutHideOverlay', 'GLU_TESS_END_DATA', 'GL_DEPTH_RANGE',
           'GL_COLOR_ATTACHMENT11', 'GL_CLAMP_TO_EDGE',
           'GL_COLOR_ATTACHMENT13', 'GL_COLOR_ATTACHMENT12',
           'GL_DSDT_MAG_INTENSITY_NV', 'glPushMatrix',
           'GL_NEAREST_CLIPMAP_LINEAR_SGIX', 'glOrtho',
           'GL_DUAL_LUMINANCE_ALPHA4_SGIS', 'GL_DT_SCALE_NV',
           'GLU_NURBS_ERROR23', 'GL_MAX_RATIONAL_EVAL_ORDER_NV',
           'GL_RENDERBUFFER_GREEN_SIZE',
           'GL_MAX_DUAL_SOURCE_DRAW_BUFFERS', 'GL_QUAD_ALPHA8_SGIS',
           'GLU_PARAMETRIC_TOLERANCE', 'GL_SPRITE_SGIX',
           'GL_PIXEL_MAP_S_TO_S_SIZE',
           'GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT',
           'GL_SWIZZLE_STRQ_ATI', 'glIndexiv', 'GLU_U_STEP',
           'GL_NORMAL_ARRAY',
           'GL_IMPLEMENTATION_COLOR_READ_FORMAT_OES',
           'GL_TRANSFORM_FEEDBACK_BUFFER_EXT', 'glPixelZoom',
           'GL_DYNAMIC_DRAW_ARB', 'GL_CONTINUOUS_AMD',
           'GL_POINT_SMOOTH', 'GLUT_GAME_MODE_ACTIVE',
           'GL_DEPTH_CLEAR_VALUE',
           'GL_VIDEO_CAPTURE_FIELD_LOWER_HEIGHT_NV',
           'GL_UNSIGNED_INT_SAMPLER_BUFFER_EXT',
           'GL_GEOMETRY_INPUT_TYPE', 'GLU_OUTLINE_POLYGON',
           'glMinmax', 'glutBitmapTimesRoman24', 'GLU_LINE',
           'GLU_EDGE_FLAG',
           'GL_MAX_PROGRAM_TOTAL_OUTPUT_COMPONENTS_NV',
           'GL_PROGRAM_ERROR_STRING_NV', 'GL_COMBINER7_NV',
           'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE', 'GL_CURRENT_BIT',
           'GL_PROXY_TEXTURE_COLOR_TABLE_SGI',
           'GL_T2F_IUI_N3F_V3F_EXT', 'GLU_MAP1_TRIM_2',
           'GL_RGBA32F_ARB', 'GL_VERTEX_PRECLIP_SGIX',
           'GL_BLEND_COLOR_EXT', 'GL_MAX_VARYING_FLOATS',
           'GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS',
           'GL_SIGNED_LUMINANCE_NV', 'GL_TEXTURE_CUBE_MAP_NEGATIVE_Y',
           'GL_SCALE_BY_ONE_HALF_NV', 'GL_SAMPLER_2D_SHADOW',
           'GL_RESAMPLE_DECIMATE_SGIX', 'GL_UNSIGNED_INT_24_8_NV',
           'GL_MATRIX2_ARB', 'GL_VERTEX_ATTRIB_ARRAY0_NV',
           'GLU_NURBS_ERROR16', 'GL_ONE_MINUS_DST_COLOR',
           'GL_TEXTURE_CUBE_MAP_NEGATIVE_Z', 'GLU_NURBS_END_DATA',
           'GL_UNDEFINED_APPLE', 'GL_NORMAL_MAP_NV',
           'GL_ACCUM_ALPHA_BITS', 'GL_MAX_FRAMEZOOM_FACTOR_SGIX',
           'GL_FLOAT', 'GLU_NURBS_ERROR12',
           'GL_NUM_INSTRUCTIONS_TOTAL_ATI', 'glGenTextures',
           'GL_COLOR_BUFFER_BIT', 'GLU_NURBS_ERROR13',
           'GL_UNPACK_RESAMPLE_SGIX', 'GL_SPOT_CUTOFF',
           'glutCreateSubWindow', 'GL_COLOR_FLOAT_APPLE',
           'GL_INDEX_ARRAY_BUFFER_BINDING_ARB',
           'GL_TEXTURE_LUMINANCE_SIZE', 'GL_YCRCBA_SGIX',
           'GL_INVALID_VALUE', 'GL_EVAL_VERTEX_ATTRIB1_NV',
           'GL_NEAREST_MIPMAP_NEAREST',
           'GL_COMPRESSED_SLUMINANCE_EXT', 'glutTimerFunc',
           'GL_SLUMINANCE8_EXT', 'GLU_NURBS_ERROR18',
           'GL_TEXTURE8_ARB', 'GL_RENDERBUFFER_STENCIL_SIZE_EXT',
           'GL_COMBINER1_NV', 'GL_SWIZZLE_STR_ATI',
           'GL_CONTEXT_COMPATIBILITY_PROFILE_BIT', 'GL_LINK_STATUS',
           'glNormal3bv', 'GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM_ARB',
           'glutChangeToSubMenu', 'GL_FLOAT_VEC3_ARB', 'glGetMinmax',
           'GLUT_KEY_DOWN',
           'GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS_EXT',
           'GL_ELEMENT_ARRAY_POINTER_APPLE', 'GL_YCRCB_SGIX',
           'GL_SIGNED_HILO16_NV', 'GL_CON_30_ATI',
           'GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN',
           'GL_MATRIX3_ARB', 'GL_MAT_SHININESS_BIT_PGI',
           'GL_INT8_VEC2_NV', 'GL_INTENSITY_FLOAT32_ATI',
           'glutInitDisplayMode', 'glVertex3sv',
           'GL_TEXTURE_COORD_ARRAY_SIZE', 'GL_AND_INVERTED',
           'GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS',
           'GL_PROXY_TEXTURE_4D_SGIS', 'glutSolidTeapot',
           'glutJoystickGetNumAxes', 'GL_DRAW_INDIRECT_BUFFER',
           'GL_NUM_COMPRESSED_TEXTURE_FORMATS_ARB',
           'glutJoystickSetSaturation', 'GL_INTENSITY32I_EXT',
           'GL_BUMP_ENVMAP_ATI', 'GL_VERTEX_ID_NV',
           'GL_POLYGON_OFFSET_POINT', 'GL_LUMINANCE12_EXT',
           'GL_COMBINE_ALPHA', 'glMultiTexCoord2dv', 'GL_RIGHT',
           'GL_OUTPUT_TEXTURE_COORD31_EXT',
           'GL_LUMINANCE4_ALPHA4_EXT', 'GLUT_INIT_PROFILE',
           'GLUT_WINDOW_BUFFER_SIZE', 'GL_QUARTER_BIT_ATI',
           'GL_ALPHA8UI_EXT', 'GL_DEPTH_COMPONENT16',
           'GL_MAX_SAMPLE_MASK_WORDS', 'glMultiTexCoord3dvARB',
           'glMultiTexCoord2s', 'GL_UNSIGNALED',
           'GL_MAX_TEXTURE_MAX_ANISOTROPY_EXT', 'GL_RGB32I',
           'glMultiTexCoord2i', 'GL_SRC1_RGB', 'GL_CON_11_ATI',
           'GL_MATRIX13_ARB', 'glMultiTexCoord2d', 'GL_BGRA_INTEGER',
           'glMultiTexCoord2f', 'GLU_EXTERIOR', 'GL_FALSE',
           'GL_COLOR_ARRAY_BUFFER_BINDING_ARB', 'GL_DSDT_NV',
           'GL_FLOAT_R16_NV', 'GL_COMPRESSED_SLUMINANCE_ALPHA_EXT',
           'GL_PROGRAM_BINDING_ARB', 'GL_SOURCE2_RGB_EXT',
           'GL_FRAMEZOOM_FACTOR_SGIX', 'GLUT_INIT_MAJOR_VERSION',
           'GL_PIXEL_TEX_GEN_ALPHA_NO_REPLACE_SGIX',
           'GL_MAX_GEOMETRY_BINDABLE_UNIFORMS_EXT',
           'GL_MAX_PROGRAM_ENV_PARAMETERS_ARB', 'GLUT_KEY_F12',
           'GLUT_KEY_F10', 'GL_UNSIGNED_INT8_VEC4_NV',
           'GL_PIXEL_MAP_I_TO_G_SIZE', 'GL_TEXTURE_CUBE_MAP_ARRAY',
           'GL_PROGRAM_POINT_SIZE', 'GL_PIXEL_MAP_I_TO_R',
           'GLUT_NUM_SPACEBALL_BUTTONS',
           'GL_POST_CONVOLUTION_BLUE_SCALE_EXT',
           'GL_INDEX_ARRAY_ADDRESS_NV', 'GL_HISTOGRAM_BLUE_SIZE_EXT',
           'GL_UNSIGNED_INT_VEC2_EXT', 'GL_FENCE_APPLE',
           'GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR_ARB', 'glVertex2sv',
           'GL_DISCRETE_AMD', 'GL_DOT_PRODUCT_TEXTURE_CUBE_MAP_NV',
           'GL_ALPHA16_EXT', 'GL_EYE_RADIAL_NV',
           'GL_DEPTH_PASS_INSTRUMENT_MAX_SGIX', 'GL_DYNAMIC_COPY_ARB',
           'GL_MAP1_GRID_SEGMENTS', 'GL_TEXTURE5_ARB',
           'GL_ATTRIB_STACK_DEPTH',
           'GL_MAX_PROGRAM_PARAMETER_BUFFER_BINDINGS_NV',
           'GL_LINE_WIDTH',
           'GL_PROXY_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP',
           'GL_DOUBLE_VEC3_EXT', 'glutWireCube',
           'GL_MAX_RECTANGLE_TEXTURE_SIZE_NV', 'glMultiTexCoord4fv',
           'glRasterPos3i', 'GL_COLOR_ATTACHMENT14', 'glRasterPos3d',
           'glRasterPos3f', 'glCompressedTexImage3D',
           'GL_COLOR_ATTACHMENT0_EXT',
           'GL_DEPTH_PASS_INSTRUMENT_SGIX',
           'GL_MAX_FRAGMENT_UNIFORM_COMPONENTS',
           'GLUT_FORWARD_COMPATIBLE', 'GL_SOURCE0_RGB_EXT',
           'GL_FRAGMENT_LIGHT4_SGIX',
           'GL_NORMAL_ARRAY_PARALLEL_POINTERS_INTEL', 'GL_RGBA16UI',
           'GL_MAX_VERTEX_UNITS_ARB', 'GL_LINE_SMOOTH_HINT',
           'glRasterPos3s', 'GLUT_KEY_LEFT', 'GL_FRONT',
           'GL_INDEX_MATERIAL_FACE_EXT', 'GL_CULL_VERTEX_IBM',
           'glConvolutionFilter1D', 'GL_AMBIENT',
           'GL_SECONDARY_COLOR_ARRAY_LENGTH_NV', 'GL_READ_ONLY',
           'GL_MAX_FRAGMENT_UNIFORM_VECTORS',
           'GL_UNSIGNED_SHORT_1_15_REV_MESA', 'GL_NEAREST',
           'GL_MAX_DEBUG_LOGGED_MESSAGES_ARB',
           'glMultiTexCoord2ivARB', 'GL_NUM_EXTENSIONS', 'glIsList',
           'GL_PURGEABLE_APPLE', 'GL_FRAMEBUFFER_BINDING',
           'GLU_TESS_BEGIN', 'GL_UNSIGNED_INT_24_8',
           'GL_NORMAL_ARRAY_BUFFER_BINDING', 'GL_OPERAND1_ALPHA',
           'GLUT_CURSOR_TEXT', 'GLU_NURBS_ERROR17', 'GL_SET',
           'GL_BUFFER_GPU_ADDRESS_NV', 'GLU_NURBS_END_DATA_EXT',
           'GL_DOT_PRODUCT_CONST_EYE_REFLECT_CUBE_MAP_NV',
           'GL_COMBINER_MAPPING_NV',
           'GL_POST_CONVOLUTION_RED_BIAS_EXT',
           'GL_MAT_AMBIENT_BIT_PGI',
           'GL_UNSIGNED_INT_SAMPLER_1D_ARRAY',
           'GL_COLOR_ATTACHMENT11_EXT',
           'GL_POST_TEXTURE_FILTER_BIAS_RANGE_SGIX',
           'GL_UNSIGNED_INT_SAMPLER_2D_ARRAY', 'GL_TEXTURE9',
           'GL_INVALID_ENUM', 'GL_HALF_APPLE',
           'GL_MAX_VERTEX_VARYING_COMPONENTS_EXT',
           'GL_COLOR_MATRIX_STACK_DEPTH', 'GLU_NURBS_COLOR_DATA_EXT',
           'GL_RENDERBUFFER_ALPHA_SIZE_EXT',
           'GL_UNSIGNED_INT_IMAGE_CUBE_EXT', 'GL_MATRIX5_ARB',
           'GL_DEPTH_BUFFER_FLOAT_MODE_NV', 'GL_DEPTH_COMPONENT',
           'glCompressedTexSubImage1D', 'GL_FOG_START',
           'GL_MULTISAMPLE_COVERAGE_MODES_NV',
           'GL_PRESENT_DURATION_NV', 'glCopyConvolutionFilter1D',
           'GL_OBJECT_BUFFER_USAGE_ATI',
           'GL_PROGRAM_INSTRUCTIONS_ARB',
           'GL_ARRAY_ELEMENT_LOCK_FIRST_EXT',
           'GL_PREFER_DOUBLEBUFFER_HINT_PGI',
           'GL_COMPARE_REF_TO_TEXTURE', 'GL_PROJECTION_STACK_DEPTH',
           'GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE',
           'GL_HI_SCALE_NV', 'GL_TEXTURE_MIN_FILTER',
           'glutShowOverlay', 'GL_STACK_UNDERFLOW',
           'GL_MAP2_VERTEX_ATTRIB3_4_NV',
           'GL_CONVOLUTION_FILTER_BIAS_EXT', 'GL_AUX1', 'GL_AUX0',
           'GL_AUX3', 'GL_AUX2', 'GL_VERTEX_ARRAY_RANGE_APPLE',
           'GLU_NURBS_TEXTURE_COORD_DATA', 'GL_MAP1_TANGENT_EXT',
           'GL_COLOR_ATTACHMENT6_EXT', 'GL_TEXTURE_2D_ARRAY_EXT',
           'GL_DEPTH_STENCIL_ATTACHMENT', 'GL_PRIMARY_COLOR_ARB',
           'GL_ADD', 'GLUT_CURSOR_TOP_LEFT_CORNER',
           'GL_VERTEX_ARRAY_LIST_STRIDE_IBM', 'GL_POINT_SPRITE',
           'GL_VERSION_1_2_DEPRECATED', 'GL_WRAP_BORDER_SUN',
           'GL_MODELVIEW_STACK_DEPTH', 'GL_TEXTURE_INTERNAL_FORMAT',
           'GL_CONSERVE_MEMORY_HINT_PGI', 'GL_SHADER_SOURCE_LENGTH',
           'GL_CON_15_ATI', 'GL_MIRRORED_REPEAT_ARB',
           'GLUT_CURSOR_NONE', 'GL_SCALEBIAS_HINT_SGIX',
           'GL_FLOAT_R32_NV', 'GL_NUM_INSTRUCTIONS_PER_PASS_ATI',
           'GL_COMBINER5_NV', 'GL_CND0_ATI', 'GL_FRAGMENT_SHADER_ATI',
           'GLUT_KEY_BEGIN', 'glRasterPos4fv', 'GL_REG_3_ATI',
           'GL_VERTEX_ARRAY_PARALLEL_POINTERS_INTEL',
           'GL_TEXTURE_RECTANGLE_NV', 'GL_ATTRIB_ARRAY_SIZE_NV',
           'GLUT_ENTERED', 'GL_WEIGHT_ARRAY_POINTER_ARB', 'glNewList',
           'GL_MAX_PIXEL_MAP_TABLE',
           'GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY_ARB',
           'GL_INDEX_ARRAY_LIST_IBM', 'glHint',
           'GL_POST_CONVOLUTION_GREEN_BIAS',
           'GL_ELEMENT_ARRAY_BARRIER_BIT_EXT',
           'GL_UNSIGNED_INT_SAMPLER_RENDERBUFFER_NV',
           'glutStrokeHeight', 'GL_RENDERBUFFER_SAMPLES',
           'GL_DEBUG_SEVERITY_MEDIUM_ARB', 'GL_POLYGON_STIPPLE',
           'glMultiTexCoord2fARB', 'GL_DEBUG_TYPE_PORTABILITY_ARB',
           'GL_MATERIAL_SIDE_HINT_PGI', 'GL_UNSIGNED_INT16_NV',
           'GL_UNSIGNED_INT64_VEC3_NV', 'GL_OP_DOT3_EXT',
           'GL_PROGRAM_BINARY_FORMATS', 'glScalef', 'GL_LOW_INT',
           'glScaled', 'GLU_V_STEP', 'GL_LUMINANCE16UI_EXT',
           'GL_BINORMAL_ARRAY_POINTER_EXT', 'glCopyColorTable',
           'GL_GEOMETRY_INPUT_TYPE_EXT',
           'GL_MAX_VERTEX_OUTPUT_COMPONENTS', 'GL_KEEP',
           'GL_TEXTURE_MAG_SIZE_NV', 'GL_INDEX_ARRAY_STRIDE',
           'GLUT_ELAPSED_TIME', 'GL_MAX_PALETTE_MATRICES_ARB',
           'GL_SIGNED_NEGATE_NV', 'GL_Z4Y12Z4CB12Z4CR12_444_NV',
           'GL_CON_6_ATI', 'GL_PROGRAM_STRING_NV',
           'glMultiTexCoord3iARB', 'GL_OPERAND2_RGB_EXT',
           'GL_MATRIX_EXT', 'GL_OR', 'GL_VERTEX_ARRAY_TYPE',
           'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER',
           'GL_VERTEX_ATTRIB_ARRAY2_NV', 'glGetTexParameteriv',
           'GL_EYE_PLANE_ABSOLUTE_NV', 'GL_CONVOLUTION_HEIGHT',
           'GL_SAMPLER_1D_ARRAY', 'GLUT_CURSOR_BOTTOM_SIDE',
           'GL_DS_BIAS_NV', 'GL_ACTIVE_SUBROUTINES', 'GL_LINE_LOOP',
           'GL_PACK_INVERT_MESA', 'GL_DSDT8_MAG8_INTENSITY8_NV',
           'GL_TEXTURE6_ARB', 'GLU_TESS_ERROR_DATA',
           'GL_PROGRAM_ALU_INSTRUCTIONS_ARB', 'GL_COLOR_TABLE_SCALE',
           'GL_TEXTURE_BINDING_CUBE_MAP_ARRAY_ARB',
           'GL_COLOR_INDEX2_EXT', 'GL_BACK_RIGHT',
           'GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS',
           'GL_INT_SAMPLER_CUBE_EXT', 'GLUT_BORDERLESS',
           'GLU_AUTO_LOAD_MATRIX', 'glutWindowStatusFunc',
           'GL_R1UI_T2F_C4F_N3F_V3F_SUN', 'GL_ALPHA_TEST',
           'GL_READ_FRAMEBUFFER', 'GL_SLUMINANCE8_ALPHA8',
           'glDisable', 'GL_LUMINANCE4_ALPHA4', 'GL_UNIFORM_OFFSET',
           'GL_PROGRAM_UNDER_NATIVE_LIMITS_ARB',
           'GLU_DOMAIN_DISTANCE', 'GL_TEXTURE1', 'GLUnurbs',
           'GL_VERTEX_SHADER_INVARIANTS_EXT', 'GL_OBJECT_PLANE',
           'GL_LUMINANCE_FLOAT16_APPLE', 'GL_MODELVIEW20_ARB',
           'GL_UNPACK_SKIP_VOLUMES_SGIS',
           'GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH_EXT',
           'glutAddSubMenu', 'GL_HISTOGRAM_BLUE_SIZE', 'glRectfv',
           'GL_T2F_IUI_V3F_EXT', 'glGetLightfv', 'glutSetWindowData',
           'GL_PROXY_TEXTURE_2D', 'GL_FUNC_ADD', 'GL_ABGR_EXT',
           'GL_IMAGE_2D_RECT_EXT', 'GL_COMBINE_ALPHA_ARB',
           'GL_BUFFER_ACCESS', 'GL_EYE_POINT_SGIS',
           'glMultiTexCoord3s', 'GL_LINES_ADJACENCY', 'GLsync',
           'glutSetColor', 'GL_MVP_MATRIX_EXT', 'GL_R8',
           'GL_NORMAL_ARRAY_COUNT_EXT', 'glMultiTexCoord3i',
           'glMultiTexCoord3f', 'GL_PIXEL_UNPACK_BUFFER_EXT',
           'glMultiTexCoord3d',
           'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_EXT',
           'GL_VERTEX_WEIGHT_ARRAY_SIZE_EXT',
           'GL_DOT_PRODUCT_PASS_THROUGH_NV',
           'GL_MIN_FRAGMENT_INTERPOLATION_OFFSET_NV',
           'GL_OCCLUSION_TEST_RESULT_HP',
           'GL_LUMINANCE16_ALPHA16_SNORM',
           'GL_MAP1_VERTEX_ATTRIB4_4_NV', 'GL_UNPACK_CMYK_HINT_EXT',
           'GL_SPARE0_PLUS_SECONDARY_COLOR_NV', 'GLU_NURBS_MODE',
           'GL_OUTPUT_TEXTURE_COORD16_EXT', 'GL_HISTOGRAM_RED_SIZE',
           'GL_MAP2_VERTEX_ATTRIB15_4_NV', 'GL_VOLATILE_APPLE',
           'GL_RGBA_UNSIGNED_DOT_PRODUCT_MAPPING_NV', 'GL_ADD_ATI',
           'GL_RGB_422_APPLE', 'GLUT_CURSOR_HELP',
           'GL_FRAGMENT_LIGHT2_SGIX', 'GL_NUM_PROGRAM_BINARY_FORMATS',
           'GL_SURFACE_MAPPED_NV', 'GL_SAMPLES_EXT',
           'GL_DEBUG_CATEGORY_DEPRECATION_AMD',
           'GL_IMAGE_TRANSLATE_X_HP', 'glReadBuffer',
           'GL_POLYGON_SMOOTH_HINT', 'GL_INDEX', 'GLU_TESS_ERROR3',
           'GL_R11F_G11F_B10F', 'GLUT_CORE_PROFILE',
           'GL_TEXTURE31_ARB', 'GL_VERTEX_SHADER_OPTIMIZED_EXT',
           'GL_MEDIUM_FLOAT', 'glPushName', 'glGetClipPlane',
           'glVertex4dv', 'glPopMatrix', 'glBlendColor',
           'GL_REG_23_ATI', 'GL_SEPARABLE_2D', 'glIndexubv',
           'GL_MAP2_VERTEX_ATTRIB8_4_NV',
           'GL_TEXTURE_COMPARE_OPERATOR_SGIX',
           'GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_ATTRIBS_NV',
           'glRasterPos4d', 'GL_SRGB8', 'glutSwapBuffers',
           'GL_REG_17_ATI', 'GL_DOMAIN', 'GL_TEXTURE_PRIORITY_EXT',
           'glVertex3fv', 'glRasterPos4s',
           'GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS',
           'glutSpaceballMotionFunc', 'GL_RGB10_EXT',
           'GL_MAX_TRACK_MATRICES_NV', 'GL_R8UI',
           'GL_COLOR_TABLE_INTENSITY_SIZE', 'GL_INVERSE_TRANSPOSE_NV',
           'GLUquadric', 'glActiveTexture',
           'GL_OUTPUT_TEXTURE_COORD13_EXT', 'GLU_MAP1_TRIM_3',
           'GL_ACTIVE_SUBROUTINE_UNIFORMS', 'GL_EMBOSS_MAP_NV',
           'GL_BOOL_ARB', 'GL_MATRIX22_ARB',
           'GLUT_GAME_MODE_DISPLAY_CHANGED', 'GL_PIXEL_TEXTURE_SGIS',
           'GL_PROGRAM_MATRIX_EXT', 'GL_TRIANGLES',
           'GL_SAMPLER_2D_ARRAY_SHADOW', 'glutPostWindowRedisplay',
           'GL_COLOR_ATTACHMENT12_EXT', 'GL_IMAGE_BINDING_NAME_EXT',
           'GLUT_MENU_IN_USE',
           'GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING',
           'glMultiTexCoord3sv', 'GLU_NURBS_ERROR29',
           'GL_ASYNC_MARKER_SGIX', 'GL_READ_PIXEL_DATA_RANGE_NV',
           'GL_NORMAL_ARRAY_STRIDE_EXT', 'GLU_NURBS_ERROR25',
           'GLU_NURBS_ERROR24', 'GLU_NURBS_ERROR27',
           'GLU_NURBS_ERROR26', 'GLU_NURBS_ERROR21',
           'GLU_NURBS_ERROR20', 'GL_SLUMINANCE', 'GL_TEXTURE_WRAP_S',
           'GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_EXT',
           'GL_UNSIGNED_NORMALIZED_ARB', 'GL_GLOBAL_ALPHA_FACTOR_SUN',
           'GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_ARB', 'GL_RG8',
           'GL_CON_10_ATI', 'glMultiTexCoord4iv',
           'GL_MAX_PROGRAM_PARAMETERS_ARB', 'GL_SAMPLER_2D_ARRAY',
           'glutLeaveGameMode', 'GLU_NURBS_TEX_COORD_EXT',
           'GL_ALPHA16F_ARB', 'GL_COLOR_TABLE_SGI',
           'GL_MIRRORED_REPEAT', 'GL_RENDERBUFFER_BLUE_SIZE_EXT',
           'GL_SAMPLE_BUFFERS_EXT', 'GL_QUERY_NO_WAIT_NV',
           'GLU_BEGIN', 'GL_MAX_VERTEX_STREAMS_ATI',
           'glTexCoordPointer', 'GL_PIXEL_MAP_B_TO_B',
           'GL_TEXTURE14_ARB', 'glutStopVideoResizing',
           'GL_SIGNED_RGBA8_NV', 'GL_TEXTURE_BUFFER_EXT',
           'GL_PIXEL_MAP_R_TO_R_SIZE', 'GL_EVAL_VERTEX_ATTRIB9_NV',
           'GL_SECONDARY_COLOR_ARRAY_LIST_STRIDE_IBM', 'int64_t',
           'GL_QUERY_COUNTER_BITS_ARB', 'GL_COLOR_TABLE_RED_SIZE',
           'GL_REPLACEMENT_CODE_ARRAY_SUN', 'GL_COLOR_LOGIC_OP',
           'GLU_NURBS_ERROR37', 'GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_EXT',
           'GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH',
           'GL_HISTOGRAM_SINK_EXT', 'glutWireIcosahedron',
           'GL_OUTPUT_TEXTURE_COORD27_EXT',
           'GL_DETAIL_TEXTURE_MODE_SGIS',
           'GL_STENCIL_BACK_PASS_DEPTH_PASS_ATI',
           'GL_EVAL_VERTEX_ATTRIB2_NV',
           'GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCAL_CONSTANTS_EXT',
           'GL_Z6Y10Z6CB10Z6Y10Z6CR10_422_NV', 'glTexEnviv',
           'GL_STENCIL_CLEAR_VALUE', 'GL_SPHERE_MAP',
           'GL_COMPRESSED_TEXTURE_FORMATS_ARB',
           'GL_TEXTURE_SWIZZLE_G', 'glSelectBuffer',
           'GL_ARRAY_BUFFER_ARB', 'GL_X_EXT', 'GL_OPERAND0_ALPHA_EXT',
           'GL_RGB_SCALE', 'GLU_OUT_OF_MEMORY', 'glBlendFunc',
           'GL_BINORMAL_ARRAY_EXT', 'GL_TEXTURE_BINDING_BUFFER_ARB',
           'GL_TEXTURE_CUBE_MAP_NEGATIVE_X',
           'GL_DETAIL_TEXTURE_2D_SGIS', 'GL_MAD_ATI',
           'GL_MAX_PROGRAM_NATIVE_TEMPORARIES_ARB',
           'GL_OP_SET_GE_EXT', 'GL_RGB_FLOAT16_ATI',
           'GL_ACTIVE_VERTEX_UNITS_ARB',
           'GL_NUM_GENERAL_COMBINERS_NV', 'GL_PRIMITIVES_GENERATED',
           'GL_TRANSFORM_FEEDBACK_BINDING', 'GLUT_DIRECT_RENDERING',
           'GL_MOV_ATI', 'GLUT_ACTION_ON_WINDOW_CLOSE',
           'GL_CURRENT_RASTER_INDEX', 'GL_TEXTURE_DEPTH_SIZE_ARB',
           'GL_MODELVIEW_PROJECTION_NV', 'glutSetWindowTitle',
           'GL_COMPRESSED_SRGB', 'GL_OFFSET_HILO_TEXTURE_2D_NV',
           'GL_TEXTURE_DEPTH_TYPE', 'GLU_TESS_BEGIN_DATA',
           'GL_COMPRESSED_SLUMINANCE_ALPHA', 'glutExtensionSupported',
           'GL_DRAW_INDIRECT_UNIFIED_NV', 'glEnd', 'glutWireCylinder',
           'GL_DRAW_BUFFER15_ATI', 'GL_MAX',
           'GL_CURRENT_RASTER_COLOR', 'GLUT_HAS_JOYSTICK',
           'GL_FOG_COORDINATE_ARRAY_LIST_IBM', 'GL_LUMINANCE4_EXT',
           'GL_RENDERBUFFER_GREEN_SIZE_EXT',
           'GL_PROXY_TEXTURE_2D_ARRAY',
           'GL_COMPRESSED_SIGNED_LUMINANCE_LATC1_EXT',
           'GL_CON_21_ATI', 'glMultTransposeMatrixf',
           'glMultTransposeMatrixd', 'GL_TEXTURE23_ARB',
           'glClearColor', 'GL_IMAGE_CUBIC_WEIGHT_HP',
           'GL_COLOR_SUM_CLAMP_NV', 'GL_INT_IMAGE_1D_EXT',
           'glutIconifyWindow',
           'GL_OBJECT_ACTIVE_ATTRIBUTE_MAX_LENGTH_ARB',
           'glutRemoveMenuItem', 'GL_MAX_FOG_FUNC_POINTS_SGIS',
           'GL_SPRITE_TRANSLATION_SGIX',
           'GL_MAX_GEOMETRY_PROGRAM_INVOCATIONS_NV',
           'GL_HALF_FLOAT_NV', 'glPushClientAttrib',
           'GL_TEXTURE_RENDERBUFFER_NV', 'GL_BUMP_ROT_MATRIX_ATI',
           'GL_ACCUM', 'GLUT_JOYSTICK_AXES', 'GL_LIGHT_ENV_MODE_SGIX',
           'GL_PROXY_TEXTURE_1D_ARRAY', 'GL_MINMAX_FORMAT_EXT',
           'GLUT_KEY_UP', 'GL_TEXTURE_BINDING_2D_ARRAY_EXT',
           'GLU_ERROR', 'GL_TEXTURE_FIXED_SAMPLE_LOCATIONS',
           'GL_VERTEX_ARRAY_SIZE', 'GL_TEXTURE_COORD_ARRAY_COUNT_EXT',
           'GL_MAX_ARRAY_TEXTURE_LAYERS_EXT',
           'GL_FRAMEBUFFER_ATTACHMENT_LAYERED_ARB',
           'GL_STENCIL_BACK_PASS_DEPTH_FAIL_ATI',
           'GL_SHADER_INCLUDE_ARB', 'GLUT_WINDOW_Y', 'GLUT_WINDOW_X',
           'GL_POST_CONVOLUTION_GREEN_SCALE_EXT',
           'GL_RECLAIM_MEMORY_HINT_PGI',
           'GL_UNPACK_CLIENT_STORAGE_APPLE', 'GL_STENCIL_BUFFER_BIT',
           'GL_ALPHA16I_EXT', 'GL_MIRROR_CLAMP_EXT',
           'GL_MAX_TEXTURE_BUFFER_SIZE_EXT', 'GL_MODELVIEW5_ARB',
           'GL_SEPARATE_ATTRIBS_EXT', 'GL_GPU_ADDRESS_NV',
           'GL_DEPTH_CLAMP_FAR_AMD', 'GLU_TESS_MISSING_END_CONTOUR',
           'GL_INDEX_TEST_REF_EXT', 'GL_DUAL_TEXTURE_SELECT_SGIS',
           'GL_SAMPLE_MASK_SGIS', 'GL_CONST_EYE_NV', 'GL_DEPTH_SCALE',
           'GL_FLOAT_RGBA_MODE_NV', 'GL_TEXTURE_CUBE_MAP',
           'GL_CURRENT_OCCLUSION_QUERY_ID_NV', 'GL_OP_ADD_EXT',
           'GL_RGB32UI_EXT', 'GL_CURRENT_RASTER_DISTANCE',
           'GL_SAMPLER_CUBE_MAP_ARRAY', 'glCompressedTexSubImage2D',
           'GL_POINT_SIZE_MAX_EXT', 'GL_EVAL_VERTEX_ATTRIB0_NV',
           'GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS', 'GL_MAX_VIEWPORTS',
           'glGetTexParameterfv', 'GL_TEXTURE_STORAGE_HINT_APPLE',
           'GL_TEXTURE7_ARB', 'GL_NORMAL_ARRAY_LIST_IBM',
           'GL_MAX_FRAGMENT_INPUT_COMPONENTS', 'GL_REG_6_ATI',
           'GL_DRAW_PIXEL_TOKEN', 'glutMouseWheelFunc',
           'GLU_EXTENSIONS',
           'GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS_NV',
           'GL_INTENSITY4_EXT', 'GL_LUMINANCE32F_ARB',
           'glMultiTexCoord4sARB', 'GL_COMBINER_CD_DOT_PRODUCT_NV',
           'GL_SAMPLER_1D_SHADOW', 'GL_RGB8I_EXT',
           'GL_FRAGMENT_LIGHT3_SGIX', 'GL_TEXTURE_HI_SIZE_NV',
           'GL_PROGRAM_ADDRESS_REGISTERS_ARB', 'GLUT_FULL_SCREEN',
           'GL_TEXTURE_INTENSITY_TYPE_ARB', 'GL_COMPRESSED_RGB_ARB',
           'GL_PROXY_TEXTURE_1D', 'GLUT_DEVICE_IGNORE_KEY_REPEAT',
           'GL_TEXTURE_1D_STACK_MESAX', 'GL_INTENSITY8_SNORM',
           'GL_FRAGMENT_DEPTH', 'GL_VERTEX_ATTRIB_ARRAY_NORMALIZED',
           'GL_UNSIGNED_INT_IMAGE_1D_ARRAY_EXT', 'GL_OP_POWER_EXT',
           'GL_DOT_PRODUCT_NV', 'GL_CUBIC_EXT',
           'GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_EXT',
           'GL_FOG_COORDINATE', 'GL_SPOT_EXPONENT',
           'GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET_NV',
           'GL_CONSTANT_COLOR', 'GL_TEXTURE_INDEX_SIZE_EXT',
           'GL_PIXEL_TEX_GEN_ALPHA_REPLACE_SGIX',
           'GL_ARRAY_ELEMENT_LOCK_COUNT_EXT',
           'GL_RGBA_SIGNED_COMPONENTS_EXT',
           'GL_REFERENCE_PLANE_EQUATION_SGIX',
           'GL_TRIANGLE_STRIP_ADJACENCY_ARB',
           'GL_MAX_VERTEX_UNIFORM_VECTORS',
           'GL_LUMINANCE_ALPHA_FLOAT32_ATI',
           'GL_POST_CONVOLUTION_GREEN_SCALE',
           'GL_COMBINER_AB_DOT_PRODUCT_NV', 'glutJoystickSetDeadBand',
           'glutSpaceballButtonFunc', 'GL_TRANSPOSE_COLOR_MATRIX',
           'GLUT_WINDOW_BORDER_WIDTH', 'GL_ALLOW_DRAW_OBJ_HINT_PGI',
           'GL_SHADER_OPERATION_NV',
           'GL_POST_COLOR_MATRIX_BLUE_BIAS_SGI',
           'GL_TRANSFORM_FEEDBACK_VARYINGS',
           'GL_FOG_COORDINATE_ARRAY_POINTER', 'GL_FLOAT_R_NV',
           'GL_PIXEL_CUBIC_WEIGHT_EXT', 'GL_FLOAT_VEC4_ARB',
           'GL_OUTPUT_TEXTURE_COORD12_EXT', 'glGenLists',
           'GL_CON_3_ATI', 'GL_SHADER_TYPE', 'GL_PIXEL_MAP_S_TO_S',
           'GL_MATRIX2_NV', 'GL_UNSIGNED_SHORT_5_5_5_1',
           'GLU_NURBS_TESSELLATOR', 'GL_COLOR_ARRAY_STRIDE',
           'GL_DUAL_INTENSITY12_SGIS', 'GL_EVAL_VERTEX_ATTRIB6_NV',
           'GL_DRAW_BUFFER11_ARB', 'glEndList',
           'GL_CLAMP_TO_BORDER_SGIS', 'GL_INNOCENT_CONTEXT_RESET_ARB',
           'GL_VERTEX_ARRAY_RANGE_POINTER_APPLE',
           'GL_MAX_ELEMENTS_INDICES', 'GL_BUMP_ROT_MATRIX_SIZE_ATI',
           'GLU_TESS_VERTEX', 'GL_NO_ERROR', 'GL_SCALAR_EXT',
           'GL_GEOMETRY_VERTICES_OUT',
           'GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS', 'GL_RGB8',
           'GLUT_LEFT_BUTTON', 'GL_MAX_RENDERBUFFER_SIZE_EXT',
           'glIndexMask', 'glutButtonBoxFunc', 'GL_REDUCE',
           'GL_OP_MIN_EXT', 'GL_TEXTURE_SAMPLES', 'GL_RGB4',
           'GL_RGB5', 'GL_MODELVIEW22_ARB', 'GL_CULL_FACE',
           'GL_POST_COLOR_MATRIX_GREEN_BIAS',
           'GL_FOG_OFFSET_VALUE_SGIX', 'glColor3fv',
           'GL_SAMPLE_COVERAGE_VALUE',
           'GL_MAX_CUBE_MAP_TEXTURE_SIZE_ARB', 'GL_GREEN_BIT_ATI',
           'GL_EYE_LINE_SGIS', 'GL_PROXY_TEXTURE_CUBE_MAP',
           'GL_RENDERBUFFER_EXT',
           'GL_VERTEX_ATTRIB_ARRAY_NORMALIZED_ARB', 'GL_OP_MADD_EXT',
           'glutSetCursor', 'GL_MAX_ELEMENTS_VERTICES',
           'GL_COLOR_INDEXES', 'glRotated',
           'GL_EVAL_VERTEX_ATTRIB4_NV',
           'GL_SECONDARY_COLOR_ARRAY_SIZE', 'GL_NEVER',
           'GL_STENCIL_VALUE_MASK', 'GL_BLEND_DST',
           'glutCreateWindow', 'GL_NUM_FILL_STREAMS_NV',
           'GL_DECR_WRAP_EXT', 'GL_INT16_NV', 'glRotatef',
           'GL_OUTPUT_COLOR1_EXT', 'GLU_NURBS_END_EXT',
           'GL_DOT_PRODUCT_TEXTURE_3D_NV', 'GL_COLOR_INDEX12_EXT',
           'GL_WAIT_FAILED', 'GL_MAX_PROGRAM_PATCH_ATTRIBS_NV',
           'GL_LOAD', 'GL_ZERO_EXT', 'glMultiTexCoord2fv',
           'GL_COLOR_TABLE_RED_SIZE_SGI', 'GL_TEXTURE25_ARB',
           'GL_ARRAY_OBJECT_BUFFER_ATI', 'GL_COMPRESSED_RGBA_ARB',
           'GL_MAP2_VERTEX_3', 'GL_MAP2_VERTEX_4',
           'GL_TEXTURE_WRAP_Q_SGIS', 'GL_DEPTH_COMPONENT32',
           'GL_INSTRUMENT_BUFFER_POINTER_SGIX', 'glColorPointer',
           'GL_FRAMEBUFFER_BARRIER_BIT_EXT', 'GL_COLOR_SUM',
           'GL_TEXTURE_CUBE_MAP_ARRAY_ARB', 'GL_FOG_COORDINATE_EXT',
           'GL_TEXTURE_TOO_LARGE_EXT', 'GL_MAP2_COLOR_4', 'GL_VENDOR',
           'GL_ELEMENT_ARRAY_BUFFER_ARB',
           'GL_MODELVIEW1_STACK_DEPTH_EXT', 'GL_ACCUM_BUFFER_BIT',
           'GL_OUTPUT_TEXTURE_COORD29_EXT',
           'GL_POST_CONVOLUTION_RED_SCALE_EXT', 'GL_ISOLINES',
           'GL_TRANSFORM_FEEDBACK_BUFFER_BINDING_EXT',
           'GL_ACTIVE_PROGRAM', 'GLvoid', 'GL_MAP1_BINORMAL_EXT',
           'GL_PACK_RESAMPLE_SGIX', 'GL_SINGLE_COLOR',
           'GL_SAMPLE_COVERAGE', 'glGetMaterialiv', 'GLUtesselator',
           'GL_TEXTURE_MATERIAL_FACE_EXT', 'GL_TESS_GEN_POINT_MODE',
           'GL_TESS_GEN_MODE', 'GL_DRAW_BUFFER1_ARB',
           'GL_UNSIGNED_INT64_VEC4_NV', 'GLU_NURBS_ERROR33',
           'GL_OUTPUT_TEXTURE_COORD9_EXT', 'GLU_NURBS_ERROR31',
           'glVertex4f', 'GL_STRICT_SCISSOR_HINT_PGI',
           'GL_ACTIVE_TEXTURE_ARB', 'GL_DEPTH_COMPONENT24_SGIX',
           'GLU_INVALID_VALUE', 'GL_LUMINANCE', 'glNormal3s',
           'GLUT_CURSOR_BOTTOM_LEFT_CORNER',
           'GL_PROXY_TEXTURE_CUBE_MAP_ARRAY',
           'GL_MAX_PN_TRIANGLES_TESSELATION_LEVEL_ATI',
           'glutJoystickGetDeadBand', 'GL_IMAGE_BUFFER_EXT',
           'GL_COLOR_TABLE_SCALE_SGI', 'glNormal3i',
           'GL_FULL_RANGE_EXT', 'glNormal3f', 'GL_AUTO_NORMAL',
           'GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS', 'glNormal3b',
           'GL_QUERY_BY_REGION_WAIT_NV', 'GL_VERTEX_WEIGHTING_EXT',
           'glMultiTexCoord4dv', 'glutRemoveOverlay', 'GLUT_KEY_F8',
           'GL_SEPARATE_SPECULAR_COLOR', 'glutWireSphere',
           'GL_SOURCE1_ALPHA_ARB', 'GL_TEXTURE_MATRIX',
           'GL_LUMINANCE12_ALPHA4_EXT', 'GL_REG_13_ATI', 'GL_RG16F',
           'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL',
           'GL_LINES_ADJACENCY_ARB', 'GL_RG16I', 'GL_WRITE_ONLY',
           'GL_TEXTURE_COORD_NV', 'GL_ALPHA32I_EXT',
           'GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE',
           'GL_STENCIL_ATTACHMENT',
           'GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING_ARB',
           'GL_SAMPLER_2D', 'glFrontFace',
           'GL_UNSIGNED_INT_8_24_REV_MESA',
           'GL_CURRENT_RASTER_NORMAL_SGIX',
           'GL_GEOMETRY_INPUT_TYPE_ARB', 'GL_TEXTURE_3D_BINDING_EXT',
           'GL_SHININESS', 'GL_DRAW_FRAMEBUFFER',
           'GL_STENCIL_BACK_WRITEMASK', 'GL_RGB10_A2UI',
           'GL_RGBA8I_EXT', 'GL_FOG_COORDINATE_ARRAY_STRIDE']
