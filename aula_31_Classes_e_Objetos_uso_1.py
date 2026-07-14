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
        self.saldo-=valor #saldo = saldo - valor

    def gerar_extrato(self):
        print(f" numero: {self.numero}\n cpf: {self.cpf}\n saldo: {self.saldo}\n")

def main():
    c1=Conta(numero=1, cpf=1, nomeTitular="Joao", saldo=0) #objeto sendo instanciado
    c1.deposito(300)   #chama o método deposito para c1
    c1.gerar_extrato() #chama o método gerar_extrato para c1
    c1.sacar(100)      #chama o método sacar para c1
    c1.gerar_extrato() #chama o método gerar_extrato para c1
    
    #print(f"Nome do Titular: {c1.nomeTitular}")
    #print(f"Numero da conta: {c1.numero}")
    #print(f"CPF do Titular da conta: {c1.cpf}")
    #print(f"Saldo da conta: {c1.saldo}")
    
if __name__=="__main__":
    main()
    

