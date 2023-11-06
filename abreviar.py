nome = input()
partes = nome.split()

if len(partes) <= 2:
    nome_abreviado = nome
else:
    nome_abreviado = partes[0]
    for parte in partes[1:-1]:
        if len(parte) > 3:
            nome_abreviado += " " + parte[0] + "."
        else:
            nome_abreviado += " " + parte
    nome_abreviado += " " + partes[-1]

print(nome_abreviado)
