#transferencia entre contas
# criamos um método para transferencia de valores entre contas
class Conta:
    #metodo construtor
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero=numero
        self.cpf=cpf
        self.nomeTitular=nomeTitular
        self.saldo=saldo
        
    #metodo para deposito, aumenta o saldo
    def deposito(self, valor):
        self.saldo+=valor #saldo = saldo + valor
        
    #metodo para saque, reduz o saldo
    def sacar(self, valor):
        if self.saldo<valor:
            return False
        else:
            self.saldo-=valor #saldo = saldo - valor
            return True #retorno da função (True=verdadeiro)
        
    #metodo para extrato
    def gerar_extrato(self):
        print(f" numero: {self.numero}\n cpf: {self.cpf}\n saldo: {self.saldo}\n")
        
    #metodo para tranferir valor de saldo entre objetos (contas)
    def transferencia(self, contaDestino, valor):
        #se obj solicitante (conta), não tem saldo
        if self.saldo<valor:
            return("Sem saldo suficiente.")
        #caso contrário, obj solicitante (conta), tem saldo suficiente
        else:
            #contaDestino, é o nome do obj que irá receber os dados,
            #conta que receberá o valor transferido.
            #deposito, método do obj destino(contaDestino)
            contaDestino.deposito(valor)
            #reduz da conta solicitante
            self.saldo-=valor
            return("Transferencia Realizada")
        
#o programa começa aqui
def main():
    #cria os objetos(contas)
    conta1=Conta(numero=1, cpf=123, nomeTitular="Joao", saldo=1000) #objeto sendo instanciado
    conta2=Conta(numero=3, cpf=456, nomeTitular="Maria", saldo=500) #objeto sendo instanciado

    #mostra o saldo atual
    print("Saldo antes da transferência:")
    print(f"Saldo da conta 1: R${conta1.saldo}")
    print(f"Saldo da conta 2: R${conta2.saldo}")
    
    #conta1 solicita a transferencia pra conta2 do valor=300
    conta1.transferencia(conta2, valor=300)
    
    print("\nSaldo depois da transferência:")
    print(f"Saldo da conta 1: R${conta1.saldo}")
    print(f"Saldo da conta 2: R${conta2.saldo}")
        
    #verifica o endereço de memória
    #if (conta1!=conta2):
        #print("Endereço de memórias diferentes")

    #imprime os endereços de memória
    #print(conta1)
    #print(conta2)
    
    #print(conta1.saldo)
    #print(conta2.saldo)
    #conta1.depositar(300)
    #print(conta1.saldo)
    #print(conta2.saldo)
    
    #conta1 recebe o mesmo endereço de memória da conta2
    #conta1=conta2
    
    #if (conta1==conta2):
        #print("Endereços iguais de Memória")
    
    #imprime os endereços de memória
    #print(conta1)
    #print(conta2)
    
    #conta1.depositar(1000)
    #print(conta1.saldo)
    #print(conta2.saldo)
    
    #print(conta1.nomeTitular)
    #print(conta2.nomeTitular)
    
    #valor_saque=200
    #resultado_saque=conta1.sacar(valor_saque) #vai vir true ou false que é o resultado do método
    #c1.depositar(300)  #chama o método depositar para c1
    #c1.gerar_extrato() #chama o método gerar_extrato para c1
    #c1.sacar(100)      #chama o método sacar para c1
    #c1.gerar_extrato() #chama o método gerar_extrato para c1
    
    #validando o retorno para verificar se o saque foi realizado
    #if resultado_saque: #se o resultado do saque for verdadeiro
        #print(f"Saque de R${valor_saque} realizado com sucesso")
        #print(f"Saldo atual: R${conta1.saldo}\n")
    #else: #se o resultado do saque for falso
        #print("Saldo insuficiente para realizar o saque.\n")
    
    #print(f"Nome do Titular: {c1.nomeTitular}")
    #print(f"Numero da conta: {c1.numero}")
    #print(f"CPF do Titular da conta: {c1.cpf}")
    #print(f"Saldo da conta: {conta1.saldo}")
    
if __name__=="__main__":
    main()