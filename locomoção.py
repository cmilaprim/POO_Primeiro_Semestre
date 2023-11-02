dia = int(input())
km = int(input())

ValorD = 45 * dia
cortesiaDiaria = km / dia 

if cortesiaDiaria  > 60:
    valorKM = (cortesiaDiaria  - 60) * 0.5
else:
    valorKM = 0

ValorT = valorKM +  ValorD
print(f'{ValorT:.2f}')