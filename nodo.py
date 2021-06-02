import socket
import requests


class Nodo:
    def __init__(self):
        #arreglo donde se guarda los numeros por nodo
        self.listaVecinos = []
        self.net = set()
        self.netCalculated = set()
        self.ip=self.get_ip_address()
        self.conect=False


    def saveVecino(self,numero):
        if len(self.listaVecinos)>2:
            return self.listaVecinos

        self.listaVecinos.append(numero)
        return self.listaVecinos


    def getVecinos(self):
        return self.listaVecinos

    def updateVecinos(self):

        pass

    def connect(self,hostname, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(hostname)
        socket.setdefaulttimeout(0.5)
        result = sock.connect_ex((hostname, port))
        sock.close()
        return result == 0

    def get_ip_address(self):
        #netifaces.interfaces()
        #interfaces=ni.interfaces()
        #ni.ifaddresses('eth0')
        #ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
        #print(ip)  # should print "192.168.100.37"
        #return ip
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        print(s.getsockname()[0])
        ip=s.getsockname()[0]
        self.ip=ip
        s.close()
        return ip

    def getneighbordHood(self):
        #ip= self.get_ip_address('eth0')
        for i in range(0, 6):
            res = self.connect("172.28.5." + str(i), 2000)
            print(res)
            if res and "172.28.5." + str(i)!=self.ip:
                print("Device found at: ", "172.28.5."+ str(i) + ":" + str(2000))
                self.net.add("172.28.5." + str(i))


    def createconetions(self):
        print(self.net)
        for i in self.net:
            #obtengo los vecinos
            r = requests.get( "http://"+i+":2000/vecinos")
            print(r)
            print("http://"+i+":2000/vecinos"+" - "+str(r))
            if r.status_code==200:
               listavecinosnodovecino=r.json()
               print("http://"+i+":2000/vecinos"+str(listavecinosnodovecino))
               #si no tengo los dos llenos em agrego y loa grego
               if len(self.listaVecinos)<2 and len(listavecinosnodovecino)<2:
                   r =requests.post("http://" + i + ":2000/vecinos/add",None,{"ip":self.ip })
                   if r.status_code==200:
                       print("vecino agregado "+ self.ip +">> <<"+i )
                       self.saveVecino(i)
                       self.conect=True
            #de lo contrario sigo