# Função recursiva para método de Euclides
def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a%b)


a = int(input())
b = int(input())

# Solução iterativa para método de Euclides
while b != 0:
    resto = a % b
    a = b
    b = resto
print(a)

print(mdc(50, 65))