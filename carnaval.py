notas = [float(y) for y in input().split()]
notas.sort()
notas.pop(0)
notas.pop()
print(sum(notas))