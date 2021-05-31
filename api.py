from flask import Flask, jsonify, json
from flask import request

from nodo import Nodo

app= Flask(__name__)
listanumeros = []

#Funcion suma 
@app.route('/Numero', methods=['GET'])
def Lista ():
    suma = 0 
    for z in listanumeros:
       suma = suma + z
    return jsonify('Suma del servidor: ' +suma)

#Funcion para insertar 
@app.route('/Agregar', methods=['POST'])
def Agregar():
    listanumeros.append(request.json['numeros'])
    return jsonify({'Numero almacenado '})

#funcion para traer la suma de las listas 
@app.route('/Traer', methods=['GET'])
def Traer():
    informaciones = request.get("https://localhost:3000/Numero")
    suma = 0
    for i in listanumeros:
        suma = suma + i
    sumaNodo = []
    sumaNodo.append({'suma de los numeros: ': str(suma)})
    sumaNodo.append(json.loads(informaciones.content))
    return jsonify('valor total: '+ sumaNodo)


#funcion para traer la suma de las listas
@app.route('/vecinos', methods=['GET'])
def barrio():
    NodeObj= Nodo()
    neighbordHood=NodeObj.getneighbordHood()
    if neighbordHood:
        for node in neighbordHood:
            print("preguntar por vecinos")
            print("si no tienne hacer conexio mutua")

    return  jsonify("no hay nodos"), 400

if __name__ == "__main__":

    app.run(host='127.0.0.1', port='2000', debug=True)
