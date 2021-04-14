escolha = int(input('Qual elemento da sequência de Fibonacci você quer mostrar: '))
n1 = 0
n2 = 1
cont = 3
print('{} → {}'.format(n1, n2), end='')
while cont <= escolha:
    n3 = n1 + n2
    print(' → {}'.format(n3), end='')
    n1 = n2
    n2 = n3
    cont += 1
print('\nFIM!')
