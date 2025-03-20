# Faça um Slicing na matriz mostrando apenas as linhas A, C e E
# juntamente com as colunas X e Y. Em seguida, mostre qual seria a soma dos
# elementos de cada uma destas linhas e cada uma destas colunas.
import numpy as np
import pandas as pd

np.random.seed(10)

df = pd.DataFrame(
index=['A', 'B', 'C', 'D', 'E'],
columns=['W', 'X', 'Y', 'Z'],
data=np.random.randint(1, 50, [5, 4]))

sliced_df = df.loc[['A', 'C', 'E'], ['X', 'Y']]
print(sliced_df)

print(sliced_df.loc['A'].sum(axis=0))
print(sliced_df.loc['C'].sum(axis=0))
print(sliced_df.loc['E'].sum(axis=0))
print(sliced_df['X'].sum(axis=0))
print(sliced_df['Y'].sum(axis=0))
