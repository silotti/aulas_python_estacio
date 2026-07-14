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
tv1=Televisao(pcanal=2 , min=2,  max=10 )
print(f"TV1 Está no canal: ",tv1.canal,"\n")
print(f"Mudando canal para cima...")
#muda 20 vezes o canal para cima e a cada loop imprime o canal que está
for x in  range (1,20):
    tv1.aumentar_canal()
    print(f"Canal Sintonizado TV1: ",tv1.canal)

#pode ser apenas: tv2=Televisao(10, 2, 10)
tv2 = Televisao(pcanal=10, min=2, max=10)
print(f"\nTV2 Está no canal ",tv2.canal,"\n")
print(f"Mudando canal para baixo...")
for x in  range (1,20):
    tv2.diminuir_canal()
    print(f"Canal Sintonizado TV2: ",tv2.canal)        
        
    
    
    

