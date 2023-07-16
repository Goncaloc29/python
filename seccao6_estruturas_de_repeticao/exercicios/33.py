""" Dados n e dois números inteiros positivos, i e j , diferentes de 0, imprimir em ordem
crescente os n primeiros naturais que são múltiplos de i ou de j e oude ambos. Exemplo:
Para » = 6,i = 2 ej = 3 a saída deverá ser: 0,2,3,4,6,8. """

n = int(input("Introduza a quantidade de numero que pretende encontrar: "))
a = int(input("Introduza o valor a: "))
b = int(input("Introduza o valor b: "))

numeros = []
contador = 1
i = 0

while contador <= n:
    if i % a == 0 or i % b == 0:
        contador += 1
        numeros.append(i)
        i += 1
    else:
        i += 1

print(numeros)