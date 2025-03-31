# Carregue o Dataset paises.csv e em seguida mostre:
# a.Quais são os países da OCEANIA;
# b.Quantos países são da OCEANIA;
# Dica: para busca de padrões textuais no Pandas, use métodos da subclasse str da
# Series. Ex: series.str.contains(‘texto’)
import pandas as pd

df = pd.read_csv('C111-LAB/Exercícios5-Parte3/paises.csv', delimiter=';')
print("A:")
print(df[df['Region'].str.contains('OCEANIA')]['Country'].tolist())
print("B:")
print(df[df['Region'].str.contains('OCEANIA')]['Country'].count())
