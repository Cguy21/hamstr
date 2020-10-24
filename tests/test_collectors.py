from unittest.mock import MagicMock

import pytest

from hamstr.collectors import Collector, pipeline


def test_not_implemented_collector():

    class TestCollector(Collector):
        model = int

    collector = TestCollector()

    with pytest.raises(NotImplementedError):
        collector.run()


@pytest.fixture
def collector():

    class TestCollector(Collector):
        model = int

        def collect(self):
            return 42

    return TestCollector


@pytest.mark.parametrize(
    'obj, model, ret', [
        (42, int, [42]),
        ('42', int, [42]),
        ([42], int, [42])
    ]
)
def test_basic_collector(collector, obj, model, ret):
    assert collector().run() == ret


def test_pipeline_registration(collector):
    
    class TestCollector(collector):

        @pipeline
        def smaller_than_42(self, integer):
            if integer > 42:
                return 42
            return integer
