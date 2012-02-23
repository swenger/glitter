from rawgl import gl as _gl

from Context import get_default_context

class GLObject(object):
    def __init__(self, context=None):
        self._context = context or get_default_context()

class ManagedObject(GLObject):
    _generate_id = NotImplemented # constructor function, e.g. glGenShader
    _delete_id = NotImplemented # destructor function, e.g. glDeleteShader
    _type = NotImplemented # type (if appropriate), e.g. GL_VERTEX_SHADER
    _db = NotImplemented # name of corresponding object database in context, e.g. "shaders"

    def __init__(self, context=None):
        if any(x is NotImplemented for x in (self._generate_id, self._delete_id)):
            raise TypeError("%s is abstract" % self.__class__.__name__)
        super(ManagedObject, self).__init__(context)
        with self._context:
            if len(self._generate_id.argtypes) == 0:
                self._id = self._generate_id()
            elif len(self._generate_id.argtypes) == 1:
                self._id = self._generate_id(self._type)
            else:
                _id = _gl.GLuint()
                self._generate_id(1, _gl.pointer(_id))
                self._id = _id.value
        getattr(self._context, self._db)._objects[self._id] = self

    def __del__(self):
        try:
            with self._context:
                if len(self._delete_id.argtypes) == 1:
                    self._delete_id(self._id)
                else:
                    self._delete_id(1, _gl.pointer(_gl.GLuint(self._id)))
            self._id = 0
        except:
            pass

class BindableObject(GLObject):
    # this is not generic; e.g. binding buffers to different targets,
    # framebuffers to read or draw only, or textures and samplers to different
    # units is not covered

    # _on_bind and _on_release, if defined, will be called by the context when
    # the value is bound and released

    _binding = NotImplemented # name of corresponding binding in context, e.g.  "array_buffer_binding"

    def __init__(self, context=None):
        super(BindableObject, self).__init__(context)
        if any(x is NotImplemented for x in (self._binding,)):
            raise TypeError("%s is abstract" % self.__class__.__name__)
        self._stack = []
    
    def bind(self):
        old_binding = getattr(self._context, self._binding)
        setattr(self._context, self._binding, self)
        return old_binding

    def __enter__(self):
        self._context.__enter__()
        self._stack.append(self.bind())

    def __exit__(self, type, value, traceback):
        setattr(self._context, self._binding, self._stack.pop())
        self._context.__exit__(type, value, traceback)

class BindReleaseObject(GLObject):
    bind = NotImplemented
    release = NotImplemented

    def __init__(self, context=None):
        super(BindReleaseObject, self).__init__(context)
        if any(x is NotImplemented for x in (self.bind, self.release)):
            raise TypeError("%s is abstract" % self.__class__.__name__)
    
    def __enter__(self):
        self._context.__enter__()
        self.bind()

    def __exit__(self, type, value, traceback):
        self.release()
        self._context.__exit__(type, value, traceback)


class BeginEndObject(GLObject):
    _target = NotImplemented
    _begin = NotImplemented
    _end = NotImplemented

    def __init__(self, context=None):
        super(BeginEndObject, self).__init__(context)
        if any(x is NotImplemented for x in (self._begin, self._end)):
            raise TypeError("%s is abstract" % self.__class__.__name__)

    def begin(self):
        if self._target is NotImplemented:
            self._begin(self._id)
        else:
            self._begin(self._target, self._id)

    def end(self):
        if self._target is NotImplemented:
            self._end()
        else:
            self._end(self._target)

    def __enter__(self):
        self.begin()

    def __exit__(self, type, value, traceback):
        self.end()

