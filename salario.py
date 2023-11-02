horasN = int(input('Horas trabalhadas: '))
horasE= int(input('Horas extras: '))

base = 2500
ValorhorasN = base / 200
ValorhorasE = ValorhorasN * 1.2

salarioN = ValorhorasN * horasN
salarioE = ValorhorasE * horasE
salarioT = salarioE + salarioN

ir = salarioT * 0.09
inss = salarioT * 0.13
salarioL = salarioT - ir - inss

print(f'Salário Bruto: R${salarioT}')
print(f'IR: R${ir}')
print(f'INSS: R${inss}')
print(f'Salário Liquido: R${salarioL}')