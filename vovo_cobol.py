while True:
    try:
        frase = input()
        f = frase.lower().replace('-', ' ').split()
        for i in f:
            if 'c' not in f[0] or f[1]:
               print('BUG')
            else:
                print('GRACE HOPPER') 
        
    except EOFError:
        break