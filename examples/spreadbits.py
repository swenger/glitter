#!/usr/bin/env python

"""Convert a binary volume into a float volume."""

import numpy

def spreadbits(data):
    if data.ndim == 3:
        data = data.reshape((1,) + data.shape)

    assert data.ndim == 4 and data.shape[-1] == 4, "expected shape (n_slices, height, width, 4), got shape %s" % data.shape
    assert data.dtype == numpy.uint32, "expected dtype uint32, got dtype %s" % data.dtype.name

    data = data.swapaxes(3, 2).swapaxes(2, 1) # swap color channels to second axis
    data = data[:, ::-1] # reverse color channels, why?
    data = data.reshape((-1,) + data.shape[2:]) # unify slices and color channels

    volume = numpy.zeros((data.shape[0] * 32,) + data.shape[1:] + (3,), dtype=numpy.float32)

    for i, s in enumerate(data):
        for j in range(32):
            volume[32 * i + j] = (s & (1 << j)).astype(numpy.bool)[:, :, None]

    return volume

if __name__ == "__main__":
    import sys
    import h5py

    infilename = sys.argv[1]
    outfilename = sys.argv[2]

    with h5py.File(infilename, "r") as f:
        data = f["data"].value

    volume = spreadbits(data)

    with h5py.File(outfilename, "w") as f:
        f.create_dataset("data", data=volume, compression="lzf")

