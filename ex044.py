preço = float(input('Digite o valor da compra: R$'))
print('FORMAS DE PAGAMENTO\n[1] à vista dinheiro/cheque\n[2] à vista cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão')
aux = int(input(''))
if aux == 1:
    preço = preço*0.9
elif aux == 2:
    preço = preço*0.95
elif aux == 3:
    preço = preço
    parcela = preço/2
    print('Serão duas parcelas de R${:.2f} cada'.format(parcela))
elif aux == 4:
    preço = preço*1.2
    meses = int(input('Digite em quantas parcelas você deseja dividir: '))
    parcela = preço/meses
    print('Parcelando em {} vezes o e o preço de cada uma é: {}'.format(meses, parcela))
else:
    print('NÚMERO INVALIDO, TENTE NOVAMENTE!')
print('O preço total da compra é: R${:.2f}'.format(preço))
