x = int(input())
y = int(input())
count = 0
for i in range(x, y+1):
    if x == y == 2:
        count += 1
    else:
        if i % 2 and i % 3!=0: 
            count+=1
print(count)
