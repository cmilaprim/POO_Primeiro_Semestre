while True:  
    num_jogadas = int(input())
    if num_jogadas == 0:
        break
    joao = 0
    maria = 0
    
    resultado = [int(w) for w in input().split()]
    for i in resultado:
        if i == 0:
                maria += 1
        elif i == 1:
                joao +=1            
    print(f"Mary won {maria} times and John won {joao} times")