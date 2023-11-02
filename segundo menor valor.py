n = int(input())
menor =0 
segundo_menor = 0
for i in range(n):
        numero = int(input())
        if numero < menor:
            segundo_menor = menor
            menor = numero
        elif numero < segundo_menor and numero != menor:
            segundo_menor = numero

if segundo_menor == float('inf'):
    print("Não há segundo menor valor, pois todos os valores são iguais.")
else:
    print(segundo_menor)