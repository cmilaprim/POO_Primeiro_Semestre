n = int(input('Número: '))
horas = n // 3600
n %= 3600
min = n // 60
seg = n % 60
print('{}:{}:{}'.format(horas, min, seg))