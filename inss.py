salarioB = float(input('Salário: '))

if salarioB <= 720:
    inss = salarioB * 0.0765
elif 720 < salarioB <= 1200:
    inss = salarioB * 0.09
elif 1200 < salarioB <= 2400:
    inss = salarioB * 0.11
elif salarioB > 2400:
    inss = 264
print(f"{inss}")