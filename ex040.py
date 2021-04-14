n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print('A média é {}',format(media))
if media < 5:
    print('Aluno REPROVADO!')
elif media < 7:
    print('Aluno de RECUPERAÇÃO!')
else:
    print('Aluno APROVADO!')
