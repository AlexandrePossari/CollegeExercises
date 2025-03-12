# Quala media de gastos de uma missão especial se baseando em
# missões que possuam valores disponíveis (>0)?
import numpy as np

dataset = np.loadtxt('C111-LAB/Exercícios4-Parte3/space.csv', delimiter = ';', dtype=str, encoding='utf-8')

available_value_count = 0
total_cost = 0

for data in dataset[1:]:
    # print(data[6])
    if(float(data[6]) > 0):
        available_value_count += 1
        total_cost += float(data[6])

print("Média: ", total_cost/available_value_count)