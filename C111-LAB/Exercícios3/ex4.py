# Faça um programa que leia o nome e peso de 3 pessoas e no final
# mostre o nome da pessoa mais pesada e a mais leve

pessoas = []

for i in range(3):
    nome = input("Nome da pessoa: ")
    peso = float(input("Peso (kg): "))
    pessoas.append((nome, peso))

mais_pesada = max(pessoas, key=lambda x: x[1])
mais_leve = min(pessoas, key=lambda x: x[1])

print(f"Mais pesada é {mais_pesada[0]} com {mais_pesada[1]} kg.")
print(f"Mais leve é {mais_leve[0]} com {mais_leve[1]} kg.")
