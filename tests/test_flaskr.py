import pytest


@pytest.fixture
def client():
    test1()


def test1():
    assert 1 == 1
