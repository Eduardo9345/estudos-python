## Fixture serve para reaproveitar os parametros a serem usados para testagem

# 🔹 O que são fixtures?
# Fixtures são formas de preparar dados ou contexto antes de rodar os testes.
# Elas servem para evitar repetição e deixar o código mais organizado.

import pytest

@pytest.fixture
def list_sample():
    return [10, 9, 8, 7, 6]

def test_sum(list_sample):
    assert (sum(list_sample) == 40) # reaproveita a lista
    
def test_len(list_sample):
    assert (len(list_sample) == 5)
