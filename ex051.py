print('='*30)
print('10 PRIMEIROS TERMOS DE UMA PA')
print('='*30)
a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
for c in range(0, 10):
    an = a1 + (c)*r
    print(an, end= ' → ')
print('ACABOU')
