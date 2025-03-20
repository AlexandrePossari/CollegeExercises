# Apresente o crescimento/declínio no mercado de cada linguagem do
# primeiro ano para o segundo ano
import pandas as pd
import numpy as np

seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python':9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

print(seriesAno2.sub(seriesAno1))


