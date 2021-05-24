
class Operaciones:

    def __init__(self):
        self.i = 0
        #arreglo donde se guarda los numeros por nodo
        self.listanumeros = []
        

    def saveNum(self,numero):
        self.listanumeros.append(numero)
        print(self.listanumeros)
        

    def sumNums (self):
        self.suma = 0
        for i in self.listanumeros:
            self.suma += i
            
        print(self.suma)
        return self.suma
