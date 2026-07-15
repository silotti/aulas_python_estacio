class Pessoa:
    def __init__(self, nomePes):
        self.nome = nomePes

#instanciando e imprimindo
pes1 = Pessoa("Ana") #cria obj pes1: #nomePes: Ana
pes2 = Pessoa("João") #cria obj pes2: #nomePes: Joao
print(pes1.nome, "-")
print(pes2.nome, "-")