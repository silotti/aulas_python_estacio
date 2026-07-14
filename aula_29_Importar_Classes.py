#criando uma classe chamada Conta primeira letra maiuscula
#boa pratica é,
#criar um arquivo .py para cada classe com o nome da classe,
#arquivo com a classe, com a primeira letra minúscula,
#facilita pra importar pra outros projetos

#arquivo:conta.py
class Conta:
    def __init__(self, p_numero, p_nome):
        self.numero = p_numero
        self.nome = p_nome
        
### Se estiver em arquivos separados usar:(from conta import Conta)
### do arquivo: conta.py , usa a classe: Conta

#arquivo:principal.py
#from conta import Conta

def main():
    v_conta = Conta(1, "João")
    print(v_conta.nome)

if __name__ == "__main__":
    main()