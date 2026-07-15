class Endereco:
    def __init__(self, rua, cidade):
        self.rua = rua
        self.cidade = cidade
    def mostrar(self):
        print(f"Endereço: {self.rua}, {self.cidade}")

class Pessoa:
    def __init__(self, nome, rua, cidade):
        self.nome = nome
        self.endereco = Endereco(rua, cidade)
    def mostrar(self):
        print(f"Pessoa: {self.nome}")
        self.endereco.mostrar()

# Uso
pessoa2 = Pessoa("Bruno", "Rua B", "Cidade Y")

# Imprimir
pessoa2.mostrar()