""" Façaum programa que leia dois vetores de 10 elementos. Crie um vetor que seja a união
entre os 2 vetores anteriores, ou seja, que contém os números dos dois vetores. Não
deve conter números repetidos. """

vetor1 = set() # Set vazio
vetor2 = set() # Set vazio

print()
print("Introduzir valores para o primeiro vetor")
print()

for i in range(10): # para cada posição da lista
    numero = int(input(f"Introduza um numero para a posição {i}: ")) # pede um numero
    vetor1.add(numero) # adiciona o numero à lista


print()
print("Introduzir valores para o segundo vetor")
print()

for i in range(10): # para cada posição da lista
    numero = int(input(f"Introduza um numero para a posição {i}: ")) # pede um numero
    vetor2.add(numero) # adiciona o numero à lista

uniao = vetor1.union(vetor2) # cria um set com a união dos dois sets

print(uniao) # imprime o set

