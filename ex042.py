n1 = float(input('Digite o valor do primeiro segmento de triângulo: '))
n2 = float(input('Digite o valor do segundo segmento de triângulo: '))
n3 = float(input('Digite o valor do terceiro segmento de triângulo: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos digitados podem formar um triângulo!')
    if n1 == n2 and n2 == n3:
        print('O triangulo é EQUILÁTERO!')
    if n1 != n2 and n1 != n3 and n2 != n3:
        print('O triangulo é ESCALENO!')
    else:
        print('O triangulo é ISÓCELES!')
else:
    print('Os segmentos digitados NÃO podem formar um triângulo!')
