# Agregação e composição NÃO usam os termos pai e filha.
# Pessoa → Classe todo (Classe que contém)
# Cliente → Classe parte (Classe contida)

#Pessoa (todo) -> composição
#├── Cliente c1
#└── Cliente c2

# *classe sendo criada dentro do __init__ → COMPOSIÇÃO
# você vê a classe sendo instanciada ali dentro: Cliente(...)
#-------------------------------------------------------------
class Cliente:
    def __init__(self, nome):
        self.nome=nome

class Pessoa:
    def __init__(self):
        # composição: Pessoa cria Clientes
        self.vivente=[Cliente("João"), Cliente("Maria")]
        
#USO:
pessoa=Pessoa()

print(pessoa.vivente[0].nome)
print(pessoa.vivente[1].nome)