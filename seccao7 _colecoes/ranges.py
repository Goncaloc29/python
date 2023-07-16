""" Ranges são utilizados para gerar sequencias numéricas, não de forma aleatória, mas sim de maneira especifica.

formas gerais:

# forma 1

range(valor de parada) 

for num in range(11):
    print(num)

# forma 2

range(valor de inicio, valor de parada)

for num in range(1, 11):
    print(num)
    
# forma 3

range(valor de inicio, valor de parada, passo)

for num in range(1, 11, 2):
    print(num)

# forma 4 (inversa)

for num in range(10, 0, -1):
    print(num)

# 
"""