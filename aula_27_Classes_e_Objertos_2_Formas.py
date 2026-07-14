class Conta1:
    numero = 0
    cpf = 0
    nomeTitular = ""
    saldo = 0.0

c2 = Conta1()
c2.numero = 2
c2.cpf = 222
c2.nomeTitular = "Maria"
c2.saldo = 2000

print(f"Nome do Titular: {c2.nomeTitular}")
print(f"Numero da conta: {c2.numero}")
print(f"CPF do Titular da conta: {c2.cpf}")
print(f"Saldo da conta: {c2.saldo}")

#ou com metodo construtor __init__

class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero=numero
        self.cpf=cpf
        self.nomeTitular=nomeTitular
        self.saldo=saldo

c1=Conta(numero=1, cpf=111, nomeTitular="Joao", saldo=1000)
print(f"Nome do Titular: {c1.nomeTitular}")
print(f"Numero da conta: {c1.numero}")
print(f"CPF do Titular da conta: {c1.cpf}")
print(f"Saldo da conta: {c1.saldo}")

#RESUMINDO, facilita a criar novos objetos "instanciar novos objetos":
#Sem construtor:
#c2 = Conta()
#c2.numero = 2
#c2.cpf = 222
#c2.nomeTitular = "Maria"
#c2.saldo = 2000

#Com construtor __init__ dá pra agrupar:
#c1 = Conta(1, 111, "Joao", 1000)