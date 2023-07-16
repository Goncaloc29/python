""" 
Tuplas (tuple)

Tuplas são bastante parecidas com listas.	
Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda operação em uma tupla gera uma nova tupla.

Cuidado 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(type(tupla2))

Cuidado 2: Tuplas com 1 elemento

tupla3 = (4)  # Isso não é uma tupla!
print(type(tupla3))

tupla4 = (4,)  # Isso é uma tupla!
print(type(tupla4))

tupla5 = 4,
print(type(tupla5))

# Podemos gerar uma tupla dinamicamente com range(inicio, fim, passo)

tupla = tuple(range(11))
print(tupla)

# Desempacotamento de tupla
~
tupla = ('Geek University', 'Programação em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)

# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis.

# Soma*, Valor Máximo*, Valor Mínimo* e Tamanho

# * Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)  # Tuplas são imutáveis
print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)

# Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)

print(3 in tupla)

# Iterando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

for indice, valor in enumerate(tupla):
    print(indice, valor, tupla[indice])

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('a'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# Iterar com while

i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificamos em qual índice um elemento está na tupla

print(meses.index('Junho'))

# Slicing

# tupla[inicio:fim:passo]

print(meses[5:9])

# Por que utilizar tuplas?

# - Tuplas são mais rápidas do que listas.

# - Tuplas deixam seu código mais seguro*.

# Isso porque trabalhar com elementos imutáveis traz segurança para o seu código.

* Isso não significa que se você utilizar tuplas seu código nunca terá erros.

"""