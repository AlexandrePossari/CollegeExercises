# Desenvolva um programa que leia o nome, idade e sexo de n pessoas.
# No final, mostre:
# a. A média de idade do grupo
# b. Quantas mulheres têm menos de 20 anos

pessoas = []
total_idade = 0
mulheres_menos_20 = 0

n = int(input("Número de pessoas a serem cadastradas? "))

for _ in range(n):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()
    
    pessoas.append({"nome": nome, "idade": idade, "sexo": sexo})
    total_idade += idade
    
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

media_idade = total_idade / n if n > 0 else 0

print(f"\nMédia de idade do grupo: {media_idade:.2f}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}")