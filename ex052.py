n = int(input('Digite um número: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print('{} '.format(c), end=' ')
if cont == 2:
    print('\n\033[mO número é divisível {} vezes por isso é primo!'.format(cont, n))
else:
    print('\n\033[mO número é divisível {} vezes por isso NÃO é primo!'.format(cont, n))
