#Criar Classe e Instanciar Objeto para a Classe
#*** Criação da classe Conta.
class Conta:
    #metodo construtor da classe
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero=numero
        self.cpf=cpf
        self.nomeTitular=nomeTitular
        self.saldo=saldo

#observe os parametros passados na criação do objeto
#*** Intanciamos o objeto chamado c1.
def main():
    #intacia objeto c1, que é "do tipo", "da classe", (Conta).
#*** Passamos como parametro pro metodo construtor da classe os dados,
#*** numero da conta é 1, cpf é 1, nome é Joao e saldo é 1000.
    c1=Conta(numero=1, cpf=1, nomeTitular="Joao", saldo=1000) #objeto sendo instanciado
    #Acessamos o objeto c1 e lemos os atributos,
    # e exibimos os atributos: nomeTitular, numero, cpf, saldo
    
    print(f"Nome do Titular: {c1.nomeTitular}")
    print(f"Numero da conta: {c1.numero}")
    print(f"CPF do Titular da conta: {c1.cpf}")
    print(f"Saldo da conta: {c1.saldo}")
    
#Quando um script python é executado, a variável reservada
#NAME referente a ele tem valor igual a "__main__".
#Neste caso, a condição do IF a seguir será TRUE.
#Então o que está no corpo do IF será executado. No caso,
#é um chamado ao método main do script

if __name__=="__main__":
    main()
    
#(SAIDA DE DADOS)
# Nome do Titular: Joao
# Numero da conta: 1
# CPF do Titular da conta: 1
# Saldo da conta: 1000
