import pytest

from hamstr.collectors import Collector
from hamstr.endpoints import endpoint, Endpoint


@pytest.fixture
def collector():

    class BaseCollector(Collector):
        endpoints = [endpoint('https://api.example.com')]

    return BaseCollector
