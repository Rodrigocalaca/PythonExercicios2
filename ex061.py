a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
termos = int(input('Quantos termos quer verificar: '))
cont = 1
aux = 1
while cont <= termos:
    an = a1 + (aux - 1)*r
    cont +=1
    aux += 1
    print('{} →'.format(an), end=' ')
print('Fim!')