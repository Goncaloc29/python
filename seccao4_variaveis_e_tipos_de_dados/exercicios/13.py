""" Leia uma distância em quilómetros e apresente-a convertida em milhas. A fórmula de
conversão é: (M =K/1.61) sendo K a distância em quilómetros e M em milhas. """

distancia = float(input("Distância em km? "))

milhas = distancia/1.61

print("A distancia {:.2f}km, em milhas é {:.2f}".format(distancia, milhas))


