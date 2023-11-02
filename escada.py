while True:    
    num_pessoas = int(input())
    if num_pessoas ==0:
        break
    else:
        tempo = [int(w) for w in input().split()]
        tempo_total = 10
        for i in range(1,len(tempo)):
            if tempo[i] - tempo[i-1] >10:
                tempo_total +=10
            else:
                tempo_total += tempo[i] - tempo[i-1]
        print(tempo_total)