from registros_ig import app
from flask import render_template,request,redirect,flash
from registros_ig.models import *
from datetime import date,datetime
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
    ganancia=select_ingreso()
    gastos=select_egreso()
    return render_template("index.html",datos = dic,ingreso=ganancia, egreso=gastos)

@app.route("/new", methods= ["GET","POST"])
def create():
    form = MovementsForm()

    if request.method == "GET":
        return render_template("create.html", dataForm=form)
    else:
        if form.validate_on_submit():
            insert([form.date.data.isoformat(),
                    form.concept.data,
                    form.quantity.data
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
    form = MovementsForm()
    if request.method == "GET":
        resultado = select_by(id)

        form.date.data = datetime.strptime(resultado[1],"%Y-%m-%d")
        form.concept.data = resultado[2]
        form.quantity.data = resultado[3]

        return render_template("update.html", dataForm=form,idForm= id)
    else:
        update_by(id,[form.date.data.isoformat(),
                      form.concept.data,
                      form.quantity.data
                      ])
        flash("Movimiento actualizado correctamente")
        return redirect("/")
                            

