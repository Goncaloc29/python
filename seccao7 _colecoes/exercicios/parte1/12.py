""" Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos
juntamente com o maior, o menor e a média dos valores. """

numeros = []

for i in range(5): # para cada posição da lista
    valor = int(input(f"Introduza o valor para a posição: {i}: ")) # pede um numero
    numeros.append(valor) # adiciona o numero à lista

print(f"Os numeros introduzidos foram: {numeros}, o maior é {max(numeros)}, e o menor é {min(numeros)} e a média é {sum(numeros) / len(numeros)}.") # imprime numeros, maior, menor e media


