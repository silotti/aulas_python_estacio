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

# Criando os funcionários
f1 = Funcionario("Ana", "Analista")
f2 = Funcionario("Carlos", "Desenvolvedor")

# Criando o departamento e adicionando os funcionários
dep = Departamento("TI")
dep.adicionar_funcionario(f1)
dep.adicionar_funcionario(f2)

print("Antes de remover o departamento:")
dep.listar_funcionarios()

# Removendo a referência ao departamento
dep = None

print("\nDepois de remover o departamento:")
print("Os funcionários ainda existem:")
print(f"Nome: {f1.nome}, Cargo: {f1.cargo}")
print(f"Nome: {f2.nome}, Cargo: {f2.cargo}")