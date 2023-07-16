import math

ponto1 = input()
ponto2 = input()

str = ponto1.split(" ")

x1 = float(str[0])
y1 = float(str[1])


str2 = ponto2.split(" ")

x2 = float(str2[0])
y2 = float(str2[1])

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("%.4f" % distancia)

