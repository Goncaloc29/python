"""
Modulo Collections - Counter

Collections -> High-performance Container Datetypes

https://docs.python.org/3/library/collections.html#collections.Counter

Counter -> Recebe um iteravel como parametro e cria um objeto do tipo Collections Counter que é parecido com um dicionario, contendo como chave o elemento da lista passada como parametro e como valor a quantidade de ocorrencias desse elemento.

# Utilizando o Counter
from collections import Counter
# Podemos utilizar qualquer iteravel, aqui usamos uma lista

# Exemplo 1
lista = [1, 1, 1, 1, 12, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]
res = Counter(lista)
print(type(res))
print(res)

# Exemplo 2
print(Counter('Geek University'))

# Exemplo 3

texto = Es lohnt sich, jeden Tag ein paar Minuten zu lernen. Untersuchungen haben gezeigt, dass Teilnehmer, die regelmäßig lernen, häufiger ihre Ziele erreichen. Reserviere dir Zeit zum Lernen und lass dich von unserem Lernplaner daran erinnern.

palavras = texto.split()

print(Counter(palavras))

# Encontrando as 5 palavras com mais ocorrencias no texto
print(Counter(palavras).most_common(5))

"""