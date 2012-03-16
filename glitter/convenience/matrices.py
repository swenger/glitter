"""Convenience factory methods for geometric transform matrices.

@author: Stephan Wenger
@date: 2012-03-05
"""

import numpy as _np

def identity_matrix():
    return _np.matrix(_np.eye(4))

def rotation_matrix(angle, axis, degrees=False):
    if degrees:
        angle = _np.deg2rad(angle)
    c, s = _np.cos(angle), _np.sin(angle)
    x, y, z = axis / _np.sqrt(sum(a ** 2 for a in axis))
    return _np.matrix((
        (x * x * (1 - c) + c,     x * y * (1 - c) - z * s, x * z * (1 - c) + y * s, 0),
        (y * x * (1 - c) + z * s, y * y * (1 - c) + c,     y * z * (1 - c) - x * s, 0),
        (z * x * (1 - c) - y * s, z * y * (1 - c) + x * s, z * z * (1 - c) + c,     0),
        (0,                       0,                       0,                       1),
        ))

def scale_matrix(*s):
    if len(s) == 3:
        x, y, z = s
    elif len(s) == 1:
        x = y = z = s[0]
    else:
        raise ValueError("invalid scaling parameter")
    return _np.matrix(((x, 0, 0, 0), (0, y, 0, 0), (0, 0, z, 0), (0, 0, 0, 1)))

__all__ = ["identity_matrix", "rotation_matrix", "scale_matrix"]

