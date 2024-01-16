import sqlite3
from registros_ig import ORIGIN_DATA
from registros_ig.conexion import Conexion

def seletc_all():
    conectar = Conexion("select * from movements;")

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
    conexion = sqlite3.connect(ORIGIN_DATA)
    cur = conexion.cursor()
    res = cur.execute(f"select * from movements where id={id};")
    result = res.fetchall()
    conexion.close()
    return result[0]


def delete_by(id):
    conexion = sqlite3.connect(ORIGIN_DATA)
    cur = conexion.cursor()
    cur.execute(f"delete from movements where id={id};")
    conexion.commit()

    conexion.close()

    

