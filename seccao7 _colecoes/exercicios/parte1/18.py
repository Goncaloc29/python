""" Faça um programa que leia um vetor de 10 números. Leia um número x. Conte os
múltiplos de um número inteiro x no vetor e mostre-os na tela. """

numeros = []

while len(numeros) < 5: # enquanto o tamanho da lista for menor que 5
    valor = int(input(f"Introduza o valor para a posição:: ")) # pede um numero
    if valor not in numeros: # se o valor não estiver na lista
        numeros.append(valor) # adiciona o numero à lista
    else:
        print("Valor já existe na lista, adicionar outro") # imprime mensagem de erro

print()
x = float(input("Introduza um numero x: "))
print()

x = int(x)
vetor_resultado = []

for numero in numeros: # para cada numero na lista
    if numero % x == 0: # se o numero for multiplo de x
        vetor_resultado.append(numero) # adiciona o numero à lista

print(vetor_resultado) # imprime a lista
