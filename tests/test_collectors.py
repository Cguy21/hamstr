from unittest.mock import MagicMock

import pytest

from stoord.app import Stoord


@pytest.fixture
def app():
    app = Stoord()
    return app


@pytest.mark.parametrize(
    'obj, model, ret', [
        (42, int, [42]),
        ('42', int, [42]),
        ([42], int, [42])
    ]
)
def test_basic_collector(app, obj, model, ret):
    
    def collector():
        return obj

    app.add_collector(collector, model)
    returns = app.collectors['collector'].run()

    assert returns == ret


def test_collector_decorator(app):

    @app.collector(int)
    def collector():
        return 42

    returns = app.collectors['collector'].run()

    assert returns == [42]


@pytest.mark.parametrize(
    'obj, returns', [
        (1, [42]),
        (101, [101])
    ]
)
def test_collector_with_callback(app, obj, returns):

    def callback(integer):
        if integer > 100:
            return integer
        return 42

    @app.collector(int, callbacks=[callback])
    def collector():
        return obj

    assert app.collectors['collector'].run() == returns
