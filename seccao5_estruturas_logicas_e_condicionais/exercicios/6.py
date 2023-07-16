# Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
# assim como a diferença existente entre ambos.

valor1 = float(input("Introduza o primeiro valor: "))
valor2 = float(input("Introduza o segundo valor: "))

if valor1 > valor2:
    print("O valor maior é: {:.2f}".format(valor1))
    print("a diferença entre os valores é: {:.2f}".format(valor1 - valor2))
elif valor2 > valor1:
    print("O valor maior é: {:.2f}".format(valor2))
    print("a diferença entre os valores é: {:.2f}".format(valor2 - valor1))
else:
    print("São iguais!")