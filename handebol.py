jogadores, jogos = [int(x) for x in input().split()]
historicos = []
for i in range(jogadores):
    gols = [int(x) for x in input().split()]
    historicos.append(gols)
soma_todos = 0
for historico in historicos:
    fator = 1
    for gol in historico:
        fator *= gol
    if fator > 0:
        soma_todos += 1
print(soma_todos)