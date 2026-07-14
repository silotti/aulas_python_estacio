# Agregação e composição NÃO usam os termos pai e filha.
# Pessoa → Classe todo (Classe que contém)
# Cliente → Classe parte (Classe contida)

#Pessoa (todo) -> agregação
#├── Cliente c1
#└── Cliente c2

# *parâmetro entrando no __init__ → AGREGAÇÃO
# aparece variável clientes, vindo de fora:
#def __init__(self, clientes):
#    self.clientes = clientes
#-------------------------------------------------------------
class Cliente:
    def __init__(self, nome):
        self.nome=nome

class Pessoa:
    def __init__(self, vivente):
        # agregação: Pessoa apenas referencia Clientes externos
        self.vivente=vivente

#USO:        
# os Clientes existem ANTES da Pessoa
c1=Cliente("João")
c2=Cliente("Maria")

# Pessoa apenas "usa" esses objetos
pessoa=Pessoa([c1, c2])

print(c1.nome)
print(c2.nome)