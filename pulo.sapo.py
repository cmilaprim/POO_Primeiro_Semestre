altura_maxima , numero_de_pulos = [int(x) for x in input().split()]
altura = [int(x) for x in input().split()]
for h in range(numero_de_pulos-1):
    maior_pulo = max([(abs(altura[h] - altura[h+1]))])
resultado = 'YOU WIN' if maior_pulo <= altura_maxima else 'GAME OVER' 
print(resultado)
