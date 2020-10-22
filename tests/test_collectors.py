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

        @pipeline
        def is_not_41(self, integer):
            if integer == 41:
                return 

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
    pass
