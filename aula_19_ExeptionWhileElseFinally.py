### Exemplo de Código Python
# Except com While
#laço while o break finaliza se der certo
while True:
    try:
        numero=int(input("Digite o número: "))
        mult=numero*3
        print(mult)
        divisao=12/mult
        print(divisao)
        
    #except se valor invalido
    except ValueError:
        print("Entre com um número válido")
    
    #except se divisão por zero
    except ZeroDivisionError:
        print("O número não pode ser zero tente novamente")
        
    #else so entra se nenhuma exceção usada e coloca o break aqui
    else:
        print("Entrou no else")
        break
    #finally alguo que sempre será executado
    finally:
        print("Entrou no finally")        