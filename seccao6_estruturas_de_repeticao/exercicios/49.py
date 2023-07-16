# O funcionário chamado Carlos tem um colega chamado João que recebe um salário que
# equivale a um terço do seu salário. Carlos gosta de fazer aplicações na caderneta de
# poupança e vai aplicar seu salário integralmente nela, pois está rendendo 2% ao mês.
# João aplicará seu salário integralmente no fundo de renda fixa, que está rendendo 5%
# ao mês. Construa um programa que deverá calcular e mostrar a quantidade de meses
# necessários para que o valor pertencente aJoão iguale ou ultrapasse o valor pertencente
# a Carlos. Teste com outros valores para as taxas.

salario_carlos = float(input("Introduza o salario do Carlos: ")) # Salário Carlos

salario_joao = salario_carlos / 3 # Salario Joao

caderneta = 0.02 # Investimento carlos
renda_fixa = 0.05 # Investimento Joao

meses = 0

while salario_joao < salario_carlos:
    salario_carlos *= (1 + caderneta)
    salario_joao *= (1 + renda_fixa)
    meses += 1

print("Levará", meses, "meses para que o valor pertencente a João iguale ou ultrapasse o valor pertencente a Carlos.")

print("Salario do Joao: {:.2f}".format(salario_joao))
print("Salario do Carlos: {:.2f}".format(salario_carlos))
