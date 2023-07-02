from flask import Flask, render_template
from markupsafe import escape


promociones = { 
    "Gold": {
        "beneficios": "30% de descuencto en todas las compras",
        "Membresía": "10% de nuestros clientes"},
    "Silver": {"beneficios": "20% de descuencto en todas las compras",
    "Membresía": "30% de nuestros clientes"}}

app=Flask(__name__)
@app.get ("/")
def home():
    return render_template ("home.html") 

@app.get ("/clientes")
def clientes():
    return render_template("clientes.html",promociones=promociones.items())
    
@app.get("/cliente/<id>")
def get_cliente(id):
    if id in promociones:
        promocion = promociones[id]
        return render_template('cliente.html', id=id, promocion=promocion)
    else:
        return ("no hay producto", 404)