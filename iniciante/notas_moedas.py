valor = float(input(""))

notas = [100, 50, 20, 10, 5, 2]

moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
    qtd_notas = int(valor // nota)
    print("{} nota(s) de R$ {},00".format(qtd_notas, nota))
    valor = valor % nota

print("MOEDAS:")
for moeda in moedas:
    qtd_moedas = int(valor // moeda)
    print("{} moeda(s) de R$ {:.2f}".format(qtd_moedas, moeda))
    valor = valor % moeda

