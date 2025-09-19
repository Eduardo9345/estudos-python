from functions import somar_lista, encontrar_valor
import pytest #Tratamento de exceções

def test_somar_lista():
    assert (somar_lista([1, 2, 3, 4]) == 10)