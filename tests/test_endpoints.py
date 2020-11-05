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


@pytest.mark.parametrize(
    'base, endpoint, joined', [
        ('https://api.example.com', 'examples', 'https://api.example.com/examples'),
        ('https://api.example.com/examples', 'https://api.example.com/examples', 'https://api.example.com/examples')
    ]
)
def test_get_full_url(base, endpoint, joined):
    service = Service(base)
    full = service.get_url(endpoint)
    assert full == joined


def test_service_update(service):
    assert service.base_url == 'https://api.example.com'
    assert service.api_key == None
    assert service.offset_name == 'offset'
    assert service.limit_name == 'limit'

    service.update(
        api_key='test',
    )
    assert service.api_key == 'test'

    with pytest.raises(AttributeError):
        service.update(nonexist='should raise')
        service.nonexist


def test_endpoint_introspection(service):
    test_endpoint = Endpoint('examples', service=service)
    assert test_endpoint.url == service.get_url('examples')
    assert test_endpoint.api_key == service.api_key
