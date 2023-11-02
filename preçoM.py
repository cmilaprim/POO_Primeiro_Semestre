comprimento = float(input())
largura = float(input())
gavetas = int(input())
madeira = input().upper()

area = comprimento * largura
if area > 2:
    preço_area = (area * 100) + 50
else:
    preço_area = area * 100

if madeira == 'MOGNO':
    preço_madeira = 150
elif madeira == 'CARVALHO':
    preço_madeira = 125
else:
    preço_madeira = 0

preço_gavetas = gavetas * 30

preço_total = preço_area + preço_madeira + preço_gavetas
if preço_total <= 200:
    preço_t = 200
else:
    preço_t = preço_total
print(preço_t)