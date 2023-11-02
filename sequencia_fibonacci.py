n = int(input())
t1 = t2 = 1
if n == 1 or n == 2:
    print('1')
else:
    count = 3
    while count <= n:
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        count = count + 1
print(t3)