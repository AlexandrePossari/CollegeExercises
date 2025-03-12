# Encontre quantas missões espaciais neste Dataset foram realizadas
# pelos Estados Unidos (EUA)
import numpy as np

dataset = np.loadtxt('C111-LAB/Exercícios4-Parte3/space.csv', delimiter = ';', dtype=str, encoding='utf-8')

total_count = 0

for data in dataset[1:]:
    print(np.char.find(data[2], "USA"))
    print(data[2])
    if(np.char.find(data[2], "USA") != -1):
        total_count += 1

print("Total de: ", total_count)
