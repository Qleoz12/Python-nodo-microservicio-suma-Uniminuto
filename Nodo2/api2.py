from flask import Flask, app
from flask import request
import json
app= Flask(__name__)
listanumeros = []

#Funcion suma 
@app.route('/numero/agregar')
def agregar():
    numero = request.args.get('numero')
    print(numero)


#Funcion para insertar 

@app.route('/numero/agregar')
def agregar():
    numero = request.args.get('numero')
    print(numero)


if __name__ == "__main__":
    app.run('127.0.0.2', '5005', debug=True)
