"""
Funções com retorno

- Funções que retornam valores, devem retornar estes valores com a palavra reservada return;

- O retorno, finaliza a função, ou seja, ela sai da execução da função;

- Podemos ter, em uma função, diferentes returns;

- Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;

OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar a execução da função para outras funções.

OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é None.

OBS: Funções Python que retornam valores, devem retornar estes valores com a palavra reservada return. Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar a execução da função para outras funções.


# Exemplo 1 - Refatorando uma função
def quadrado_de_7():
    return 7 * 7

Criamos uma variavel para receber o retorno da função
ret = quadrado_de_7()
print(f'Retorno: {ret}')


# Exemplo 2

def diz_oi():
    return 'Oi!'
alguem = 'Pedro'
print(diz_oi() + alguem)

OBS: Sobre a palavra reservada return

- Ela finaliza a função, ou seja, ela sai da execução da função;

- Podemos ter, em uma função, diferentes returns;

- Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;

# Exemplo 3 - Refatorando a primeira função

def diz_oi():
    print('Estou sendo executado antes do retorno...')
    return 'Oi!'
    print('Estou sendo executado após o retorno...')

print(diz_oi())

# Exemplo 4

def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

# Exemplo 5

def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)

# Exemplo 6

def soma_impares(numeros):
    total = 0
    for numero in numeros:
        if numero % 2 != 0:
            total = total + numero
    return total

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

# vamos criar uma função para jogar a moeda

from random import random

def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação desnecessária.

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    else:
        return False

print(eh_impar())



"""