f, o, l = [int(bolo) for bolo in input().split()]
fMin = 2
oMin = 3
lMin = 5
maximo = min(f // fMin, o // oMin, l // lMin)
print(maximo)