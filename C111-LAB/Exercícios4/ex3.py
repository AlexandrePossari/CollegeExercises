# 3. Mini Campo Minado
# a) Crie um NumPy Array 2 x 2 formado apenas por 0’s
# b) Em seguida, adicione um número 1 em uma posição aleatória desta matriz ;
# c) Faça uma entrada de dados para solicitar o usuário que faça uma jogada
# (selecione uma posição da matriz) 
#   I. Se ele selecionar todas as posições em que
#   o número 1 não se encontra, mostre a mensagem “Congratulations ! You beat the game! :)”
#   II. Senão, se dentro das 3 primeiras jogadas ele achar o número 1 , mostre
#   a mensagem “Game Over! :( Try Again!”

import numpy as np

mtz1 = np.zeros([2,2])
num1 = np.random.choice([0, 1])
num2 = np.random.choice([0, 1])
mtz1[num1,num2] = 1
print(mtz1)

tentativas = 3

while tentativas > 0:
    indice_escolhido1 = int(input("Digite a linha da matriz em que o 1 não está(0 ou 1): "))
    indice_escolhido2 = int(input("Digite a coluna da matriz em que o 1 não está(0 ou 1): "))
    if((indice_escolhido1 == num2) and (indice_escolhido2 == num1)):
        print("Game Over! :( Try Again!")
        break
    tentativas -= 1

if tentativas == 0:
    print("Congratulations ! You beat the game! :)")