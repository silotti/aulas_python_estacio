#__ pra deixar privado
#decorator: @property -> ver o atributo privado
#decorator: @<metodo>.setter ->p/ mexer no atributo privado de fora da classe
#atributos de classe: total_contas
#decorator: @classmethod -> mexer no atributo de classe que está privada
#decorator: @staticmethod  ->métodos estáticos, retorna valor de um atributo de classe, sem ter um objeto
class Conta:  
    __total_contas=0 #atributo da classe privado
    
    @classmethod
    def get_total_contas(cls): #cls atributo especial da classe
        return cls.__total_contas
    
    @staticmethod #retorna valor de um atributo de classe, sem ter um objeto 
    def nome_banco():
        return "Banco Muquirana"
    
    def __init__(self, numero, saldo):
        self.__numero=numero #atributo privado
        self.__saldo=saldo #atributo privado
        type(self).__total_contas+=1 #no atributo da classe, permite acesso
    
    @property #metodo decorador pra ver a saldo, vira minha propriedade
    def saldo(self):
        return self.__saldo
             
    @saldo.setter #metodo decorador pra mexer no saldo do property
    def saldo(self, valor):
        if valor<0:
            print ("Valor inválido")
        else:
            self.__saldo=valor
        
    def sacar(self, valor):
        if self.__saldo<valor:
            return False
        else:
            self.__saldo-=valor
            return True
        
    def gerar_saldo(self):
        print(f"Conta: {self.__numero}")
        print(f"Saldo: R${self.__saldo:10.2f}")

        
        
            
        