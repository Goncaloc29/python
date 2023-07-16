""" Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendose que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de imposto sobre o salário-base. """

salario = float(input("Introduza o salario:"))

gratificacao = salario * 0.05

imposto = salario * 0.07

salario_liquido = salario + gratificacao - imposto

print("O salario a receberr é {:.2f} euros.".format(salario_liquido))