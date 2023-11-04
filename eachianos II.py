num = int(input())

for _ in range(num):
    frase = input()
    palavra = input()
    posiçao = frase.find(palavra)
    if posiçao != -1:
        print(*posiçao)
    else:
        print(-1)