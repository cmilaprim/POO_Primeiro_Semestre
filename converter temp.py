EOrigem = str(input('Escala de origem [c, f, k]: '))
valor = float(input('Valor: '))
EDestino = str(input('Escala destino [c, f, k]: '))

if EOrigem == 'c':
    if EDestino == 'k':
        temp = valor + 273
    else:
        temp = (valor * 1.8) + 32
elif EOrigem == 'k':
    if  EDestino == 'c':
        temp = valor - 273
    else:
        temp = ((valor - 273) * 1.8) + 32
else:
    if EDestino == 'c':
        temp = (valor - 32) / 1.8
    else:
        temp = ((((valor - 32) * 5 ) / 9 ) + 273)
print(f'{temp:.2f}')