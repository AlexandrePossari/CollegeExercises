# 5. Faça um programa que leia um número entre 1000 e 9999 e mostre na tela 
# • qual o número da unidade
# • número da dezena 
# • número da centena 
# • E número do milhar
   

numero = int(input("Número entre 1000 e 9999: "))
if 1000 <= numero <= 9999:
    milhar = numero // 1000
    centena = (numero % 1000) // 100
    dezena = (numero % 100) // 10
    unidade = numero % 10
    
    print(f"Número: {numero}")
    print(f"Milhar: {milhar}")
    print(f"Centena: {centena}")
    print(f"Dezena: {dezena}")
    print(f"Unidade: {unidade}")
else:
    print("Número digitado não estava entre 1000 e 9999")
