from functions import is_positive, valida_email

def test_soma():
    assert (sum([1, 2, 3])) == 6 #Assert verifica se o trecho bate com a segunda parte - pytest no terminal para rodar

def test_is_positive():
    assert (is_positive(5)) == True
    assert (is_positive(-1)) == False
    
def test_email():
    assert (valida_email("email@gmail.com")) == True
    assert (valida_email("emailgmailcom")) == False