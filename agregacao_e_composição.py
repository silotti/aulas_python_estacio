class Endereco:
    def __init__(self, ruaEnd, cidadeEnd):
        self.rua = ruaEnd
        self.cidade = cidadeEnd

    def mostrar(self):
        print(f"Endereço: {self.rua}, {self.cidade}")

# herança: é o pai que manda pro PessoaA e pro PessoaC
class Pessoa:
    """Base com o comportamento comum às duas formas de relação."""
    def mostrar(self):
        print(f"Pessoa: {self.nomePessoa}")
        self.local.mostrar()

# agregação: recebe um Endereço já existente pela instancia
class PessoaA(Pessoa):
    def __init__(self, nomeA, enderecoA):
        self.nomePessoa = nomeA
        self.local = enderecoA

# composição: cria o próprio Endereço internamente
class PessoaC(Pessoa):
    def __init__(self, nomeC, ruaC, cidadeC):
        self.nomePessoa = nomeC
        self.local = Endereco(ruaC, cidadeC)

# Uso (instanciando e enviando os dados)
enderecoAgregado = Endereco("Rua A", "Cidade X")
pessoaAgregada = PessoaA("Ana", enderecoAgregado)

pessoaComposta = PessoaC("Bruno", "Rua B", "Cidade Y")

# Imprimir
#enderecoAgregado.mostrar()
pessoaAgregada.mostrar()
pessoaComposta.mostrar()