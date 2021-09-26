
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

#! Lista de donde se guarda la Línea y el valor del tiempo de ensamblaje
class NODO_lineaensamblajeTime:
    def __init__(self,  linea = None, tiempo=None , siguiente = None):
        self.linea=linea
        self.tiempo=tiempo
        self.siguiente = siguiente

class lista_ComponenteDeLinea:
    def __init__(self):
        self.cabezalinea2 = None
        self.siguiente=None
        self.anterior=None
        self.abajo=None
        self.arriba=None

    def insertar_ComponenteDeLinea(self, linea, tiempo):
        if self.cabezalinea2 is None:
            self.cabezalinea2=NODO_lineaensamblajeTime(linea=linea, tiempo=tiempo)
            return
        linea_actual=self.cabezalinea2
        while linea_actual.siguiente:
            linea_actual=linea_actual.siguiente
        linea_actual.siguiente=NODO_lineaensamblajeTime(linea=linea, tiempo=tiempo)

    def recorrer_ComponenteDeLinea(self):
        if self.cabezalinea2 is None:
            print("List has no element")
            return
        linea_actual=self.cabezalinea2
        print("La línea: ", linea_actual.linea, "   tiempo : ", linea_actual.tiempo,"-->")
        while linea_actual.siguiente:
            linea_actual=linea_actual.siguiente
            print("La línea: ", linea_actual.linea, "   tiempo : ", linea_actual.tiempo,"-->")

    def buscar_ComponenteDeLinea(self, linea):
        linea_actual=self.cabezalinea2
        if linea_actual is None:
            return "estavacio"
        while linea_actual is not None:
            if int(linea_actual.linea)  ==int(linea) :
                return int(linea_actual.tiempo)
            else:
                linea_actual=linea_actual.siguiente
        return False
