#método decorado @
# deve ser utilizado apenas internamente
# Utilizando o decorator @property, podemos proteger os atributos
# e acessá-los somente por meio de métodos "decorados" 

@property #definindo o método decorado
def saldo(self):
    return self._saldo

# o decorado @setter força todas as alterações de valor dos
# atributos privados a passar por esses métodos.
@saldo.setter #definindo método setter
def saldo(self, saldo):
    if saldo<0:
        print("saldo inválido")
    else:
        self._saldo=saldo