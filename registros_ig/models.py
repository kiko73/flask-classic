import sqlite3
from registros_ig import ORIGIN_DATA

def seletc_all():
    conexion = sqlite3.connect(ORIGIN_DATA)
    cur = conexion.cursor()
    res = cur.execute("select * from movements;")
    filas = res.fetchall()
    columnas = res.description

    lista_diccionario = []
    
    for f in filas:
        posicion = 0
        diccionario = {}
        for c in columnas:
            diccionario[c[0]] = f[posicion]
            posicion +=1

        lista_diccionario.append(diccionario)
    conexion.close()

    return lista_diccionario


def insert(registroForm):
    conexion = sqlite3.connect(ORIGIN_DATA)
    cur = conexion.cursor()
    res = cur.execute("insert into movements (date,concept,quantity) values (?,?,?);",registroForm)

    conexion.commit()

    conexion.close()

def select_by(id):
    conexion = sqlite3.connect(ORIGIN_DATA)
    cur = conexion.cursor()
    res = cur.execute(f"select * from movements where id={id};")
    result = res.fetchall()
    return result[0]
    

