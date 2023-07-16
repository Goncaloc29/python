""" Faça um programa que some os números primos existentes entre a e b, onde a e b são números informados pelo usuário """

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
sum = 0
for i in range(a, b + 1):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
    if prime:
        # sempre que encontrar um numero adiciona ao contador
        sum += 1
print("The sum of prime numbers between {} and {} is {}".format(a, b, sum))

