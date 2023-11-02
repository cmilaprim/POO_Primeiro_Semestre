n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))

p1 = float(input('Peso da primeira nota: '))
p2 = float(input('Peso da segunda nota: '))
p3 = float(input('Peso da terceira nota: '))

mediaP = ((n1 * p1) + (n2 * p2) + (n3 * p3)) / (p1 + p2 + p3)

print('{}'.format(mediaP <= 6))

