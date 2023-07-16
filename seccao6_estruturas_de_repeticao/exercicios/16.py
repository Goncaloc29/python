""" Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os
números ímpares de 1 até N em ordem decrescente. """

n = int(input("Introduza um numero impar: "))

while n % 2 == 0:
    print("Numero introduzido é par, tente de novo!")
    n = int(input("Introduza um numero impar: "))

i = 0

lista = []

for numero in range(1, n):
    if numero % 2 == 1:
        lista.append(numero)
        numero += 1
    else:
        numero += 1

# imprimir a lista por ordem decrescente
lista.sort(reverse=True)
print(lista)