from math import factorial
n = int(input('Digite um número para ser cálculado o fatorial: '))
print(factorial(n))
cont = n
fat = 1
for cont in range(n, 0, -1):
    fat = fat * cont
    cont -= 1
#while cont > 0:
    #fat = fat * cont
    #cont = cont - 1
print('resultado: {}'.format(fat))

