#agrega mais altera classe: Pessoa
class Endereco:
    def __init__(self, ruaEnd, cidadeEnd):
        self.rua=ruaEnd 
        self.cidade=cidadeEnd

class Pessoa:
    def __init__(self, nomePes, end1Pes):
        self.nome=nomePes
        self.end1=end1Pes

pes1=Pessoa("Ana", Endereco("Rua A","Cidade X"))
print(pes1.nome, "-" , pes1.end1.rua, pes1.end1.cidade)
