# Mostre o nome das empresas que já realizaram missões espaciais,
# juntamente com suas respectivas quantidades de missões (use
# o for no final para mostrar as informações)
import numpy as np

dataset = np.loadtxt('C111-LAB/Exercícios4-Parte3/space.csv', delimiter = ';', dtype=str, encoding='utf-8')

company_set = set()
company_dict = { }

for data in dataset[1:]:
    company_set.add(str(data[1]))
    if(data[1] in company_dict):
        company_dict[str(data[1])] += 1
    else:
        company_dict[str(data[1])] = 1

for company in company_dict:
    print("Company:", company, "| Mission quantity:", company_dict[company])
