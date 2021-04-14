frase = str(input('Digite uma frase para a verificação: ')).strip().upper()
junto = frase.replace(' ', '')
inverso = ''
print(junto)
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(inverso)
if junto == inverso:
    print('A palavra {} é um palíndromo!'.format(frase))
else:
    print('A palavra {} NÃO é um palíndromo!'.format(frase))