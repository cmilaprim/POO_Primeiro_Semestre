valor = int(input('Valor: R$'))
valor10 = valor * 0.8

if valor >= 500:
    valorF = valor10 * 0.9 
elif valor >= 1000:
    valorF = valor10 * 0.85
print(f'{valorF:.2f}')


