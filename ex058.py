from random import randint
computador = randint(0, 10)
palpite = 1
print('===== JOGO DA ADIVINHAÇÃO =====')
n = int(input('Digite um número: '))
while n != computador:
    print('Você errou!')
    n = int(input('Digite um número: '))
    palpite += 1
if n == computador:
    print('Parábens você acertou, o computador escolheu {} e você {}'.format(computador, n))
    print('Você acertou em {} tentativas'.format(palpite))

