""" Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua
média. """

contador = 0
lista = []

while contador < 10:
    numero = int(input("Introduza um numero: "))
    if numero > 0:
        lista.append(numero)
        contador += 1
    else:
        print("Numero não válido!")        

""" print(sum(lista))
print(len(lista)) """

media = sum(lista) / len(lista)

print("A media é: {:.2f}".format(media))

