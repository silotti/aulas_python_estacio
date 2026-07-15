import datetime

#Extrato que acumula transações e formata exibição
class Extrato:
    def __init__(self):
        #lista das transações da conta, que começa vazia
        self.transacoes=[] 
    
    def imprimir(self, numeroConta, saldo):
        print(f"Extrato da Conta: {numeroConta} \n")
        for col in self.transacoes:
            print(f"{col[0]:15s} {col[1]:10.2f} {col[2]:>14s}{col[3].strftime('%d/%b/%y')}")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
         
#Conta do cliente com extrato
class Conta:
   def __init__(self, cl_clientes, numero, saldo):
      self.cl_clientes = cl_clientes
      self.numero = numero
      self.saldo = saldo
      self.dataabertura = datetime.datetime.today()
      self.extrato = Extrato() #inicializando a composição

   def depositar(self, valor, tipo="DEPOSITO"):
      self.saldo += valor
      self.extrato.transacoes.append([tipo, valor, "Data: ", datetime.datetime.today()])

   def sacar(self, valor):
      if self.saldo < valor:
         return False
      else:
         self.saldo -= valor
         #append adiciona um dado na lista
         self.extrato.transacoes.append(["SAQUE", valor, "Data: ", datetime.datetime.today()])
         return True

   def transfereValor(self, contaDestino, valor):
      if self.saldo < valor:
         return ("Não existe saldo suficiente")
      else:
         contaDestino.depositar(valor, tipo="TRANSFERENCIA_C") #credito
         self.saldo -= valor
         self.extrato.transacoes.append(["TRANSFERENCIA_D", valor, "Data", datetime.datetime.today()])
         return("Transferencia Realizada")

   def gerarSaldo(self):
      import types
      data_vazia = types.SimpleNamespace(strftime=lambda formato: "")
      self.extrato.transacoes.append(["SALDO", self.saldo, "", data_vazia])

#Cliente
class Cliente:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco

#aqui acaba as classes --------------------------------------

cliente1 = Cliente(123, "Joao", "Rua 1")
cliente2 = Cliente(345, "Maria","Rua 2")
cliente3 = Cliente(567, "Ana", "Rua 3")

#criando uma conta com dois clientes, fazendo uma agregação com uma lista
conta2 = Conta(cl_clientes=[cliente3], numero=777, saldo=1500)
conta1 = Conta(cl_clientes=[cliente1, cliente2], numero="7020-1", saldo=2000)
conta1.gerarSaldo()
conta2.transfereValor(conta1, 250) #da conta2 para conta1
conta1.gerarSaldo()
conta1.transfereValor(conta2, 250) #da conta1 para conta2
conta1.gerarSaldo()
conta1.depositar(1000)
conta1.gerarSaldo()
conta1.sacar(1500)
conta1.sacar(250)
conta1.gerarSaldo()
conta1.extrato.imprimir(conta1.numero, conta1.saldo)