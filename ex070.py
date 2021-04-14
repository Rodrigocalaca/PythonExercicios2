total = produtosMaiores = menor = 0
nomebarato = ''
aux = 0
while True:
    produto = str(input(f'Digite o nome do {aux + 1}° produto: ')).strip()
    preço = 0
    while preço <= 0:
        preço = float(input(f'Digite o preço do {aux + 1}° produto: '))
    aux += 1
    total += preço
    if preço > 1000:
        produtosMaiores += 1
    if aux == 1:
        menor = preço
        nomebarato = produto
    else:
        if preço < menor:
            menor = preço
            nomebarato = produto
    flag = ' '
    while flag not in 'SN':
        flag = str(input('Quer continuar? [SIM/NÃO]')).strip().upper()[0]
    if flag == 'N':
        break
print(f'''O total da compra foi: {total}
Existem {produtosMaiores} produtos com preço maior do que R$1000,00''')
print(f'O produto mais barato foi: {nomebarato}')
