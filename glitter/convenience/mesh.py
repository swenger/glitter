"""Mesh loading methods.

@todo: Implement loading from obj, ply etc.

@author: Stephan Wenger
@date: 2012-03-06
"""

import os
import h5py
from glitter.convenience.pipeline import Pipeline
from glitter.convenience.defaultpipeline import get_default_program

def load_mesh(filename, context=None, **kwargs):
    loader = globals().get("load_%s" % (os.path.splitext(filename)[1][1:].lower()))
    if not loader:
        raise ValueError("no loader for '%s'" % filename)
    return loader(filename, context=context, **kwargs)

def load_hdf5(filename, color_defaults_to_position=True, context=None, **kwargs):
    with h5py.File(filename, "r") as f:
        kwargs["in_position"] = f["vertices"].value
        if "colors" in f:
            kwargs["in_color"] = f["colors"].value
        elif color_defaults_to_position:
            kwargs["in_color"] = kwargs["in_position"]
        if "indices" in f:
            kwargs["elements"] = f["indices"].value
    return Pipeline(get_default_program(color=("in_color" in kwargs), context=context), use_framebuffer=False, **kwargs)

load_mesh.supported_formats = tuple(sorted(key[5:] for key, value in globals().items()
        if key.startswith("load_") and callable(value) and value is not load_mesh))

__all__ = ["load_mesh", "load_hdf5"]

