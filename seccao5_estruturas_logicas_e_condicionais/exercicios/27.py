""" Escreva um programa que, dada a idade de um nadador, classifique-o em uma das
seguintes categorias:
Categoria Idade
Infantil A 5 a 7
Infantil B 8 a 10
Juvenil A 11 a 13
Juvenil B 14 a 17
Sénior maiores de 18 anos """

""" idade_nadador = int(input("Introduza a idade do nadador: ")) """

continuar = "s"

while continuar == "s":
    idade_nadador = int(input("Introduza a idade do nadador: "))
    if idade_nadador >= 5 and idade_nadador <= 7:
        print("Infantil A")
    elif idade_nadador >= 8 and idade_nadador <= 10:
        print("Infantil B")
    elif idade_nadador >= 11 and idade_nadador <= 13:
        print("Juvenil A")
    elif idade_nadador >= 14 and idade_nadador <= 17:
        print("Juvenil B")
    elif idade_nadador >= 18:
        print("Sénior")
    resposta = input("Deseja continuar a introduzir idades? (s/n)")
    while resposta != "s" and resposta != "n":
        print("Opção inválida. Tente novamente.")
        resposta = input("Deseja continuar? (s/n)")
    # Atualiza a variável continuar com a resposta do usuário
    continuar = resposta