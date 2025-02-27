# 4. Crie uma matriz de tamanho qualquer. Extraia seu número de linhas e
# colunas, multiplique-os, e diga se esta matriz poderia se tornar um vetor
# unidimensional com número par ou ímpar de elementos 

import numpy as np

rows, cols = np.random.randint(2, 51, size=2)
matriz = np.random.randint(0, 10, size=(rows, cols))
num_linhas, num_colunas = matriz.shape

total_elementos = num_linhas * num_colunas
paridade = "par" if total_elementos % 2 == 0 else "ímpar"

print(f"O vetor unidimensional teria um número {paridade} de elementos")
