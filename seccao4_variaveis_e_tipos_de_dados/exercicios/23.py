""" Leia um valor de comprimento em metros e apresente-o convertido em jardas. A fórmula
de conversão é: J=M/0.91 = sendo J o comprimento em jardas e M o comprimento em
metros """

comprimento = float(input("Introduza o comprimentos em metros: "))

jardas = comprimento / 0.91

print("{:.2f}".format(jardas))
