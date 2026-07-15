class Endereco:
    def __init__(self, ruaEnd, cidadeEnd):
        self.rua = ruaEnd
        self.cidade = cidadeEnd

class Pessoa:
    def __init__(self, nomePes):
        self.nome = nomePes

#classes independentes
pes1 = Pessoa("Ana") #cria obj pes1: #nomePes
local1 = Endereco("Rua A", "Cidade A") #cria obj local1:ruaEnd, cidadeEnd
print(pes1.nome, "-", local1.rua, local1.cidade)

#classes agregadas(vinculas), local1 agora é atributo de pes1 
pes1 = Pessoa("Ana") #cria obj pes1: #nomePes
pes1.local1 = Endereco("Rua A", "Cidade A") #cria obj pes1.local1:ruaEnd, cidadeEnd
print(pes1.nome, "-", pes1.local1.rua, pes1.local1.cidade)
