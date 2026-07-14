class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero=numero
        self.cpf=cpf
        self.nomeTitular=nomeTitular
        self.saldo=saldo

def main():
    c1=Conta(numero=1, cpf=1, nomeTitular="Joao", saldo=1000) #objeto sendo instanciado
    
    print(f"Nome do Titular: {c1.nomeTitular}")
    print(f"Numero da conta: {c1.numero}")
    print(f"CPF do Titular da conta: {c1.cpf}")
    print(f"Saldo da conta: {c1.saldo}")
    
if __name__=="__main__":
    main()
    

