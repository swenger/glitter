# add to gl.py to remove deprecated commands that sneaked into gl3.h
# https://www.khronos.org/bugzilla/show_bug.cgi?id=335

deprecated_commands = """glVertexP2ui
glVertexP2uiv
glVertexP3ui
glVertexP3uiv
glVertexP4ui
glVertexP4uiv
glTexCoordP1ui
glTexCoordP1uiv
glTexCoordP2ui
glTexCoordP2uiv
glTexCoordP3ui
glTexCoordP3uiv
glTexCoordP4ui
glTexCoordP4uiv
glMultiTexCoordP1ui
glMultiTexCoordP1uiv
glMultiTexCoordP2ui
glMultiTexCoordP2uiv
glMultiTexCoordP3ui
glMultiTexCoordP3uiv
glMultiTexCoordP4ui
glMultiTexCoordP4uiv
glNormalP3ui
glNormalP3uiv
glColorP3ui
glColorP3uiv
glColorP4ui
glColorP4uiv
glSecondaryColorP3ui
glSecondaryColorP3uiv""".split()

for cmd in deprecated_commands:
    if cmd in globals():
        del globals()[cmd]
    if cmd in __all__:
        __all__.remove(cmd)
del deprecated_commands

