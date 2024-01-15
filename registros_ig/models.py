import sqlite3

def seletc_all():
    conexion = sqlite3.connect("data/movimientos.sqlite")
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
    conexion = sqlite3.connect("data/movimientos.sqlite")
    cur = conexion.cursor()
    res = cur.execute("insert into movements (date,concept,quantity) values (?,?,?);",registroForm)

    conexion.commit()

    conexion.close()

