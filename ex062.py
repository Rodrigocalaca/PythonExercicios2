a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
cont = 1
aux = 1
termos = 10
total = 0
while termos != 0:
    total += termos
    while cont <= total:
        an = a1 + (aux - 1)*r
        cont +=1
        aux += 1
        print('{} →'.format(an), end=' ')
    print('PAUSA')
    termos = int(input('\nQuantos termos a mais você quer mostrar? '))
print('Você mostrou {} termos'.format(total))
