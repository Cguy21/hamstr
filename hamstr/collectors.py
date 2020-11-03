

class CollectorMeta(type):

    def __new__(mcs, name, bases, namespace, **kwargs):
        cls = super().__new__(mcs, name, bases, namespace, **kwargs)
        return cls


class Collector(metaclass=CollectorMeta):
    pass
