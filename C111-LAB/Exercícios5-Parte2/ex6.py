# Utilizando do DataFrame exemplo do tópico 5.3 deste material, calcule a
# média dos elementos da coluna X que são menores que 30
# importando o numpy e o pandas
import numpy as np
import pandas as pd

np.random.seed(10)

df = pd.DataFrame(
index=['A', 'B', 'C', 'D', 'E'],
columns=['W', 'X', 'Y', 'Z'],
data=np.random.randint(1, 50, [5, 4]))

print((df['X'][df['X'] < 30]).mean())
