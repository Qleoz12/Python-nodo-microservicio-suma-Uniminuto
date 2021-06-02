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





@app.route('/vecinos', methods=['GET'])
def vecinos():
    return jsonify(NodeObj.getVecinos()),200

@app.route('/vecinos/add', methods=['POST'])
def vecinos_agregar():
    _rq=request.get_json()
    print("***********")
    print(str(_rq))
    print(str(NodeObj))
    return jsonify(NodeObj.saveVecino(_rq['ip'])),200

@app.route('/conectarNodos', methods=['GET'])
def conectarNodos():
    NodeObj.getneighbordHood()
    NodeObj.createconetions()
    if NodeObj.conect:
        print(NodeObj.getVecinos())
        NodeObj.conect=False
        return jsonify("se creacion conexiones"), 200

    return  jsonify("no hay nodos"), 400

if __name__ == "__main__":
    NodeObj = Nodo()
    app.run(host='0.0.0.0', port='2000', debug=True)
