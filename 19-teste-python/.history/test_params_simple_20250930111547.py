import pytest

def adicionar(x, y):
    return x + y

@pytest.mark.parametrize( # Parâmetros pré definidos
    "entrada_x, entrada_y, resultado_esperado",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (5, 7, 12)
    ]
)
def test_adicionar(entrada_x, entrada_y, resultado_esperado):
    resultado = adicionar(entrada_x, entrada_y)
    
    assert (resultado == resultado_esperado)