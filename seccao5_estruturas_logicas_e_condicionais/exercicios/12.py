# Ler um número inteiro. Se o número lido for negativo, escreva a mensagem “Número
# inválido”. Se o número for positivo, calcular o logaritmo deste numero.

numero = int(input("Digite um número inteiro: "))

algoritmo = sum(int(digito) for digito in str(numero))

print("O algoritmo do número é:", algoritmo)
