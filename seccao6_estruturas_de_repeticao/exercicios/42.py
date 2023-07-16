""" Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e
escreva para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize
a entrada de dados com um valor negativo ou zero. """
import math

n = 1

while n > 0:
    n = int(input("Número: "))
    if n > 0:
        print("Quadrado: ", n**2)
        print("Cubo: ", n**3)
        print("Raiz quadrada (sqrt): ", math.sqrt(n))
        print("Raiz quadrada (+0.5): ", n**0.5)

