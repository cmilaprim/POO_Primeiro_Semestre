n = int(input())
soma = 0
distancia_centro = 20
cont = 0
praia_distante = ' '
for i in range(n):
    praia, distancia = input().split(';')
    distancia = int(distancia)
    soma += distancia
    distancia_media = soma / n
    if distancia <= distancia_centro:
        distancia = distancia_centro
        cont += 1 
    elif distancia > distancia_centro:
        distancia_centro = distancia
        praia_distante = praia
print(f'{praia_distante};{cont};{round(distancia_media,1)}')
'''4
Jurerê;20
Ribeirão da Ilha;26
Pântano do Sul;31
Cacupe;15'''