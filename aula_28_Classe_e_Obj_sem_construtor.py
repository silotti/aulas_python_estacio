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

#ou outro exemplo
class Teste():
    # definiu o método de classe f que contém a impressão: foo
    def f(self):
        print("foo")

#def main():, não é obrigatório, porém, diz onde o programa começa.
#ex. de uso
#def main():
     #carregar_dados()
     #processar_dados()
     #gerar_relatorio()
        
def main():
    obj_x=Teste() #Objeto: obj_x sendo instanciado "Criando o objeto"
    obj_x.f() #chamando o método da classe f, que imprime texto na tela

#ao usar if __name__ == "__main__":, 
# você garante que o código dentro do main() só será 
# executado quando o arquivo for rodado diretamente, 
# não quando ele for importado como um módulo.
if __name__=="__main__":
    main()
    
#novamente    
    
    
class Teste():
    def f(self):
        print("abc")
        
def main():
    objeto_1=Teste()
    objeto_1.f()
    
if __name__=="__main__":
    main()