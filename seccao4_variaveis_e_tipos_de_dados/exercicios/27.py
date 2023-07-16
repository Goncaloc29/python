""" Leia um valor de área em hectares e apresente-o convertido em metros quadrados m2.
A fórmula de conversão é: M = H * 10000, sendo M a área em metros quadrados e H
a área em hectares. """

h = float(input("Introduza a area em hectares: "))

m = h * 10000

print("A area de {:.2f} hectares, em metros quadrados é {:.2f}".format(h, m))
