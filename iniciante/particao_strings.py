""" Calculo Simples
Partir strings para variaveis """


entrada1 = input()
entrada2 = input()

str = entrada1.split(" ")

a = int(str[0])
b = int(str[1])
c = float(str[2])

str2 = entrada2.split(" ")

d = int(str2[0])
e = int(str2[1])
f = float(str2[2])

value_entrada1 = (b * c)

value_entrada2 = (e * f)

soma = value_entrada1 + value_entrada2


print("VALOR A PAGAR: R$ %.2f" %soma)
