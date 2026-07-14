#programação procedural (estruturada)
def fatorial(n):
    if n==0:
        return 1
    else:
        return n*fatorial(n-1)
print("Fatorial de 5 (procedural):", fatorial(5))

#programação orientada a objetos
class Fatorial:
    #'self' é a referencia a si mesmo
    def calcular(self, n):
        if n==0:
            return 1
        else:
            return n*self.calcular(n-1)

#estancia o objeto
f=Fatorial()
print("Fatorial de 5 (orientado a objetos):", f.calcular(5))