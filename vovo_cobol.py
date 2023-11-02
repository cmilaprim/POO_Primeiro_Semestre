while True:
    try:
        frase = input()
        f = frase.lower().replace('-', ' ').split()
        for i in f:
            if 'c' not in i[0] or i[1]:
               print('BUG')
            else:
                print('GRACE HOPPER') 
        
    except EOFError:
        break