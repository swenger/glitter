class InstanceDescriptorMixin(object):
    def __getattribute__(self, name):
        attr = super(InstanceDescriptorMixin, self).__getattribute__(name)
        if hasattr(attr, "__get__"):
            return attr.__get__(self, self.__class__)
        else:
            return attr

    def __setattr__(self, name, value):
        try:
            attr = super(InstanceDescriptorMixin, self).__getattribute__(name)
            return attr.__set__(self, value)
        except AttributeError:
            return super(InstanceDescriptorMixin, self).__setattr__(name, value)

class Binding(object):
    def get(self):
        raise NotImplementedError

    def set(self, id):
        raise NotImplementedError
    
    def __enter__(self):
        self.old_id = self.get()
        self.set(self.id)

    def __exit__(self, type, value, traceback):
        self.set(self.old_id)

