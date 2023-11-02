contador = 0
pares = 0
impares = 0
negativos = 0
positivos = 0
while contador < 5:
    x = int(input())
    if x % 2 == 0:
        pares +=1
    if x % 2 == 1:
        impares +=1
    if x > 0:
        positivos += 1
    if x < 0:
        negativos += 1
    contador += 1
print(f'{pares} valor(es) par(es)\n{impares} valor(res) impar(es)\n{positivos} valor(res) positivo(s)\n{negativos} valor(res) negativo(s)' )