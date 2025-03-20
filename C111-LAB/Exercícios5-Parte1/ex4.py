# Baseado nos resultados da Questão3,
# mostre apenas os dados das linguagens que tiveram crescimento
import pandas as pd
import numpy as np

seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python':9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

seriesFinal = seriesAno2.sub(seriesAno1)
print(seriesFinal[seriesFinal > 0]) 