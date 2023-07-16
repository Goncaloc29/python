""" Faça um programa que calcule a área de um triângulo, cuja base e altura são fornecidas
pelo usuário. Esse programa não pode permitir a entrada de dados inválidos, ou seja,
medidas menores ou iguais a 0. """

base = 0

while base <= 0:
    base = int(input("Introduza a medida da base: "))
    if base <= 0:
        print("Valor errado, tente de novo!")

altura = 0

while altura <= 0:
    altura = int(input("Introduza a medida da altura: "))
    if altura <= 0:
        print("Valor errado, tente de novo!")

area = (base * altura) / 2

print("A area do triangulo é: ", area)

""" while True:
    base = float(input("Digite a medida da base do triângulo: "))
    altura = float(input("Digite a medida da altura do triângulo: "))

    if base <= 0 or altura <= 0:
        print("As medidas fornecidas são inválidas. Por favor, digite valores maiores que zero.")
    else:
        area = (base * altura) / 2
        print("A área do triângulo é:", area)
        break """