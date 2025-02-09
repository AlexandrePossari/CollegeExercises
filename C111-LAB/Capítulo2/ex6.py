# 6. Peça ao usuário para entrar com um número decimal. Em seguida,
# aplique e mostre o resultado:
# • da raiz quadrada deste número 
# • função teto 
# • função chão 
# • sua parte inteira

import math

num = float(input("Número decimal: "))

raiz_quadrada = math.sqrt(num)
teto = math.ceil(num)
chao = math.floor(num)
parte_inteira = math.trunc(num)

print(f"Raiz quadrada: {raiz_quadrada}")
print(f"Função teto: {teto}")
print(f"Função chão: {chao}")
print(f"Parte inteira: {parte_inteira}")
