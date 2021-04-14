n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um número inteiro [999 para parar de digitar]: '))
    soma += n
    cont += 1
print('A soma foi {} e você digitou {} vezes'.format(soma - 999, cont - 1))
