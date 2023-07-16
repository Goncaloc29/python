# Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado,
# uma sequência arbitrária de notas (válidas no intervalo de 10 a 20) eque mostre na tela,
# como resultado, a correspondente média aritmética, O numero de notas com que o aluno
# pretenda efetuar o cálculo não será fornecido ao programa, o qual terminará quando for
# introduzido um valor que não seja válido como nota de aprovação.

notas = []
nota = 15

while nota >= 10 and nota <= 20:
    nota = float(input("Introduza a nota do aluno: "))
    notas.append(nota)
    # print(notas)


notas.remove(nota)
# print(notas)
soma = sum(notas) / len(notas)
print("A média das notas é {:.2f}".format(soma))