""" Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais
e os escreva na tela. """

from collections import Counter

numeros = [] # lista vazia

for i in range(10): # para cada posição da lista
    numero = int(input(f"Introduza um numero para a posição {i}: ")) # pede um numero
    numeros.append(numero) # adiciona o numero à lista

contador = (Counter(numeros)) # cria um dicionario com os numeros e as suas respectivas ocorrencias

for chave, valor in contador.items(): # para cada chave e valor do dicionario
    if valor > 1: # se o valor for maior que 1
        print(f"Valor {chave} aparece {valor} vezes na sequencia.") # imprime o valor e a sua ocorrencia