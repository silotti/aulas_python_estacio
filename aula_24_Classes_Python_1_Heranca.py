#Pessoa → classe pai (superclasse)
#Cliente → classe filha (subclasse)

#Cliente é um Pessoa
#Cliente ganha tudo que Pessoa tiver

# *( ) parênteses na classe → HERANÇA
#-------------------------------------------------------------
class Pessoa:
    pass

#cliente é uma pessoa, por isso recebe dados da Pessoa
class Cliente(Pessoa):
    pass
