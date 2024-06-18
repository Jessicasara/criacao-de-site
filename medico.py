class Medico:
    medicos = []
  
    def __init__ (self, nome, especialidade, crm):
        self.nome = nome
        self.especialidade = especialidade
        self.crm = crm
        Medico.medicos.append(self)

    def __str__(self):
      return f' Nome: {self.nome} |  Especialidade: {self.especialidade} | CRM {self.crm}'

medico1 = Medico('Dr. José Alberto', 'Cardiologista', 57432)
medico2 = Medico('Dr. Mario Gloss', 'Clinico Geral', 78945)
medico3 = Medico('Dra. Lacraia Gonçalves', 'Neurologista', 78954)

print(medico1)
print(medico2)
print(medico3)