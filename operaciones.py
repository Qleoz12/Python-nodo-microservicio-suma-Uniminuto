i = 0
listanumeros = []
tamaño= int(input("por favor digite el numero de digitos a sumar : "))   
class Guardar_numero ():
 for i in range(tamaño):
    numeros= input("digite el numero por favor: ")
    listanumeros.append(numeros)
    print(listanumeros)

class sumar_numero ():
    def sumalista(listanumeros):
        sumaTotal = 0
        for i in listanumeros:
            sumaTotal = sumaTotal + i
        return sumaTotal    

    print(sumalista(listanumeros))
