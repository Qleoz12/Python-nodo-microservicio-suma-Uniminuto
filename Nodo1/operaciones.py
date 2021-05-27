
class Operaciones:

    def __init__(self):
        self.i = 0
        #Lista donde se guarda los numeros por nodo
        self.listanumeros = []
        self.listasumas = []
        
    #Funcion para enviar los numeros a la lista obtenidos por parametro
    def saveNum(self,numero):
        self.listanumeros.append(numero)
        print(self.listanumeros)
        
    #Funcion para realizar la suma de los numeros de la lista
    def sumNums (self):
        self.suma = 0
        for i in self.listanumeros:
            self.suma += i
    #Se imprime la suma guardada en la variable suma      
        print(self.suma)
        return self.suma
    
    #Recibo por parametros las sumas de los demas nodos y armo un arreglo
    def saveNumNet(self,suma):
        self.listasumas.append(suma)
        print(self.listasumas)
    #Sumamos los numeros recibidos de las sumas de los demas nodos    
    def sumNumsNet (self):
        self.sumaNet = 0
        for i in self.listasumas:
            self.sumaNet += i
        print(self.sumaNet + self.suma)
        return self.sumaNet
    
