f1 = input()
f2 = input()
eh_anagrama = len(f1) == len(f2) and f1 != f2
if eh_anagrama:
    for letra in f1:
        if f1.count(letra) != f2.count(letra):
            eh_anagrama = False
            break
    
print(eh_anagrama) 
