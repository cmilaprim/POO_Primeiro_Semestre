try:
    while True:
        resultado = 'GRACE HOPPER'
        cobol = 'cobol'

        palavras = input().lower().split('-')

        for i in range(len(palavras)):
            if palavras[i][0] != cobol[i]:
                resultado = 'BUG'
                break
        print(resultado)  
except EOFError:
    pass
