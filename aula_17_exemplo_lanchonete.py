### Exemplo de Código Python
# Lanchonete
#Atribuição de variáveis
hamburguer = 10.50
batata_frita = 4.00
refrigerante = 3.00
#Entrada de dados do usuário
quantidade_hamburguer = int(input("Digite a quantidade de hambúrgueres desejados: "))
quantidade_batata = int(input("Digite a quantidade de batatas fritas desejadas: "))
quantidade_refrigerante = int(input("Digite a quantidade de refrigerantes desejados: "))
#Cálculo do preço total
preco_total = (hamburguer * quantidade_hamburguer) + (batata_frita * quantidade_batata) + (refrigerante * quantidade_refrigerante)

#Saída de dados
print("O preço total do seu pedido é: R$", preco_total)
#Exemplo de Saída de Dados:
#Digite a quantidade de hambúrgueres desejados: 2
#Digite a quantidade de batatas fritas desejadas: 3
#Digite a quantidade de refrigerantes desejados: 5
#O preço total do seu pedido é: R$ 48.0