sequencia = [int(x) for x in input().split()]
if sequencia[-1] > sequencia[0]:
    print('C')
elif sequencia[-1] < sequencia[0]:
    print('D')
else:
    print('N')