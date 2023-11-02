salarioB = float(input())
dep = int(input())

if salarioB <= 1372.81:
    aliquota = 0
    dedução = 0
elif 1372.82 <= salarioB <= 2743.25:
    aliquota = (15/100) * salarioB
    dedução = salarioB - 205.95
else:
    aliquota = (27,5 / 100) * salarioB
    dedução = salarioB - 548.82

if salarioB <= 720:
    inss = (7.65 / 100) * salarioB
elif 720 < salarioB <= 1200:
    inss = (9 / 100) * salarioB
elif 1200 < salarioB <= 2400:
    inss = (11 / 100) * salarioB
else:
    inss = (11 /100) * 2400

DescontoPorDependentes = 137.99 * dep

IRRF = (salarioB - DescontoPorDependentes - inss) * (aliquota - dedução)
print(IRRF)