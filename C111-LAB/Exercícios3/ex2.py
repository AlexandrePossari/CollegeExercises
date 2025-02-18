# Crie dois conjuntos, um para cada loja. Identifique quais modelos de smartphones cada uma delas vendem. 
# Em seguida, mostre quais modelos no total você terá opção de comprar se visita-las 
# e quais modelos se encontram disponíveis em ambas as lojas

loja_1 = {'Samsung', 'Apple', 'Motorola'}
loja_2 = {'Motorola', 'Xiaomi'}

print(len(loja_1 | loja_2))
print(loja_1 | loja_2)
