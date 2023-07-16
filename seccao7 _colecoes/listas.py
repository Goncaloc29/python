import random

""" 
listas

Listas em Python funcional como vetores em outras linguagens, com a diferença de serem dinâmicos e também de podermos colocar qualquer tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:

- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos.

- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado.

As listas em Python são representadas por colchetes: []

# Exemplos 1 - Declaração de listas

# Declaração de lista vazia

lista1 = [random.randrange(1, 50, 1) for i in range(7)]

print(lista1)

lista1.sort()

print(lista1)

lista2 = list()

# Exemplos 2 - Declaração de listas com elementos


# Exemplos 3 - Acessando elementos de uma lista

# Positivos [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Negativos [-9, -8, -7, -6, -5, -4, -3, -2, -1]

lista = [1, 2, 3, 'a', 'b', 'c', True, 10.34, [1, 2, 3]]

print(lista[0])  # 1
print(lista[1])  # 2
print(lista[2])  # 3
print(lista[3])  # a
print(lista[4])  # b
print(lista[5])  # c
print(lista[6])  # True
print(lista[7])  # 10.34
print(lista[8])  # [1, 2, 3]

# podemos facilmente contar o numero de ocorrencias de um valor em uma lista com o método count

print('Quantidade de e:', lista5.count('e'))

print(lista1)
lista1.append(-7) # append para acrecentar um elemento por vez
lista1.append(-45)



lista1.append(7, 45, 46) # append para acrecentar um elemento por vez, isto não vai funcionar 

lista1.extend([7, 45, 46]) # extend para acrecentar varios elementos por vez
print(lista1)
lista1.reverse()
print(lista1)

# podemos inserir um novo elemento na lista informando a posição do indice, não substitiuindo o valor inicial
lista1.insert(2, 99)
print(lista1)

# podemos facilmente juntar duas listas

lista10 = lista1 + lista5
print(lista10)
lista10.sort()
print(lista10)

# podemos facilmente inverter uma lista

lista10.reverse()
print(lista10)

print(lista1[::-1]) # outra forma de inverter uma lista


# copiando uma lista para outra (Shallow Copy e Deep Copy)

lista11 = lista1.copy()
print(lista11)

# tamanho da lista
print(len(lista11))

# podemos facilmente remover o ultimo elemento de uma lista

# Obs: O pop não somente remove o ultimo elemento mas também o retorna

print(lista1)
lista1.pop()
print(lista1)

# podemos remover um elemento pelo indice
# Obs: Os elementos a direita deste indice serão deslocados para a esquerda
# Obs: Se não houver elemento no indice informado teremos o erro IndexError

print(lista1)
lista1.pop(2)
print(lista1)

# podemos remover todos os elementos (zerar a lista)

print(lista1)
lista1.clear()
print(lista1)

# podemos facilmente repetir elementos em uma lista

nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# podemos facilmente converter uma string para uma lista

# Exemplo 1

curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas.

# Exemplo 2

curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

#convertendo uma lista em uma string

lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string

curso = ' '.join(lista6)
print(curso)

# iterando sobre listas

# Exemplo 1 - Utilizando for

# somar os elementos da lista
soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# utilizando variáveis em listas

num1 = 1
num2 = 2
num3 = 3

lista1 = [num1, num2, num3]

print(lista1)

# Fazemos acesso aos elementos de forma indexada

print(lista1[0])  # 1
print(lista1[1])  # 2
print(lista1[2])  # 3

# fazer acesso aos elementos de forma indexada inversa

print(lista1[-1])  # 3
print(lista1[-2])  # 2
print(lista1[-3])  # 1
"""
lista1 = [1, 2, 7, 21, -14]

lista3 = [1, 2, 3, 4, 5]

lista4 = [1, 2, 3, 'a', 'b', 'c']

lista5 = [1, 2, 3, 'a', 'b', 'c', 'e', 'b', 'e',]

lista6 = [1, 2, 3, 'a', 'b', 'c', True, 10.34, [1, 2, 3]]

lista7 = [1, 2, 3, 'a', 'b', 'c', True, 10.34, [1, 2, 3]]

lista8 = [1, 2, 3, 'a', 'b', 'c', True, 10.34, [1, 2, 3]]

lista9 = [1, 2, 3, 'a', 'b', 'c', True, 10.34, [1, 2, 3]]

lista10 = [1, 2, 3, 'a', 'b', 'c', True, 10.34, [1, 2, 3]]

lista11 = [1, 2, 3, 'a', 'b', 'c', True, 10.34, [1, 2, 3]]




print(lista1)
lista1.sort()
print(lista1)





