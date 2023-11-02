import math

for _ in range(int(input())):
    n = int(input())

    soma_divisores = 0

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            soma_divisores += i
            soma_divisores += n // i
            
    if n != 1 and soma_divisores+1 == n:
        print(f"{n} eh perfeito")
    else:
        print(f"{n} nao eh perfeito")