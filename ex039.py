from datetime import date
anonas = int(input('Digite o ano de nascimento: '))
atual = date.today().year
if atual - anonas > 18:
    diferença = (atual - anonas) - 18
    print('O tempo de se alistar já foi expirado a {} anos!'.format(diferença))
elif atual - anonas < 18:
    diferença = 18 - (atual - anonas)
    print('Você deve se alistar em {} anos!'.format(diferença))
else:
    print('Você deve se alistar esse ano!')
