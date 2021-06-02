from flask import Flask, jsonify, json, app
from flask import request
from operaciones import Operaciones
from nodo import Nodo
app= Flask(__name__)
listanumeros = []
_operaciones=Operaciones()

#Funcion suma 
@app.route('/Numero/<datoNumero>', methods=['GET'])
def Lista (datoNumero):
    #capturar el numero por la api
    _operaciones.saveNum(datoNumero )
    return jsonify('se ha guardado el numero: '+ datoNumero),200

#Funcion para insertar 
@app.route('/sumar', methods=['GET'])
def sumar():
    sumaNumeros = _operaciones.sumNums()
    return jsonify('la suma de numero: '+str(sumaNumeros)),200

#Recibo por parametros las sumas de los demas nodos y armo un arreglo
@app.route('/agregarTotal/<TotalNodo>', methods=['GET'])    
def sumatotal(TotalNodo):
    sumatotalArray =_operaciones.saveNumNet(TotalNodo)
    return jsonify('la suma total de los nodos es: '+ str(sumatotalArray)),200

#Sumamos los numeros recibidos de las sumas de los demas nodos   
@app.route('/Total', methods=['GET'])
def Total():
    TotalSuma= _operaciones.sumNumsNet()
    return jsonify('la operacion total de nodos son: '+ str(TotalSuma)),200






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
