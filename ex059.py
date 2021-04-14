n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
maior = 0
x = 0
while 5 != x :
    print('-='*20)
    print('''QUAL OPERAÇÃO DESEJA FAZER?
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] DIGITAR NOVAMENTE
    [5] SAIR''')
    x = int(input(' '))
    if x == 1:
        soma = n1 + n2
        print('A soma é: {}'.format(soma))
    elif x == 2:
        mult = n1 * n2
        print('A multiplicação é: {}'.format(mult))
    elif x == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print('O maior é: {}'.format(maior))
    elif x == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif x == 5:
        print('Obrigado por usar esse programa!')
    elif x < 1 or x > 5:
        print('Escolha inválida\nDigite um número válido!')




