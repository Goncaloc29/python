notas = input()

str = notas.split(" ")

nota1 = float(str[0])
nota2 = float(str[1])
nota3 = float(str[2])
nota4 = float(str[3])

# a dividir por 10 pq é os pesos das notas
media = (nota1 * 2 + nota2 * 3 + nota3 * 4 + nota4 * 1) / 10

print("Media: {:.1f}".format(media))

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input())
    print("Nota do exame: {:.1f}".format(nota_exame))
    media_final = (media + nota_exame) / 2
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(media_final))
