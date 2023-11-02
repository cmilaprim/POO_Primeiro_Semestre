A, B, C = (int(w) for w in input().split())
X, Y, Z = (int(w) for w in input().split())

numero = int(((X * Y) / (A * B ))) * int((Z / C))
print(numero)
