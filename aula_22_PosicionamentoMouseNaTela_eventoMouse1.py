
#importa o tkinter para gerar a janela grafica
import tkinter as tk

#função atualizar_coordenadas com event
def atualizar_coordenadas(event):
    #captura o evento(local do mouse)
    x = event.x
    y = event.y
    #texto com a coordenada do mouse
    label_coordenadas["text"] = f"Coordenadas do mouse: X={x}, Y={y}"

# Criando a janela
janela = tk.Tk()
#titulo da janela
janela.title("Tratamento de Eventos - Coordenadas do Mouse")

# Criando o widget de rótulo (texto inicial na janela)
label_coordenadas = tk.Label(janela, text="Mova o mouse sobre a janela para ver as coordenadas")
label_coordenadas.pack(padx=200, pady=100)

# Ligando o evento de movimento do mouse à função (bind pra pegar o movimento)
janela.bind("<Motion>", atualizar_coordenadas)

# Rodando o loop principal
janela.mainloop()