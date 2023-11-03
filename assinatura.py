num_alunos = int(input())
lista_assinatura = []
for _ in range(num_alunos):
    nome, assinatura_original = input().split()
    lista_assinatura.append(assinatura_original)
    
alunos_compareceram = int(input())
lista_assinatura_sala = []
for _ in range(alunos_compareceram):
    nome, assinatura_sala = input().split()
    lista_assinatura_sala.append(assinatura_sala)
    
falsificações = 0
for assinatura in lista_assinatura:
    if assinatura in lista_assinatura_sala:
        falsificações +=1

print(falsificações)