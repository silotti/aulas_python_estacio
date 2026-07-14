class Endereco:
    def __init__(self, ruaEnd, cidadeEnd):
        self.rua = ruaEnd
        self.cidade = cidadeEnd

class Pessoa:
    def __init__(self, nomePes, ruaPes, cidadePes):
        self.nome = nomePes
        self.local = Endereco(ruaPes, cidadePes)  #Pessoa cria o próprio Endereco

pes1 = Pessoa("Ana", "Rua A", "Cidade A") #nomePes, ruaEnd, cidadeEnd
print(pes1.nome, "-", pes1.local.rua, pes1.local.cidade)