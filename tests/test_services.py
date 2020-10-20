from unittest.mock import MagicMock

import pytest

from stoord.services import Service


@pytest.fixture
def service():
    service = Service('test')
    return service


@pytest.mark.parametrize(
    'obj, model, ret', [
        (42, int, [42]),
        ('42', int, [42]),
        ([42], int, [42])
    ]
)
def test_basic_collector(service, obj, model, ret):
    
    def collector():
        return obj

    service.add_collector(collector, model)
    returns = service.collectors['collector'].collect()

    assert returns == ret


def test_collector_decorator(service):

    @service.collector(int)
    def collector():
        return 42

    returns = service.collectors['collector'].collect()

    assert returns == [42]
