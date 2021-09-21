from PyQt5 import QtCore, QtGui, QtWidgets
from productos import *
from lineas import *
from ventana import *
import ventana
import loadfile
import os

#?▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
#!OBJETOS
class producto:
    def __init__(self, nombre, elaboracion): #el self es como el this de java, indicandole que los atributos pertenecen a esa clase
        
        self.nombre = nombre
        self.elaboracion = elaboracion
class ensamblaje:
    def __init__(self, line, component):
        self.line = line
        self.component = component

#?▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
#! Lista en listas de PRODUCTOS tienen ENSAMBLES como lista dobleenlazada en cascada
class Node: 
    def __init__(self, id=None, producto = None, siguiente = None,anterior=None, abajo=None,arriba=None):
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
    
    def addcombobox(self, iditem, nameitem):

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Codigo Fuente/images/Gear1.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                              
        ventana.combo.addItem(icon1,str(nameitem))
    def addcombobox2(self, iditem, nameitem):

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Codigo Fuente/images/descargar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                              
        ventana.combo2.addItem(icon1,str(nameitem))
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

    def llenarListaLineas(self, Product_a_optimizar,nameproducto):
        # try: 
        listalista_lineas=lista_Linea()
        listalista_componentes=lista_Componente()
        listaCabecera = Product_a_optimizar.cabecera 
        while listaCabecera.producto != str(nameproducto):
            listaCabecera = listaCabecera.siguiente
        print(listaCabecera.producto)
        cont=0
        temp = listaCabecera.abajo
        while temp != None:
            print(temp.ensamblaje.line, " con ", temp.ensamblaje.component, end='->')

            listalista_lineas.insertar_lineas(cont, temp.ensamblaje.line)
            listalista_componentes.insertar_componente(cont, listalista_lineas, temp.ensamblaje.component)
            cont+=1
            temp = temp.abajo
        print('Null')
        listalista_componentes.calculoTiempoOptimizado(listalista_lineas, listalista_componentes)
        # except Exception as e:
        #     print("List index out of range :( ")
        #     print(e)  

    def generarGRAPHVIZ(self, lista, producto):
       
        listaCabecera = lista.cabecera 
        while listaCabecera.producto != str(producto):
            listaCabecera = listaCabecera.siguiente
        if listaCabecera:
            print('El producto es: ',listaCabecera.producto)
        else:
            print('list index out of range')
        productotext= str(listaCabecera.producto).strip()
        graphtext="""
        digraph grid{	               
            layout=dot   
            fontcolor="black" 
            label=" """+str(listaCabecera.producto)+"""  " 
            labelloc = "t"
            bgcolor="yellow:orange"                
            edge [weight=1000 style=bold color=black]
            node[shape=square style="filled"  color="green:cyan" gradientangle="315"]
            \n
            rank=same{"""
        temp = listaCabecera.abajo       
        while temp != None:
            print(temp.ensamblaje.line, " con ", temp.ensamblaje.component, end='->')
            Nodotext="L"+str(temp.ensamblaje.line)+"C"+str(temp.ensamblaje.component)
            graphtext+=str(Nodotext)+"->"
            temp = temp.abajo
        print('Null')
        try:
            graphtext=graphtext.rstrip(graphtext[-1])
            graphtext=graphtext.rstrip(graphtext[-1])
            graphtext+="""}}"""
            productotext=productotext.replace(" ","")           
            file=open('Graficos_generados/Grafico_'+str(productotext)+'.dot','w')
            file.write(graphtext)
            file.close()
            os.system('dot -Tpng Graficos_generados/Grafico_'+str(productotext)+'.dot -o Graficos_generados/graficoimagen_'+str(productotext)+'.png')
            os.startfile(r"Graficos_generados\graficoimagen_"+str(productotext)+".png")
            print("\033[1;32m"+"\nSe ha generado el gráfico" +str(productotext)+ "con éxito... \n"+'\033[0;m')
        except Exception:
            print("\033[1;31m"+"\nUps... algo salió mal :( podria haber un error, intentelo nevamente\n"+'\033[0;m')     
            return False

#?▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
# *▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▄▀▄   LINEA - COMPONENTE  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
#! Lista en listas de LINEAS tienen COMPONENTES como lista dobleenlazada en cascada
class NODO_Linea: 
    def __init__(self,  id=None , linea = None, siguiente = None,anterior=None, abajo=None,abajoensamblo=None,abajoquedo=None,  arriba=None,arribaquedo=None,arribaensamblo=None):
        self.id=id         
        self.linea=linea         
        self.siguiente = siguiente
        self.anterior=anterior
        self.abajo = abajo        
        self.abajoquedo=abajoquedo
        self.abajoensamblo=abajoensamblo
        self.arriba=arriba
        self.arribaquedo=arribaquedo
        self.arribaensamblo=arribaensamblo
class NODO_Componente:
    def __init__(self, componente= None, arriba = None, abajo=None):
        self.componente = componente
        self.arriba=arriba
        self.abajo = abajo

class lista_Linea:
    def __init__(self):
        self.lineascabeza = None
        self.siguiente=None
        self.anterior=None
        self.abajo=None
        self.arriba=None

    def insertar_lineas(self, id, linea):
        if self.lineascabeza is None:
            self.lineascabeza=NODO_Linea(id=id, linea=linea)
            return
        linea_actual=self.lineascabeza
        while linea_actual.siguiente:
            linea_actual=linea_actual.siguiente
        linea_actual.siguiente=NODO_Linea(id=id, linea=linea)

    def recorrer_lineas(self):
        if self.lineascabeza is None:
            print("List has no element")
            return
        linea_actual=self.lineascabeza
        print("ID del producto: ", linea_actual.id, "   Nombre : ", linea_actual.linea,"-->")
        while linea_actual.siguiente:
            linea_actual=linea_actual.siguiente
            print("ID del producto: ", linea_actual.id, "   Nombre : ", linea_actual.linea,"-->")

    def cantidad_lineas(self):
        contador_lineas=0
        if self.lineascabeza is None:
            return
        linea_actual=self.lineascabeza
        contador_lineas+=1
        while linea_actual.siguiente:
            linea_actual=linea_actual.siguiente
            contador_lineas+=1
        return contador_lineas

    def buscar_linea(self, linea):
        linea_actual=self.lineascabeza
        while linea_actual is not None:
            if linea_actual.linea  ==linea :          
                return True
            else:
                linea_actual=linea_actual.siguiente
        return False

    def buscar_lineapor_id(self, id):
        linea_actual=self.lineascabeza
        while linea_actual is not None:
            if int(linea_actual.id)  ==int(id) :
                return linea_actual.linea
            else:
                linea_actual=linea_actual.siguiente
        return False

    def buscar_sig_actual(self, id):
        linea_actual=self.lineascabeza
        linearetornada=self.buscar_lineapor_id(id)
        while linea_actual is not None:
            if int(linea_actual.id)  == int(id): 
                linea_actual=linea_actual.siguiente
                while   linea_actual is not None:
                    if int(linea_actual.linea)  == int(linearetornada):
                        # print("producto encontrado siguiente: ", linea_actual.linea)
                        return True, linea_actual.linea, linea_actual.id
                    else:
                        linea_actual=linea_actual.siguiente
            if linea_actual is not None:
                linea_actual=linea_actual.siguiente
        return False, None, None

    def return_idylinea(self, name):
        linea_actual=self.lineascabeza
        while linea_actual is not None:
            if  int(linea_actual.linea ) == int(name) :      
                return linea_actual
            else:
                linea_actual=linea_actual.siguiente
        return False

#todo Lista en listas de lineas
class lista_Componente:
    def __init__(self):
        self.lineascabeza = None
        self.abajo = None
        self.abajoquedo=None
        self.abajoensamblo=None

    def insertar_componente(self,id,lista,componente):
        listaComponentecabeza = lista.lineascabeza

        while listaComponentecabeza.id != int(id):
            listaComponentecabeza = listaComponentecabeza.siguiente

        listaX = listaComponentecabeza

        while listaX.abajo != None:
            listaX = listaX.abajo

        if listaX:
            ultimo = listaX
            while ultimo.abajo != None:
                ultimo = ultimo.abajo
            ultimo.abajo = NODO_Componente(componente=componente)
        else:
            listaX = NODO_Componente(componente=componente)
            listaX.abajo = NODO_Componente(componente=componente)

    def insertar_dondesequedo(self,id,lista,dondesequedo):
        listaComponentecabeza = lista.lineascabeza

        while listaComponentecabeza.id != int(id):
            listaComponentecabeza = listaComponentecabeza.siguiente

        listaX = listaComponentecabeza

        while listaX.abajoquedo != None:
            listaX = listaX.abajoquedo

        if listaX:
            ultimo = listaX
            while ultimo.abajoquedo != None:
                ultimo = ultimo.abajoquedo
            ultimo.abajoquedo = NODO_Dondesequedo(dondesequedo=dondesequedo)
        else:
            listaX = NODO_Dondesequedo(dondesequedo=dondesequedo)
            listaX.abajoquedo = NODO_Dondesequedo(dondesequedo=dondesequedo)

    def insertar_yaseensamblo(self,id,lista,yaseensamblo):
        listaComponentecabeza = lista.lineascabeza

        while listaComponentecabeza.id != int(id):
            listaComponentecabeza = listaComponentecabeza.siguiente

        listaX = listaComponentecabeza

        while listaX.abajoensamblo != None:
            listaX = listaX.abajoensamblo

        if listaX:
            ultimo = listaX
            while ultimo.abajoensamblo != None:
                ultimo = ultimo.abajoensamblo
            ultimo.abajoensamblo = NODO_Yaseensamblo(yaseensamblo=yaseensamblo)
        else:
            listaX = NODO_Yaseensamblo(yaseensamblo=yaseensamblo)
            listaX.abajoensamblo = NODO_Yaseensamblo(yaseensamblo=yaseensamblo)

    def mostrar_componentes(self,lista,id):
        try:
            listaComponentecabeza = lista.lineascabeza
            while listaComponentecabeza.id != int(id):
                listaComponentecabeza = listaComponentecabeza.siguiente
            if listaComponentecabeza:
                print('La línea es: ',listaComponentecabeza.linea)
            temp = listaComponentecabeza.abajo
            print('Los Componentes son: ')
            while temp != None:
                print(temp.componente, end='->')
                temp = temp.abajo
            print('Null')
        except Exception as e:
            print("List index out of range :( ")
            print(e)

    def mostrar_dondesequedo(self,lista,id):
        try: 
            listaComponentecabeza = lista.lineascabeza 
            while listaComponentecabeza.id != int(id):
                listaComponentecabeza = listaComponentecabeza.siguiente
            if listaComponentecabeza:
                print('La línea es: ',listaComponentecabeza.linea)            
            temp = listaComponentecabeza.abajoquedo
            print('Los Componentes son: ')
            while temp != None:
                print(temp.componente, end='->')
                temp = temp.abajoquedo

            print('Null')
        except Exception as e:
            print("List index out of range :( ")
            print(e)

    def mostrar_yaseensamblo(self,lista,id):
        try: 
            listaComponentecabeza = lista.lineascabeza 
            while listaComponentecabeza.id != int(id):
                listaComponentecabeza = listaComponentecabeza.siguiente            
            if listaComponentecabeza:
                print('La línea es: ',listaComponentecabeza.linea)            
            temp = listaComponentecabeza.abajoensamblo
            print('Los Componentes son: ')
            while temp != None:
                print(temp.componente, end='->')
                temp = temp.abajoensamblo
            print('Null')
        except Exception as e:
            print("List index out of range :( ")
            print(e)

    def buscar_componente(self,lista, nombre, hijo):
        producto_actual=lista.cabecera
        while producto_actual is not None:
            if producto_actual.producto.nombre.lower() ==nombre.lower(): 
                temp = producto_actual.abajoh 
                if int(temp.hijo)  ==int(hijo) :
                    print("EL HIJO ES: ", temp.hijo)
                    return int(temp.hijo)
            else:
                producto_actual=producto_actual.siguiente
        return False

    def cantidad_componente(self,lista, id):
        # try:
        listaComponentecabeza = lista.lineascabeza
        contador_componente=0
        while listaComponentecabeza.id != int(id):
            listaComponentecabeza = listaComponentecabeza.siguiente
        temp = listaComponentecabeza.abajo
        contador_componente+=1
        while temp != None:
            temp = temp.abajo
            contador_componente+=1
        return contador_componente
        # except Exception as e:
        #     print("List index out of range :( ")
        #     print(e)

    def return_idycomponente(self, lista, id):
        listaComponentecabeza=lista.lineascabeza
        while listaComponentecabeza.id != int(id):
                listaComponentecabeza = listaComponentecabeza.siguiente
        temp = listaComponentecabeza
        return temp

    def calculoTiempoOptimizado(self, lista, listcomponent):
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        Lista_lineatodos_duplicado=lista_lineasduplicadas() #todas las lineas a de ensamble duplicadas
        Lista_Dondequedo=lista_Dondesequedo() #temporales en donde quedo de ultimo
        lista_Yaensamblo=lista_Yaseensamblo() #temporales si ya se ensamblo o no
        Lista_Linea_Resultados=loadfile.Lista_Linea_Resultados
        Lista_Compo_Resultados=loadfile.Lista_Compo_Resultados
        listaMadre1=lista.lineascabeza
        longitud_resultado=0
        #se llena la lista que contendrá el #todo resultado de las operaciones
        contadorinsercion=0
        while listaMadre1 != None:
            if not Lista_Linea_Resultados.buscar_linea(listaMadre1.linea):
                Lista_Linea_Resultados.insertar_lineas(contadorinsercion,listaMadre1.linea)
                Lista_Dondequedo.insertar_dondesequedo(listaMadre1.linea,1)#INICIA en 1 porque este en 1
                lista_Yaensamblo.insertar_yaseensamblo(listaMadre1.linea,"primero")#INICIA en False porque nadie se ha ensamblado
                longitud_resultado+=1
                contadorinsercion+=1
            listaMadre1=listaMadre1.siguiente
        #se llena la lista duplicada de lineas y sus componentes para el proceso
        Lista_Dondequedo.recorrer_lineas()
        listaMadre2=lista.lineascabeza
        while listaMadre2 != None:
            temporalcomponentdupli=listaMadre2.abajo
            Lista_lineatodos_duplicado.insertar_lineascomponenteduplicados(listaMadre2.linea,temporalcomponentdupli.componente )
            listaMadre2=listaMadre2.siguiente

        listaMadre=lista.lineascabeza
        while listaMadre!=None: #!RECORRE LA LISTA MADRE DE TODOS
            obtain_sequedo= int(Lista_Dondequedo.buscar_dondesequedo(listaMadre.linea))
            obtain_seensaamblo=lista_Yaensamblo.buscar_yaseensamblo(listaMadre.linea)
            tiempo_ensamble =  loadfile.lista_lineasprod.buscar_tiempo_linea(listaMadre.linea)
            temporalcomponent=listaMadre.abajo
            lineaMayor=listaMadre.linea
            componente_a_llegar = int(temporalcomponent.componente)
            cont=0
            print("Componente a llegar: " + str(componente_a_llegar))
            print("Donde se quedo : " + str(obtain_sequedo))
            if obtain_sequedo < componente_a_llegar:
                while obtain_sequedo <componente_a_llegar: # si quedo es menor a llegar se suma hasta que se igualen
                    obtain_sequedo+=1
                    cont+=1
            elif obtain_sequedo > componente_a_llegar: 
                while obtain_sequedo > componente_a_llegar: # si quedo es mayor a llegar se resta uno hasta que se igualen
                    obtain_sequedo-=1
                    cont+=1

            correrfilas= int(cont)+int(tiempo_ensamble)#cantidad de filas que recorrerá cada lista actual
            print("     ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬    correrfilas: ", correrfilas)
            print("             tiempoensamble: ", tiempo_ensamble)
            print("             contador: ", cont)
            listaactual=Lista_Linea_Resultados.lineascabeza
            correrfilas1=int(cont)+int(tiempo_ensamble)
            # print("☻☻☻☻☻☻☻☻☻☻☻☻    componente a llegar: ",componente_a_llegar, "lineaMayor: ", lineaMayor, " Donde se quedó: ", obtain_sequedo)
            while listaactual!= None: #!RECORRE LA LISTA DE RESULTADOS
                lineaactual=listaactual.linea
                idlineaactual=listaactual.id
                haylineasiguiente, lineasiguiente, idlineasiguiente=lista.buscar_sig_actual(idlineaactual)
                if lineasiguiente!=None:
                    componente_a_llegar_next=Lista_lineatodos_duplicado.buscar_componentedelineaduplicados(lineasiguiente)
                else:
                    componente_a_llegar_next=False
                obtain_sequedo2=Lista_Dondequedo.buscar_dondesequedo(lineaactual)                 
                # print("OBTAIN SEQUEDO 2: ", obtain_sequedo2, "Componente a llegar next: ", componente_a_llegar_next, "componente_allegar: ", componente_a_llegar)

                if   int(lineaactual) == int(lineaMayor) and  lista_Yaensamblo.buscar_yaseensamblo(lineaactual)=="primero":# and lista_Yaensamblo.buscar_yaseensamblo(lineaactual):
                    lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                    iteration=0
                    if obtain_sequedo2 < componente_a_llegar:
                        while obtain_sequedo2 <= componente_a_llegar and iteration!=correrfilas1:
                            Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                            obtain_sequedo2+=1
                            Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                            lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                            iteration+=1
                        while iteration!=correrfilas1:
                            Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                            lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                            # Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2-1)
                            iteration+=1
                        Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                        lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                        # Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2-1)
                    else:
                        while obtain_sequedo2 >= componente_a_llegar and iteration!=correrfilas1:
                            Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                            obtain_sequedo2-=1
                            Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                            lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                            iteration+=1
                        while iteration!=correrfilas1:
                            Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                            lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                            # Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2-1)
                            iteration+=1
                        Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                        lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)

                elif int(lineaactual) != int(lineaMayor) and  lista_Yaensamblo.buscar_yaseensamblo(lineaactual)=="primero":
                    lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                    iteration=0
                    if obtain_sequedo2 < componente_a_llegar_next and componente_a_llegar_next!=False:
                        while obtain_sequedo2 <= componente_a_llegar_next and iteration!=correrfilas1:
                            Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                            obtain_sequedo2+=1
                            Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                            lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                            iteration+=1
                        while iteration!=correrfilas1:
                            Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                            iteration+=1
                        Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")

                    elif obtain_sequedo2 > componente_a_llegar_next and componente_a_llegar_next!=False:
                        while obtain_sequedo2 >= componente_a_llegar_next and iteration!=correrfilas1:
                            Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                            obtain_sequedo2-=1
                            Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                            lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                            iteration+=1
                        while iteration!=correrfilas1:
                            Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                            iteration+=1
                        Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                    elif componente_a_llegar_next==False:
                        componente_a_llegar_actual=Lista_lineatodos_duplicado.buscar_componentedelineaduplicados(lineaactual)
                        while obtain_sequedo2 <= componente_a_llegar_actual and iteration!=correrfilas1:
                            Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                            obtain_sequedo2+=1
                            Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                            lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                            iteration+=1
                        while iteration!=correrfilas1:
                            Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                            iteration+=1
                        Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")



                        # for iteration in range(correrfilas):
                        #     if obtain_sequedo2 <= componente_a_llegar_next:
                        #         Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                        #         obtain_sequedo2+=1
                        #         Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                        #         lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                        #     elif obtain_sequedo2 >= componente_a_llegar_next:
                        #         Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                        #         obtain_sequedo2-=1
                        #         Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                        #         lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                        #     else:
                        #         Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")

                elif int(lineaactual) != int(lineaMayor):
                    if   haylineasiguiente==True  and lista_Yaensamblo.buscar_yaseensamblo(lineaactual)==True:
                        iteration=0
                        if obtain_sequedo2 < componente_a_llegar_next and componente_a_llegar_next!=False:
                            while obtain_sequedo2 <= componente_a_llegar_next and iteration!=correrfilas:
                                Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                                obtain_sequedo2+=1
                                Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                                lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                                iteration+=1
                            while iteration!=correrfilas:
                                Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                                iteration+=1
                            # Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")

                        elif obtain_sequedo2 > componente_a_llegar_next and componente_a_llegar_next!=False:
                            while obtain_sequedo2 >= componente_a_llegar_next and iteration!=correrfilas:
                                Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                                obtain_sequedo2-=1
                                Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                                lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                                iteration+=1
                            while iteration!=correrfilas:
                                Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                                iteration+=1
                        elif componente_a_llegar_next==False:
                            componente_a_llegar_actual=Lista_lineatodos_duplicado.buscar_componentedelineaduplicados(lineaactual)

                            if obtain_sequedo2 < componente_a_llegar_actual:
                                while obtain_sequedo2 <= componente_a_llegar_actual and iteration!=correrfilas:
                                    Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                                    obtain_sequedo2+=1
                                    Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                                    lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                                    iteration+=1
                                while iteration!=correrfilas:
                                    Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                                    iteration+=1
                                # Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")

                            elif obtain_sequedo2 > componente_a_llegar_actual:
                                while obtain_sequedo2 >= componente_a_llegar_actual and iteration!=correrfilas:
                                    Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                                    obtain_sequedo2-=1
                                    Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                                    lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                                    iteration+=1
                                while iteration!=correrfilas:
                                    Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                                    iteration+=1

                    elif haylineasiguiente==True  and lista_Yaensamblo.buscar_yaseensamblo(lineaactual)==False:
                        iteration=0
                        while iteration!=correrfilas:
                            Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                            iteration+=1

                    elif haylineasiguiente==False and lista_Yaensamblo.buscar_yaseensamblo(lineaactual)==False:
                        iteration=0
                        while iteration!=correrfilas:
                            Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                            iteration+=1
                    
                    elif haylineasiguiente==False and lista_Yaensamblo.buscar_yaseensamblo(lineaactual)==True:
                        iteration=0
                        while iteration!=correrfilas:
                            Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                            iteration+=1

                elif int(lineaactual) == int(lineaMayor):
                    if   haylineasiguiente==True  and lista_Yaensamblo.buscar_yaseensamblo(lineaactual)==True:
                        iteration=0
                        if obtain_sequedo2 < componente_a_llegar_next and componente_a_llegar_next!=False:
                            while obtain_sequedo2 <= componente_a_llegar_next and iteration!=correrfilas:
                                Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                                obtain_sequedo2+=1
                                Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                                lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                                iteration+=1
                            while iteration!=correrfilas:
                                Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                                lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                                # Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2-1)
                                iteration+=1
                            # Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                            # lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)

                        elif obtain_sequedo2 > componente_a_llegar_next and componente_a_llegar_next!=False:
                            while obtain_sequedo2 >= componente_a_llegar_next and iteration!=correrfilas:
                                Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                                obtain_sequedo2-=1
                                Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                                lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                                iteration+=1
                            while iteration!=correrfilas:
                                Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                                lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                                # Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2-1)
                                iteration+=1
                            # Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                            # lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)

                        elif componente_a_llegar_next==False:
                            componente_a_llegar_actual=Lista_lineatodos_duplicado.buscar_componentedelineaduplicados(lineaactual)

                            if obtain_sequedo2 < componente_a_llegar_actual:
                                while obtain_sequedo2 <= componente_a_llegar_actual and iteration!=correrfilas:
                                    Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                                    obtain_sequedo2+=1
                                    Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                                    lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                                    iteration+=1
                                while iteration!=correrfilas:
                                    Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                                    iteration+=1
                                # Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")

                            elif obtain_sequedo2 > componente_a_llegar_actual:
                                while obtain_sequedo2 >= componente_a_llegar_actual and iteration!=correrfilas:
                                    Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                                    obtain_sequedo2-=1
                                    Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                                    lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                                    iteration+=1
                                while iteration!=correrfilas:
                                    Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                                    iteration+=1

                    elif haylineasiguiente==True  and lista_Yaensamblo.buscar_yaseensamblo(lineaactual)==False:
                        iteration=0
                        while iteration!=correrfilas:
                            Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                            lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                            # Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2-1)
                            iteration+=1
                        # Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                        # lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)

                    elif haylineasiguiente==False and lista_Yaensamblo.buscar_yaseensamblo(lineaactual)==False:
                        iteration=0
                        while iteration!=correrfilas:
                            Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                            lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                            # Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2-1)
                            iteration+=1
                        # Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                        # lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)

                    elif haylineasiguiente==False and lista_Yaensamblo.buscar_yaseensamblo(lineaactual)==True:
                        iteration=0
                        while iteration!=correrfilas:
                            Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                            lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                            # Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2-1)
                            iteration+=1
                        # Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                        # lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)


                listaactual=listaactual.siguiente
            listaMadre = listaMadre.siguiente

        for idi in range(longitud_resultado):
            print("☻  ",Lista_Compo_Resultados.cantidad_componente(Lista_Linea_Resultados,idi))
            Lista_Compo_Resultados.mostrar_componentes(Lista_Linea_Resultados,idi)

        loadfile.Lista_Linea_Resultados=Lista_Linea_Resultados
        loadfile.Lista_Compo_Resultados=Lista_Compo_Resultados

#?▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
# ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▄▀▄   DOBLEENLAZADA PRODUCTO   ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
class Tiempoalinear:
    def __init__(self):
        self.tiempoinicial=0
    def guardartiempoalinear(self, tiempo):
        self.tiempoinicial=tiempo 
    def obtenertiempoinicial(self):
        return self.tiempoinicial
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

#?▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
# ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▄▀▄   AUXILIARES ELEMENTOS   ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
#! Lista de donde se quedo el MOVIMIENTO POR LÍNEA simple enlazada
class NODO_Dondesequedo:
    def __init__(self,  linea = None, sequedo=None , siguiente = None):
        self.linea=linea
        self.sequedo=sequedo
        self.siguiente = siguiente

class lista_Dondesequedo:
    def __init__(self):
        self.cabezaquedo = None
        self.siguiente=None
        self.anterior=None
        self.abajo=None
        self.arriba=None

    def insertar_dondesequedo(self, linea, sequedo):
        sequedo=int(sequedo)
        if self.cabezaquedo is None:
            self.cabezaquedo=NODO_Dondesequedo(linea=linea, sequedo=sequedo)
            return
        linea_actual=self.cabezaquedo
        while linea_actual.siguiente:
            linea_actual=linea_actual.siguiente
        linea_actual.siguiente=NODO_Dondesequedo(linea=linea, sequedo=sequedo)

    def actualizar_dondesequedo(self, linea, sequedo):
        linea_actual=self.cabezaquedo
        if linea_actual is None:
            return "estavacio"
        while linea_actual is not None:
            if int(linea_actual.linea)  ==int(linea):
                linea_actual.sequedo=int(sequedo)
                return
            else:
                linea_actual=linea_actual.siguiente
        return False

    def recorrer_lineas(self):
        if self.cabezaquedo is None:
            print("List has no element")
            return
        linea_actual=self.cabezaquedo
        print("La línea: ", linea_actual.linea, "   Se quedo en : ", linea_actual.sequedo,"-->")
        while linea_actual.siguiente:
            linea_actual=linea_actual.siguiente
            print("La línea: ", linea_actual.linea, "   Se quedo en : ", linea_actual.sequedo,"-->")

    def buscar_dondesequedo(self, linea):
        linea_actual=self.cabezaquedo
        if linea_actual is None:
            return "estavacio"
        while linea_actual is not None:
            if int(linea_actual.linea)  ==int(linea) :
                return int(linea_actual.sequedo)
            else:
                linea_actual=linea_actual.siguiente
        return False

#! Lista de donde se quedo el MOVIMIENTO POR LÍNEA simple enlazada
class NODO_Yaseensamblo:
    def __init__(self,  linea = None, yaseensamblo=None , siguiente = None):       
        self.linea=linea  
        self.yaseensamblo=yaseensamblo         
        self.siguiente = siguiente

class lista_Yaseensamblo:
    def __init__(self):
        self.cabezayaseensamblo = None
        self.siguiente=None
        self.anterior=None
        self.abajo=None
        self.arriba=None

    def insertar_yaseensamblo(self, linea, yaseensamblo):
        if self.cabezayaseensamblo is None:
            self.cabezayaseensamblo=NODO_Yaseensamblo(linea=linea, yaseensamblo=yaseensamblo)
            return
        linea_actual=self.cabezayaseensamblo
        while linea_actual.siguiente:
            linea_actual=linea_actual.siguiente
        linea_actual.siguiente=NODO_Yaseensamblo(linea=linea, yaseensamblo=yaseensamblo)

    def recorrer_lineas(self):
        if self.cabezayaseensamblo is None:
            print("List has no element")
            return
        linea_actual=self.cabezayaseensamblo
        print("La línea: ", linea_actual.linea, "   Ensamblado? : ", linea_actual.yaseensamblo,"-->")
        while linea_actual.siguiente:
            linea_actual=linea_actual.siguiente
            print("La línea: ", linea_actual.linea, "  Ensamblado? : ", linea_actual.yaseensamblo,"-->")

    def actualizar_yaseensamblo(self, linea, yaseensamblo):
        linea_actual=self.cabezayaseensamblo
        if linea_actual is None:
            return "estavacio"        
        while linea_actual is not None:
            if int(linea_actual.linea)  ==int(linea) :
                linea_actual.yaseensamblo=yaseensamblo
                return 
            else:
                linea_actual=linea_actual.siguiente
        return False                 

    def buscar_yaseensamblo(self, linea):
        linea_actual=self.cabezayaseensamblo
        if linea_actual is None:
            return "estavacio"
        while linea_actual is not None:
            if int(linea_actual.linea)  ==int(linea) :
                return (linea_actual.yaseensamblo)
            else:
                linea_actual=linea_actual.siguiente
        return False

#! Lista de donde se quedo el MOVIMIENTO POR LÍNEA simple enlazada
class NODO_lineasduplicadas:
    def __init__(self,  linea = None, componente=None , siguiente = None):
        self.linea=linea
        self.componente=componente
        self.siguiente = siguiente

class lista_lineasduplicadas:
    def __init__(self):
        self.cabezalinea2 = None
        self.siguiente=None
        self.anterior=None
        self.abajo=None
        self.arriba=None

    def insertar_lineascomponenteduplicados(self, linea, componente):
        if self.cabezalinea2 is None:
            self.cabezalinea2=NODO_lineasduplicadas(linea=linea, componente=componente)
            return
        linea_actual=self.cabezalinea2
        while linea_actual.siguiente:
            linea_actual=linea_actual.siguiente
        linea_actual.siguiente=NODO_lineasduplicadas(linea=linea, componente=componente)

    def recorrer_lineas(self):
        if self.cabezalinea2 is None:
            print("List has no element")
            return
        linea_actual=self.cabezalinea2
        print("La línea: ", linea_actual.linea, "   Componente : ", linea_actual.componente,"-->")
        while linea_actual.siguiente:
            linea_actual=linea_actual.siguiente
            print("La línea: ", linea_actual.linea, "   Componente : ", linea_actual.componente,"-->")

    def buscar_componentedelineaduplicados(self, linea):
        linea_actual=self.cabezalinea2
        if linea_actual is None:
            return "estavacio"
        while linea_actual is not None:
            if int(linea_actual.linea)  ==int(linea) :
                return int(linea_actual.componente)
            else:
                linea_actual=linea_actual.siguiente
        return False



class HeaderList():
    def __init__(self, First=None):
        self.First=First
    def setHeader(self, new):
        if self.First==None:
            self.First=new
        elif new.id < self.First.id:
            new.Next=self.First
            self.First.anterior=new
            self.First=new
        else:
            current=self.First
            while current.Next != None:
                if new.id<current.Next.id:
                    new.Next=current.Next
                    current.Next.anterior=current
                    new.anterior=current
                    current.Next=new
                    break
                current=current.Next
            if current.Next==None:
                current.Next=new
                new.anterior=current

    def getHeader(self, id):
        current = self.First
        while current!=None:
            if current.id==id:
                return current
            current=current.Next
        return None
class Nodomatriz:
    def __init__(self, row, column, value):
        self.row=row
        self.column=column
        self.value=value 
        self.derecha=None
        self.izquierda=None
        self.arriba=None
        self.abajo=None
class nodoHeaders:
    def __init__(self, id):
        self.id=id
        self.Next=None
        self.anterior=None
        self.accessNode=None
class matriz():
    def __init__(self):
        self.eRows=HeaderList()
        self.eColumns=HeaderList()
    def insert(self, row, column, value):
        new=Nodomatriz(row, column, value)
        # inserción encabezado por filas
        erow=self.eRows.getHeader(row)
        if erow==None:
            erow=nodoHeaders(row)
            erow.accessNode=new
            self.eRows.setHeader(erow)
        else:
            if new.column<erow.accessNode.column:
                new.derecha=erow.accessNode
                erow.accessNode.izquierda=new
                erow.accessNode=new
            else:
                current=erow.accessNode
                while current.derecha!=None:
                    if new.column<current.derecha.column:
                        new.derecha=current.derecha
                        current.derecha.izquierda=new
                        new.izquierda=current.derecha
                        current.derecha=new
                        break
                    current=current.derecha
                if current.derecha==None:
                    current.derecha=new
                    new.izquierda=current
        ecolumn=self.eColumns.getHeader(column)
        if ecolumn==None:
            ecolumn=nodoHeaders(column)
            ecolumn.accessNode=new
            self.eColumns.setHeader(ecolumn)
        else:
            if new.row<ecolumn.accessNode.row:
                new.abajo=ecolumn.accessNode
                ecolumn.accessNode.arriba=new
                ecolumn.accessNode=new
            else:
                current=ecolumn.accessNode
                while current.abajo!=None:
                    if new.row<current.abajo.row:
                        new.abajo=current.abajo
                        current.abajo.arriba=new
                        new.arriba=current
                        current.abajo=new
                        break
                    current=current.abajo
                if current.abajo ==None:
                    current.abajo=new
                    new.arriba=current
    def recorrerows(self):
        erow=self.eRows.First
        while erow!=None:
            current=erow.accessNode
            while current!=None:
                print("(",str(current.row),",",current.column,")  --> ",current.value)
                current=current.derecha
            erow=erow.Next        
    def generarHTML_individual(self):
        Lista_Linea_Resultados=loadfile.Lista_Linea_Resultados
        columnas=int(Lista_Linea_Resultados.cantidad_lineas())
        cont2=0
        ecolumn=self.eColumns.First
        contenido = ''
        htmlFile = open("Reportes/Reporte_EJEMPLO" + ".html", "w", encoding='utf-8')
        htmlFile.write("""
            <!DOCTYPE html>
            <html lang="en" >
            <head>
            <meta charset="UTF-8">
            <title>CodePen - &lt;Table&gt; Responsive</title>
            <link rel="stylesheet" href="./style.css">

            </head>
            <body>
            <!-- partial:index.partial.html -->
            <h1><span class="blue">&lt;</span>Reporte<span class="blue">&gt;</span> <span class="yellow"> de Tokens</pan></h1>
            <h2>  <a href="https://github.com/Alvaro-SP" target="_blank">Lista de Tokens</a></h2>

            <table class="container">
            <thead>
              <tr>
              <th>Tiempo</th>
 
                """
              )
        while cont2 < columnas:
            valor = str(Lista_Linea_Resultados.buscar_lineapor_id(cont2))
            htmlFile.write("          <th> Línea "+valor+"</th>")
            cont2+=1
        htmlFile.write("""
                </tr>
                </thead>
                <tbody>
            """)
        cont=1
        while ecolumn!=None:
            current=ecolumn.accessNode
            htmlFile.write("<tr>\n")
            htmlFile.write("          <td>"+str(cont)+"</td>")
            while current!=None:
                htmlFile.write("          <td>"+str(current.value)+"</td>")
                current=current.abajo
            ecolumn=ecolumn.Next
            htmlFile.write("</tr>\n")
            cont+=1

        htmlFile.write(contenido)
        htmlFile.write("""
        </tbody>
         </table>
            <!-- partial -->
        <script  src="./script.js"></script>
        </body>
        </html>""")
        htmlFile.close



    def recorrecolumns(self,m,n):
        ecolumn=self.eColumns.First
        print("\n-----------RECORRIDO COLUMNAS--------------")
        while ecolumn!=None:
            current=ecolumn.accessNode
            print("\n Columna: "+str(current.column))
            print("Fila valor")
            while current!=None:
                print(str(current.row)+"     "+current.value)
                current=current.abajo
            ecolumn=ecolumn.Next
        print("-----------FIN RECORRIDO COLUMNAS--------------")

def trash():
        pass
            # class NODO_Eselprimero:
            #     def __init__(self,  linea = None, esprimero=None , siguiente = None):
            #         self.linea=linea
            #         self.esprimero=esprimero
            #         self.siguiente = siguiente

            # class lista_esprimero:
            #     def __init__(self):
            #         self.cabezaesprimero = None
            #         self.siguiente=None
            #         self.anterior=None
            #         self.abajo=None
            #         self.arriba=None

            #     def insertar_yaseensamblo(self, linea, esprimero):
            #         if self.cabezaesprimero is None:
            #             self.cabezaesprimero=NODO_Yaseensamblo(linea=linea, esprimero=esprimero)
            #             return
            #         linea_actual=self.cabezaesprimero
            #         while linea_actual.siguiente:
            #             linea_actual=linea_actual.siguiente
            #         linea_actual.siguiente=NODO_Yaseensamblo(linea=linea, esprimero=esprimero)

            #     def recorrer_lineas(self):
            #         if self.cabezaesprimero is None:
            #             print("List has no element")
            #             return
            #         linea_actual=self.cabezaesprimero
            #         print("La línea: ", linea_actual.linea, "   Es el primero? : ", linea_actual.esprimero,"-->")
            #         while linea_actual.siguiente:
            #             linea_actual=linea_actual.siguiente
            #             print("La línea: ", linea_actual.linea, "  Ensamblado? : ", linea_actual.esprimero,"-->")

            #     def actualizar_esprimero(self, linea, esprimero):
            #         linea_actual=self.cabezaesprimero
            #         if linea_actual is None:
            #             return "estavacio"
            #         while linea_actual is not None:
            #             if int(linea_actual.linea)  ==int(linea) :
            #                 linea_actual.esprimero=esprimero
            #                 return
            #             else:
            #                 linea_actual=linea_actual.siguiente
            #         return False

            #     def buscar_esprimero(self, linea):
            #         linea_actual=self.cabezaesprimero
            #         if linea_actual is None:
            #             return "estavacio"
            #         while linea_actual is not None:
            #             if int(linea_actual.linea)  ==int(linea) :
            #                 return int(linea_actual.yaseensamblo)
            #             else:
            #                 linea_actual=linea_actual.siguiente
            #         return False





        # # try:
        # s=Tiempoalinear()
        # segundos=0
        # iterador=0
        # cont=0
        # tiempo_alinear=0
        # marcarguardartiempo=True
        # ultimoestaensamblado=False

        # listaComponentecabeza = lista.lineascabeza
        # marcarguardartiempo=True


        # while listaComponentecabeza != None:
        #     i=1 #segundos
        #     tiempo=loadfile.lista_lineasprod.buscar_tiempo_linea(listaComponentecabeza.linea)
        #     listaanterior=listaComponentecabeza.siguiente
        #     listasiguiente=listaComponentecabeza.anterior
        #     if listaComponentecabeza.abajo != None:
        #         temp = listaComponentecabeza.abajo
        #         componente_a_llegar=temp.componente
        #         componente_a_ensamblar=0

        #         if not Lista_Linea_Resultados.buscar_linea(listaComponentecabeza.linea):
        #             Lista_Linea_Resultados.insertar_lineas(cont, listaComponentecabeza.linea)
        #             a=Lista_Dondequedo.buscar_dondesequedo(listaComponentecabeza.linea)
        #             if a=="estavacio":
        #                 while i!=int(componente_a_llegar):
        #                     Lista_Compo_Resultados.insertar_componente(cont, Lista_Linea_Resultados, "Mover Brazo-C"+str(i))
        #                     i+=1
        #                 if i==int(componente_a_llegar):
        #                     Lista_Compo_Resultados.insertar_componente(cont, Lista_Linea_Resultados, "Mover Brazo-C"+str(i))
        #                     componente_a_ensamblar+=i
        #                     i+=1
        #                 tempi=i
        #                 Lista_Dondequedo.insertar_dondesequedo(listaComponentecabeza.linea, i-1)
        #             elif a==False:
        #                 pass
        #             else:
        #                 # while i <= a:
        #                 #     Lista_Compo_Resultados.insertar_componente(cont, Lista_Linea_Resultados, "No Hace NADA" )
        #                 #     i+=1

        #                 while a!=int(componente_a_llegar):
        #                     Lista_Compo_Resultados.insertar_componente(cont, Lista_Linea_Resultados, "Mover Brazo-C"+str(a))
        #                     i+=1
        #                     a+=1
        #                 if a==int(componente_a_llegar):
        #                     Lista_Compo_Resultados.insertar_componente(cont, Lista_Linea_Resultados, "Mover Brazo-C"+str(a))
        #                     componente_a_ensamblar+=i
        #                     i+=1
        #                 tempi=i
        #                 Lista_Dondequedo.insertar_dondesequedo(listaComponentecabeza.linea, i-1)

        #             while i!= int(tempi)+int(tiempo):
        #                 Lista_Compo_Resultados.insertar_componente(cont, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(componente_a_ensamblar))
        #                 if listasiguiente==None:
        #                     ultimoestaensamblado=True
        #                 i+=1
        #             while i<=int(s.obtenertiempoinicial()):
        #                 Lista_Compo_Resultados.insertar_componente(cont, Lista_Linea_Resultados, "No Hace NADA" )
        #                 i+=1
        #             if marcarguardartiempo:
        #                 tiempo_alinear=i
        #                 s.guardartiempoalinear(tiempo_alinear)
        #                 marcarguardartiempo=False
        #                 segundos+=i

        #         else:
        #             listatemp=Lista_Linea_Resultados.return_idylinea(listaComponentecabeza.linea)
        #             # while i!=int(componente_a_llegar):
        #             #     Lista_Compo_Resultados.insertar_componente(int(listatemp.id), Lista_Linea_Resultados, "Mover Brazo-C"+str(i))
        #             #     i+=1
        #             print(listatemp.id, listatemp.linea)
        #             while i!=int(componente_a_llegar):
        #                 Lista_Compo_Resultados.insertar_componente(int(listatemp.id), Lista_Linea_Resultados, "Mover Brazo-C"+str(i))
        #                 i+=1
        #             if i==int(componente_a_llegar):
        #                 Lista_Compo_Resultados.insertar_componente(int(listatemp.id), Lista_Linea_Resultados, "Mover Brazo-C"+str(i))
        #                 componente_a_ensamblar+=i
        #                 i+=1
        #             tempi=i

        #             while i!= int(tempi)+int(tiempo):
        #                 Lista_Compo_Resultados.insertar_componente(int(listatemp.id), Lista_Linea_Resultados, "ENSAMBLAR-C"+str(componente_a_ensamblar))
        #                 i+=1
        #                 if listasiguiente==None:
        #                     ultimoestaensamblado=True
        #             while i<=int(s.obtenertiempoinicial()):
        #                 Lista_Compo_Resultados.insertar_componente(int(listatemp.id), Lista_Linea_Resultados, "No Hace NADA" )
        #                 i+=1
        #             if marcarguardartiempo:
        #                 tiempo_alinear=i
        #                 s.guardartiempoalinear(tiempo_alinear)
        #                 marcarguardartiempo=False
        #                 segundos+=i
        #         cont+=1

        #     listaComponentecabeza = listaComponentecabeza.siguiente
        # if ultimoestaensamblado:
        #         iterador+=1
        # print("El tiempo optimo seria: ", segundos)

        # Lista_Compo_Resultados.mostrar_componentes(Lista_Linea_Resultados,0)
        # Lista_Compo_Resultados.mostrar_componentes(Lista_Linea_Resultados,1)
        # Lista_Compo_Resultados.mostrar_componentes(Lista_Linea_Resultados,2)
        # Lista_Compo_Resultados.mostrar_componentes(Lista_Linea_Resultados,3)
        # Lista_Compo_Resultados.mostrar_componentes(Lista_Linea_Resultados,4)
        # Lista_Compo_Resultados.mostrar_componentes(Lista_Linea_Resultados,5)
        # except Exception as e:
        #     print("List index out of range :( ")
        #     print(e)
      # elif int(lineaactual) != int(lineaMayor) and  haylineasiguiente==True  and  lista_Yaensamblo.buscar_yaseensamblo(lineaactual)==True:

                #     iteration=0
                #     if obtain_sequedo2 < componente_a_llegar_next and componente_a_llegar_next!=False:
                #         while obtain_sequedo2 <= componente_a_llegar_next and iteration!=correrfilas:
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #             obtain_sequedo2+=1
                #             Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #             lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #             iteration+=1
                #         while iteration!=correrfilas:
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                #             iteration+=1
                #         # Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")

                #     elif obtain_sequedo2 > componente_a_llegar_next and componente_a_llegar_next!=False:
                #         while obtain_sequedo2 >= componente_a_llegar_next and iteration!=correrfilas:
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #             obtain_sequedo2-=1
                #             Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #             lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #             iteration+=1
                #         while iteration!=correrfilas:
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                #             iteration+=1
                #     elif componente_a_llegar_next==False:
                #         componente_a_llegar_actual=Lista_lineatodos_duplicado.buscar_componentedelineaduplicados(lineaactual)

                #         if obtain_sequedo2 < componente_a_llegar_actual:
                #             while obtain_sequedo2 <= componente_a_llegar_actual and iteration!=correrfilas:
                #                 Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #                 obtain_sequedo2+=1
                #                 Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #                 lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #                 iteration+=1
                #             while iteration!=correrfilas:
                #                 Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                #                 iteration+=1
                #             # Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")

                #         elif obtain_sequedo2 > componente_a_llegar_actual:
                #             while obtain_sequedo2 >= componente_a_llegar_actual and iteration!=correrfilas:
                #                 Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #                 obtain_sequedo2-=1
                #                 Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #                 lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #                 iteration+=1
                #             while iteration!=correrfilas:
                #                 Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                #                 iteration+=1



                # elif int(lineaactual) != int(lineaMayor) and  haylineasiguiente==False and  lista_Yaensamblo.buscar_yaseensamblo(lineaactual)==True:
                    
                #     iteration=0
                #     if obtain_sequedo2 < componente_a_llegar_next and componente_a_llegar_next!=False:
                #         while obtain_sequedo2 <= componente_a_llegar_next and iteration!=correrfilas:
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #             obtain_sequedo2+=1
                #             Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #             lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #             iteration+=1
                #         while iteration!=correrfilas:
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                #             iteration+=1
                #         #aqui parece que debo agregar una iteracion mas Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")

                #     elif obtain_sequedo2 > componente_a_llegar_next and componente_a_llegar_next!=False:
                #         while obtain_sequedo2 >= componente_a_llegar_next and iteration!=correrfilas:
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #             obtain_sequedo2-=1
                #             Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #             lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #             iteration+=1
                #         while iteration!=correrfilas:
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                #             iteration+=1
                #     elif componente_a_llegar_next==False:
                #         componente_a_llegar_actual=Lista_lineatodos_duplicado.buscar_componentedelineaduplicados(lineaactual)
                #         while obtain_sequedo2 <= componente_a_llegar_actual and iteration!=correrfilas:
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #             obtain_sequedo2+=1
                #             Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #             lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #             iteration+=1
                #         while iteration!=correrfilas:
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                #             iteration+=1

                # elif int(lineaactual) != int(lineaMayor) and  haylineasiguiente==True  and  lista_Yaensamblo.buscar_yaseensamblo(lineaactual)==True :
                    
                #     iteration=0
                #     if obtain_sequedo2 < componente_a_llegar_next and componente_a_llegar_next!=False:
                #         while obtain_sequedo2 <= componente_a_llegar_next and iteration!=correrfilas:
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #             obtain_sequedo2+=1
                #             Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #             lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #             iteration+=1
                #         while iteration!=correrfilas:
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                #             iteration+=1
                #         #aqui parece que debo agregar una iteracion mas Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")

                #     elif obtain_sequedo2 > componente_a_llegar_next and componente_a_llegar_next!=False:
                #         while obtain_sequedo2 >= componente_a_llegar_next and iteration!=correrfilas:
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #             obtain_sequedo2-=1
                #             Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #             lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #             iteration+=1
                #         while iteration!=correrfilas:
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                #             iteration+=1
                #     elif componente_a_llegar_next==False:
                #         componente_a_llegar_actual=Lista_lineatodos_duplicado.buscar_componentedelineaduplicados(lineaactual)
                #         while obtain_sequedo2 <= componente_a_llegar_actual and iteration!=correrfilas:
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #             obtain_sequedo2+=1
                #             Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #             lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #             iteration+=1
                #         while iteration!=correrfilas:
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                #             iteration+=1

                # elif int(lineaactual) != int(lineaMayor) and  haylineasiguiente==True  and  lista_Yaensamblo.buscar_yaseensamblo(lineaactual)==False:
                    
                #     iteration=0
                #     if obtain_sequedo2 < componente_a_llegar_next and componente_a_llegar_next!=False:
                #         while obtain_sequedo2 <= componente_a_llegar_next and iteration!=correrfilas:
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #             obtain_sequedo2+=1
                #             Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #             lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #             iteration+=1
                #         while iteration!=correrfilas:
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                #             iteration+=1
                #         #aqui parece que debo agregar una iteracion mas Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")

                #     elif obtain_sequedo2 > componente_a_llegar_next and componente_a_llegar_next!=False:
                #         while obtain_sequedo2 >= componente_a_llegar_next and iteration!=correrfilas:
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #             obtain_sequedo2-=1
                #             Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #             lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #             iteration+=1
                #         while iteration!=correrfilas:
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                #             iteration+=1
                #     elif componente_a_llegar_next==False:
                #         componente_a_llegar_actual=Lista_lineatodos_duplicado.buscar_componentedelineaduplicados(lineaactual)
                #         while obtain_sequedo2 <= componente_a_llegar_actual and iteration!=correrfilas:
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #             obtain_sequedo2+=1
                #             Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #             lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #             iteration+=1
                #         while iteration!=correrfilas:
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                #             iteration+=1

                # elif int(lineaactual) == int(lineaMayor) and  obtain_sequedo2==componente_a_llegar and lista_Yaensamblo.buscar_yaseensamblo(lineaactual)==False :
                #     while iteration!=correrfilas:
                #         Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)))
                #         lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                #         iteration+=1

                # elif int(lineaactual) == int(lineaMayor) and  obtain_sequedo2==componente_a_llegar and lista_Yaensamblo.buscar_yaseensamblo(lineaactual)==False :
                #     while iteration!=correrfilas:
                #         Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)))
                #         lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                #         iteration+=1

                # elif  lista_Yaensamblo.buscar_yaseensamblo(lineaactual)==True and haylineasiguiente==False:
                #     for iteration in range(0,correrfilas): 
                #         Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No Hacer Nada")
                #         # iteration+=1

                # elif int(lineaactual)==int(lineaMayor) and haylineasiguiente==True:
                #     iteration=0
                #     if componente_a_llegar_next != False and componente_a_llegar_next!=None:
                #         if obtain_sequedo2 < componente_a_llegar:
                #             while obtain_sequedo2 <= componente_a_llegar and iteration!=correrfilas:
                #                 Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #                 obtain_sequedo2+=1
                #                 Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #                 lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #                 iteration+=1
                #             while iteration!=correrfilas:
                #                 Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                #                 lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                #                 iteration+=1
                #             #aqui parece que debo agregar una iteracion mas Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")

                #         else:
                #             while obtain_sequedo2 >= componente_a_llegar and iteration!=correrfilas:
                #                 Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #                 obtain_sequedo2-=1
                #                 Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #                 lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #                 iteration+=1
                #             while iteration!=correrfilas:
                #                 Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                #                 lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                #                 iteration+=1
                #     elif componente_a_llegar_next==False:
                #         componente_a_llegar_actual=Lista_lineatodos_duplicado.buscar_componentedelineaduplicados(lineaactual)

                #         if obtain_sequedo2 < componente_a_llegar_actual and componente_a_llegar_actual!=False:
                #             while obtain_sequedo2 <= componente_a_llegar_actual and iteration!=correrfilas:
                #                 Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #                 obtain_sequedo2+=1
                #                 Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #                 lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #                 iteration+=1
                #             while iteration!=correrfilas:
                #                 Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                #                 lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                #                 iteration+=1
                #             #aqui parece que debo agregar una iteracion mas Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")

                #         elif obtain_sequedo2 > componente_a_llegar_actual and componente_a_llegar_actual!=False:
                #             while obtain_sequedo2 >= componente_a_llegar_actual and iteration!=correrfilas:
                #                 Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #                 obtain_sequedo2-=1
                #                 Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #                 lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #                 iteration+=1
                #             while iteration!=correrfilas:
                #                 Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                #                 lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                #                 iteration+=1


                #     # if lista_Yaensamblo.buscar_yaseensamblo(lineaactual)=="primero":
                #     #     lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #     #     if int(lineaactual)==int(lineaMayor):
                #     #         for iteration in range(correrfilas):
                #     #             if obtain_sequedo2 < componente_a_llegar_next:
                #     #                 Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #     #                 obtain_sequedo2+=1
                #     #                 Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #     #                 lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #     #             elif obtain_sequedo2 > componente_a_llegar_next:
                #     #                 Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #     #                 obtain_sequedo2-=1
                #     #                 Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #     #                 lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #     #             else:
                #     #                 Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)))
                #     #                 lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                #     #     else:
                #     #          for iteration in range(correrfilas):
                #     #             if obtain_sequedo2 < componente_a_llegar_next:
                #     #                 Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #     #                 obtain_sequedo2+=1
                #     #                 Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #     #                 lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #     #             elif obtain_sequedo2 > componente_a_llegar_next:
                #     #                 Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #     #                 obtain_sequedo2-=1
                #     #                 Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #     #                 lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #     #             else:
                #     #                 Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)))
                #     #                 lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)

                #     # elif componente_a_llegar_next != False and componente_a_llegar_next!=None:
                #     #     for iteration in range(correrfilas):
                #     #         if obtain_sequedo2 != componente_a_llegar_next:
                #     #             if obtain_sequedo2 < componente_a_llegar_next:
                #     #                 Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))
                #     #                 obtain_sequedo2+=1
                #     #                 Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #     #                 lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #     #             elif obtain_sequedo2 > componente_a_llegar_next:
                #     #                 Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))
                #     #                 obtain_sequedo2-=1
                #     #                 Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #     #                 lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #     #         else:
                #     #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)))
                #     #             lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                #     # else:
                #     #     for iteration in range(correrfilas):
                #     #         Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)))
                #     #         lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)

                # elif int(lineaactual)==int(lineaMayor) and haylineasiguiente==False:
                #     if componente_a_llegar_next != False and componente_a_llegar_next != None:
                #         for iteration in range(correrfilas):
                #             if obtain_sequedo2 != componente_a_llegar_next:
                #                 if obtain_sequedo2 < componente_a_llegar_next:
                #                     Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #                     obtain_sequedo2+=1
                #                     Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #                     lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #                 elif obtain_sequedo2 >componente_a_llegar_next:
                #                     Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                #                     obtain_sequedo2-=1
                #                     Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                #                     lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                #             else:
                #                 Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)))
                #                 lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                #     else:
                #         for iteration in range(correrfilas):
                #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                #             lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)


                # Lista_Compo_Resultados.mostrar_componentes(Lista_Linea_Resultados,idlineaactual)