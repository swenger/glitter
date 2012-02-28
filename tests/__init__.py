from glitter.contexts.glut import GlutWindow # TODO use raw GLX context when it becomes available

def setup_package(): # nosetests
    globals()["glut_window"] = GlutWindow(hide=True)

