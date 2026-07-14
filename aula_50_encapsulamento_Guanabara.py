#encapsulamento só protege a manupulação não a exibição
from classes.conta_guanabara import Conta
c1=Conta(1, 1000)
c2=Conta(2, 500)
c1.sacar(200)
#sem encapsulamento
#c2.saldo=-8000

#como burlar o encapsulamento: c1._Conta__saldo=-800
#print(f"Conta 1 com R$ {c1.saldo}")
#print(f"Conta 2 com R$ {c2.saldo}")

c1.gerar_saldo()
c2.gerar_saldo()