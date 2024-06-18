class Paciente:
    pacientes = []

    def __init__(self, nome, idade, peso, genero, diagnostico, pressao, medicacao):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero
        self.diagnostico = diagnostico
        self.pressao = pressao
        self.medicacao = medicacao
        Paciente.pacientes.append(self)      

    def __str__(self):
      return f' Nome: {self.nome}  | Idade: {self.idade}  | Peso: {self.peso}  | Gênero: {self.genero}  | Diagnóstico: {self.diagnostico}  | Medicação {self.medicacao}  | Pressão {self.pressao}'
    

paciente1 = Paciente('José Alberto', 25, '80kg','Masculino','Diabético','Pressão = Alta','Medicação = Clonidina')
paciente2 = Paciente('Maria José', 35, '60kg', 'Feminino', 'Hipertensão', 'Pressão = Normal', 'Medicação = Não')
paciente3 = Paciente('João Pedro', 40, '90kg', 'Masculino', 'Dislipidemia', 'Pressão = Baixa', 'Medicação = Efortil')


print(paciente1)
print(paciente2)
print(paciente3)




