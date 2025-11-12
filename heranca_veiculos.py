class veiculos:
  def __init__(self, ano, modelo, marca):
    self.ano = ano
    self.modelo = modelo
    self.marca = marca

class carro(veiculos):
  def __init__(self, ano, modelo, marca, cavalos, tracao):
    self.ano = ano
    self.modelo = modelo
    self.marca = marca
    self.cavalos = cavalos
    self.tracao = tracao
  def exibirInfo(self):
    print(f"""Ano: {self.ano};
    Modelo: {self.modelo};
    Marca: {self.marca};
    Cavalos: {self.cavalos};
    Tracao: {self.tracao}""")
    


Uno = carro(1998, "Fiat Uno", "Fiat", 47, "FWD")
Uno.exibirInfo
