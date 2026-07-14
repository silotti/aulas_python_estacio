#métodos de classes
# definem as ações que o objeto pode realizar
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
            self.saldo-=valor
            return True

    def gerar_extrato(self):
        print(f" numero: {self.numero}\n cpf: {self.cpf}\n saldo: {self.saldo}\n")

def main():
    c1=Conta(numero=1, cpf=123, nomeTitular="Joao", saldo=1000) #objeto sendo instanciado  
    valor_saque=200
    resultado_saque=c1.sacar(valor_saque)
    
    #validando o retorno pra ver se o saque foi realizado
    if resultado_saque:
        print(f"Saque de R${valor_saque} realizado com sucesso!")
        print(f"Saldo atual: R${c1.saldo}")
    else:
        print("Saldo insuficiente para realizar o saque.")
    
if __name__=="__main__":
    main()
    

