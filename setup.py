from collections import namedtuple
import os

from setuptools.command.build_py import build_py as _build_py
from setuptools import setup, find_packages
from distutils import log

LibConfig = namedtuple("LibConfig", ["header", "defines", "include_dirs", "libs", "patterns"])

generated_modules = { # TODO this belongs into the setup() call and should be changeable through the command line interface
    "glitter.raw.gl": LibConfig("gl3.h", {"GL3_PROTOTYPES": 1}, [os.path.dirname(os.path.join(os.getcwd(), __file__)), "/usr/include/GL"], ["GL"], ['gl[A-Z].*', 'GL_[A-Z].*', 'GL[a-z].*']),
    "glitter.raw.glu": LibConfig("glu.h", {}, ["/usr/include/GL"], ["GLU"], ['glu[A-Z].*', 'GLU_[A-Z].*', 'GLU[a-z].*']),
    "glitter.raw.glut": LibConfig("freeglut.h", {}, ["/usr/include/GL"], ["glut"], ['glut[A-Z].*', 'GLUT_[A-Z].*', 'GLUT[a-z].*']),
    "glitter.raw.glx": LibConfig("glx.h", {}, ["/usr/include/GL"], ["GL", "X11"], ['glX[A-Z].*', 'GLX_[A-Z].*', 'GLX[a-z].*']),
}

class build_py(_build_py):
    def generate_xml(self, header, xml, defines={}, include_dirs=[]):
        commandline = ["h2xml.py", "-q", "-c", "-o", xml, header] + ["-D%s=%s" % x for x in defines.items()] + ["-I%s" % x for x in include_dirs]
        log.info(" ".join(commandline))
        from ctypeslib import h2xml
        h2xml.compile_to_xml(commandline)

    def generate_python(self, xml, pythonname, libs=[], patterns=[]):
        commandline = ["xml2py.py", "-kamdefst", "-o", pythonname, xml] + ["-l%s" % x for x in libs] + ["-r%s" % x for x in patterns]
        log.info(" ".join(commandline))
        from ctypeslib import xml2py
        xml2py.main(commandline)

    def find_generated_modules(self):
        if generated_modules is None:
            return []
        packages = {}
        modules = []
        for module, config in generated_modules.items():
            package, module_base = module.rsplit(".", 1)
            try:
                package_dir = packages[package]
            except KeyError:
                package_dir = packages[package] = self.get_package_dir(package)
                self.check_package(package, package_dir)
            modules.append((package, module_base, os.path.join(package_dir, module_base + ".py"), config))
        return modules

    def build_generated_module(self, module, module_file, package, config):
        if isinstance(package, str):
            package = package.split('.')
        elif not isinstance(package, (list, tuple)):
            raise TypeError(
                  "'package' must be a string (dot-separated), list, or tuple")
        outfile = self.get_module_outfile(self.build_lib, package, module)
        self.__updated_files.append(outfile)
        self.mkpath(os.path.dirname(outfile))
        
        # build using config into outfile
        if not os.path.isfile(outfile):
            xmlname = outfile + os.path.extsep + "xml"
            self.generate_xml(config.header, xmlname, config.defines, config.include_dirs)
            self.generate_python(xmlname, outfile, config.libs, config.patterns)
            os.remove(xmlname)

    def build_generated_modules(self):
        modules = self.find_generated_modules()
        for (package, module, module_file, config) in modules:
            self.build_generated_module(module, module_file, package, config)

    def run(self):
        self.build_generated_modules()
        _build_py.run(self)

setup(
    name = "glitter",
    version = "0.1.0",
    author = "Stephan Wenger",
    author_email = "wenger@cg.cs.tu-bs.de",
    description = "Intuitive OpenGL wrappers",
    license = "MIT",
    keywords = "opengl,graphics",
    long_description = """Intuitive OpenGL wrappers.

    Design principles:
      - Choose inituitive use over performance (no premature optimization; make it
        run, then make it fast). Users should not (need to) use the raw GL/GLUT
        wrappers at any time.
      - All GL state changes that are independent of objects should go through a
        Context object. Other changes go through the corresponding objects:
          - Vertex attribute pointer bindings are performed by vertex array objects
            only.
          - Settings for draw buffers other than the screen are performed by
            framebuffer objects only.
          - Texture bindings are performed by shader programs only.
          - If possible, changes in the GL should be reflected in the wrapper, but
            unchecked caching is okay to keep references to bound objects.
      - Array data is represented in numpy, but objects should convert as
        appropriate.
          - No loss of precision should occur when copying data to and from the
            GPU. Exceptions are made where iterables are accepted; numpy
            converts these to 64 bit datatypes, which are silently converted to 32
            bit in some places.
      - Binding and unbinding of objects should be possible automatically (via with
        statements) as well as manually (through properties of the context).
      - The library has a focus on GPGPU computing, but typical use for rendering
        should be as easy.
      - Platform independence should be sought for, although Linux/GLX is the
        primary target.
    """,
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
    # TODO download_url = "",
    # TODO url = "",

    install_requires = ["rawgl"],
    setup_requires=["ctypeslib"],
    packages = find_packages(),
    cmdclass={"build_py": build_py},
    # TODO test_suite = "nose.collector" (but run in build directory), add "nose" to setup_requires
)

