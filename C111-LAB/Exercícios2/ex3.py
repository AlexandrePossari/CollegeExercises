# 3. Faça um programa que leia o sexo de uma pessoa e diga se ela é
# homem (caso seja digitado M) ou mulher (caso seja digitado F). Caso
# seja digitado algo inválido, continue perguntando até que o usuário
# entre com um sexo válido

while True:
    sexo = input("Digite o sexo (M/F): ").upper()
    if sexo == "M":
        print("Homem")
        break
    elif sexo == "F":
        print("Mulher")
        break
    else:
        print("Entrada inválida. Digite M ou F")
