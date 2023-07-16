""" Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo
em vista que o desconto foi de 12% """


valor_produto = float(input("Introduza o valor do produto: "))

desconto = valor_produto * 0.12

valor_final = valor_produto - desconto

print("O valor final do produto com o respetivo desconto é {:.2f} euros.".format(valor_final))
