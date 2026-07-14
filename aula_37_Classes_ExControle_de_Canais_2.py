# Controle de Canais de TV
class Televisao:
    def __init__(self, pcanal, min, max):
        self.canal=pcanal
        self.cmin=min
        self.cmax=max
    
    def diminuir_canal(self):
        #se o canal - 1 for maior ou igual ao mínimo
        if self.canal - 1 >= self.cmin:
            #subtrai 1 do canal
            self.canal-=1
        #se não
        else:
            #setar no maior canal
            self.canal=self.cmax
    
    def aumentar_canal(self):
        if self.canal+1<=self.cmax:
            self.canal+=1
        else:
            #seto no menor canal
            self.canal=self.cmin

#recebe o canal 2, o menor canal é o 2 e o maior é o 10        
tv1=Televisao(pcanal=9 , min=2,  max=10 )
print(tv1.canal)
tv1.aumentar_canal()
print(tv1.canal)
tv1.aumentar_canal()
print(tv1.canal)
tv1.aumentar_canal()
print(tv1.canal)

#pode ser apenas: tv2=Televisao(3, 2, 10)
tv2 = Televisao(pcanal=3, min=2, max=10)
print("\n")
print(tv2.canal)
tv2.diminuir_canal()
print(tv2.canal)
tv2.diminuir_canal()
print(tv2.canal)
tv2.diminuir_canal()
print(tv2.canal)