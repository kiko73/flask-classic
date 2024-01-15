from registros_ig import app
from flask import render_template,request
from registros_ig.models import *
from datetime import date

def validarFormulario(datosFormulario):
    errores =[]#crear lista para guardar errores
    hoy = str(date.today())#esto quita la fecha de hoy
    if datosFormulario['date'] > hoy:
        errores.append("La fecha no puede ser mayor a la actual")
    if datosFormulario['concept'] == "":
        errores.append("El concepto no puede ir vacio")
    if datosFormulario['quantity'] =="" or float(datosFormulario['monto']) == 0.0: 
        errores.append("El monto debe ser distinto de 0 y de vacio")

    return errores            

@app.route("/")
def index():
    dic = seletc_all()
    return render_template("index.html",datos = dic)

@app.route("/new", methods= ["GET","POST"])
def create():
    if request.method == "GET":
        return render_template("create.html")
    else:
        return f"Aquí debo guardar en base de datos un nuevo registro: {request.form['date']}"
