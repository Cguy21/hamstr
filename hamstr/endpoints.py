from __future__ import annotations
from urllib.parse import urljoin


def endpoint(
    url_or_ending: str,
    service: Service = None,
    **options
):
    if not service:
        service = Service(**options)
    else:
        service.update(**options)
    return Endpoint(url_or_ending, service)


class Endpoint:

    def __init__(self, url: str, service: Service):
        self._url = url
        self.service = service

    @property
    def url(self):
        if self.service.base_url:
            return self.service.get_url(self._url)
        return self._url
    
    @property
    def api_key(self):
        return self.service.api_key


class Service:
    """
    Class to define and easily reuse common data for your endpoints.

    >>> example = Service('https://api.example.com', api_key='test')
    >>> endpoints = [endpoint('examples', service=example)]
    """

    def __init__(
        self,
        base_url: str = None,
        api_key: str = None,
        offset_name: str = None,
        limit_name: str = None
    ):
        self.base_url = base_url
        self.api_key = api_key
        self.offset_name = offset_name or 'offset'
        self.limit_name = limit_name or 'limit'

    def update(self, **options):
        for k, v in options.items():
            if getattr(self, k, 'not') != 'not':
                setattr(self, k, v)

    def get_url(self, endpoint: str) -> str:
        """
        Returns the result of joining `base_url` and `endpoint`.

        >>> get_full_url('examples')
        'https://api.example.com/examples'
        """
        return urljoin(self.base_url, endpoint)
