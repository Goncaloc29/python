# %% [markdown]
# # **Matriz 3 x 3**
# 
# Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estão acima da diagonal principal.

# %%
import numpy as np

# %%
matriz = np.zeros((3, 3), dtype=int) 
""" print(matriz) """

# %%
# Loop para preencher a matriz com valores do usuário
for i in range(3):
    for j in range(3):
        # Use o input para ler o valor do usuário e adicioná-lo à matriz
        elemento = int(input("Insira o elemento da posição [{}][{}]: ".format(i, j)))
        matriz[i][j] = elemento

""" print(matriz) """

# %%
# Use a função triu para acessar os elementos acima da diagonal principal
elementos_acima_diagonal = np.triu(matriz, k=1)

""" print(elementos_acima_diagonal) """

# %%
# Use a função sum para somar os elementos acima da diagonal principal
soma_acima_diagonal = np.sum(elementos_acima_diagonal) 

# Imprime a soma dos elementos acima da diagonal principal
print(soma_acima_diagonal)



# %%
