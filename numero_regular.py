n = int(input())
if n == 1:
    print(False)
else:
    for primo in (2, 3, 5):
        while n % primo == 0:
            n //= primo
    print(n == 1)