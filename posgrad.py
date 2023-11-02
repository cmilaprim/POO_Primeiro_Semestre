def eqv_num(conceito):
    if conceito == 'A':
        return 4
    elif conceito == 'B':
        return 3
    elif conceito == 'C':
        return 2
    else:
        return 0

c1 = input()
c2 = input()
c3 = input()
c4 = input()

ia = (eqv_num(c1) + eqv_num(c2) + eqv_num(c3) + eqv_num(c4)) / 4

esta_aprovado = c1 != 'E' and c2 != 'E' and c3 != 'E' and c4 != 'E' \
                and ia >= 3
print(esta_aprovado)