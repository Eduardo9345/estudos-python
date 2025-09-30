"""
O que são testes parametrizados em Python?

Testes parametrizados são uma forma de rodar o mesmo teste várias vezes com dados diferentes, sem precisar escrever várias funções de teste repetidas.
Isso é muito útil quando você quer validar a mesma lógica com diferentes entradas e saídas esperadas.

Evitam duplicação de código.

Fácil adicionar novos cenários (só incluir mais uma tupla na lista).

Ajuda a cobrir casos de borda rapidamente.
É diferente das fixtures pois roda contextos diferentes

"""

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