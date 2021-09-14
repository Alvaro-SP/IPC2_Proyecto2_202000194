
#!OBJETOS
class producto:
    def __init__(self, nombre, elaboracion): #el self es como el this de java, indicandole que los atributos pertenecen a esa clase
        
        self.nombre = nombre
        self.elaboracion = elaboracion

class ensamblaje:
    def __init__(self, line, component):
        self.line = line
        self.component = component

#! Lista en listas de PRODUCTOS tienen ENSAMBLES como lista dobleenlazada en cascada
class Node: 
    def __init__(self, id=None, producto = None, siguiente = None,anterior=None, abajo=None, arriba=None):
        self.id=id
        self.producto = producto
        self.siguiente = siguiente
        self.anterior=anterior
        self.abajo = abajo
        self.arriba=arriba

class NodeLista: 
    def __init__(self, ensamblaje= None, arriba = None, abajo=None):
        self.ensamblaje = ensamblaje
        self.arriba=arriba
        self.abajo = abajo


class listaProductos:
    def __init__(self):
        self.cabecera = None
        self.siguiente=None
        self.anterior=None
        self.abajo=None
        self.arriba=None

    def insertar_products(self, id, producto):
        if self.cabecera: 
            primer_producto = self.cabecera
            while primer_producto.siguiente != None:
                primer_producto = primer_producto.siguiente

            producto_actual=Node(id=id, producto=producto, siguiente=self.cabecera)
            self.cabecera.anterior = producto_actual
            self.primer_producto=producto_actual

            # self.cabecera.anterior=producto_actual.anterior
            # primer_producto.next = Node(id=id, producto=producto , anterior=producto_actual)
            self.cabecera=producto_actual
            
        else: 
            producto_actual=Node(id=id, producto=producto)
            self.cabecera = producto_actual
            # self.cabecera.anterior=producto_actual
                
    def recorrer(self):
        if self.cabecera is None:
            print("List has no element")
            return
        producto_actual=self.cabecera
        print("ID del producto: ", producto_actual.id, "   Nombre : ", producto_actual.producto,"-->")
        while producto_actual.siguiente:
            producto_actual=producto_actual.siguiente
            print("ID del producto: ", producto_actual.id, "   Nombre : ", producto_actual.producto,"-->")
    
    def cantidad_productos(self):
        contador_productos=0
        if self.cabecera is None:
            return
        producto_actual=self.cabecera
        contador_productos+=1
        while producto_actual.siguiente:
            producto_actual=producto_actual.siguiente
            contador_productos+=1
        return contador_productos

    def buscar_producto(self, nombre):
        producto_actual=self.cabecera
        while producto_actual is not None:
            if producto_actual.producto.lower() ==nombre.lower():          
                return True
            else:
                producto_actual=producto_actual.siguiente
        return False
   
    def return_idyproducto(self, name):
        producto_actual=self.cabecera
        while producto_actual is not None:
            if  producto_actual.producto.lower() ==name.lower():      
                return producto_actual
            else:
                producto_actual=producto_actual.siguiente
        return False
                 
#! Lista en listas
class listaEnsambles:
    def __init__(self):
        self.cabecera = None
        self.abajo = None
    
    def insertar_ensambles(self,id,lista,ensamblaje):
        listaCabecera = lista.cabecera

        while listaCabecera.id != int(id):
            listaCabecera = listaCabecera.siguiente

        listaX = listaCabecera

        while listaX.abajo != None:
            listaX = listaX.abajo

        if listaX:
            ultimo = listaX
            while ultimo.abajo != None:
                ultimo = ultimo.abajo
            ultimo.abajo = NodeLista(ensamblaje=ensamblaje)
        else:
            listaX = NodeLista(ensamblaje=ensamblaje)
            listaX.abajo = NodeLista(ensamblaje=ensamblaje)

    def mostrar_ensambles(self,lista,id):
        try: 
            listaCabecera = lista.cabecera 
            while listaCabecera.id != int(id):
                listaCabecera = listaCabecera.siguiente

            listaanterior=listaCabecera.siguiente
            listasiguiente=listaCabecera.anterior 
            if listaCabecera:
                print('El producto es: ',listaCabecera.producto)
            else:
                print('list index out of range')
            if listaanterior:
                print('El producto anterior es: ',listaanterior.producto)
            else:
                print('El producto anterior es: Null')
            
            if listasiguiente:
                print('El producto siguiente es: ',listasiguiente.producto)
            else:
                print('El producto siguiente es: Null')
            
            temp = listaCabecera.abajo
            print('Las Líneas y sus Ensambles son: ')
            while temp != None:
                print(temp.ensamblaje.line, " con ", temp.ensamblaje.component, end='->')
                temp = temp.abajo

            print('Null')
        except Exception as e:
            print("List index out of range :( ")
            print(e)


#! Lista Doble enlazada de los productos y sus ensamblajes
class Nodo_producto:
    def __init__(self, producto = None, siguiente = None, anterior=None):
        self.producto = producto
        self.siguiente = siguiente
        self.anterior = anterior

class Lista_dobleenlazada_producto:
    def __init__(self):
        self.primer_producto = None
        self.primer_ensamblaje = None
    
    def insertar(self, producto):
        if self.primer_producto is None:
            self.primer_producto = Nodo_producto(producto = producto)
        else:
            producto_actual = Nodo_producto(producto=producto, siguiente=self.primer_producto) 
            self.primer_producto.anterior = producto_actual
            self.primer_producto=producto_actual

    def recorrer(self):
        if self.primer_producto is None:
            print("List has no element")
            return
        producto_actual=self.primer_producto
        print("Nombre del producto: ", producto_actual.producto.nombre, "Elaboracion: ", producto_actual.producto.elaboracion,"-->")
        while producto_actual.siguiente:
            producto_actual=producto_actual.siguiente
            print("Nombre del producto: ", producto_actual.producto.nombre, "Elaboracion: ", producto_actual.producto.elaboracion,"-->")
    
    def cantidad_productos(self):
        contador_productos=0
        if self.primer_producto is None:
            return
        producto_actual=self.primer_producto
        contador_productos+=1
        while producto_actual.siguiente:
            producto_actual=producto_actual.siguiente
            contador_productos+=1
        return contador_productos

    def buscar_producto(self, nombre):
        producto_actual=self.primer_producto
        while producto_actual is not None:
            if producto_actual.producto.nombre.lower() ==nombre.lower():          
                return True
            else:
                producto_actual=producto_actual.siguiente
        return False
    def returnnombreyensamble(self, nombre):
        producto_actual=self.primer_producto
        while producto_actual is not None:
            if producto_actual.producto.nombre.lower() ==nombre.lower():          
                return producto_actual
            else:
                producto_actual=producto_actual.siguiente
        return False
    
    
    

        
        
      

        
    