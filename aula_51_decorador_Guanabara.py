#encapsulamento só protege a manupulação não a exibição
#decorator para acessar atributos privados
from classes.conta_decorator import Conta
c1=Conta(1, 1000)
c2=Conta(2, 50)
c3=Conta(3, 0)

c1.saldo=85 #@saldo.setter permite mudar o setter saldo
#c1.saldo=-500 ->numero negativo ele não vai deixar

print(f"Até agora temos {Conta.get_total_contas()} contas\n")

print(c1.saldo) #@property permitiu apenas mostrar, mesmo protegido
print(c2.saldo) #@property permitiu apenas mostrar, mesmo protegido

print(f"\nVolte Sempre, {Conta.nome_banco()}!\n")
