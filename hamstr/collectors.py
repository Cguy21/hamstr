from typing import Callable, Any, List, Union

import httpx
from pydantic import BaseModel, parse_obj_as


class Pipeline:
    is_pipe = True


def pipeline(obj: Any, *args, **kwargs):

    def decorator(func):
        pass
    setattr(decorator, 'is_pipe', True)

    return decorator


class CollectorMeta(type):
    
    def __new__(mcs, name, bases, namespace, **kwargs):
        for n, v in namespace.items():
            if n == 'test':
                print(dir(v))
        cls = super().__new__(mcs, name, bases, namespace)
        return cls


class Collector(metaclass=CollectorMeta):
    model: Any = None

    def __init__(self):
        self.callbacks = []

    def collect(self):
        raise NotImplementedError

    @pipeline
    def test(self):
        pass

    def run(self) -> List[Any]:
        collected = self.collect()

        if not isinstance(collected, list):
            collected = [collected]

        objects = [parse_obj_as(self.model, obj) for obj in collected]

        for callback in self.callbacks:
            objects = [callback(obj) for obj in objects]
        
        return objects
