import math
a = int(input('Digite um valor para a: '))
b = int(input('Digite um valor para b: '))
c = int(input('Digite um valormpara c: '))

delta = b**2 - 4*a*c 

x1 = (-b + math.sqrt(delta)) / (2*a)
x2 = (-b - math.sqrt(delta)) / (2*a)

print('As raízes reais são:', x1, 'e', x2)