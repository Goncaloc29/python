"""
Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se
for divisível por 400 ou se for divisível por 4 e não for divisível por 100. Por exemplo:
1988, 1992, 1996
"""

#ano = int(input("Introduza o ano: "))
continuar = "s"

while continuar == "s" or continuar == "S":
    ano = int(input("Introduza o ano: "))
    if ano % 400 == 0:
        print("Bissesto!")
    elif ano % 4 == 0 and ano % 100 != 0:
        print("Bissesto!")
    else:
        print("Não é Bissesto!")
    resposta = input("Deseja continuar a verificar anos? (s/n)")
    while resposta != "s" and resposta != "S" and resposta != "n" and resposta != "N":
        print("Opção inválida. Tente novamente.")
        resposta = input("Deseja continuar? (s/n)")
    # Atualiza a variável continuar com a resposta do usuário
    continuar = resposta