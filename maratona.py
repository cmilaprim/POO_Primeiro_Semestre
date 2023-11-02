numero_postos, distancia_intermediaria = [int(x) for x in input().split()]
posição_postos = [int(x) for x in input().split()]

distancia = max(abs(posição_postos[i] - posição_postos[i+1]) for i in range(numero_postos-1))

resultado = 'S' if distancia <= distancia_intermediaria else 'N'

print(resultado)