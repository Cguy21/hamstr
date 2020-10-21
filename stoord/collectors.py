from typing import Callable, Any, List, Union

import httpx
from pydantic import BaseModel, parse_obj_as


class Collector:
    
    def __init__(
        self,
        func: Callable[[Any], Any],
        model: Any,
        **options: Any
    ) -> None:
        self.func = func
        self.model = model
        self.callbacks = options.pop('callbacks', [])

    def run(self) -> List[Any]:
        collected = self.func()

        if not isinstance(collected, list):
            collected = [collected]

        objects = [parse_obj_as(self.model, obj) for obj in collected]

        for callback in self.callbacks:
            objects = [callback(obj) for obj in objects]
        
        return objects
