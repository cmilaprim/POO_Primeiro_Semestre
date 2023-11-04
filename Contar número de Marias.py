num = int(input())

count = 0

for _ in range(num):
    nome = input().split()
    for palavra in nome:
        if palavra == 'Maria':
            count += 1
print(count)