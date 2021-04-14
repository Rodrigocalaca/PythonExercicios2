soma = 0
maior = 0
nomevelho1 = ''
nomevelho2 = ''
totalmulher = 0
totalhomem = 0
aux = int(input('Digite quantas pessoas quer analisar: '))
for c in range(0, aux):
    print('------- {}° PESSOA -------'.format(c+1))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    genero = int(input('''Genêro:
    [1] para masculino
    [2] para feminino: '''.format(c + 1)))
    soma += idade
    if c == 1 and genero == 1:
        maior = idade
        nomevelho1 = nome
    if genero == 1 and idade > maior:
        maior = idade
        nomevelho1 = nome
    if c == 1 and genero == 2:
        maior = idade
        nomevelho2 = nome
    if genero == 2 and idade > maior:
        maior = idade
        nomevelho2 = nome
    if genero == 2:
        if idade < 20:
            totalmulher += 1
    if genero == 1:
        if idade < 20:
            totalhomem += 1
print('A média de idade do grupo é: {}'.format(soma/aux))
print('Existe {} mulher(es) menores de 20 anos'.format(totalmulher))
print('Existe {} homem(es) menores de 20 anos'.format(totalhomem))
print('O nome do homem mais velho é: {}'.format(nomevelho1))
print('O nome da mulher mais velha é: {}'.format(nomevelho2))


