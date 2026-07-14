### Exemplo de Código Python
# Atribuição de valores e variáveis
nome="Alice"
idade=30
#Entrada de dados do usuário
altura=float(input("Digite a sua altura em metros: "))
peso=float(input("Digite o seu peso em Kg: "))
#Calculo do IMC (Indice de Massa Corporal)
imc=peso/(altura**2)
#Saída de dados formatada
print(f"Nome:{nome}")
print(f"Idade:{idade}")
print(f"Altura:{altura:.2f}m")
print(f"Peso:{peso:.1f}kg")
print(f"IMC:{imc:.2f}")

###Exemplo de Saída:
#Digite a sua altura em metros: 1.80
#Digite o seu peso em Kg: 94.5
#Nome:Alice
#Idade:30
#Altura:1.80m
#Peso:94.5kg
#IMC:29.17