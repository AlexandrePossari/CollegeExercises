# 5. Crie uma matriz de tamanho 4x4 formada por números aleatórios inteiros
# entre 1 e 50 (use seed = 10 antes)
# a) Mostre o resultado da média de cada linha e cada coluna da matriz gerada
# b) Apresente o maior valor das médias das linhas e também das colunas
# c) Mostre a quantidade de aparições de cada um dos números gerados na matriz.
# Em seguida, mostre apenas os números que aparecem 2 vezes

import numpy as np

np.random.seed(10)

matriz = np.random.randint(1, 51, (4, 4))

medias_linhas = matriz.mean(axis=1)
medias_colunas = matriz.mean(axis=0)
print("\nMédias das linhas:", medias_linhas)
print("Médias das colunas:", medias_colunas)

maior_media_linha = max(medias_linhas)
maior_media_coluna = max(medias_colunas)
print("\nMaior média das linhas:", maior_media_linha)
print("Maior média das colunas:", maior_media_coluna)

valores, contagens = np.unique(matriz, return_counts=True)
contagem_dict = {int(k): int(v) for k, v in zip(valores, contagens)}
print("\nContagem de aparições de cada número:", contagem_dict)

numeros_repetidos_duas_vezes = [num for num, cont in contagem_dict.items() if cont == 2]
print("\nNúmeros que aparecem exatamente 2 vezes:", numeros_repetidos_duas_vezes)
