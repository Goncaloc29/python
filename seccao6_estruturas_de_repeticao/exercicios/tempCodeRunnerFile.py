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