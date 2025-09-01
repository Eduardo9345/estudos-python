def my_decorator(function):
    def wrapper():
        print("Antes de executar a funcao")
        function()
        print("Depois de executar a funcao")
    
    return wrapper

def split_string(function):
    def wrapper():
        string = function()
        splited_string = string.split()
        return splited_string
    
    return wrapper
