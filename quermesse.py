teste = 0
while True:
    participantes = int(input())
    if participantes == 0:
        break
    else:
        ingressos = [int(y) for y in input().split()]
        ganhador = False
        for indice, ingresso in enumerate(ingressos):
            if ingresso == indice + 1:
                ganhador = ingresso
                teste += 1
                print(f'Teste {teste}')
                print(ganhador)        
                break
