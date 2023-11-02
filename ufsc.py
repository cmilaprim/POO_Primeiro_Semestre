nota = float(input('nota: '))
decimal = nota - int(nota)
if decimal < 0.25:
   n =  round(int(nota))
elif decimal < 0.75:
    n = round(int(nota)) + 0.5
else:
    n =round(int(nota)) + 1
print(f"{n}")