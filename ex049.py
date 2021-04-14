n = int(input('Digite o número para fazer a tabuada: '))
for c in range(1, 11):
    result = n * c
    print('{} x {} = {}'.format(n, c, result))
print('ACABOU')