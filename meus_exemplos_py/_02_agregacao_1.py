class Endereco:
    def __init__(self, ruaEnd, cidadeEnd):
        self.rua=ruaEnd 
        self.cidade=cidadeEnd

class Pessoa:
    def __init__(self, nomePes):
        self.nome=nomePes

        
pes1=Pessoa("Ana")
pes1.end1=Endereco("Rua A","Cidade X")
print(pes1.nome, "-" , pes1.end1.rua, pes1.end1.cidade)