import sqlite3 as sql
def createtable():
    conn=sql.connect("alumnos.db")
    conn.commit()
    conn.close()
def inserttable():
    conn=sql.connect("alumnos.db")
    cursor=conn.cursor()
    instruccion=(
        """CREATE TABLE alumnos(
            id integer,
            nombre text,
            apellido integer

        )"""
    )
   
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
def insertalumnos(list):
    conn=sql.connect("alumnos.db")
    cursor=conn.cursor()
    instruccion=f"INSERT INTO alumnos VALUES (?,?,?)"
    cursor.executemany(instruccion,list)
    conn.commit()
    conn.close()
def search():
    conn=sql.connect("alumnos.db")
    cursor=conn.cursor()
    instruccion=f"SELECT * FROM alumnos WHERE nombre='carolina'"
    cursor.execute(instruccion)
    dato=cursor.fetchall()
    conn.commit()
    conn.close()
    print(dato)
    
lista=[(1,'yeray','cascante'),
      (2,'ivette','cascante'),
      (3,'maria','lamilla'),
      (4,'Francisco','castro'),
      (5,'Migue','cos'),
      (6,'carolina','flores'),
      (7,'peter','sancan'),
      (8,'juan','castro')]


if __name__ == "__main__":
    #createtable()
    #inserttable()
    #insertalumnos(lista)
    search()