import sys
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from xml.etree import ElementTree as ET
from lineas import *
import productos
import lineas
import re
import mensaje
import ventana
#LISTAS GLOBALES
lista_lineasprod=lineas.Lista_dobleenlazada_lineas()
lista_ComponentedeLinea=lineas.lista_ComponenteDeLinea()
lista_productos=productos.Lista_dobleenlazada_producto()
lista_lista_productos=productos.listaProductos()
lista_lista_ensambles=productos.listaEnsambles()
Matriz_Resultados=productos.matriz()
lista_tiempos=productos.lista_Tiempos()


Lista_Linea_Resultados=productos.lista_Linea()# CABEZAS DE MI LISTA DE RESULTADOS
Lista_Compo_Resultados=productos.lista_Componente()#LAS COLUMNAS DE MI LISTA DE LINEAS TODO(ENSAMBLAR,NOHACENADA,MOVER CX)

CantidadLineasProduccion=0
nombre_simulacion=""
cont=0
contadorSimulacion=0
class loadfile(QWidget):
    def __init__(self, typefile):
        super().__init__()
        self.title = 'SELECCIONAR ARCHIVO'
        self.left = 400
        self.top = 150
        self.width = 640
        self.height = 480        
        self.doc_read=False
        self.doc_2read=False
        self.typefile=typefile
        print(self.typefile)
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)         
        self.setGeometry(self.left, self.top, self.width, self.height) 
        self.openFileNameDialog()
    def openFileNameDialog(self):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _= QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","XML Files (*.xml);;All Files (*)", options=options)
            # if self.typefile==0:
            #     fileName=r"C:\Users\Sr. C\Google Drive\C U A R T O  S E M E S T R E\IPC2 E\LAB IPC2 E\PROYECTO 2\TEST FILES PROJECT 2 IPC2\machine.xml"
            # else:
            #     fileName=r"C:\Users\Sr. C\Google Drive\C U A R T O  S E M E S T R E\IPC2 E\LAB IPC2 E\PROYECTO 2\TEST FILES PROJECT 2 IPC2\simulation.xml"
            if fileName and self.typefile==0:
                self.readconfiguration(str(fileName))
            elif fileName and self.typefile==1:
                self.readsimulation(str(fileName))
            else:
                print("Nothing")
        except:
            a=mensaje.App()
            a.initUI("ERROR POR FAVOR SELECCIONE UN ARCHIVO CORRECTO")
            print("ERROR POR FAVOR SELECCIONE UNO CORRECTO")

    def readconfiguration(self, ruta):
        global lista_productos
        global lista_lineasprod
        global CantidadLineasProduccion
        global nombre_simulacion
        global cont
        global lista_lista_productos
        global lista_lista_ensambles
        try:
            contenido=ET.parse(ruta)
            root_all = contenido.getroot()
            root_str = ET.tostring(root_all)
            root_str = root_str.lower()
            root_machine = ET.fromstring(root_str)
            self.doc_read=True
            print(" El archivo se cargó exitosamente.")
        except Exception as e:
            print(e)
            print(" Ruta invalida. No se pudo encontrar el archivo.\n")

        if self.doc_read:
            # try:
            CantidadLineasProduccion  =  int((root_machine.find('cantidadlineasproduccion').text).rstrip())
            for listlineas  in  root_machine.findall('listadolineasproduccion'):
                for lineasprod in listlineas.findall('lineaproduccion'):
                    Numero = (lineasprod.find('numero').text).strip()
                    CantidadComponentes  =  (lineasprod.find('cantidadcomponentes').text).strip()
                    TiempoEnsamblaje  =  (lineasprod.find('tiempoensamblaje').text).strip()
                    if lista_lineasprod.buscar_linea(Numero)  is  False:
                        lista_ComponentedeLinea.insertar_ComponenteDeLinea(Numero, CantidadComponentes)
                        item1 = QListWidgetItem("Linea "+str(Numero))
                        item2 = QListWidgetItem(str(TiempoEnsamblaje)+ " Segundos")
                        ventana.widget_components1.addItem(item1)
                        ventana.widget_components2.addItem(item2)
                        new_linea  =  lineas.linea(None, Numero, CantidadComponentes, TiempoEnsamblaje)
                        lista_lineasprod.insertar(new_linea)
                    else:
                        print("--> La línea " + Numero + " ya existe en el sistema. No pueden existir 2 líneas iguales.")
            
            # print(CantidadLineasProduccion)            
            # print(lista_lineasprod.cantidad_lineasproduccion())
            # lista_lineasprod.recorrer()
            if int(CantidadLineasProduccion) == int(lista_lineasprod.cantidad_lineasproduccion()):
                print("las lineas de produccion son: " , CantidadLineasProduccion ,  " coincide con la cantidad en la lista de lineas: ",lista_lineasprod.cantidad_lineasproduccion() )
            else:
                print("La cantidad de Líneas no coincide con la cantidad en la lista de lineas de producción")
            for listproduct in root_machine.findall('listadoproductos'):
                for products in listproduct.findall('producto'):
                    nombre=(products.find('nombre').text).strip()
                    print("☻☻☻☻☻☻☻☻☻",nombre,"☻☻☻☻☻☻☻☻☻")
                    elaboracion=(products.find('elaboracion').text).strip()
                    if lista_productos.buscar_producto(nombre)  is  False:
                        lista_lista_productos.addcombobox(cont, nombre)
                        lista_lista_productos.addcombobox2(cont, nombre)
                        new_product=productos.producto(nombre, elaboracion)
                        lista_productos.insertar(new_product)
                        lista_lista_productos.insertar_products(cont, nombre)
                    else:
                        print("--> El producto " + nombre + " ya existe en el sistema. No pueden existir 2 productos iguales.")
                    lproducto_actual=lista_lista_productos.return_idyproducto(nombre)
                    if lproducto_actual is False:
                        print("No hay ningun producto")
                    else:
                        listalistaproducto_actual=lista_productos.returnnombreyensamble(nombre)
                        if listalistaproducto_actual is False:
                            print("No hay ningun producto")
                        else:
                            cad=str(listalistaproducto_actual.producto.elaboracion)
                            c=""
                            patron=r'(l\dpc\dp)+'
                            i=0
                            while i < len(cad):
                                try:
                                    c+=cad[i]
                                    # c=c.strip()
                                    if re.search(patron , c):
                                        print(c)
                                        lineac=c[1]
                                        compoac=c[4]
                                        if lineac.isdigit() and compoac.isdigit():

                                            objetoensamblaje=productos.ensamblaje(c[1], c[4])
                                            returntiempolinea=lista_ComponentedeLinea.buscar_ComponenteDeLinea(c[1])
                                            print(f"Linea: {c[1]} Componente: {c[4]}")
                                            if  returntiempolinea!= False and int(c[4])<=returntiempolinea:
                                                lista_lista_ensambles.insertar_ensambles(int(lproducto_actual.id), lista_lista_productos, objetoensamblaje)
                                            else:
                                                print(F"NO SE PUEDE AGREGAR LA INSTRUCCIÓN PORQUE EL COMPONENTE {c[4]} NO ESTA EN LA LINEA {c[1]} ")
                                                print("REVISAR ARCHIVO")
                                        else:
                                            print(f"ERROR DE SINTAXIS EN ESTA ELABORACIÓN  Línea: {c[1]} Componente: {c[4]} no se reconoce")
                                            w=mensaje.App()
                                            w.initUI(f"ERROR DE SINTAXIS EN ESTA ELABORACIÓN  Línea: {c[1]} Componente: {c[4]} no se reconoce")

                                        c=''
                                    elif c[-1]==" ":
                                        c=''
                                    i+=1
                                except :
                                    return
            a2=mensaje.App()
            a2.initUI("Se ha cargado el archivo MAQUINA de configuracion correctamente :)")                        

            # lista_productos.recorrer()
            print("Se han cargado las listas del archivo correctamente :)")
            # except Exception as e:
            #     print(e)
            #     print(" Ocurrió un error al procesar el archivo. Revisar las etiquetas .\n")

    def readsimulation(self, ruta):
        global lista_productos
        global nombre_simulacion
        global cont
        global lista_lista_productos
        global lista_lista_ensambles
        lista_lista_productosN=productos.listaProductos()
        lista_lista_ensamblesN=productos.listaEnsambles()
        try:
            contenido=ET.parse(ruta)
            root_all = contenido.getroot()
            root_str = ET.tostring(root_all)
            root_str = root_str.lower()
            root_machine = ET.fromstring(root_str)
            self.doc_2read=True
            print(" El archivo se cargó exitosamente.")
        except Exception as e:
            print(e)
            print(" Ruta invalida. No se pudo encontrar el archivo.\n")
        SimulNames=""
        if self.doc_2read:
            # try:
            nombre_simulacion  = str( root_machine.find('nombre').text).strip()
            lista_productos.recorrer()
            a=mensaje.App()
            a.initUI(f"ABRIENDO REPORTES DEL ARCHIVO DE SIMULACIÓN: {nombre_simulacion}")
            for listproduct in root_machine.findall('listadoproductos'):
                cont=1
                for productindividual in listproduct.findall('producto'):
                    producto=(productindividual.text).strip()
                    if lista_productos.buscar_producto(producto)  is  True:
                        # lista_lista_productosN.insertar_products(cont, producto)
                        lista_lista_ensambles.llenarListaLineas2(lista_lista_productos,nombre_simulacion, producto)
                        SimulNames+=f"    {cont}.    {producto}  --->\n"
                        # lista_lista_productos.addcombobox(cont, producto)
                        # lista_lista_productos.addcombobox2(cont, producto)
                        cont+=1
                    else:
                        print("--> El producto " + producto + " no existe en el sistema. El archivo de configuración no lo posee.")
                        continue
                    # lproducto_actual=lista_lista_productos.return_idyproducto(producto)
                    # if lproducto_actual is False:
                    #     print("No hay ningun producto")
                    # else:
                    #     listalistaproducto_actual=lista_productos.returnnombreyensamble(producto)
                    #     print("hola")
                    #     if listalistaproducto_actual is False:
                    #         print("No hay ningun producto")
                    #     else:
                    #         cad=str(listalistaproducto_actual.producto.elaboracion)
                    #         print(cad)
                    #         c=""
                    #         patron=r'(l\dpc\dp)+'
                    #         i=0
                    #         while i < len(cad):
                    #             c+=cad[i]
                    #             c=c.rstrip()
                    #             if re.search(patron , c):
                    #                 # print(c)
                    #                 # print(f"linea: {c[1]} Componente: {c[4]}")
                    #                 objetoensamblaje=productos.ensamblaje(c[1], c[4])
                    #                 lista_lista_ensamblesN.insertar_ensambles(int(lproducto_actual.id), lista_lista_productos, objetoensamblaje)
                    #                 c=''
                    #             i+=1 
                    # lista_lista_ensambles.llenarListaLineas(lista_lista_productos, producto)
            # lista_lista_productos=lista_lista_productosN
            # lista_lista_ensambles=lista_lista_ensamblesN
            a2=mensaje.App()
            a2.initUI("El Archivo posee los siguientes PRODUCTOS:  \n"+SimulNames)
            print("")
            lista_lista_productos.recorrer()
            print("")
            # lista_lista_ensambles.mostrar_ensambles(lista_lista_productos,0)
            # except Exception as e:
            #     print(e)
            #     print(" Ocurrió un error al procesar el archivo. Revisar las etiquetas .\n")
            print("Se han cargado las listas del archivo correctamente :)")
            a2=mensaje.App()
            a2.initUI("Se han cargado las listas del archivo correctamente :)")
        # for i in range(int(lista_lista_productos.cantidad_productos())):


    def agregardatos_HTML(self):
        global Lista_Linea_Resultados
        global Lista_Compo_Resultados
        global Matriz_Resultados
        columnas=Lista_Linea_Resultados.cantidad_lineas()

        filas=int(Lista_Compo_Resultados.cantidad_componente(Lista_Linea_Resultados, 1))
        cont=1
        columnast=int(columnas)
        seconds=1

        while cont <= columnast:
            lineatext=Lista_Linea_Resultados.buscar_lineapor_id(cont-1)
            self.table_ensamblaje.setRowCount(filas)
            # print("FILAS: ", filas)
            filast=Lista_Compo_Resultados.return_idycomponente(Lista_Linea_Resultados, cont-1)
            temp=filast.abajo
            for c in range(filas):
                if temp != None:
                    Matriz_Resultados.insert(cont, c, str(temp.componente))
                    temp=temp.abajo
            cont+=1

