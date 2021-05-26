from flask import Flask, jsonify, json, app
from flask import request

app= Flask(__name__)
listanumeros = []

#Funcion suma 
@app.route('/Numero',methods=['GET'])
def Lista ():
    suma = 0 
    for z in listanumeros:
       suma = suma + z
    return jsonify('Suma del servidor: ' +suma)

#Funcion para insertar 
@app.route('/Agregar')
def Agregar():
    listanumeros.append(request.json['numeros'])
    return jsonify({'Numero almacenado '})


if __name__ == "__main__":
    app.run('127.0.0.2', '3000', debug=True)
