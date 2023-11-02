kwh = int(input())
valor = min(kwh,30)
v = valor * 0.09556
kwh -= valor

valor = min(kwh, 70)
v = valor * 0.16698
kwh -= valor

valor = min(kwh, 100)
v = valor * 0.25052
kwh -= valor

v += kwh * 0.27836
print(v)
