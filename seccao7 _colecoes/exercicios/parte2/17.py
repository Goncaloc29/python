""" 
Leia uma matriz 10 x 3 com as notas de 10 alunos em 3 provas. Em seguida, escreva
o número de alunos cuja pior nota foi na prova 1, o número de alunos cuja pior nota foi
na prova 2, e o número de alunos cuja pior nota foi na prova 3. Em caso de empate
das piores notas de um aluno, o critério de desempate é arbitrário, mas o aluno deve ser
contabilizado apenas uma vez. 
"""

import numpy as np

notas = np.zeros((10, 3))

for i in range(10):
    for j in range(3):
        nota = float(input(f"Digite a nota do aluno {i+1} na prova {j+1}: "))
        notas[i][j] = nota

print(notas)
