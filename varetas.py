n = int(input())
while n!=0:
    soma_pares = 0 
    for i in range(n):
        Ci, Vi = (int(w) for w in input().split())
        soma_pares += Vi // 2
    numero_retangulos = soma_pares // 2
    print(numero_retangulos)
    n = int(input())
