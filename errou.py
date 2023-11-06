quantidade = int(input())

for _ in range(quantidade):
    conta = input().split()

    a = int(conta[0])
    b = int(conta[2])
    opração = conta[1]
    resultado = int(conta[4])

    if opração == '+':
        resultado_certo = a + b
    if opração == 'x':
        resultado_certo = a * b
    if opração == '-':
        resultado_certo = a - b
        
    dif = abs(resultado - resultado_certo)
    respota = 'E' + 'r'*dif + 'ou!'
    print(respota)
