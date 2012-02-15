from gl import glut

def motion(x, y):
    print "motion(%d, %d)" % (x, y)
motion_c = glut.glutMotionFunc.argtypes[0](motion)

glut.glutInit(glut.pointer(glut.c_int()), glut.pointer(glut.c_char_p()))
glut.glutCreateWindow("")
glut.glutMotionFunc(motion_c)
glut.glutMainLoop()

