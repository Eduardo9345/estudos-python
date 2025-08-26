def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if(num2 == 0):
        raise ValueError("Não se pode dividir por 0!")
    
    return num1 / num2