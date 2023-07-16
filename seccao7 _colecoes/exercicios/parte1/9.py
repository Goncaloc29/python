""" 
Crie um programa que lê 6 valores inteiros pares náo repetidos e, em seguida, mostre na tela os valores
lidos na ordem inversa. 
"""

valores_pares = []                                                                  # lista vazia

while len(valores_pares) < 6:                                                       # enquanto o tamanho da lista for menor que 6
    valor = int(input("Introduza um valor par: "))                                  # pede um numero
    if valor == 0:                                                                  # se o valor for 0
        print("Valor não é par, introduzir novamente")                              # imprime mensagem de erro
        print()                                                                     # imprime uma linha em branco
    elif valor % 2 == 1:
        print("Valor não é par, introduzir novamente")                              # imprime mensagem de erro
        print()                                                                     # imprime uma linha em branco
    else:
        if valor not in valores_pares:                                              # se o valor não estiver na lista
            valores_pares.append(valor)                                             # adiciona o numero à lista  
        else: 
            print("Valor é par mas já existe na lista, introduzir novamente")       # imprime mensagem de erro
            print()
        

valores_pares.reverse()                                                             # inverte a lista
print(valores_pares)                                                                # imprime a lista