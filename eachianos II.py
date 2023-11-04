codigo = input()
x = 0
for parenteses in codigo:
    if parenteses == '(':
        x += 1
    elif x > 0 and parenteses == ')':
        x -= 1
if x == 0:
    print("Partiu RU!")
else:
    print(f"Ainda temos {x} assunto(s) pendente(s)!")
