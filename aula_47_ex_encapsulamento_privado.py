#encapsulamento metodos e atributos: publicos, privados e decorados
# como evitar a alteração indevida?
# com o uso de _ _ indica que um atributo é privado, ou seja,
# somente pode ser alterado por um método da classe.

class Conta:
    def __init__(self, numero, saldo):
        self.numero=numero  #atributo privado
        self.saldo=saldo    #atributo privado

def main():
    conta=Conta(numero=1, saldo=1000)
    saldo=conta.saldo
    print(saldo)
    
if __name__=="__main__":
    main()
