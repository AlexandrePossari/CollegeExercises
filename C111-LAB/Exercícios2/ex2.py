# 2. Mostre a tabuada de um número que o usuário escolher dentro de um
# intervalo específico também escolhido por ele

n_a_ser_multiplicado = int(input('Selecione o número para ver a tabuada:'))
inicio_tabela = int(input('Selecione o número que começar multiplicando o número escolhido:'))
fim_tabela = int(input('Selecione o número que terminará multiplicando o número escolhido:'))

for i in range(inicio_tabela, fim_tabela):
    print(n_a_ser_multiplicado*i)
