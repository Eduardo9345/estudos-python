class Carro():

    def __init__(self, modelo="", marca="", ano=0):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano

    def __str__(self):
        return f"- Modelo: {self.modelo}\n- Marca: {self.marca}\n- Ano: {self.ano}"
    
    def acelerar(self):
        print(f"O carro {self.modelo} está acelerando!")

class Caminhao(Carro):

    def __init__(self, modelo="", marca="", ano=0):
        super().__init__(modelo, marca, ano)
        self.combustivel = "Diesel"

    def acelerar(self):
        print("Queimando diesel!")
        return super().acelerar()
    
    def get_combustivel(self):
        return self.combustivel

carro1 = Carro("Palio", "Volgwagen", 2013)

print(carro1)
carro1.acelerar()

carro2 = Caminhao("Truck", "Mercedes-Benz", 2015)

print(carro2)
print(carro2.get_combustivel())
carro2.acelerar()