import sys
import sqlite3
conn = sqlite3.connect(':memory:')


class crearDB:
    c = conn.cursor()

    c.execute('''CREATE TABLE CINE
                     (id_cine int PRIMARY KEY, nombre_cine text )''')
    c.execute("INSERT into CINE values (1,'CinePlaneta')")
    c.execute("INSERT into CINE values (2,'CineStark')")

    c.execute('''CREATE TABLE PELICULA
                     (id_pelicula int PRIMARY KEY, nombre_pelicula text )''')

    c.execute("INSERT into PELICULA values (1,'IT')")
    c.execute("INSERT into PELICULA values (2,'La hora Final')")
    c.execute("INSERT into PELICULA values (3,'Desaparecido')")
    c.execute("INSERT into PELICULA values (4,'Deep el Pulpo')")

    c.execute('''CREATE TABLE FUNCION
                    (id_funcion int PRIMARY KEY, hora int, minuto int)''')
#funciones cine 1
    c.execute("INSERT into FUNCION values (1,19,0)")
    c.execute("INSERT into FUNCION values (2,20,30)")
    c.execute("INSERT into FUNCION values (3,22,0)")
    c.execute("INSERT into FUNCION values (4,21,0)")
    c.execute("INSERT into FUNCION values (5,20,0)")
    c.execute("INSERT into FUNCION values (6,23,0)")
    c.execute("INSERT into FUNCION values (7,16,0)")
#funciones cine 2
    c.execute("INSERT into FUNCION values (8,21,0)")
    c.execute("INSERT into FUNCION values (9,23,0)")
    c.execute("INSERT into FUNCION values (10,16,0)")
    c.execute("INSERT into FUNCION values (11,20,0)")




    c.execute('''CREATE TABLE ENTRADA
                    (id_entrada int PRIMARY KEY, id_pelicula int, id_funcion int, cantidad int,
                    FOREIGN KEY(id_pelicula) REFERENCES PELICULA(id_pelicula),
                    FOREIGN KEY(id_funcion) REFERENCES FUNCION(id_funcion)
                    )''')

    c.execute('''CREATE TABLE CINE_PELICULA
                    (id_cine int, id_pelicula int,
                    PRIMARY KEY (id_cine, id_pelicula),
                    FOREIGN KEY(id_pelicula) REFERENCES PELICULA(id_pelicula)
                    )''')
#cinePlaneta
    c.execute("INSERT into CINE_PELICULA values (1,1)")
    c.execute("INSERT into CINE_PELICULA values (1,2)")
    c.execute("INSERT into CINE_PELICULA values (1,3)")
    c.execute("INSERT into CINE_PELICULA values (1,4)")
#cineStark
    c.execute("INSERT into CINE_PELICULA values (2,3)")
    c.execute("INSERT into CINE_PELICULA values (2,4)")

    c.execute('''CREATE TABLE PELICULA_FUNCION
                    (id_pelicula int, id_funcion int,
                    PRIMARY KEY (id_pelicula, id_funcion),
                    FOREIGN KEY(id_pelicula) REFERENCES PELICULA(id_pelicula),
                    FOREIGN KEY(id_funcion) REFERENCES FUNCION(id_funcion)
                    )''')

    c.execute("INSERT into PELICULA_FUNCION values (1,1)")
    c.execute("INSERT into PELICULA_FUNCION values (1,2)")
    c.execute("INSERT into PELICULA_FUNCION values (1,3)")
    c.execute("INSERT into PELICULA_FUNCION values (2,4)")
    c.execute("INSERT into PELICULA_FUNCION values (3,5)")
    c.execute("INSERT into PELICULA_FUNCION values (3,6)")
    c.execute("INSERT into PELICULA_FUNCION values (3,8)")
    c.execute("INSERT into PELICULA_FUNCION values (3,9)")
    c.execute("INSERT into PELICULA_FUNCION values (4,7)")
    c.execute("INSERT into PELICULA_FUNCION values (4,10)")
    c.execute("INSERT into PELICULA_FUNCION values (4,11)")



    conn.commit()
    c.close()
if __name__ == '__main__':
    pass
