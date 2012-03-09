from glitter import Sampler, EnumConstant

def check_property(sampler, name):
    value = getattr(sampler, name)
    if isinstance(value, EnumConstant):
        valid_values = value._enum._reverse_dict.values()
        for value in valid_values:
            setattr(sampler, name, value)
            assert getattr(sampler, name) == value, "property %s is broken" % name
    else:
        setattr(sampler, name, value)
        assert getattr(sampler, name) == value, "property %s is broken" % name

def test_property_generator():
    sampler = Sampler(0)
    properties = [x for x in dir(sampler) if x != "context" and not x.startswith("_") and type(getattr(Sampler, x)) == property]

    for p in properties:
        yield check_property, sampler, p

