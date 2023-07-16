""" Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto
escalar entre eles. Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o
produto escalar. """

vetor1 = []                                                             # lista vazia
vetor2 = []                                                             # lista vazia

print()
print("Introduzir valores para o primeiro vetor")
print()

for i in range(3):                                                      # para cada posição da lista
    numero = int(input(f"Introduza um numero para a posição {i}: "))    # pede um numero
    vetor1.append(numero)                                               # adiciona o numero à lista


print()
print("Introduzir valores para o segundo vetor")
print()

for i in range(5):                                                      # para cada posição da lista
    numero = int(input(f"Introduza um numero para a posição {i}: "))    # pede um numero
    vetor2.append(numero)                                               # adiciona o numero à lista

                                                                        # Acrescentar zeros ao vetor caso não tenham o mesmo comprimento
dif = len(vetor2) - len(vetor1)                                         # diferença entre os comprimentos dos vetores
if dif > 0:                                                             # se o vetor 2 for maior
    for i in range(dif):                                                # ciclo para acrescentar zeros ao vetor 1
        vetor1.append(0)                                                # acrescentar zeros ao vetor 1
elif dif < 0:                                                           # se o vetor 1 for maior
    for i in range(abs(dif)):                                           # ciclo para acrescentar zeros ao vetor 2
        vetor2.append(0)                                                # acrescentar zeros ao vetor 2

""" print(vetor1)
print(vetor2) """

produto_escalar = 0                                                    # variavel para guardar o produto escalar

for i in range(len(vetor1)):                                           # para cada posição da lista
    produto_escalar += vetor1[i] * vetor2[i]                           # calcula o produto escalar

print(produto_escalar)                                                 # imprime o produto escalar