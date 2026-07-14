#Agregação e composição NÃO usam os termos pai e filha.
#Pessoa → Classe todo(Classe que contém)
#Cliente → Classe parte(Classe contida)

#Conta
# │
# ├── clientes  -> agregação
# │      ├── Cliente 1
# │      └── Cliente 2
# │
# └── extrato   -> composição
#        └── Extrato

#Conta e Cliente → agregação.
#Conta e Extrato → composição.

import datetime
class Cliente:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco

class Extrato:
    def __init__(self):
        #lista das transações da conta, que começa vazia
        self.transacoes=[] 
    
    def extrato(self, numeroConta):
        print(f"Extrato: {numeroConta} \n")
        for p in self.transacoes:
            print(f"{p[0]:15s} {p[1]:10.2f} {p[2]:10s} {p[3].strftime('%d/%b/%y')}")

class Conta:
   def __init__(self, clientes, numero, saldo):
      self.clientes = clientes
      self.numero = numero
      self.saldo = saldo
      self.dataabertura = datetime.datetime.today()
      self.extrato = Extrato()

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

def main():
    cliente1 = Cliente(123, "Joao", "Rua 1")
    cliente2 = Cliente(345, "Maria","Rua 2")

    #criando uma conta com dois clientes, fazendo uma agregação com uma lista
    conta1 = Conta(clientes=[cliente1, cliente2], numero=1, saldo=2000)
    conta1.depositar(1000)
    conta1.sacar(1500)
    conta1.extrato.extrato(conta1.numero)
    
if __name__=="__main__":
    main()