from __future__ import annotations
from urllib.parse import urljoin
from dataclasses import dataclass


def endpoint(
    url: str,
    *,
    api_key: str = None,
    headers: dict = None,
    schema: Schema = None,
    offset_name: str = None,
    limit_name: str = None,
    service: Service = None
):
    """
    Creates Endpoints for collector to use.
    """
    if service:
        url = urljoin(service.base_url, url)
        if headers:
            headers.update(service.headers or {})

        # function args have higher priority
        # than service args.
        api_key = api_key or service.api_key
        offset_name = offset_name or service.offset_name 
        limit_name = limit_name or service.limit_name
    return Endpoint(
        url,
        api_key=api_key,
        headers=headers,
        offset_name=offset_name,
        limit_name=limit_name
    )


class Endpoint:

    def __init__(
        self,
        url: str,
        *,
        api_key: str = None,
        headers: dict = None,
        offset_name: str = None,
        limit_name: str = None
        
    ):
        self.url = url
        self.api_key = api_key
        self.headers = headers
        self.offset_name = offset_name or 'offset'
        self.limit_name = limit_name or 'limit'
        


@dataclass
class Service:
    base_url: str = None
    api_key: str = None
    headers: dict = None
    offset_name: str = None
    limit_name: str = None
