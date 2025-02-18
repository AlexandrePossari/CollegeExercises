# Faça um programa que leia o nome e a média de um aluno
# e guarde-os em um dicionário. Em seguida, a partir da média (para ser
# aprovado deve ter média >=50), gere a situação final do aluno (‘AP’
# ou ‘RP’), que também deve ser guardada neste dicionário. No final,
# mostre todo o conteúdo deste dicionário

aluno = {}
aluno['nome'] = input("Seu nome? ")
aluno['media'] = int(input("Sua média? "))

if(aluno['media'] >= 50):
    aluno['situacao'] = 'AP'
else:
    aluno['situacao'] = 'RP'

print(aluno)
