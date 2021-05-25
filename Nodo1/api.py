from flask import Flask, jsonify, json, app
from flask import request

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


'''#funcion para traer la suma de las listas 
@app.route('/Traer', methods=['GET'])'''
 
    

if __name__ == "__main__":

    app.run(host='127.0.0.1', port='2000', debug=True)
