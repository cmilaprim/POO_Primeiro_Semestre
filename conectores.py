x = [int(x) for x in input().split()]
y = [int(x) for x in input().split()]
compativel = 'Y'
for i in range(1, len(y), 2):
        if x[i] == y[i]:
            compativel = 'N'
            break
print(compativel)
    