valores = input()

str = valores.split(" ")

a = int(str[0])
b = int(str[1])
c = int(str[2])
d = int(str[3])


if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
