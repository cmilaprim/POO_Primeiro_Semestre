ocorrencia = -1
numero_mais_frequente = 0
while True:
    num_perguntas, quantidade_necessaria = [int(x) for x in input().split()]
    if num_perguntas == 0:
        break
    else:
        perguntas = [int(y) for y in input().split()]
        for pergunta in set(perguntas):
            frequencia = perguntas.count(pergunta)
            if frequencia >= quantidade_necessaria:
                ocorrencia = frequencia
                numero_mais_frequente = pergunta
        print(numero_mais_frequente)