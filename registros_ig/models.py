import sqlite3
from registros_ig import ORIGIN_DATA
from registros_ig.conexion import Conexion

def seletc_all():
    conectar = Conexion("select * from movements order by date DESC;")

    filas = conectar.res.fetchall()
    columnas = conectar.res.description

    lista_diccionario = []
    
    for f in filas:
        posicion = 0
        diccionario = {}
        for c in columnas:
            diccionario[c[0]] = f[posicion]
            posicion +=1

        lista_diccionario.append(diccionario)
    conectar.con.close()

    return lista_diccionario


def insert(registroForm):

    conectarInsert = Conexion("insert into movements(date,concept,quantity) values(?,?,?);", registroForm)
    conectarInsert.con.commit()
    conectarInsert.con.close()


def select_by(id):
    conectarSelectBy = Conexion(f"select * from movements where id={id};")
    result = conectarSelectBy.res.fetchall()
    conectarSelectBy.con.close()

    return result[0]


def delete_by(id):
    conectDeleteBy = Conexion(f"delete from movements where id={id};")
    conectDeleteBy.con.commit()
    conectDeleteBy.con.close

def update_by(id,registro):
    conectUpdate = Conexion(f"update movements set date=?, concept=? , quantity=? where id={id};",registro)
    conectUpdate.con.commit()
    conectUpdate.con.close()

def select_ingreso():
    conectIngreso = Conexion("select sum(quantity) from movements where quantity >0;")
    resultadoIngreso = conectIngreso.res.fetchall()
    conectIngreso.con.close()

    return resultadoIngreso[0][0]

def select_egreso():
    conectEgreso = Conexion("select sum(quantity) from movements where quantity <0;")
    resultadoEgreso = conectEgreso.res.fetchall()
    conectEgreso.con.close()

    return resultadoEgreso[0][0]



    

