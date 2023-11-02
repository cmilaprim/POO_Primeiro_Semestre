num_competidores, n_folhas, qtd_folhas_competidor = [int(w) for w in input().split()]
a = num_competidores * qtd_folhas_competidor
if n_folhas >= a :
    print('S')
else: 
    print('N')