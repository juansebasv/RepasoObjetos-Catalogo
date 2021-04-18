from flask import Flask, render_template
from fabricas import *
from productos import *
from random import choice

app = Flask(__name__)

@app.route('/v1')
def principal_v1():
    fabricas = [FabricaHumanos(), FabricaOrcos()]
    fabrica = choice(fabricas)
    arma = fabrica.crear_producto(Arma())
    escudo = fabrica.crear_producto(Escudo())

    productos = []

    productos.append(arma)
    productos.append(escudo)    

    return render_template("productos.html", productos = productos)

@app.route('/v2')
def principal_v2():
    fabricas = [FabricaHumanos(), FabricaOrcos()]
    fabrica = choice(fabricas)
    arma = fabrica.crear_producto(Arma())
    escudo = fabrica.crear_producto(Escudo())
    montura = fabrica.crear_producto(Montura())
    personaje = fabrica.crear_producto(Personaje())

    productos = []

    productos.append(arma)
    productos.append(escudo)
    productos.append(montura)
    productos.append(personaje)

    return render_template("productos.html", productos = productos)

if __name__ == '__main__':
    app.run(debug=True)