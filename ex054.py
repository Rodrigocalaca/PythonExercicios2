from datetime import date
atual = date.today().year
aux1 = 0
aux2 = 0
for c in range(0, 7):
    ano = int(input('Digite o ano de nascimento da {}{} pessoa: '.format(c+1, '°')))
    idade = atual - ano
    if idade >= 18:
        aux1 += 1
    else:
        aux2 += 1
print('Existem {} pessoas maiores de idade e {} menores de idade!'.format(aux1, aux2))
