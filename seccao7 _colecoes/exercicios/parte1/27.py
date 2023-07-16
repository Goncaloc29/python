""" Leia 10 números inteiros e armazene em um vetor. Em seguida escreva os elementos
que são primos e suas respecttvas posições no vetor. """

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True


vetor = []

for i in range(10):
    valor = int(input("Digite um valor para a posição " + str(i) + " do vetor:" ))
    vetor.append(valor)

for i in range(len(vetor)):
    if is_prime(vetor[i]):
        print("O valor {} na posição {} é primo!".format(vetor[i], vetor.index(vetor[i])))


