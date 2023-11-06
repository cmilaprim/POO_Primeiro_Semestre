notas = dict()

n = int(input())
for _ in range(n):
    valor = float(input())
    quantidade = int(input())
    notas[valor] = quantidade
saque = float(input())

notas_nece = []
for valor in sorted(notas.keys(), reverse=True):
    quantidade = min(int(saque/valor), notas[valor])
    saque -= quantidade * valor
    notas_nece.append(quantidade)
    
print(*notas_nece[::-1])