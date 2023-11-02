salário = float(input('salário: '))
minimo = float(input('minimo: '))

if salário <= 3 * minimo:
    novo = salário * 1.2
elif 3 * minimo < salário <= 5 * minimo:
    novo = salário * 1.15
else:
    novo = salário * 1.10

if novo > 20 * minimo:
    novo = 20 * minimo
elif novo < 1.5 * minimo:
    novo = 1.5 * minimo

print(f'{novo:.2f}')