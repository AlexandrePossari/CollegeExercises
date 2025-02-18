# 1. Crie uma lista preenchida com os 5 primeiros colocados de um Campeonato de Futebol, na ordem de colocação. 
# Depois mostre :
# a. Apenas os 3 primeiros colocados
# b. Os últimos 2 colocados
# c. Uma lista com os times em ordem alfabética
# d. Em que posição da tabela se encontra o Barcelona

primeiros_colocados = ['Igrejinha FC', 'time 1', 'Barcelona', 'time 2', 'time 3']
print(primeiros_colocados[:3])
print(primeiros_colocados[3:5])
primeiros_colocados.sort()
print(primeiros_colocados)
primeiros_colocados = ['Igrejinha FC', 'time 1', 'Barcelona', 'time 2', 'time 3']
print(primeiros_colocados.index('Barcelona') + 1)

