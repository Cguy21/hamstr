import pytest
from pydantic import BaseModel

from hamstr.collectors import Collector
from hamstr.endpoints import endpoint, Endpoint


@pytest.fixture
def collector():

    class BaseCollector(Collector):
        interval = 3600
        endpoints = [endpoint('https://api.example.com')]

        class Model:
            a: int

    return BaseCollector


def test_collector_construction(collector):
    with pytest.raises(AttributeError):
        collector.Model

    assert collector.model

    settings = {
        'INTERVAL': 3600
    }

    assert collector.settings == settings
    with pytest.raises(AttributeError):
        collector.interval


def test_collector_settings(collector):
    project_settings = {}
    cli_settings = {}
    instance = collector()

    assert instance.settings == collector.settings
