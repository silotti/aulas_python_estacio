#criando uma classe chamada Conta
#lembrar de criar um arquivo para cada classe com o nome da classe

#construtores e metodo init e self
#self é a forma da classe se referir a ela mesma
#--init-- é o método construtor que cria o objeto da classe 
class Conta:
    #self a gente não usa quando faz objeto,
    #no metodo construtor o self serve pra ele aponta pra sí próprio
    #metodo construtor: def _ _init_ _ ([parametro1],[parametro2], ...):
    def __init__(self, numero, cpf, nomeTitular, saldo):
        #o proprio objeto(self) com o atributo(.numero), recebe o parametro(numero),
        #o atributo .numero, vai receber o numero, que veio como parametro
        #portanto: numero vira o próprio atributo, facilitando o uso,
        #em vez de objeto.numero=1 usa-se apenas numero=1
        self.numero=numero
        self.cpf=cpf
        self.nomeTitular=nomeTitular
        self.saldo=saldo
#assim já cria um objeto novo c1 com os dados:
c1=Conta(numero=1, cpf=1, nomeTitular="Joao", saldo=1000)

#ver os dados do objeto c1:
print(f"Nome do Titular: {c1.nomeTitular}")
print(f"Numero da conta: {c1.numero}")
print(f"CPF do Titular da conta: {c1.cpf}")
print(f"Saldo da conta: {c1.saldo}")