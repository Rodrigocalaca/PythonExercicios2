pessoas = 0
homens = 0
mulheres = 0
aux = 1
while True:
    sexo = ' '
    idade = int(input(f'Digite a IDADE da {aux}° pessoa: '))
    while sexo not in 'MF':
        sexo = str(input(f'Digite o GENÊRO da {aux}° pessoa [MASCULINO/FEMININO]: ')).strip().upper()[0]
    aux += 1
    if idade > 18:
        pessoas += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    flag = ' '
    while flag not in 'SN':
        flag = str(input('Quer continuar? [SIM/NÃO]: ')).strip().upper()[0]
    if flag in 'N':
        break
print(f'''Existem {pessoas} pessoas maiores de 18 anos
Foram cadastrados {homens} homens
Existem {mulheres} mulheres menores de 20 anos''')
