teste = 1
while True:
    aeroportos, num_voo = [int(w) for w in input().split()]
    if aeroportos and num_voo == 0:
        break
    else:
        quantidade = [0] * (aeroportos + 1)
        for i in range(num_voo):
            partida, chegada = [int(w) for w in input().split()]
            quantidade[partida] += 1
            quantidade [chegada] += 1
        maior_quantidade = max(quantidade)
        
        codigo_aero = []
        for cod_aero in range(1, aeroportos + 1):
            if quantidade[cod_aero] == maior_quantidade:
                codigo_aero.append(cod_aero)
        print(f'Teste {teste}')
        print(*codigo_aero)
        teste += 1