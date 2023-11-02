nc = int(input())
c = set()
for i in range(nc):
    c.add(input())

nt = int(input())
t = set()
for i in range(nt):
    t.add(input())

calouros_doadores = len(c.intersection(t))
proporção = calouros_doadores / nc
print(proporção)

