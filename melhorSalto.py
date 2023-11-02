n = int(input(''))
melhor_salto = -1
saltador = ''
for i in range(n):
    s1, s2, s3, nome = input().split()
    maior_salto = max(float(s1), float(s2), float(s3))
    if maior_salto > melhor_salto:
        melhor_salto = maior_salto
        saltador = nome
print(saltador)