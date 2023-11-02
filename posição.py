n = int(input())
maior = 0
for i in range(n):
    numero = int(input())
    if i == 1:
        maior = numero
    else:
        if numero > maior:
            maior = numero