from weakref import WeakSet
from rawgl import gl as _gl

from Context import default_context

class GLObject(object):
    _generate_id = NotImplemented
    _delete_id = NotImplemented
    _type = NotImplemented
    _db = {}

    def __init__(self, other=None, context=None):
        if any(x is NotImplemented for x in (self._generate_id, self._delete_id)):
            raise TypeError("%s is abstract" % self.__class__.__name__)
        if other is None:
            self._context = context or default_context
            with self._context:
                if len(self._generate_id.argtypes) == 0:
                    self._id = self._generate_id()
                elif len(self._generate_id.argtypes) == 1:
                    self._id = self._generate_id(self._type)
                else:
                    _id = _gl.GLuint()
                    self._generate_id(1, _gl.pointer(_id))
                    self._id = _id.value
        else:
            if other._generate_id != self._generate_id:
                raise TypeError("cannot cast %s into %s" % (other.__class__.__name__, self.__class__.__name__))
            if other._clone_into.im_func == GLObject._clone_into.im_func: # _clone_into has not been overridden
                raise TypeError("cannot clone %s" % other.__class__.__name__)
            self._context = other._context
            self._id = other._id
            other._clone_into(self)
        self._db.setdefault((self._generate_id.__name__, self._id), WeakSet()).add(self)

    @classmethod
    def _retrieve(cls, _id):
        return cls._db.get((cls._generate_id.__name__, _id), None)

    def __del__(self):
        try:
            self._db[self._generate_id.__name__, self._id].remove(self) # TODO will self have been removed from the WeakSet anyway by now?
        except:
            pass
        try:
            if not self._db[self._generate_id.__name__, self._id]: # nobody uses the _id any more, so free it
                if len(self._delete_id.argtypes) == 1:
                    self._delete_id(self._id)
                else:
                    self._delete_id(1, _gl.pointer(_gl.GLuint(self._id)))
                self._id = 0
        except:
            pass

    def _clone_into(self, other):
        pass

class BindableObject(GLObject):
    _binding = NotImplemented

    def __init__(self, other=None, context=None):
        super(BindableObject, self).__init__(other, context)
        if any(x is NotImplemented for x in (self._binding,)):
            raise TypeError("%s is abstract" % self.__class__.__name__)
        self._stack = []
    
    def bind(self):
        old_binding = getattr(self._context, self._binding)
        setattr(self._context, self._binding, self._id)
        return old_binding

    def __enter__(self):
        self._stack.append(self.bind())

    def __exit__(self, type, value, traceback):
        setattr(self._context, self._binding, self._stack.pop())

class BeginEndObject(GLObject):
    _target = NotImplemented
    _begin = NotImplemented
    _end = NotImplemented

    def __init__(self, other=None, context=None):
        super(BeginEndObject, self).__init__(other, context)
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

