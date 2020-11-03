from __future__ import annotations
from urllib.parse import urljoin


def endpoint(
    url_or_ending: str,
    *,
    service: Service = None,
    api_key: str = None,
    offset_name: str = None,
    limit_name: str = None
):
    if not service:
        service = Service(
            api_key=api_key,
            offset_name=offset_name,
            limit_name=limit_name
        )
    return Endpoint(url_or_ending, service)


class Endpoint:

    def __init__(
        self,
        url_or_ending: str,
        service: Service
    ):
        self.service = service
        if self.service.base_url:
            self.url = self.service.get_full_url(url_or_ending)
        else:
            self.url = url_or_ending


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

    def get_full_url(self, endpoint: str) -> str:
        """
        Returns the result of joining `base_url` and `endpoint`.

        >>> get_full_url('examples')
        'https://api.example.com/examples'
        """
        return urljoin(self.base_url, endpoint)
