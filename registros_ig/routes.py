from registros_ig import app
from flask import render_template

@app.route("/")
def index():
    diccionario = [{"fecha":"2024-01-01","concept":"Nomina enero","monto":1500},
                   {"fecha":"2024-01-02","concept":"Compra de reyes","monto":-100},
                   {"fecha":"2024-01-02","concept":"Compra de mercadona","monto":-100},
                   {"fecha":"2024-01-02","concept":"Compra de roscón","monto": -20}]
    return render_template("index.html",variable= diccionario)