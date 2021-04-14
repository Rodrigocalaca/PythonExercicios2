from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''SUAS OPÇÕES
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('QUAL VOCÊ DESEJA JOGAR? '))
if jogador < 0 or jogador > 2:
    print('NÚMERO INVÁLIDO!')
else:
    print('-='*15)
    print('O computador jogou: {}'.format(itens[computador]))
    print('O jogador jogou: {}'.format(itens[jogador]))
    print('-='*15)
    if computador == 0:
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('VITÓRIA!')
        elif jogador == 2:
            print('DERROTA!')
    elif computador == 1:
        if jogador == 0:
            print('DERROTA!')
        elif jogador == 1:
            print('EMPATE!')
        elif jogador == 2:
            print('VITÓRIA!')
    elif computador == 2:
        if jogador == 0:
            print('VITÓRIA!')
        elif jogador == 1:
            print('DERROTA!')
        elif jogador == 2:
            print('EMPATE!')

