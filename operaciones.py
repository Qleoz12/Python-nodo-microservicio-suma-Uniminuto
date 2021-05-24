i = 0
listanumeros = []
tamaño = 3
numeros = int
class Guardar_numero ():
    
    for i in range(tamaño):
        numeros= int(input("digite el numero por favor: "))
        listanumeros.append(numeros)
    print(listanumeros)
    

def sumNums (listanumeros):
        suma = 0
        for i in listanumeros:
            suma += i
        return suma    
print(sumNums(listanumeros))
