import math
n = int(input())
numeros = []
for _ in range(n):
    numeros.append(float(input()))
produto = 1
for i in numeros:
    produto *= i
media = (produto) ** (1 / n)
print(media)