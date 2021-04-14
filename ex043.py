peso = float(input('Digite seu peso em kilogramas: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso/(altura**2)
print('O IMC dessa pessoa é de {}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc < 25:
    print('PESO IDEAL')
elif imc < 30:
    print('SOBREPESO')
elif imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
