def test_soma():
    assert (sum([1, 2, 3])) == 6 #Assert verifica se o trecho bate com a segunda parte - pytest no terminal para rodar



def test_is_positive():
    assert (is_positive(5)) == True
    assert (is_positive(-1)) == False