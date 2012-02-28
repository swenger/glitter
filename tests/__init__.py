from glitter.context.glut import GlutWindow # TODO use raw GLX context when it becomes available

def setup_package():
    globals()["glut_window"] = GlutWindow(hide=True)

