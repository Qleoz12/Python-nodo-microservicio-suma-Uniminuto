from flask import Flask, jsonify, json, app
from flask import request

app= Flask(__name__)
listanumeros = []

#Funcion suma 
@app.route('/agregar',methods=['GET'])
def Agregar():
    suma = 0 
    for n in listanumeros:
       suma = suma + n
    return jsonify('Suma del servidor: ' +suma)

#Funcion para insertar 

@app.route('/numero/agregar')
def agregar():
    numero = request.args.get('numero')
    print(numero)


#funcion para traer la suma de las listas 

if __name__ == "__main__":

    app.run(host='0.0.0.0', port='2000', debug=True)
