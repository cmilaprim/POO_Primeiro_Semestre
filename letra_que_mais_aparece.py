f = input()
letra_mais_ocorre = ''
ocorrencias = -1
for letra in set(f.lower().replace(' ', '')):
    n = f.count(letra)
    if n > ocorrencias:
        ocorrencias = n
        letra_mais_ocorre = letra
print(letra_mais_ocorre)