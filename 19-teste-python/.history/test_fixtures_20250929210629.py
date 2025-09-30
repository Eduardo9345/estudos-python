## Fixture serve para reaproveitar os parametros a serem usados para testagem

import pytest

@pytest.fixture
def list_sample():
    return [10, 9, 8, 7, 6]

def test_sum(list_sample):
    assert (sum(list_sample) == 40) # reaproveita a lista
