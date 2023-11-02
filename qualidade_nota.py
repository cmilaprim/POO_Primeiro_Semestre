n1 = float(input())
n2 = float(input())
n3 = float(input())

media = (n1 + n2 + n3 ) / 3

if 9 >= media >= 10:
    print('Ótimo') 
elif 7.5 <= media < 9:
    print('Bom')
elif 6 <= media < 7.5:
    print('Satisfatório')
elif 0 <= media < 6:
    print('Insuficiente')

