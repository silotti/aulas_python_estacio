class Endereco:
    def __init__(self, ruaEnd, cidadeEnd):
        self.rua = ruaEnd
        self.cidade = cidadeEnd
        
class Pessoa:
    def __init__(self, nomePes, localPes):
        self.nome = nomePes
        self.local = localPes #Espaço p/ classe:Endereço, dados vem na instancia

loc1 = Endereco("Rua A", "Cidade A") #cria variável loc1 com obj
loc2 = Endereco("Rua B", "Cidade B") #cria variável loc2 com obj
pes1 = Pessoa("Ana", [loc1, loc2]) #nomePes, localPes
for c in pes1.local[:1]: #mostra só 1º item, tirando [:1],mostra tudo
    print(pes1.nome, "-", c.rua, c.cidade)

#ou
print("\n")  
x=pes1.local[0]
print(pes1.nome, "-", x.rua, x.cidade) #mostra o 1º
print(pes1.nome, "-", pes1.local[1].rua, pes1.local[1].cidade) #mostra o 2º