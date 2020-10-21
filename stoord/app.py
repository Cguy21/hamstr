from typing import Callable, Any

from starlette.applications import Starlette

from .collectors import Collector


class Stoord(Starlette):

    def __init__(
        self,
        debug: bool = False,
        routes: list = None,
        middleware: list = None,
        exception_handlers: dict = None,
        on_startup: list = None,
        on_shutdown: list = None,
    ):
        super().__init__(debug, routes, middleware, exception_handlers,
                         on_startup, on_shutdown)
        self.collectors = {}

    def add_collector(self, func: Callable, model: Any, **options: Any) -> None:
        collector = Collector(func, model, **options)
        name = func.__name__
        self.collectors[name] = collector

    def collector(self, model: Any, **options: Any):
        """
        Decorator used to register a collector function.
        This does the same as :meth:`add_collector`.
        """

        def decorator(func: Callable) -> Callable:
            self.add_collector(func, model, **options)
            return func

        return decorator
