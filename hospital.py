class Hospital:
    hospital = []
  
    def __init__(self, nome, contato, cor, endereco):
      self.nome = nome
      self.contato = contato
      self.cor = cor
      self.endereco = endereco   
      Hospital.hospital.append(self)

    def __str__(self):
      return f' Nome: {self.nome} |  Contato: {self.contato} | Cor: {self.cor} | Endereço: {self.endereco}'

hospital1 = Hospital('Hospital Santa Casa', 784510369, 'Verde', 'Rua São Paulo, nº 96')
hospital2 = Hospital('Hospital Das Cinicas', 985476313, 'Azul' , 'Av. Brasil, nº 85')
hospital3 = Hospital('Hospital Bom Jesus', 789541236, 'Amarelo', 'Rua Silveiro Rosa, nº 25')
  
print(hospital1)
print(hospital2)
print(hospital3)