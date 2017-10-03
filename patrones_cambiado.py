import sys
import patrones_cambiado_conexion

from patrones_cambiado_conexion import *
class Entrada:
    def __init__(self, entrada_id, pelicula_id, funcion_id, cantidad):
        self.entrada_id = entrada_id
        self.pelicula_id = pelicula_id
        self.funcion_id = funcion_id
        self.cantidad = cantidad

class Pelicula:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.funciones = {}

    def anadir_funcion(self, funcion):
        self.funciones[funcion.id] = funcion
    def __str__(self):
        return "id_pelicula: %s, nombre_pelicula:  %s" % (self.id, self.nombre)

class Funcion:
    def __init__(self, id, hora, minuto):
        if (hora>=24 or hora<0 or minuto>=60 or minuto<0):
            raise ValueError('la wea fome culiao')
        self.id = id
        self.hora = hora
        self.minuto = minuto
        self.entradas = {}

    def toDic_1(self):
        return {"id": self.id, "hora": self.format_2digits(self.hora) + ":" + self.format_2digits(self.minuto)}
    def format_2digits(self, value):
        if (value<10):
            return "0" + str(value)
        else:
            return str(value)
    def anadir_Entrada(self, entrada):
        self.entradas[entrada.entrada_id] = entrada
    def __str__(self):
        return "id_funcion: %s, hora:  %s" % (self.id, self.format_2digits(self.hora) + ":" + self.format_2digits(self.minuto))
        #return str(self.toDic_1())

class Cine:
    def __init__(self):
        self.lista_peliculas = {}
        

    def anadir_pelicula(self, pelicula):
        self.lista_peliculas[pelicula.id]=pelicula

    def listar_peliculas(self):
        return self.lista_peliculas

    def listar_funciones(self, pelicula_id):
        return self.listar_peliculas()[int(pelicula_id)].funciones

    def listar_entradas(self, pelicula_id, funcion_id):
        return self.listar_funciones(pelicula_id)[int(funcion_id)].entradas

    def guardar_entrada(self, entrada):
        self.listar_entradas(entrada.pelicula_id, entrada.funcion_id)[entrada.entrada_id]=entrada

class CinePlaneta(Cine):
    def __init__(self):
        super(CinePlaneta, self).__init__()
        pass


class CineStark(Cine):
    def __init__(self):
        super(CineStark, self).__init__()
        pass

class CineManager:
    #static variables
    cinePlaneta = CinePlaneta()
    cineStark = CineStark()
    def __init__(self):
        self.cinePlaneta = CinePlaneta()
        self.cineStark = CineStark()
        conn = Coneccion()
        conn.crearDB()
        conn.inserts()
        self.init_general(conn, CineManager.cinePlaneta)
        self.init_general(conn, CineManager.cineStark)
        #self.init_CinePlaneta()
        #self.init_CineStark()

    def init_general(self, conn, cine):
        conn = Coneccion()
        x = None
        if cine == CineManager.cinePlaneta:
            x = 1
        elif cine == CineManager.cineStark:
            x = 2
        peliculas_Planeta=conn.listar_peliculas(x)
        for peli in peliculas_Planeta:
            funciones = conn.listar_funciones(x, peli.id)
            for funcion in funciones:
                peli.anadir_funcion(funcion)
            cine.anadir_pelicula(peli)

    def init_CinePlaneta(self):
        peliculaIT = Pelicula(1, 'IT')
        peliculaIT.anadir_funcion(Funcion(1, 19, 00))
        peliculaIT.anadir_funcion(Funcion(2, 20, 30))
        peliculaIT.anadir_funcion(Funcion(3, 22, 00))
        CineManager.cinePlaneta.anadir_pelicula(peliculaIT)

        peliculaHF = Pelicula(2, 'La Hora Final')
        peliculaHF.anadir_funcion(Funcion(1, 21, 00))
        CineManager.cinePlaneta.anadir_pelicula(peliculaHF)

        peliculaD = Pelicula(3, 'Desparecido')
        peliculaD.anadir_funcion(Funcion(1, 20, 00))
        peliculaD.anadir_funcion(Funcion(2, 23, 00))
        CineManager.cinePlaneta.anadir_pelicula(peliculaD)

        peliculaDeep = Pelicula(4, 'Deep El Pulpo')
        peliculaDeep.anadir_funcion(Funcion(1, 16, 00))
        CineManager.cinePlaneta.anadir_pelicula(peliculaDeep)

    def init_CineStark(self):
        peliculaD = Pelicula(1, 'Desparecido')
        peliculaD.anadir_funcion(Funcion(1, 21, 00))
        peliculaD.anadir_funcion(Funcion(2, 23, 00))
        CineManager.cineStark.anadir_pelicula(peliculaD)

        peliculaDeep = Pelicula(2, 'Deep El Pulpo')
        peliculaDeep.anadir_funcion(Funcion(1, 16, 00))
        peliculaDeep.anadir_funcion(Funcion(2, 20, 00))
        CineManager.cineStark.anadir_pelicula(peliculaDeep)


    def anadir_pelicula(self, cine, pelicula):
        if (cine == CinePlaneta):
            cinePlaneta.anadir_pelicula(pelicula)
        elif (cine == CineStark):
            cineStark.anadir_pelicula(pelicula)
        else:
            pass


    def listar_opciones(self):
        print('Ingrese la opción que desea realizar')
        print('(1) Listar cines')
        print('(2) Listar cartelera')
        print('(3) Comprar entrada')
        print('(0) Salir')
    def listar_cines(self):
        print('Lista de cines')
        print('1: CinePlaneta')
        print('2: CineStark')
    def encapsular(self, arg):
        print('********************')
        for elemento in arg:
            if callable(elemento):
                elemento()
            else:
                print(elemento)
        print('********************')
    def select_cine(self):
        cine = input('Primero elija un cine:')
        if cine == '1':
            # CinePlaneta
            cine = CineManager.cinePlaneta
        elif cine == '2':
            cine = CineManager.cineStark
        return cine
    def gestionar(self):
        terminado = False;
        while not terminado:
            self.listar_opciones()
            opcion = input('Opción: ')

            if opcion == '1':
                self.gestionar_mostar_cines()

            elif opcion == '2':
                self.gestionar_mostar_peliculas()

            elif opcion == '3':
                self.gestionar_anadir_entrada()
            elif opcion == '0':
                terminado = True
            else:
                print(opcion)
    def gestionar_mostar_cines(self):
        self.encapsular([self.listar_cines])
    def gestionar_mostar_peliculas(self):
        self.encapsular([self.listar_cines])

        cine = self.select_cine()

        peliculas = cine.listar_peliculas()
        def aux():
            for keys,values in peliculas.items():
                print(str(keys) + ":" + str(values))

        self.encapsular([aux]) 
    def gestionar_anadir_entrada(self):
        self.encapsular(['COMPRAR ENTRADA', self.listar_cines])
        cine = self.select_cine()

        peliculas = cine.listar_peliculas()
        for keys,values in peliculas.items():
            print(str(keys) + ":" + str(values))

        pelicula_elegida = input('Elija pelicula:')
        valid = False
        while not valid:
            def aux():
                print('Ahora elija la función (debe ingresar el formato hh:mm): ')
                for keys,values in cine.listar_funciones(pelicula_elegida).items():
                    print(str(keys) + ":" + str(values))
            self.encapsular([aux]) 
            funcion_elegida = input('Funcion:')
            funcion_elegida = funcion_elegida.split(":")
            hora = int(funcion_elegida[0])
            minuto = int(funcion_elegida[1])
            for keys,values in cine.listar_funciones(pelicula_elegida).items():
                if(values.hora==hora and values.minuto==minuto):
                    funcion_elegida=keys
                    valid = True
                    break;


        cantidad_entradas = input('Ingrese cantidad de entradas: ')

        conn = Coneccion()
        entrada = conn.anadir_entrada(pelicula_elegida, funcion_elegida, cantidad_entradas)
        #entrada = Entrada(len(cine.listar_entradas(pelicula_elegida, funcion_elegida))+1, pelicula_elegida, funcion_elegida, cantidad_entradas)
        cine.guardar_entrada(entrada)
        print('Se realizó la compra de la entrada. Código es {}'.format(entrada.entrada_id))

def main():
    
    cineManager = CineManager() 
    cineManager.gestionar()



if __name__ == '__main__':
    main()
