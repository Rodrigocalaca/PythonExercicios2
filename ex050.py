soma = 0
for c in range(0, 6):
    n = int(input('Digite o {}{} valor inteiro: '.format(c + 1, '°')))
    if n % 2 == 0:
        soma += n
print('A soma dos números pares digitados é {}'.format(soma))

