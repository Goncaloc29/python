peso = float(input("Informe seu peso (em kg): "))
altura = float(input("Informe sua altura (em metros): "))

imc = peso / altura**2

print("Seu IMC é: {:.2f}".format(imc))

classificacoes = {
    (0, 18.5): "Abaixo do Peso",
    (18.5, 25): "Saudável",
    (25, 30): "Peso em excesso",
    (30, 35): "Obesidade Grau I",
    (35, 40): "Obesidade Grau II (severa)",
    (40, float('inf')): "Obesidade Grau III (mórbida)"
}

for intervalo, classificacao in classificacoes.items():
    if intervalo[0] <= imc < intervalo[1]:
        print("Classificação: {}".format(classificacao))