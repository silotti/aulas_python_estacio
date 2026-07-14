#importa o tkinter para gerar a janela grafica
import tkinter as tk

#função pega a coordenada com event
def capturar_clic(event):
    #captura o evento(local do mouse)
    x = event.x
    y = event.y
    #texto com a coordenada do mouse
    label_coordenadas["text"] = f"Último clique: X={x}, Y={y}"

# Criando a janela
janela = tk.Tk()
#captura quando usado o botão esquerdo do mouse
janela.title("Tratamento de Eventos - Captura de Clique Esquerdo")

# Criando o widget de rótulo
label_coordenadas = tk.Label(janela, text="Clique em qualquer lugar da janela")
#aonde vai colocar as coordenadas
label_coordenadas.pack(padx=200, pady=100)

# Ligando o evento de clique do mouse à função
#Button-1 (botão esquerdo do mouse), Button-3(botão direito do mouse), Button-2(botão central do mouse)
#capturar_clic(chama a função de capturar a posição do mouse)
janela.bind("<Button-1>", capturar_clic)

# Rodando o loop principal
#põe a janela pra rodar
janela.mainloop()