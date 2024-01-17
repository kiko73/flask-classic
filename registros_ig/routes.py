from registros_ig import app
from flask import render_template,request,redirect,flash
from registros_ig.models import *
from datetime import date
from registros_ig.forms import MovementsForm

def validarFormulario(datosFormulario):
    errores =[]#crear lista para guardar errores
    hoy = str(date.today())#esto quita la fecha de hoy
    if datosFormulario['date'] > hoy:
        errores.append("La fecha no puede ser mayor a la actual")
    if datosFormulario['concept'] == "":
        errores.append("El concepto no puede ir vacio")
    if datosFormulario['quantity'] =="" or float(datosFormulario['quantity']) == 0.0: 
        errores.append("El monto debe ser distinto de 0 y de vacio")

    return errores            

@app.route("/")
def index():
    dic = seletc_all()
    return render_template("index.html",datos = dic)

@app.route("/new", methods= ["GET","POST"])
def create():
    form = MovementsForm()

    if request.method == "GET":
        return render_template("create.html", dataForm=form)
    else:
        if form.validate_on_submit():
            insert([request.form['date'],
                request.form['concept'],
                request.form['quantity']
                ])
            flash("Movimiento registrado correctamente")
            return redirect("/")
        else:
            return render_template("create.html",dataForm=form)
        
    
@app.route("/delete/<int:id>",methods=["GET","POST"])
def remove(id):
    if request.method == "GET":
        resultado = select_by(id)
        return render_template("delete.html", data=resultado)
    else:
        #return "registro para eliminar"
        delete_by(id)
        flash("Movimiento borrado correctamente")

        return redirect("/")
    
@app.route("/update/<int:id>",methods=["GET","POST"])
def update(id):
    if request.method == "GET":
        return "mostrar el formulario"
    else:
        return "editar este registro"
                            

