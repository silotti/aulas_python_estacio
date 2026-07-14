#comunicação entre objetos na memória (objeto na memória)
# Uma classe pode ter várias instâncias (objetos) na memória,
# cada um com seus próprios valores de atributos.
# Para comparar se duas referências de memória apontam para o mesmo objeto,
# usamos os operadores == e !=
class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero=numero
        self.cpf=cpf
        self.nomeTitular=nomeTitular
        self.saldo=saldo

    #metodo da classe Conta pra depositar valor
    def deposito(self, valor):
        self.saldo+=valor #saldo = saldo + valor

    def sacar(self, valor):
        if self.saldo<valor:
            return False
        else:
            self.saldo-=valor #saldo = saldo - valor
            return True #retorno da função (True=verdadeiro)

    def gerar_extrato(self):
        print(f" numero: {self.numero}\n cpf: {self.cpf}\n saldo: {self.saldo}\n")

def main():
    conta1=Conta(numero=1, cpf=123, nomeTitular="Joao", saldo=0) #objeto sendo instanciado
    conta2=Conta(numero=3, cpf=456, nomeTitular="Maria", saldo=0) #objeto sendo instanciado

    #verifica o endereço de memória
    if (conta1!=conta2):
        print("Endereço de memórias diferentes:")

    #imprime os endereços de memória
    print(conta1)
    print(conta2)
    
    print(conta1.saldo)
    print(conta2.saldo)
    conta1.deposito(300)
    print(conta1.saldo)
    print(conta2.saldo)
    
    #conta1 recebe o mesmo endereço de memória da conta2
    conta1=conta2
    
    if (conta1==conta2):
        ...
        print("\nEndereços iguais de Memória:")
    
    #imprime os endereços de memória
    print(conta1)
    print(conta2)
    
    print(conta1.saldo)
    print(conta2.saldo)
    conta1.deposito(1000)
    print(conta1.saldo)
    print(conta2.saldo)
    print(conta1.nomeTitular)
    print(conta2.nomeTitular)
    
if __name__=="__main__":
    main()
    

