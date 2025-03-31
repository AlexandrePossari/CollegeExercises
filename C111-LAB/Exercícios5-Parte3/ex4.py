# Busque o nome de todos os países do Dataset que não possuem costa marítima 
# (Coastline (coast/area ratio) == 0) e guarde-os em um novo arquivo chamado
# noCoast.csv;
import pandas as pd

df = pd.read_csv('C111-LAB/Exercícios5-Parte3/paises.csv', delimiter=';')

df[df['Coastline (coast/area ratio)'] == 0]['Country'].to_csv('C111-LAB/Exercícios5-Parte3/noCoast.csv')
