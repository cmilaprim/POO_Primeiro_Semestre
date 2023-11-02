
def temperaturas(escala):
    # Retorna temperatura de congelamento e de ebulicao da escala
    if escala == 'C':
        return (0, 100)
    elif escala == 'F':
        return (32, 212)
    elif escala == 'K':
        return (273.15, 373.15)
    else:
        return (491.67, 671.67)
 
    
origem = input().upper()
temp_orig = float(input())
destino = input().upper()

cg_orig, eb_orig = temperaturas(origem)
cg_dest, eb_dest = temperaturas(destino)

temp_dest = (temp_orig-cg_orig) * (eb_dest-cg_dest) / (eb_orig-cg_orig) + cg_dest

print(temp_dest)