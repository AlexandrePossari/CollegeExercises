# Encontre qual foi a missão 
# mais cara realizada pela empresa “SpaceX”
import numpy as np

dataset = np.loadtxt('C111-LAB/Exercícios4-Parte3/space.csv', delimiter = ';', dtype=str, encoding='utf-8')

biggest_cost = 0

for data in dataset[1:]:
    print(data[4])
    if(data[1] == "SpaceX"):
        if(float(data[6]) > biggest_cost):
            biggest_cost = float(data[6])
            mission_name = data[4]

print("Mission ", mission_name, " with the cost of: ", biggest_cost)
