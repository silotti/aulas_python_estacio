class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        for f in self.funcionarios:
            print(f"{f.nome}, {f.cargo}")

# Exemplo de uso
f1 = Funcionario("Ana", "Analista")
f2 = Funcionario("Carlos", "Desenvolvedor")

dep = Departamento("TI")
dep.adicionar_funcionario(f1)
dep.adicionar_funcionario(f2)

dep.listar_funcionarios()
