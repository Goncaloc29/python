""" 
Loop while

forma geral 

while expressão_booleana:
    //execução do loop

O bloco do while será repetido enquando a expressão boleana for verdadeira.

Expressão boleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo:

num = 5

num < 5

 """
# Exemplo 1

""" num = 1

while num < 10:
    print(num)
    num = num + 1 """

# OBS: Em um loop while, é importante que cuidemos do critério de parada para não causar um loop infinito.

# Exemplo 2

""" resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ') """




""" Saindo de loop com break
Utilizamos o break para sair de loops de maneira projetada. """


# exemplo 1

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Sai do loop')


# exemplo 2

while True:
    comando = input('Digite "sair" para sair: ')
    if comando == 'sair':
        break


