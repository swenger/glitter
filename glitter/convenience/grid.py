"""Provides coordinate handling methods for pixel and other grids.

@author: Kai Ruhl
@since: 2013-03"""

import numpy as np


def get_pixel_index_grid(wid, hei, ndim=2, normalize=False, dtype=np.float32):
    """Given width and height, returns an array containing the pixel x and y
    position at each position, and zeros at additional dimensions."""
    nx, ny = np.arange(wid), np.arange(hei)
    if normalize:
        nx = (nx + .5) / wid
        ny = (ny + .5) / hei
    mx, my = np.meshgrid(nx, ny)
    mz = np.zeros((hei, wid, ndim - 2), dtype=np.float32)
    M = dtype(np.dstack((mx, my, mz)))
    return M


def get_triangle_index_grid(wid, hei):
    """Given width and height, and assuming a meshgrid containing each pixel
    position, returns a triangle index configuration suitable for a mesh
    surface visualizing the points."""
    xy = np.arange(wid * hei).reshape(hei, wid)[:-1, :-1] # omit -1 element.
    I = np.dstack((xy, xy + 1, xy + wid, xy + 1, xy + wid + 1, xy + wid))
    I = I.reshape(hei - 1, (wid - 1) * 2, 3) # triangles
    return I
