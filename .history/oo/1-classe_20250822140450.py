class Carro():

    def __init__(self, modelo="", marca="", ano=0):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano

    def __str__(self):
        return f"Modelo: {self.modelo}\n- Marca: {self.marca}\n- Ano: {self.ano}"

carro1 = Carro("Palio", "Volgwagen", 2013)