from setuptools import setup, find_packages

setup(
    name = "glitter",
    version = "0.1.0",
    author = "Stephan Wenger",
    author_email = "wenger@cg.cs.tu-bs.de",
    description = "Intuitive OpenGL wrappers",
    install_requires = ["rawgl"],
    setup_requires=["nose>=1.0"],
    license = "MIT",
    keywords = "opengl,graphics",
    # TODO download_url = "",
    # TODO url = "",
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
    packages = find_packages(),
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
    test_suite = 'nose.collector',
)

