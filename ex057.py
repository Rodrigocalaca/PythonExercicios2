s = 'M'
s = str(input('Digite o sexo da pessoa, escolhendo [M/F]: ')).strip().upper()
while s != 'M' and s != 'F':
    s = str(input('Digite o sexo da pessoa, escolhendo [M/F]: ')).strip().upper()
if s == 'M':
    print('Masculino!')
if s == 'F':
    print('Feminino!')
print('Fim!')
