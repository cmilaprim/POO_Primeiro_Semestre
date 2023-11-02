valorV = float(input('Valor do veículo: '))
sexo = input('Sexo: ').upper()[0]
idade = int(input('Idade: '))

valorDesconto = valorV * 0.1
if sexo == 'M' and idade <= 24:
    print(valorDesconto)
elif sexo == 'M' :
    if 25 <= idade <= 30:
        desconto = 0.9
    elif idade >= 33:
        desconto = 0.8
if sexo == 'F' :
    if idade <= 24:
        desconto = 0.95
    elif 25 <= idade <= 33:
        desconto = 0.8
    elif idade >= 33:
        desconto = 0.65

valorGeral = valorDesconto * desconto
print(valorGeral)