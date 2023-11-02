while True:
    quantidade = list()
    ocorrencia = 0
    num_mais_aparece = ' '
    teste = 0
    num_aeroportos, num_voo = [int(w) for w in input().split()]
    if num_voo == 0:
        break
    else:   
        for i in range(num_voo):
            partida, chegada = [int(w) for w in input().split()]
            quantidade.append(partida)
            quantidade.append(chegada)
        for num in set(quantidade):
            total = quantidade.count(num)
            teste += 1
            if total > ocorrencia:
                ocorrencia = total               
                num_mais_aparece = num
    print(f'Teste {teste}')
    print(num_mais_aparece)          
            
            