area = int(input())
galão = 25
area_por_litro = 18
litros = area / area_por_litro
galões_nece = round(litros)
if galões_nece == 0:
    galão_nece = 1
    
valor = galão_nece * galão
print(area, galão_nece, round(valor))