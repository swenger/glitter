import numpy

from glitter import EnumConstant
from glitter.contexts import context_manager

def check_property(context, name):
    value = getattr(context, name)
    try:
        if isinstance(value, EnumConstant):
            if name in ("draw_buffer", "read_buffer"):
                return # avoid problems with unavailable stereo buffers
            valid_values = list(value._enum._reverse_dict.values())
            for value in valid_values:
                setattr(context, name, value)
                assert numpy.all(getattr(context, name) == value), "property %s is broken" % name
        else:
            if type(value) is float:
                value *= 0.5
                setattr(context, name, value)
                assert numpy.all(getattr(context, name) == value), "property %s is broken" % name
                value += 0.5
                setattr(context, name, value)
                assert numpy.all(getattr(context, name) == value), "property %s is broken" % name
    except AttributeError:
        pass # "AttributeError: can't set attribute" is okay for read-only attributes

def test_property_generator():
    context = context_manager.current_context or context_manager.create_default_context()
    properties = [x for x in dir(context) if not x.startswith("_")]

    for p in properties:
        yield check_property, context, p

