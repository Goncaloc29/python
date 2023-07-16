"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintaxe da List Comprehension

[ dado for dado in iterável ]

# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10

res = [numero / 2 for numero in numeros]

print(res)

def funcao(valor):
    return valor * valor
    
res = [funcao(numero) for numero in numeros]

# List Comprehension vs Loop

# Loop

numeros_dobrados = []
for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

# List Comprehension
priunt([numero * 2 for numero in numeros])

Outros exemplos

nome = 'Geek University'

print([letra.upper() for letra in nome])

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([amigo.title() for amigo in amigos])

print([numero * 3 for numero in range(1, 10)])

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

print([str(numero) for numero in [1, 2, 3, 4, 5]])

"""