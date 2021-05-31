import socket

class Nodo:

    def __init__(self):
        #arreglo donde se guarda los numeros por nodo
        self.listaVecinos = []
        self.net = []


    def saveVecino(self,numero):
        if self.listaVecino.size()>2:
            return

        self.listaVecino.append(numero)


    def getVecinos(self):
        return self.listaVecino

    def updateVecinos(self):

        pass

    def connect(self,hostname, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(hostname)
        socket.setdefaulttimeout(0.5)
        result = sock.connect_ex((hostname, port))
        sock.close()
        return result == 0

    def getneighbordHood(self):
        for i in range(1, 254):
            res = self.connect("192.168.0." + str(i), 2000)
            if res:
                print("Device found at: ", "192.168.0." + str(i) + ":" + str(22))

