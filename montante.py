import math
capital = float(input('Capital aplicado: '))
n = int(input('meses: '))
taxa = float(input('Taxa da aplicação: '))

taxaporcem = taxa / 100
p = 1 + taxaporcem
m = capital * ((p)**n)

print('O montante é de {:.2f}'.format(m))