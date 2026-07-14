###Compara o primeiro numero com o segundo numero
#importa o tkinter para gerar a janela grafica
import tkinter as tk
from tkinter import messagebox

def comp_numeros():
    try:
        num1=float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num1 > num2 :
            messagebox.showinfo("Resultado", f"O numero {num1} é maior que {num2}")
        elif num1 == num2 :
            messagebox.showinfo("Resultado", f"O numero {num1} é  igual a {num2}")
        else:
            messagebox.showinfo("Resultado", f"O numero {num1} é menor que {num2}")
    except ValueError:
            messagebox.showerror("Erro", "Por favor, insira números válidos.")
 
#função para aceitar apenas numeros
def apenas_numeros(texto_futuro):
    """
    Função de validação que permite apenas números, ponto, vírgula ou sinal de menos.
    texto_futuro representa como o texto vai ficar se a digitação for aceita.
    """
    # Permite campo vazio (caso o usuário apague tudo)
    if texto_futuro == "":
        return True
    
    # Substitui vírgula por ponto para aceitar ambos os formatos decimais
    texto_futuro = texto_futuro.replace(',', '.')
    
    try:
        # Se o texto for apenas um sinal de menos '-', permite (para números negativos)
        if texto_futuro == "-":
            return True
        float(texto_futuro)
        return True
    except ValueError:
        return False
 
# Criando a janela
janela=tk.Tk()
janela.title("Comparando Numeros")

# Registrando a função de validação no Tkinter
valida_cmd = janela.register(apenas_numeros)
 
# Criando os widgets
label_num1=tk.Label(janela, text="Número 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")
# Adicionado: validate="key" e validatecommand que passa o texto futuro (%P)
# não permite a digitação de letras
entry_num1 = tk.Entry(janela, validate="key", validatecommand=(valida_cmd, '%P'))
entry_num1.grid(row=0, column=1, padx=10, pady=5)
 
label_num2=tk.Label(janela, text="Número 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")
# Adicionado: validate="key" e validatecommand que passa o texto futuro (%P)
entry_num2 = tk.Entry(janela, validate="key", validatecommand=(valida_cmd, '%P'))
entry_num2.grid(row=1, column=1, padx=10, pady=5)
 
botao_comp=tk.Button(janela, text="Comparar", command=comp_numeros)
botao_comp.grid(row=2, columnspan=2, padx=10, pady=5)
 
# Rodando o loop principal
janela.mainloop()