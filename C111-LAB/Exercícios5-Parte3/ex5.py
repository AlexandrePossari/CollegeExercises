# Faça uma função que receba a taxa de mortalidade de cada país (Deathrate) e
# retorne o texto ‘Balanced’ caso o valor seja < 9 e ‘Urgent’ caso contrário. Em
# seguida, crie um campo no Dataset chamado ‘Humanitarian Help’ que receba estes
# valores para cada país. No final, mostre o Dataset para verificar se a inserção da nova
# coluna foi feita com sucesso.
import pandas as pd

df = pd.read_csv('C111-LAB/Exercícios5-Parte3/paises.csv', delimiter=';')

def func(dr):
    if dr < 9:
        return 'Balanced'
    else:
        return 'Urgent'

df['Humanitarian Help'] = df['Deathrate'].apply(func)
print(df)