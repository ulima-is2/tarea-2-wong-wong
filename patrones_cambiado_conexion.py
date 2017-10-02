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

    c.execute('''CREATE TABLE FUNCION
                    (id_funcion int PRIMARY KEY, hora int, minuto int)''')


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

    c.execute('''CREATE TABLE PELICULA_FUNCION
                    (id_pelicula int, id_funcion int,
                    PRIMARY KEY (id_pelicula, id_funcion),
                    FOREIGN KEY(id_pelicula) REFERENCES PELICULA(id_pelicula),
                    FOREIGN KEY(id_funcion) REFERENCES FUNCION(id_funcion)
                    )''')




    conn.commit()
    c.close()
if __name__ == '__main__':
    pass
