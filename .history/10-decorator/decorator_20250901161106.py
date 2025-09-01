def my_decorator(function):
    def wrapper():
        print("Antes de executar a funcao")
        function()
        print("Depois de executar a funcao")
    
    return wrapper