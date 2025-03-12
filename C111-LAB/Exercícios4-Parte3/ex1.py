# Apresente a porcentagem de missões que deram certo
import numpy as np

dataset = np.loadtxt('C111-LAB/Exercícios4-Parte3/space.csv', delimiter = ';', dtype=str, encoding='utf-8')

total_count = 0
success_count = 0

for data in dataset:
    if(data[7] == "Success"):
        success_count += 1
    total_count += 1

print(success_count/total_count * 100, "%")