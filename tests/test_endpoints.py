import pytest

from hamstr.endpoints import Endpoint, endpoint, Service


def test_endpoint_constructor():
    url = 'https://api.example.com/examples'
    from_func = endpoint(url)
    assert from_func.url == url


def test_endpoint_with_service():
    service = Service('https://api.example.com')
    from_func = endpoint('examples', service=service)
    assert from_func.url == 'https://api.example.com/examples'


@pytest.fixture
def service() -> Service:
    example = Service('https://api.example.com')
    return example
