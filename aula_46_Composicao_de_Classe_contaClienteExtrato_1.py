#Classe ContaClienteExtrato usado em:38_Ageregacao_de_Classes.py
#A composição é uma forma mais forte de associação
#onde 1 obj é parte do outro e não pode existir de forma independente

import datetime
from classe_extrato import Extrato

class Conta:
   def __init__(self, clientes, numero, saldo):
      self.clientes = clientes
      self.numero = numero
      self.saldo = saldo
      self.dataabertura = datetime.datetime.today()
      self.extrato = Extrato() #inicializando a composição

   def depositar(self, valor):
      self.saldo += valor
      self.extrato.transacoes.append(["DEPOSITO", valor, "Data", datetime.datetime.today()])

   def sacar(self, valor):
      if self.saldo < valor:
         return False
      else:
         self.saldo -= valor
         self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
         return True

   def transfereValor(self, contaDestino, valor):
      if self.saldo < valor:
         return ("Não existe saldo suficiente")
      else:
         contaDestino.depositar(valor)
         self.saldo -= valor
         self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.datetime.today()])
         return("Transferencia Realizada")

   def gerarSaldo(self):
      print(f"numero: {self.numero}\nsaldo: {self.saldo}")