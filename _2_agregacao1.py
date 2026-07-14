class Endereco:
    def __init__(self, ruaEnd, cidadeEnd):
        self.rua = ruaEnd
        self.cidade = cidadeEnd

class Pessoa:
    def __init__(self, nomePes):
        self.nome = nomePes


pes1 = Pessoa("Ana") #cria obj pes1
pes1.local1 = Endereco("Rua A", "Cidade A") #atributo1 p/ obj pes1
pes1.local2 = Endereco("Rua B", "Cidade B") #atributo2 p/ obj pes1
print(pes1.nome, "-", pes1.local1.rua, pes1.local1.cidade)
print(pes1.nome, "-", pes1.local2.rua, pes1.local2.cidade)