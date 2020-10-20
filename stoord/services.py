from typing import Callable, Any, List, Union

import httpx
from pydantic import BaseModel, parse_obj_as


class Collector:
    
    def __init__(self, func: Callable[[Any], Any], model: Any) -> None:
        self.func = func
        self.model = model

    def collect(self) -> List[Any]:
        returns = self.func()

        if isinstance(returns, list):
            objects = returns
        else:
            objects = [returns]

        return [parse_obj_as(self.model, obj) for obj in objects]


class Service:

    http_library = httpx

    def __init__(
        self,
        name: str,
        base_url: str = None,
        api_key: str = None,
    ) -> None:
        self.name = name
        self.base_url = base_url
        self.api_key = api_key
        self.collectors = {}

    def add_collector(self, func: Callable, model: Any) -> None:
        collector = Collector(func, model)
        name = func.__name__
        self.collectors[name] = collector

    def collector(self, model: Any):
        """
        Decorator used to register a collector function.
        This does the same as :meth:`add_collector`.
        """

        def decorator(func: Callable) -> Callable:
            self.add_collector(func, model)
            return func
    
        return decorator

    # http client lib aliases
    get = http_library.get
    options = http_library.options
    head = http_library.head
    post = http_library.post
    put = http_library.put
    patch = http_library.patch
    delete = http_library.delete
