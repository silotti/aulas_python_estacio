#usado em: 40_ex_encapsulamento_privado_2.py

class ContaPrivada:
    def __init__(self, numero, saldo):
        self.__numero=numero  #atributo privado
        self.__saldo=saldo    #atributo privado
        
    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor])
            return True
