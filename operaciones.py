
class Operaciones:

    def __init__(self):
        self.i = 0
        #arreglo donde se guarda los numeros por nodo
        self.listanumeros = []
        

    def saveNum(self,numero):
        self.listanumeros.append(numero)
        print(self.listanumeros)
        

    def sumNums (self):
        suma = 0
        for i in listanumeros:
            suma += i
            
        print(suma)
        return suma
