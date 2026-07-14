#métodos com retorno
# serve para validar o estado de um objeto
class Conta():
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero=numero
        self.cpf=cpf
        self.nomeTitular=nomeTitular
        self.saldo=saldo

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
    c1=Conta(numero=1, cpf=123, nomeTitular="Joao", saldo=100) #objeto sendo instanciado
    valor_saque=200
    resultado_saque=c1.sacar(valor_saque) #vai vir true ou false que é o resultado do método
   
    #validando o retorno para verificar se o saque foi realizado
    if resultado_saque: #se o resultado do saque for verdadeiro
        print(f"Saque de R${valor_saque} realizado com sucesso")
        print(f"Saldo atual: R${c1.saldo}\n")
    else: #se o resultado do saque for falso
        print("Saldo insuficiente para realizar o saque.\n")
    
if __name__=="__main__":
    main()
    

