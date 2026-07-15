class Conta:
    def __init__(self, numero, saldo):
        #__ faz atributo ficar privado, (init é construtor)
        self.__numero=numero #__ deixa privado
        self.__saldo=saldo #__ deixa privado
        
    def sacar(self, valor):
        if self.__saldo<valor:
            return False
        else:
            self.__saldo-=valor
            return True
    def gerar_saldo(self):
        print(f"Conta: {self.__numero}")
        print(f"Saldo: R${self.__saldo:10.2f}")

        
        
            
        