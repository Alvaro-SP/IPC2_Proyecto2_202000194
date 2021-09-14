import os
#!OBJETOS
class linea:
    def __init__(self, id, numero, cantidad, tiempo): #el self es como el this de java, indicandole que los atributos pertenecen a esa clase
        self.id = id
        self.numero = numero
        self.cantidad = cantidad
        self.tiempo = tiempo
        
class Nodo_linea:
    def __init__(self, linea = None, siguiente = None, anterior=None):
        self.linea = linea
        self.siguiente = siguiente
        self.anterior = anterior

class Lista_dobleenlazada_lineas:
    def __init__(self):
        self.primera_linea = None
    
    def insertar(self, linea):
        if self.primera_linea is None:
            self.primera_linea = Nodo_linea(linea = linea)
        else:
            linea_actual = Nodo_linea(linea=linea, siguiente=self.primera_linea) 
            self.primera_linea.anterior = linea_actual
            self.primera_linea=linea_actual
    
    def recorrer(self):
        if self.primera_linea is None:
            print("List has no element")
            return
        linea_actual=self.primera_linea
        print("Número de línea: ", linea_actual.linea.numero, "Cantidad de componentes: ", linea_actual.linea.cantidad, "Tiempo de Ensamblaje: ", linea_actual.linea.tiempo, "-->")
        while linea_actual.siguiente:
            linea_actual=linea_actual.siguiente
            print("Número de línea: ", linea_actual.linea.numero, "Cantidad de componentes: ", linea_actual.linea.cantidad, "Tiempo de Ensamblaje: ", linea_actual.linea.tiempo, "-->")
    
    def cantidad_lineasproduccion(self):
        contador_lineas=0
        if self.primera_linea is None:
            return
        linea_actual=self.primera_linea
        contador_lineas+=1
        while linea_actual.siguiente:
            linea_actual=linea_actual.siguiente
            contador_lineas+=1
        return contador_lineas
    
    def buscar_linea(self, numero):
        linea_actual=self.primera_linea
        while linea_actual is not None:
            if int(linea_actual.linea.numero)==int(numero):          
                return True
            else:
                linea_actual=linea_actual.siguiente
        return False
    
        
    
    def procesar_ruta(self, nombre):
        terreno_actual = self.primer_terreno
        while terreno_actual and terreno_actual.terreno.nombre.lower() != nombre.lower():
            terreno_actual = terreno_actual.siguiente
        if terreno_actual is None:
            print("--> No se ha encontrado el terreno", nombre + "\n")
        else:
            print("\n-> Datos del terreno:")
            print("Nombre:", terreno_actual.terreno.nombre, "  Dimensiones:", str(terreno_actual.terreno.filas), "x", str(terreno_actual.terreno.columnas))
            print("Inicio:", str(terreno_actual.terreno.inicio_x) + ",", str(terreno_actual.terreno.inicio_y), "  Fin:", str(terreno_actual.terreno.fin_x) + ",", str(terreno_actual.terreno.fin_y))
            if terreno_actual.terreno.inicio_x == terreno_actual.terreno.fin_x and terreno_actual.terreno.inicio_y == terreno_actual.terreno.fin_y:
                gas = terreno_actual.terreno.lista_casillas.obtener_gasolina(terreno_actual.terreno.fin_x, terreno_actual.terreno.fin_y)
                if gas is not None:
                    print("Las posiciones de inicio y fin coinciden, por lo que el robot no se desplaza.\n")
                else:
                    print("Las posiciones de inicio y fin coinciden, pero no se encuentran dentro de la matriz del terreno", terreno_actual.terreno.nombre + "\n")
            else:
                terreno_actual.terreno.lista_casillas.marcado_casillas(terreno_actual.terreno.filas, terreno_actual.terreno.columnas)
                terreno_actual.terreno.lista_casillas.escribir_ruta()
                print("\n-> Ruta mas optima:")
                for i in range(terreno_actual.terreno.filas):
                    fila = ""
                    for j in range(terreno_actual.terreno.columnas):
                        id_actual = terreno_actual.terreno.lista_casillas.obtener_ID(i + 1, j + 1)
                        camino = str(terreno_actual.terreno.lista_casillas.obtener_camino(id_actual))
                        fila = fila + "[ " + camino + " ]  "
                    print(fila)
                print("")
                print("-> Gasolina requerida para la ruta:")
                print(str(terreno_actual.terreno.lista_casillas.gasolina_total()) + " unidades")
                if terreno_actual.terreno.lista_casillas.gasolina_total() <= 9999:
                    print("-> La ruta encontrada es factible para r2e2. No consume más de 9999 unidades.\n")
                else:
                    print("-> La ruta encontrada NO es factible para r2e2. Esta consume más de su capacidad (9999 unidades).\n")

    def archivo_salida(self, nombre):
        terreno_actual = self.primer_terreno
        while terreno_actual and terreno_actual.terreno.nombre.lower() != nombre.lower():
            terreno_actual = terreno_actual.siguiente
        if terreno_actual is None:
            print("--> No se ha encontrado el terreno", nombre + "\n")
        else:
            terreno_actual.terreno.lista_casillas.marcado_casillas(terreno_actual.terreno.filas, terreno_actual.terreno.columnas)
            terreno_actual.terreno.lista_casillas.escribir_ruta()
            terreno_actual.terreno.lista_casillas.crear_xml_salida(terreno_actual.terreno.nombre, terreno_actual.terreno.inicio_x, terreno_actual.terreno.inicio_y, terreno_actual.terreno.fin_x, terreno_actual.terreno.fin_y, terreno_actual.terreno.lista_casillas.gasolina_total(), terreno_actual.terreno.filas, terreno_actual.terreno.columnas)
    
    def graficar_terreno(self, nombre):
        terreno_actual = self.primer_terreno
        while terreno_actual and terreno_actual.terreno.nombre.lower() != nombre.lower():
            terreno_actual = terreno_actual.siguiente
        if terreno_actual is None:
            print("--> No se ha encontrado el terreno", nombre + "\n")
        else:
            print("\n-> Datos del terreno:")
            print("Nombre:", terreno_actual.terreno.nombre, "  Dimensiones:", terreno_actual.terreno.filas, "x", terreno_actual.terreno.columnas)
            dot_creado = terreno_actual.terreno.lista_casillas.crear_grafica(terreno_actual.terreno.nombre, terreno_actual.terreno.filas, terreno_actual.terreno.columnas)
            if dot_creado is True:
                print("\n--> Archivo .dot creado exitosamente. Ver: Graficas DOT - PNG")
                try:
                    os.chdir('Graficas DOT - PNG')
                    os.system('dot -Tpng ' + terreno_actual.terreno.nombre + '.dot -o ' + terreno_actual.terreno.nombre + '.png')
                    os.chdir('..')
                    print("--> Archivo .png creado exitosamente. Ver: Graficas DOT - PNG\n")
                except:
                    print("\n--> Ocurrió un error en la creación del archivo .png :(\n")
            else:
                print("\n--> Ocurrió un error en la creación del archivo .dot :(\n")
