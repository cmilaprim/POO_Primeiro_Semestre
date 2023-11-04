gabarito = input()
resposta = input()
nota = 0
for resp in range(len(gabarito)):
    if gabarito[resp] == resposta[resp]:
        nota += 1
print(nota)