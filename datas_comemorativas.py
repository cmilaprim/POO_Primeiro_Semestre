
def numero_de_festas(data1, data2, data3):
    if data1 == data2 == data3:
        return 1  
    elif data1 == data2 or data1 == data3 or data2 == data3:
        return 2  
    else:
        return 3  

data1 = int(input())
data2 = int(input())
data3 = int(input())
num_festas = numero_de_festas(data1, data2, data3)
print(num_festas)