idade = int(input('Idade: '))

anos =  idade / 365
idade %= 365

meses = idade / 30
dias = idade % 30

print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))