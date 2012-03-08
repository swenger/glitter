from setuptools import setup, find_packages

setup( # TODO build docs and rawgl automatically, add test target
    name = "glitter",
    version = "0.1.0",
    author = "Stephan Wenger",
    author_email = "wenger@cg.cs.tu-bs.de",
    description = "GL InTuiTive Extensions Repository",
    license = "MIT",
    keywords = "opengl,graphics",
    download_url = "", # TODO
    url = "", # TODO
    long_description = """Intuitive OpenGL wrapper.

    """, # TODO
    requires = ["rawgl"], # TODO package rawgl with glitter
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
)

