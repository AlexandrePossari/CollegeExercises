# Crie duas Series com os seguintes valores: 
# • seriesAno1: {‘Java’: 16.25, ‘C’: 16.04, ‘Python’:9.85}
# • seriesAno2: {‘C’: 16.21, ‘Python’: 12.12, ‘Java’: 11.68}7
import pandas as pd

labels1=['Java', 'C', 'Python']
labels1=['C', 'Python', 'Java']
dados1=[16.25, 16.04, 9.85]
dados1=[16.21, 12.12, 11.68]

seriesAno1 = pd.Series(index=labels1, data=dados1)
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

print(seriesAno1)
print(seriesAno2)
print(type(seriesAno1))
print(type(seriesAno2))