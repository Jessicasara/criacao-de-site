class Escaleiro:
  escaleiro = []
  
  def __init__(self, nome, registro, telefone):
    self._nome = nome
    self._registro = registro
    self._telefone = telefone
    Escaleiro.escaleiro.append(self)

escaleiro1 = Escaleiro('Joaquim Filho', 'MG - 98567125', 985671236)
print(escaleiro1)

class Cor:
  def __init__(self, nome, rgb):
    self.nome = nome
    self.rgb = rgb

  def exibir_cor(self):
    print(f'Cor: {self.nome} | RGB: {self.rgb}')

cor1 = Cor('Verde', (0, 255, 0))
cor2 = Cor('Vermelho', (255,0,0))
cor3 = Cor('Amarelo', (255,255,0))