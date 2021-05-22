from flask import Flask, app
import flask
from flask import request

app= Flask(__name__)
i = 0
listanumeros = []

#request param
@app.route('/numero/agregar')
def agregar():
    numero = request.args.get('numero')
    print(numero)

'''tamaño = int
tamaño = int(input("por favor digite el numero de digitos a sumar : "))   
class Guardar_numero ():
  for i in range(tamaño):
    numeros= input("digite el numero por favor: ")
    listanumeros.append(numeros)
    print(listanumeros)

@app.route('/validacion/suma')                  
def sumalista(listanumeros):
        sumaTotal = 0
        for i in listanumeros:
            sumaTotal = sumaTotal + i
        return sumaTotal    

        print(sumalista(listanumeros))
'''



## inicio explico

if __name__ == "__main__":
    app.run('127.0.0.2', '5005', debug=True)
