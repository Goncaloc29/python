"""
for em python

for item in interavel:
    //execução do loop
"""


""" nome = "Geek University"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) """  # temos que transformar em uma lista

# Exemplo de for 1 (iterando em uma string)
""" for letra in nome:
    print(letra) """

# Exemplo de for 2 (iterando sobre uma lista)
""" for numero in lista:
    print(numero) """

# Exemplo de for 3 (iterando sobre um range)
"""
range(valor_inicial, valor_final)
OBS: O valor final não é inclusive.
"""
""" for numero in range(1, 10):
    print(numero) """

""" for i, v in enumerate(nome):
    print(nome[i])
 """
""" for valor in enumerate(nome):
    print(valor)
 """
""" qtd= int(input('Quantas vezes esse loop deve rodar? '))
somatorio = 0 """

""" for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    somatorio = somatorio + num
print(f'O somatório é {somatorio}') """

""" nome = 'Geek University'
for letra in nome:
    print(letra, end='') """

for x in range(3):
    for num in range(1, 11):
        print('\U0001f600' * num)



