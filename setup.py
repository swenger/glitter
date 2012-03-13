import os
import re

from setuptools import Command
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as _build_py
from distutils import log

class generate_py_base(Command):
    user_options = [
        ("header=", None, "header file"),
        ("defines=", None, "C preprocessor variables to define"),
        ("include-dirs=", None, "C include directories (separated by %s)" % os.pathsep),
        ("libs=", None, "names of libraries to link against (separated by %s)" % os.pathsep),
        ("patterns=", None, "regular expressions for symbols to include (separated by whitespace)"),
        ("force", None, "rebuild even if target files exist"),
    ]
    
    def generate_xml(self, header, xml, defines=[], include_dirs=[]):
        commandline = ["h2xml.py", "-q", "-c", "-o", xml, header] + ["-D%s" % x for x in defines] + ["-I%s" % x for x in include_dirs]
        log.debug(" ".join(commandline))
        from ctypeslib import h2xml
        h2xml.compile_to_xml(commandline)

    def generate_python(self, xml, pythonname, libs=[], patterns=[]):
        commandline = ["xml2py.py", "-kamdefst", "-o", pythonname, xml] + ["-l%s" % x for x in libs] + ["-r%s" % x for x in patterns]
        log.debug(" ".join(commandline))
        from ctypeslib import xml2py
        xml2py.main(commandline)

    def initialize_options(self):
        self.header = None
        self.defines = []
        self.include_dirs = []
        self.libs = []
        self.patterns = []
        self.force = None

    def finalize_options(self):
        self.set_undefined_options("generate_py", ("force", "force"))
        if isinstance(self.defines, basestring):
            self.defines = re.findall("[A-Za-z0-9_]+", self.defines)
        if isinstance(self.include_dirs, basestring):
            self.include_dirs = self.include_dirs.split(os.pathsep)
        if isinstance(self.libs, basestring):
            self.libs = self.libs.split(os.pathsep)
        if isinstance(self.patterns, basestring):
            self.patterns = self.patterns.split()

    def run(self):
        basename = os.path.join("glitter", "raw", self.name)
        if self.distribution.package_dir is not None:
            basename = os.path.join(self.distutils.package_dir, basename)
        xmlname = basename + os.path.extsep + "xml"
        pyname = basename + os.path.extsep + "py"
        if self.force or not os.path.isfile(pyname):
            self.generate_xml(self.header, xmlname, self.defines, self.include_dirs)
            self.generate_python(xmlname, pyname, self.libs, self.patterns)
            os.remove(xmlname)

class generate_gl(generate_py_base):
    description = "generate ctypes wrapper for OpenGL"
    name = "gl"

    def initialize_options(self):
        generate_py_base.initialize_options(self)
        self.header = os.path.join(os.path.dirname(os.path.join(os.getcwd(), __file__)), "gl3.h")
        self.defines = ["GL3_PROTOTYPES"]
        self.include_dirs = ["/usr/include/GL"]
        self.libs = ["GL"]
        self.patterns = ['gl[A-Z].*', 'GL_[A-Z].*', 'GL[a-z].*']

class generate_glu(generate_py_base):
    description = "generate ctypes wrapper for GLU"
    name = "glu"

    def initialize_options(self):
        generate_py_base.initialize_options(self)
        self.header = "glu.h"
        self.include_dirs = ["/usr/include/GL"]
        self.libs = ["GLU"]
        self.patterns = ['glu[A-Z].*', 'GLU_[A-Z].*', 'GLU[a-z].*']
        
class generate_glut(generate_py_base):
    description = "generate ctypes wrapper for GLUT"
    name = "glut"

    def initialize_options(self):
        generate_py_base.initialize_options(self)
        self.header = "freeglut.h"
        self.include_dirs = ["/usr/include/GL"]
        self.libs = ["glut"]
        self.patterns = ['glut[A-Z].*', 'GLUT_[A-Z].*', 'GLUT[a-z].*']

class generate_glx(generate_py_base):
    description = "generate ctypes wrapper for GLX"
    name = "glx"

    def initialize_options(self):
        generate_py_base.initialize_options(self)
        self.header = "glx.h"
        self.include_dirs = ["/usr/include/GL"]
        self.libs = ["GL", "X11"]
        self.patterns = ['glX[A-Z].*', 'GLX_[A-Z].*', 'GLX[a-z].*']

class generate_py(Command):
    description = "generate ctypes wrappers"
    
    user_options = [
        ("force", None, "rebuild even if target files exist"),
    ]
    
    commands = ["generate_gl", "generate_glu", "generate_glut", "generate_glx"]

    def initialize_options(self):
        self.force = None

    def finalize_options(self):
        self.set_undefined_options("build", ("force", "force"))

    def run(self):
        for command in self.commands:
            self.run_command(command)

class build_py(_build_py):
    def run(self):
        self.run_command("generate_py")
        _build_py.run(self)

setup(
    name = "glitter",
    version = "0.1.1",
    author = "Stephan Wenger",
    author_email = "wenger@cg.cs.tu-bs.de",
    description = "Intuitive OpenGL wrappers",
    license = "MIT",
    keywords = "opengl,graphics",
    long_description = open("README.txt").read(),
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Multimedia :: Graphics :: 3D Rendering",
        "Topic :: Software Development :: Libraries",
        ],
    download_url = "http://pypi.python.org/pypi/glitter",
    url = "http://packages.python.org/glitter",
    setup_requires=["ctypeslib", "nose"],
    packages = find_packages(),
    test_suite = "nose.collector",
    cmdclass= {
        "generate_gl": generate_gl,
        "generate_glu": generate_glu,
        "generate_glut": generate_glut,
        "generate_glx": generate_glx,
        "generate_py": generate_py,
        "build_py": build_py,
    },
)

