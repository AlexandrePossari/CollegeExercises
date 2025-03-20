# Utilizando do mesmo DataFrame, apresente a média dos elementos da
# linha D usando a função loc() como base e a soma dos elementos da linha E
# usando a função iloc() como base
import numpy as np
import pandas as pd

np.random.seed(10)

df = pd.DataFrame(
index=['A', 'B', 'C', 'D', 'E'],
columns=['W', 'X', 'Y', 'Z'],
data=np.random.randint(1, 50, [5, 4]))

print(df.loc['D'].mean())
print(df.iloc[4:].sum(axis=1))

