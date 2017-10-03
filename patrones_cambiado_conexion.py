import sys
import sqlite3
import patrones_cambiado
from patrones_cambiado import *
conn = sqlite3.connect(':memory:')



class Coneccion():
    def crearDB(self):
        c = conn.cursor()

        c.execute('''CREATE TABLE CINE
                         (id_cine int PRIMARY KEY, nombre_cine text )''')
        c.execute('''CREATE TABLE PELICULA
                         (id_pelicula int PRIMARY KEY, nombre_pelicula text )''')
       
        c.execute('''CREATE TABLE CINE_PELICULA
                        (id_cine int, id_pelicula int,
                        PRIMARY KEY (id_cine, id_pelicula),
                        FOREIGN KEY(id_pelicula) REFERENCES PELICULA(id_pelicula)
                        )''') 
        c.execute('''CREATE TABLE FUNCION
                        (id_funcion int PRIMARY KEY, id_cine int, id_pelicula, hora int, minuto int,
                        FOREIGN KEY(id_cine, id_pelicula) REFERENCES CINE_PELICULA(id_cine, id_pelicula)
                            )''')
        c.execute('''CREATE TABLE ENTRADA
                        (id_entrada INTEGER PRIMARY KEY AUTOINCREMENT, id_funcion int, cantidad int,
                        FOREIGN KEY(id_funcion) REFERENCES FUNCION(id_funcion)
                        )''')
        conn.commit()
        c.close()

    def listar_Cines(self):
        c = conn.cursor()
        c.execute("SELECT * FROM CINE")
        rows = c.fetchall()
        pass
    def listar_peliculas(self, id_cine):
        c = conn.cursor()
        c.execute("""SELECT PELICULA.id_pelicula, nombre_pelicula FROM PELICULA
            JOIN CINE_PELICULA ON PELICULA.id_pelicula = CINE_PELICULA.id_pelicula 
            WHERE id_cine = (?)""", (id_cine,) )
        rows = c.fetchall()
        result = []
        for row in rows:
            result.append(Pelicula(row[0],row[1]))
        c.close() 
        return result
        
    def listar_funciones(self, id_cine, id_pelicula):
        c = conn.cursor()
        c.execute("""SELECT id_funcion, id_cine, id_pelicula, hora, minuto FROM FUNCION 
            WHERE id_cine = (?) and id_pelicula = (?)""", (id_cine, id_pelicula) )
        rows = c.fetchall()
        result = []
        for row in rows:
            result.append(Funcion(row[0],row[3],row[4]))
        c.close() 
        return result
    def listar_entradas(self, id_funcion):
        c = conn.cursor()
        c.execute("""SELECT E.id_entrada, F.id_pelicula, E.id_funcion, E.cantidad FROM ENTRADA E
            JOIN FUNCION F ON E.id_funcion = F.id_funcion
            WHERE id_funcion = ? """, (id_funcion) )
        rows = c.fetchall()
        result = []
        for row in rows:
            result.append(Entrada(row[0], row[1], row[2], row[3]))
        c.close() 
        return result
    def anadir_entrada(self, id_pelicula, id_funcion, cantidad):
        c = conn.cursor()
        c.execute("""INSERT INTO ENTRADA(id_funcion, cantidad)
            VALUES (?, ?)""", (id_funcion, cantidad) )
        result = Entrada(c.lastrowid, id_pelicula, id_funcion, cantidad)
        c.close()
        return result
    def inserts(self):

        
        c = conn.cursor()

        c.execute("INSERT into CINE values (1,'CinePlaneta')")

        c.execute("INSERT into CINE values (2,'CineStark')")

        # peliculas
        c.execute("INSERT into PELICULA values (1,'IT')")
        c.execute("INSERT into PELICULA values (2,'La hora Final')")
        c.execute("INSERT into PELICULA values (3,'Desaparecido')")
        c.execute("INSERT into PELICULA values (4,'Deep el Pulpo')")



        #cinePlaneta

        c.execute("INSERT into CINE_PELICULA values (1,1)")

        c.execute("INSERT into CINE_PELICULA values (1,2)")

        c.execute("INSERT into CINE_PELICULA values (1,3)")
        c.execute("INSERT into CINE_PELICULA values (1,4)")

        #cineStark

        c.execute("INSERT into CINE_PELICULA values (2,3)")
        c.execute("INSERT into CINE_PELICULA values (2,4)")

        #funciones cine 1

        c.execute("INSERT into FUNCION values (1,1,1,19,0)")

        c.execute("INSERT into FUNCION values (2,1,1,20,30)")

        c.execute("INSERT into FUNCION values (3,1,1,22,0)")

        c.execute("INSERT into FUNCION values (4,1,2,21,0)")

        c.execute("INSERT into FUNCION values (5,1,3,20,0)")

        c.execute("INSERT into FUNCION values (6,1,3,23,0)")

        c.execute("INSERT into FUNCION values (7,1,4,16,0)")
        #funciones cine 2

        c.execute("INSERT into FUNCION values (8,2,3,21,0)")

        c.execute("INSERT into FUNCION values (9,2,3,23,0)")

        c.execute("INSERT into FUNCION values (10,2,4,16,0)")

        c.execute("INSERT into FUNCION values (11,2,4,20,0)")   


        c.close()
