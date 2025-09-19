from functions import somar_lista, encontrar_valor
import pytest #Tratamento de exceções

def test_somar_lista():
    assert (somar_lista([1, 2, 3, 4]) == 10)
    assert (somar_lista([2.3, 4.5, 1.2]) == 8.0)
    assert (somar_lista([]) == 0)
    
    with pytest.raises(ValueError):
        somar_lista([1, 2, 'a'])