n1 = int(input('primeiro número: '))
n2 = int(input('segundo número: '))

if n1 <= n2:
    tamanho = n2 - (n1 + 1)
else: 
    tamanho = n1 - (n2 + 1) 
print(f'{tamanho}')