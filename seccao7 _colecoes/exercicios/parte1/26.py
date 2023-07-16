""" 26, 14, 7, 31, 35, 12, 18, 23, 9
 """
""" Faça um programa que calcule o desvio padrão de um vetor v contendo n = 10 números,
onde m é a media do vetor. """

import math # para usar a função sqrt

numeros = [] # lista vazia

for i in range(10): # para cada posição da lista
    numero = float(input(f"Introduza um numero para a posição {i}: ")) # pede um numero
    numeros.append(numero) # adiciona o numero à lista

media = sum(numeros) / len(numeros) # calcula a media

dif = [] # lista vazia

for i in range(len(numeros)): # para cada posição da lista
    dif.append((numeros[i] - media) ** 2) # adiciona o quadrado da diferença entre o numero e a media

media_dif = sum(dif) / len(dif) # calcula a media das diferenças

desvio_padrao = math.sqrt(media_dif) # calcula o desvio padrão

print("O desvio padrão dos valores introduzidos é : {:.2f}.".format(desvio_padrao)) # imprime o desvio padrão


""" print(soma)
print(num_elementos)
print(media) """

