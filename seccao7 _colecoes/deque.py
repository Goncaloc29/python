"""
Modulo Collections - Deque

https://docs.python.org/3/library/collections.html#collections.deque

Podemos dizer que o deque é uma lista de alta performance.

# Importa
from collections import deque

# Criando deques

deq = deque('geek')

print(deq)

# Adicionando elementos no deque

deq.append('y')  # Adiciona no final

print(deq)

deq.appendleft('k')  # Adiciona no começo

print(deq)

# Remover elementos

print(deq.pop())  # Remove e retorna o último elemento

print(deq)

print(deq.popleft())  # Remove e retorna o primeiro elemento

print(deq)

# Podemos remover todos os elementos (zerar o deque)

deq.clear()

print(deq)

# Podemos reverter o deque

deq = deque('geek')

deq.reverse()

print(deq)

# Podemos fazer o rotate

deq.rotate(1)

print(deq)


"""