class Endereco:
    def __init__(self, ruaEnd, cidadeEnd):
        self.rua = ruaEnd
        self.cidade = cidadeEnd

class Pessoa:
    def __init__(self, nomePes, localPes):
        self.nome = nomePes
        self.local = localPes #Espaço p/ classe:Endereço, dados vem na instancia

pes1 = Pessoa("Ana", Endereco("Rua A", "Cidade A")) #nomePes, ruaEnd, cidadeEnd
print(pes1.nome, "-", pes1.local.rua, pes1.local.cidade)