assunto = input().split()
if len(assunto) %  2 == 0:
    print('Partiu RU!')
else:
    x = len(assunto) % 2 
    print(f'Ainda temos {x} assunto(s) pendente(s)!')