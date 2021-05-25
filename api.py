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


## inicio explico

if __name__ == "__main__":
    app.run('127.0.0.2', '5005', debug=True)
