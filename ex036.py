valcasa = float(input('Digite o valor da casa desejada: '))
sal = float(input('Digite o valor do salário do comprador: '))
quant = float(input('Digite a quantidade de anos que deseja pagar: '))
prestacao = valcasa/(quant*12)
if prestacao > 0.3*sal:
    print('O valor da prestação é de {:.2f}, o que é muito alto financeamento negado!'.format(prestacao))
else:
    print('O valor da prestação é de {:.2f}, o que está dentro do pedido, financemanto aceito!'.format(prestacao))