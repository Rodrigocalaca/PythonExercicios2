from random import randint
soma = 0
vitorias = 0
while True:
    escolha = ' '
    n = int(input('Digite um valor pra jogar PAR ou IMPAR: '))
    computador = randint(0, 10)
    while escolha not in 'PI':
        escolha = str(input('PAR ou IMPAR: ')).strip().upper()[0]
    soma = n + computador
    if escolha == 'P':
        if soma % 2 == 0:
            print(f'Você jogou {n} e o computador jogou {computador} o que da {soma}, VITÓRIA!')
            vitorias += 1
        if soma % 2 != 0:
            print(f'Você jogou {n} e o computador jogou {computador} o que da {soma}, DERROTA!')
            break
    elif escolha == 'I':
        if soma % 2 != 0:
            print(f'Você jogou {n} e o computador jogou {computador} o que da {soma}, VITÓRIA!')
            vitorias += 1
        if soma % 2 == 0:
            print(f'Você jogou {n} e o computador jogou {computador} o que da {soma}, DERROTA!')
            break
print(f'Você obteve {vitorias} vitorias consecutivas!')
print('FIM!')