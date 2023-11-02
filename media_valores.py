quantidade = int(input('quantidade: '))
soma = 0

for i in range(quantidade):
    números = float(input('números: '))
    soma += números
media = soma / quantidade
print(media)