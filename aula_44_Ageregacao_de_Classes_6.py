class Endereco:
    def __init__(self, rua, cidade):
        self.rua = rua
        self.cidade = cidade
    def mostrar(self):
        print(f"Endereço: {self.rua}, {self.cidade}")

class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
    def mostrar(self):
        print(f"Pessoa: {self.nome}")
        self.endereco.mostrar()

# Uso
endereco1 = Endereco("Rua A", "Cidade X")
pessoa1 = Pessoa("Ana", endereco1)

# Imprimir
pessoa1.mostrar()
