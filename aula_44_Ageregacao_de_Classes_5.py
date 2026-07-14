class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

class Departamento:
    def __init__(self, nome, funcionarios):
        self.nome = nome
        self.funcionarios = funcionarios  # Referência a uma lista externa

    def listar_funcionarios(self):
        for f in self.funcionarios:
            print(f"{f.nome}, {f.cargo}")

# Lista de funcionários independente
funcionarios = [
    Funcionario("Ana", "Analista"),
    Funcionario("Carlos", "Desenvolvedor")
]

# Criando o departamento referenciando a lista
dep = Departamento("TI", funcionarios)

print("Antes de remover o departamento:")
dep.listar_funcionarios()

# Removendo a referência ao departamento
dep = None

print("\nDepois de remover o departamento:")
print("Os funcionários ainda existem:")
for f in funcionarios:
    print(f"Nome: {f.nome}, Cargo: {f.cargo}")