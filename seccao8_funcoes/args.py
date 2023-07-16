"""
Entendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá chamar de qualquer coisa, desde que
comece com asterisco.

Exemplo:

*xis

Mas por convenção, utilizamos *args para definições de funções e **kwargs para definições de dicionários.

Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis.

# Exemplos

# Exemplo 1

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 6, 9))

# Entendo o args

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(3, 4, 5))
print(soma_todos_numeros(4, 5, 6, 7))
print(soma_todos_numeros(5, 6, 7, 8, 9))

# Outros exemplos

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não tenho certeza quem você é ...'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))

def soma_todos_numeros(*args):
    return sum(args)

# print(soma_todos_numeros())
# print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6]  # Desempacotador

print(soma_todos_numeros(*numeros))

# OBS: O asterisco serve para que informemos ao Python que estamos passando como argumento uma coleção de dados. Desta forma, ele saberá que precisará antes desempacotar estes dados.

"""