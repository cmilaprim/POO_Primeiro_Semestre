n = int(input())
mercado = []

for coisas in range(n):
    item = input().split()
    lista = set(item)
    print(sorted(lista))