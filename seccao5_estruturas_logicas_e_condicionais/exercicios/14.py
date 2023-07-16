""" A notafinal deum estudante é calculada apartir de três notas atribuídas entre o intervalo
de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral
e a um exame final. A média das três notas mencionadas anteriormente obedece aos
pesos: Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo
com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de
recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias. """

valores = input("Introduza as 3 notas separadas por espaço: ")

notas = valores.split()

trabalho = notas[0]
semestre = notas[1]
final = notas[2]

# para saber o peso será sempre a nota * o peso na cadeira a dividir pelo total da avaliação
trabalho = (float(trabalho) * 2) / 10
semestre = (float(semestre) * 3) / 10
final = (float(final) * 5) / 10

media = (trabalho + semestre + final)

if media >= 0 and media <= 2.9:
    print("REPROVADO - Média {:.2f}".format(media))
if media >= 3 and media <= 4.9:
    print("RECUPERAÇÃO - Média {:.2f}".format(media))
if media >= 5 and media <= 10:
    print("APROVADO - Média {:.2f}".format(media))
if media > 10:
    print("ERRO")