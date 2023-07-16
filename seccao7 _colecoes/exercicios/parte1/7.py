""" Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima
o vetor, o maior elemento e a posição que ele se encontra. """

numeros = [] # lista vazia

for i in range(10): # para cada posição da lista
    numero = int(input(f"Introduza um numero para a posição {i}: ")) # pede um numero
    numeros.append(numero) # adiciona o numero à lista

maior = max(numeros) # calcula o maior numero da lista
posicao_maior = numeros.index(maior) # calcula a posição do maior numero da lista

print(f"O maior numero é {maior} e está na posição {posicao_maior}.") # imprime o maior numero e a sua posição