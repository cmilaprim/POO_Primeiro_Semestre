def fatorial(n):
    fat = 1
    for i in range(2, n+1):
        fat *= i
    return fat


def fatorialR(n):
    if n == 0:
        return 1
    else:
        return n * fatorialR(n-1)


n = int(input()) 
print(fatorial(n))