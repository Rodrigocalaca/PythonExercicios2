parar = 'C'
soma = 0
cont = 0
while parar == 'C':
    n = int(input('Digite um valor inteiro: '))
    soma += n
    parar = str(input('Você quer parar de digitar [CONTINUAR/PARAR]:  ')).strip().upper()
    parar = parar[0]
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('A média dos números digitados foi {} e você digitou {} números'.format(soma/cont, cont))
print('O maior foi {} e o menor foi {}'.format(maior, menor))

