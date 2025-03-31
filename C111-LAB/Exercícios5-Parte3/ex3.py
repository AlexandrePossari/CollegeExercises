# Agrupe os países por Regiões. 
# Em seguida, mostre a média de alfabetização (Literacy (%)) de cada região do planeta;
import pandas as pd

df = pd.read_csv('C111-LAB/Exercícios5-Parte3/paises.csv', delimiter=';')
print(df.groupby('Region')['Literacy (%)'].mean())