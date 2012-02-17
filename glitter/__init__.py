# TODO imports, __all__
# TODO move tests to separate package

def setup_package(): # nosetests
    from glitter.GlutWindow import GlutWindow # TODO use own class with OpenGL 4.2 context
    globals()["glut_window"] = GlutWindow()

