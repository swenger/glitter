import numpy

from glitter import ArrayBuffer, Datatype, uint8, int8, uint16, int16, uint32, int32, float32

def check_buffer(shape, dtype, vrange):
    minval, maxval = vrange
    data = ((maxval - minval) * numpy.random.random(shape) + minval).astype(dtype.as_numpy())
    buf = ArrayBuffer(data)
    assert (buf.data == data).all(), "data is broken"
    assert buf.shape == data.shape, "shape is broken"
    assert buf.dtype == Datatype.from_numpy(data.dtype), "dtype is broken"
    assert buf._size == data.nbytes, "_size is broken"

def test_generator():
    shapes = ((4, 4, 4, 4), (4, 4, 4, 3), (4, 16, 8, 3), (5, 4, 4, 3), (5, 5, 5, 3), (6, 6, 6, 3), (7, 13, 5, 3), (1, 1, 3, 3))
    dtypes = (uint8, int8, uint16, int16, uint32, int32, float32)
    vranges = ((0, (1<<8)-1), (-1<<7, (1<<7)-1), (0, (1<<16)-1), (-1<<15, (1<<15)-1), (0, (1<<32)-1), (-1<<31, (1<<31)-1), (-10.0, 10.0))

    for shape in shapes:
        for dtype, vrange in zip(dtypes, vranges):
            yield check_buffer, shape, dtype, vrange

