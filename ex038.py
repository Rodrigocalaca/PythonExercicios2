n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n2 > n1:
    maior=n2
    menor=n1
    print('O maior é {} e o menor é {}'.format(maior, menor))
elif n2 < n1:
    maior=n1
    menor=n2
    print('O maior é {} e o menor é {}'.format(maior, menor))
else:
    print('Os números são iguais!')
