from flask import Flask, jsonify, json, app
from flask import request
from operaciones import Operaciones

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
@app.route('/sumaTotal', methods=['GET'])    
def sumatotal():
    sumatotal =_operaciones.sumNumNet()
    return jsonify('la suma total de los nodos es: '+ str(sumatotal)),200

#Sumamos los numeros recibidos de las sumas de los demas nodos   
@app.route('/Total', methods=['GET'])
def Total():
    TotalSuma= _operaciones.sumNumsNet()
    return jsonify('la operacion total de nodos son: '+ str(TotalSuma)),200

if __name__ == "__main__":

    app.run(host='127.0.0.1', port='2000', debug=True)
