# Se estas porcentagens de crescimento/declínio se mantivessem iguais
# para os próximos 2 anos, qual seria a linguagem mais popular?
# Dica: use o método nlargest(1) no final para retornar rapidamente
# a label e maior valor de uma Series
import pandas as pd

seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python':9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

seriesSubstract = seriesAno2.sub(seriesAno1)
seriesFinal = seriesAno2.add(seriesSubstract)
seriesFinal = seriesFinal.add(seriesSubstract)

print(seriesFinal.nlargest(1))


