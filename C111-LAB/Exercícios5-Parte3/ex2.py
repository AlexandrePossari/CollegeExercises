# Encontre o nome e a região do país que possui a maior população segundo este Dataset
import pandas as pd

df = pd.read_csv('C111-LAB/Exercícios5-Parte3/paises.csv', delimiter=';')
df_with_max_pop = df[df['Population'] == df['Population'].max()]
print('Nome:')
print(f'{list(df_with_max_pop['Country'])[0]}')
print('Região:')
print(f'{list(df_with_max_pop['Region'])[0]}')