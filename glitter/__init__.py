# TODO imports, __all__

def setup_package(): # nosetests
    from glitter.GlutWindow import GlutWindow # TODO use raw GLX context
    globals()["glut_window"] = GlutWindow()

