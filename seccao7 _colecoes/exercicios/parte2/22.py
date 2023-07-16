# %% [markdown]
# # Multiplicação de 2 Matrizes
# 
# Faça um programa que leia duas matrizes A e D de tamanho 3 x 3 e calcule C = A * B

# %%
import numpy as np

# %%
# definição da matriz A
A = np.zeros((3, 3), dtype=int)
print(A)

# %%
# definição da matriz B
B = np.zeros((3, 3), dtype=int)
print(B)

# %%
# Loop para preencher a matriz A com valores do usuário
for i in range(3):
    for j in range(3):
        # Use o input para ler o valor do usuário e adicioná-lo à matriz
        elemento = int(input("Insira o elemento da posição [{}][{}]: ".format(i, j)))
        A[i][j] = elemento

print(A)

# %%
# Loop para preencher a matriz B com valores do usuário
for i in range(3):
    for j in range(3):
        # Use o input para ler o valor do usuário e adicioná-lo à matriz
        elemento = int(input("Insira o elemento da posição [{}][{}]: ".format(i, j)))
        B[i][j] = elemento

print(B)

# %%
# Use a função dot para multiplicar as matrizes
C = np.dot(A, B)

# Imprime o resultado da multiplicação
print(C)


