# 1. Crie um programa que leia seu nome completo e mostre:
# • Seu nome com todas as letras maiúsculas
# • Seu nome com todas as letras minúsculas
# • Quantas letras ao todo tem seu nome
# • E como seria se trocássemos seu último nome para “do Inatel”

nome_completo = input('Qual seu nome completo?')
print(nome_completo.upper())
print(nome_completo.lower())
print(len(nome_completo))
partes_nome = nome_completo.split()    
if len(partes_nome) > 1:
    partes_nome[-1] = "do Inatel"
nome_modificado = " ".join(partes_nome)
print(nome_modificado)
