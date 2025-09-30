import pytest

def calcular_area(base, altura):
    return base * altura


@pytest.fixture
def dados_teste():
    """
    Fixture que fornece diferentes conjuntos de dados para
    testar a função de calculo de  área
    """
    return  [
        {"base" : 2, "altura" :  3, "resultado_esperado" : 6},
        {"base" : 5, "altura" :  4, "resultado_esperado" : 20},
        {"base" : 7, "altura" :  2, "resultado_esperado" : 14},
        {"base" : 0, "altura" :  10, "resultado_esperado" : 0},
        {"base" : 10, "altura" :  0, "resultado_esperado" : 0}
    ]


@pytest.mark.parametrize(
    "dados",
    [
        {"base" : 2, "altura" :  3, "resultado_esperado" : 6},
        {"base" : 5, "altura" :  4, "resultado_esperado" : 20},
        {"base" : 7, "altura" :  2, "resultado_esperado" : 14},
        {"base" : 0, "altura" :  10, "resultado_esperado" : 0},
        {"base" : 10, "altura" :  0, "resultado_esperado" : 0}
    ]
)
def test_calcular_area(dados):
    base = dados['base']
    altura = dados['altura']
    esperado = dados ['resultado_esperado']
    
    resultado = calcular_area(base, altura)
    
    assert(resultado == esperado)