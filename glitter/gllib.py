import ctypes
import os
import re
import subprocess

import pygccxml

class Constant(object): # TODO casting to OpenGL types
    registry = {}

    @classmethod
    def lookup(cls, name):
        return cls.registry[name][0]

    def __init__(self, name, value):
        self.name = name
        try:
            self.value = eval(value) # TODO evaluate as in C
            if name.startswith("GL_"): # TODO only for error return values
                Constant.registry.setdefault(self.value, []).append(self)
        except:
            self.value = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return "%s (0x%X)" % ("/".join(x.name for x in Constant.registry[self.value]), self.value)

def get_defines(headerfile):
    stdout, stderr = subprocess.Popen(["gccxml", "-E", "-dM", headerfile], stdout=subprocess.PIPE).communicate()
    define_re = re.compile(r'#define ([a-zA-Z_][a-zA-Z0-9_]*) ([^\n]*)\n')
    defines = [(key, Constant(key, value)) for key, value in define_re.findall(stdout)]
    return dict((name, constant) for name, constant in defines if constant.value is not None and name.startswith("GL_"))

def getattr_rec(obj, names):
    if len(names) == 0:
        return obj
    else:
        return getattr_rec(getattr(obj, names[0]), names[1:])

def ctypes_from_gccxml(lib, t):
    """Convert a pygccxml type to a ctypes type."""

    if isinstance(t, pygccxml.declarations.restrict_t):
        return ctypes_from_gccxml(lib, t.base)
    if isinstance(t, pygccxml.declarations.const_t):
        return ctypes_from_gccxml(lib, t.base)
    if isinstance(t, pygccxml.declarations.pointer_t):
        if isinstance(t.base, pygccxml.declarations.void_t):
            return ctypes.c_void_p
        if isinstance(t.base, pygccxml.declarations.char_t):
            return ctypes.c_char_p
        if isinstance(t.base, pygccxml.declarations.wchar_t):
            return ctypes.c_wchar_p
        return ctypes.POINTER(ctypes_from_gccxml(lib, t.base))
    if isinstance(t, pygccxml.declarations.array_t):
        return ctypes.ARRAY(ctypes_from_gccxml(lib, t.base), t.size)
    if isinstance(t, pygccxml.declarations.bool_t):
        return ctypes.c_bool
    if isinstance(t, pygccxml.declarations.char_t):
        return ctypes.c_char
    if isinstance(t, pygccxml.declarations.double_t):
        return ctypes.c_double
    if isinstance(t, pygccxml.declarations.float_t):
        return ctypes.c_float
    if isinstance(t, pygccxml.declarations.int_t):
        return ctypes.c_int
    if isinstance(t, pygccxml.declarations.long_double_t):
        return ctypes.c_longdouble
    if isinstance(t, pygccxml.declarations.long_int_t):
        return ctypes.c_long
    if isinstance(t, pygccxml.declarations.long_long_int_t):
        return ctypes.c_longlong
    if isinstance(t, pygccxml.declarations.long_long_unsigned_int_t):
        return ctypes.c_ulonglong
    if isinstance(t, pygccxml.declarations.long_unsigned_int_t):
        return ctypes.c_ulong
    if isinstance(t, pygccxml.declarations.short_int_t):
        return ctypes.c_short
    if isinstance(t, pygccxml.declarations.short_unsigned_int_t):
        return ctypes.c_ushort
    if isinstance(t, pygccxml.declarations.signed_char_t):
        return ctypes.c_char
    if isinstance(t, pygccxml.declarations.unsigned_char_t):
        return ctypes.c_ubyte
    if isinstance(t, pygccxml.declarations.unsigned_int_t):
        return ctypes.c_uint
    if isinstance(t, pygccxml.declarations.wchar_t):
        return ctypes.c_wchar
    if isinstance(t, pygccxml.declarations.void_t):
        return None
    if isinstance(t, pygccxml.declarations.cpptypes.declarated_t):
        return ctypes_from_gccxml(lib, getattr_rec(lib, [x for x in t.decl_string.split("::") if x])) # resolve namespace into nested modules
    if type(t) == type(ctypes.Structure) and issubclass(t, ctypes.Structure):
        return t
    raise NotImplementedError("no ctypes equivalent for %s %s" % (t.__class__.__name__, t.decl_string))

class OpenGLError(Exception):
    pass

class InvalidEnumError(OpenGLError):
    pass

class InvalidValueError(OpenGLError):
    pass

class InvalidOperationError(OpenGLError):
    pass

class InvalidFramebufferOperationError(OpenGLError):
    pass

class OutOfMemoryError(OpenGLError):
    pass

class UnknownError(OpenGLError):
    def __init__(self, error):
        self.error = error

def check_gl_error(result, func, arguments):
    if func.__name__ == "glGetError":
        try:
            return func.result_converter(result)
        except AttributeError:
            return result
    error = gl.glGetError()
    if error == gl.GL_NO_ERROR:
        try:
            return func.result_converter(result)
        except AttributeError:
            return result
    if error == gl.GL_INVALID_ENUM:
        raise InvalidEnumError()
    if error == gl.GL_INVALID_VALUE:
        raise InvalidValueError()
    if error == gl.GL_INVALID_OPERATION:
        raise InvalidOperationError()
    if error == gl.GL_INVALID_FRAMEBUFFER_OPERATION:
        raise InvalidFramebufferOperationError()
    if error == gl.GL_OUT_OF_MEMORY:
        raise OutOfMemoryError()
    raise UnknownError(error)

def load_dll(lib_name, header_name, define_symbols=[]):
    lib = ctypes.CDLL(lib_name)
    lib.__dict__.update(get_defines(header_name))
    for logger in pygccxml.utils.loggers.all:
        logger.level = pygccxml.utils.logging.ERROR
    config = pygccxml.parser.config.gccxml_configuration_t(define_symbols=define_symbols)
    declarations = pygccxml.parser.parse([header_name], config=config)[0].declarations

    for declaration in sorted(declarations, key=lambda x: x.location.line if x.location else 0):
        if not declaration.location or os.path.basename(declaration.location.file_name) == "gccxml_builtins.h": # skip default includes
            continue
        if isinstance(declaration, pygccxml.declarations.typedef_t):
            setattr(lib, declaration.name, declaration.type)
        elif isinstance(declaration, pygccxml.declarations.free_function_t):
            try:
                func = getattr(lib, declaration.name)
                func.restype = ctypes_from_gccxml(lib, declaration.return_type)
                if declaration.return_type.decl_string.lstrip(":") == "GLenum":
                    func.result_converter = Constant.lookup
                func.argtypes = [ctypes_from_gccxml(lib, a.type) for a in declaration.arguments]
                func.errcheck = check_gl_error
                func.__doc__ = "%s %s(%s)" % (
                        declaration.return_type.partial_decl_string.lstrip(":"),
                        declaration.name,
                        ", ".join("%s %s" % (t.partial_decl_string.lstrip(":"), a.name)
                            for t, a in zip(declaration.argument_types, declaration.arguments)))
            except (AttributeError, NotImplementedError):
                try:
                    delattr(lib, declaration.name)
                except:
                    pass

    return lib

gl = load_dll("/usr/lib/nvidia-current/libGL.so", "/usr/local/include/GL3/gl3.h", ["GL3_PROTOTYPES"])

# TODO http://www.opengl.org/registry/specs/ARB/glx_create_context.txt

