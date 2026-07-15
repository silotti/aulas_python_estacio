#compoe alterando classe: Pessoa
class Endereco:
    def __init__(self, ruaEnd, cidadeEnd):
        self.rua=ruaEnd 
        self.cidade=cidadeEnd

class Pessoa:
    def __init__(self, nomePes, ruaPes, cidadePes):
        self.nome=nomePes
        self.end1=Endereco(ruaPes, cidadePes)

pes1=Pessoa("Ana", "Rua A","Cidade X")
print(pes1.nome, "-" , pes1.end1.rua, pes1.end1.cidade)
