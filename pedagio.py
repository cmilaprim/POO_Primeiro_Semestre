L, D = (int(w) for w in input().split())
K, P = (int(f) for f in input().split())
n_pegadio = int(L/D)
valor = (n_pegadio * P) + K * L
print(valor)