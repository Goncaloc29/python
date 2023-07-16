"""
Funções com parâmetro padrão (de entrada)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional

print('Geek University')
print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória

def quadrado(numero):
    return numero * numero

print(quadrado(3))
print(quadrado())  # TypeError

# Funções onde a passagem de parâmetro seja opcional, devem ter o parâmetro com um valor default (padrão)

def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(2, 3))  # 2 * 2 * 2
print(exponencial(3, 2))  # 3 * 3

print(exponencial(3))  # Por padrão eleva ao quadrado
print(exponencial(3, 5))  # 3 * 3 * 3 * 3 * 3

# OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração.

# ERRO!
def teste(num=2, potencia): 
    return num ** potencia

print(teste(6))

# Correto
def teste(potencia, num=2):
    return num ** potencia

print(teste(6))

# Outros exemplos

def soma(num1, num2):
    return num1 + num2

print(soma(4, 3))
print(soma(4))  # TypeError
print(soma())  # TypeError

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor!'
    return f'Olá {nome}'
print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany'))

# Por quê utilizar parâmetros com valor default?

- Nos permite ser mais flexíveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código;

# Quais tipos de dados podemos utilizar como valores default para parâmetros?

- Qualquer tipo de dado: Números, strings, floats, booleanos, listas, tuplas, dicionários, funções, etc;

# Exemplo

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def sub(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, sub))

# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek'  # Variável global

def diz_oi():
    instrutor = 'Python'  # Variável local
    return f'Oi {instrutor}'
print(diz_oi())

OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência.


Atenção com variáveis globais (Se puder evitar, evite!)

total = 0

def incrementa():
    total = total + 1  # A variável local total está sendo criada
    return total

print(incrementa())

# OBS: A função incrementa está tentando fazer a alteração de uma variável global, mas ela não está declarada como global.

# Correção

total = 0

def incrementa():
    global total  # Avisando que queremos utilizar a variável global
    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())


"""