from typing import Callable, Any, List, Union

from pydantic import BaseModel, parse_obj_as


class Collector():
    model: Any = None

    def __init__(self):
        self.callbacks = []

    def collect(self):
        raise NotImplementedError

    def run(self) -> List[Any]:
        collected = self.collect()

        if not isinstance(collected, list):
            collected = [collected]

        objects = [parse_obj_as(self.model, obj) for obj in collected]

        for callback in self.callbacks:
            objects = [callback(obj) for obj in objects]
        
        return objects
