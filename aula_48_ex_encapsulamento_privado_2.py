#encapsulamento metodos e atributos: publicos, privados e decorados
# é um tipo de burla, de atributos privados.
# pq o python não possui atributos privados reais,
# acesso pode ser obtido assim:

from classes.aula_conta_privada import ContaPrivada

conta=ContaPrivada(numero=1, saldo=1000)
saldo1=conta._ContaPrivada__saldo
print(saldo1)

#está privado não acessa assim:
#saldo2=conta.saldo
#print(saldo2)