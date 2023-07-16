""" Um funcionário recebe aumento anual. Em 1995 foi contratado por 2000 reais. Em 1996
recebeu aumento de 1.5%. A partir de 1997, os aumentos sempre correspondem ao
dobro do ano anterior. Faça programa que determine o salário atual do funcionário. """

salario = 2000

aumento = salario * 0.015

for i in range(1997, 2023 + 1):
    aumento *= 2

print("Salario atual do funcionario é: ", salario + aumento)
