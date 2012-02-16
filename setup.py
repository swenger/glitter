from distutils.core import setup

setup(
  name = "glitter",
  version = "0.1.0",
  author = "Stephan Wenger",
  author_email = "wenger@cg.cs.tu-bs.de",
  description = "GL InTuiTive Extensions Repository",
  license = "MIT",
  packages = ["glitter", "rawgl"], # TODO run make and only include gl.py, glu.py and glut.py from rawgl
)

