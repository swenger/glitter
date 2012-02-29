"""Error classes.

@author: Stephan Wenger
@date: 2012-02-29
"""

class GlitterError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class ShaderError(GlitterError):
    pass

class ShaderCompileError(ShaderError):
    pass

class ShaderLinkError(ShaderError):
    pass

class ShaderValidateError(ShaderError):
    pass

