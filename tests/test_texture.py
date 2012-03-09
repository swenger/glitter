import numpy

from glitter import Texture3D, Datatype, EnumConstant, Texture, uint8, int8, uint16, int16, uint32, int32, float32

def check_texture(shape, dtype, vrange):
    minval, maxval = vrange
    data = ((maxval - minval) * numpy.random.random(shape) + minval).astype(dtype.as_numpy())
    texture = Texture3D(data)
    assert (texture.data == data).all(), "data is broken"
    assert texture.shape == data.shape, "shape is broken (was %s, is %s)" % (data.shape, texture.shape)
    assert texture.dtype == Datatype.from_numpy(data.dtype), "dtype is broken (was %s, is %s)" % (Datatype.from_numpy(data.dtype), texture.dtype)

def test_texture_generator():
    shapes = ((4, 4, 4, 4), (4, 4, 4, 3), (4, 16, 8, 3), (5, 4, 4, 3), (5, 5, 5, 3), (6, 6, 6, 3), (7, 13, 5, 3), (1, 1, 3, 3))
    dtypes = (uint8, int8, uint16, int16, uint32, int32, float32)
    vranges = ((0, (1<<8)-1), (-1<<7, (1<<7)-1), (0, (1<<16)-1), (-1<<15, (1<<15)-1), (0, (1<<32)-1), (-1<<31, (1<<31)-1), (-10.0, 10.0))

    for shape in shapes:
        for dtype, vrange in zip(dtypes, vranges):
            yield check_texture, shape, dtype, vrange

def check_property(texture, name):
    value = getattr(texture, name)
    if isinstance(value, EnumConstant):
        valid_values = value._enum._reverse_dict.values()
        for value in valid_values:
            setattr(texture, name, value)
            assert getattr(texture, name) == value, "property %s is broken" % name
    else:
        setattr(texture, name, value)
        assert getattr(texture, name) == value, "property %s is broken" % name

def test_property_generator():
    texture = Texture3D(numpy.random.random((1, 1, 1, 4)).astype(numpy.float32))
    properties = [x for x in dir(texture) if x != "sampler" and not x.startswith("_") and type(getattr(Texture, x)) == property]

    for p in properties:
        if p in ("data", "shape", "dtype"):
            continue
        if getattr(Texture, p).fset is None:
            continue
        yield check_property, texture, p

