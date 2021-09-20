
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

    def buscar_tiempo_linea(self, numero):
        linea_actual=self.primera_linea
        while linea_actual is not None:
            if int(linea_actual.linea.numero)==int(numero):          
                return linea_actual.linea.tiempo
            else:
                linea_actual=linea_actual.siguiente
        return False