while True:
    qntd_perguntas, qtnd_min = [int(w) for w in input().split()]
    if qntd_perguntas and qtnd_min == 0:
        break
    
    perguntas = [int(w) for w in input().split()]

    quantidade = [0] * (qntd_perguntas + 1)
    for pergunta in perguntas:
        quantidade[pergunta] += 1
        maior_qntd = max(quantidade)
    
    mais_perguntada = []
    for pergunta in range(1, qntd_perguntas + 1):
        if quantidade[pergunta] >= maior_qntd:
            mais_perguntada.append(pergunta)
    print(mais_perguntada)

"""while True:
    num_perguntas, quantidade_necessaria = [int(x) for x in input().split()]
    if num_perguntas == 0:
        break
    else:
        ocorrencia = -1
        pergunta_mais_frequente = 0
        perguntas = [int(y) for y in input().split()]
        for pergunta in set(perguntas):
            frequencia = perguntas.count(pergunta)
            if frequencia >= quantidade_necessaria:
                ocorrencia = frequencia
                pergunta_mais_frequente = pergunta
        print(pergunta_mais_frequente)
 """