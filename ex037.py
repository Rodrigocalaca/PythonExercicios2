n = int(input('Digite um número inteiro para ser convertido: '))
print('DIGITE O NÚMERO INDICADO PARA ESCOLHER A BASE DA CONVERSÃO')
b = int(input('[1] para BINÁRIO\n[2] para OCTAL\n[3] para HEXADECIMAL\nSua opção: '))
if b == 1:
    print('O número escolhido para BINÁRIO é igual a {}'.format(bin(n)[2:]))
elif b == 2:
    print('O número escolhido para OCTAL é igual a {}'.format(oct(n)[2:]))
elif b == 3:
    print('O número escohido para HEXADECIMAL é igual a {}'.format(hex(n)[2:]))
else:
    print('A opção escolhida não é válida!')

