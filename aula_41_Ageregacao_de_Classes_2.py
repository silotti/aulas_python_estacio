#from conta import Conta #usando outro arquivos
from classes.cliente import Cliente
from aula_46_Composicao_de_Classe_contaClienteExtrato_1 import Conta

def main():
    cliente1 = Cliente(123, "Joao", "Rua 1")
    cliente2 = Cliente(345, "Maria","Rua 2")

    #criando uma conta com dois clientes, fazendo uma agregação com uma lista
    conta1 = Conta(clientes=[cliente1, cliente2], numero=1, saldo=2000)
    conta1.depositar(1000)
    conta1.sacar(1500)
    conta1.extrato.extrato(conta1.numero)
    
if __name__=="__main__":
    main()