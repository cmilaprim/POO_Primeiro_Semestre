massa_inicial = float(input())
massa_final = 0.5
tempo = 0
if massa_final == 0.5:
    tempo = 50
while massa_inicial > massa_final:
    massa_inicial /= 2
    tempo = tempo + 50
print(tempo)