# 4. Desenvolva um script que pergunte a distância de uma viagem em
# Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens
# até 200Km e R$0.45 para viagens mais longas

distancia = float(input("Distância da viagem em Km: "))
if distancia < 0:
    print("A distância não pode ser negativa")
else:
    if distancia <= 200:
        preco = distancia * 0.50
    else:
        preco = distancia * 0.45
    print(f"O preço da passagem é: R${preco:.2f}")


