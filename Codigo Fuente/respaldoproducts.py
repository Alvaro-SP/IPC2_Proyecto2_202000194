"""
    def calculoTiempoOptimizado(self, lista, listcomponent):
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        Lista_lineatodos_duplicado=lista_lineasduplicadas() #todas las lineas a de ensamble duplicadas
        Lista_Dondequedo=lista_Dondesequedo() #temporales en donde quedo de ultimo
        lista_Yaensamblo=lista_Yaseensamblo() #temporales si ya se ensamblo o no
        Lista_Linea_Resultados=lista_Linea()
        Lista_Compo_Resultados=lista_Componente()
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
        print("ORDENAMIENTO BURBUJA DE LA LISTA DE LINEAS CABEZA")
        Lista_Linea_Resultados.bubblesort()
        Lista_Linea_Resultados.recorrer_lineas()
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
            print("◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘ ")
            print("             Línea:  ", listaMadre.linea)
            print("Donde se quedo al inicio :      " + str(obtain_sequedo))
            if obtain_sequedo == componente_a_llegar:
                cont=0
            elif obtain_sequedo < componente_a_llegar:
                while obtain_sequedo < componente_a_llegar: # si quedo es menor a llegar se suma hasta que se igualen
                    obtain_sequedo+=1
                    cont+=1
            elif obtain_sequedo > componente_a_llegar: 
                while obtain_sequedo > componente_a_llegar: # si quedo es mayor a llegar se resta uno hasta que se igualen
                    obtain_sequedo-=1
                    cont+=1
            correrfilas= int(cont)+int(tiempo_ensamble)-1#cantidad de filas que recorrerá cada lista actual
            print("Donde se quedo despues :      " + str(obtain_sequedo))
            print("Componente a llegar:  " + str(componente_a_llegar))
            print("Filas que se corren:  ", correrfilas)
            print("Tiempo de ensamble:   ", tiempo_ensamble)
            print("Contador a sumar:     ", cont)
            listaactual=Lista_Linea_Resultados.lineascabeza
            correrfilas1=int(cont)+int(tiempo_ensamble)
            # print("☻☻☻☻☻☻☻☻☻☻☻☻    componente a llegar: ",componente_a_llegar, "lineaMayor: ", lineaMayor, " Donde se quedó: ", obtain_sequedo)
            while listaactual!= None: #!RECORRE LA LISTA DE RESULTADOS
                lineaactual=listaactual.linea
                idlineaactual=listaactual.id
                haylineasiguiente, lineasiguiente, idlineasiguiente=lista.buscar_sig_actual(idlineaactual)
                if haylineasiguiente:
                    componente_a_llegar_next=int(Lista_lineatodos_duplicado.buscar_componentedelineaduplicados(lineasiguiente))
                else:
                    componente_a_llegar_next=False
                obtain_sequedo2=Lista_Dondequedo.buscar_dondesequedo(lineaactual)
                # print("OBTAIN SEQUEDO 2: ", obtain_sequedo2, "Componente a llegar next: ", componente_a_llegar_next, "componente_allegar: ", componente_a_llegar)

                if   int(lineaactual) == int(lineaMayor) and  lista_Yaensamblo.buscar_yaseensamblo(lineaactual)=="primero"=="primero":# and lista_Yaensamblo.buscar_yaseensamblo(lineaactual):
                    # lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
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
                    # lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
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
                    elif obtain_sequedo2==componente_a_llegar_next:
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
                        elif obtain_sequedo2 == componente_a_llegar_next and componente_a_llegar_next!=False:
                            while iteration!=correrfilas:
                                Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                                iteration+=1
                        # elif componente_a_llegar_next==False:
                        #     componente_a_llegar_actual=Lista_lineatodos_duplicado.buscar_componentedelineaduplicados(lineaactual)

                        #     if obtain_sequedo2 < componente_a_llegar_actual:
                        #         while obtain_sequedo2 <= componente_a_llegar_actual and iteration!=correrfilas:
                        #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                        #             obtain_sequedo2+=1
                        #             Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                        #             lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                        #             iteration+=1
                        #         while iteration!=correrfilas:
                        #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                        #             iteration+=1
                        #         # Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")

                        #     elif obtain_sequedo2 > componente_a_llegar_actual:
                        #         while obtain_sequedo2 >= componente_a_llegar_actual and iteration!=correrfilas:
                        #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                        #             obtain_sequedo2-=1
                        #             Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                        #             lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                        #             iteration+=1
                        #         while iteration!=correrfilas:
                        #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                        #             iteration+=1
                        #     elif obtain_sequedo2 == componente_a_llegar_next and componente_a_llegar_next!=False:
                        #         while iteration!=correrfilas:
                        #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                        #             iteration+=1

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
                        if obtain_sequedo2 < componente_a_llegar and componente_a_llegar!=False:
                            while obtain_sequedo2 <= componente_a_llegar and iteration!=correrfilas:
                                Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                                obtain_sequedo2+=1
                                Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                                lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                                iteration+=1
                            while iteration!=correrfilas:
                                Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                                lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                                Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                                # Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2-1)
                                iteration+=1
                            # Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                            # lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)

                        elif obtain_sequedo2 > componente_a_llegar and componente_a_llegar!=False:
                            while obtain_sequedo2 >= componente_a_llegar and iteration!=correrfilas:
                                Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                                obtain_sequedo2-=1
                                Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                                lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                                iteration+=1
                            while iteration!=correrfilas:
                                Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                                lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                                Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                                # Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2-1)
                                iteration+=1
                            # Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                            # lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                        elif obtain_sequedo2 == componente_a_llegar and componente_a_llegar!=False:
                            Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                            lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                            Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                            # Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2-1)
                            iteration+=1
                        # elif componente_a_llegar==False:
                        #     componente_a_llegar_actual=Lista_lineatodos_duplicado.buscar_componentedelineaduplicados(lineaactual)

                        #     if obtain_sequedo2 < componente_a_llegar_actual:
                        #         while obtain_sequedo2 <= componente_a_llegar_actual and iteration!=correrfilas:
                        #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                        #             obtain_sequedo2+=1
                        #             Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                        #             lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                        #             iteration+=1
                        #         while iteration!=correrfilas:
                        #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                        #             iteration+=1
                        #         # Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")

                        #     elif obtain_sequedo2 > componente_a_llegar_actual:
                        #         while obtain_sequedo2 >= componente_a_llegar_actual and iteration!=correrfilas:
                        #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "Mover Brazo-C"+str(obtain_sequedo2))                        
                        #             obtain_sequedo2-=1
                        #             Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                        #             lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,False)
                        #             iteration+=1
                        #         while iteration!=correrfilas:
                        #             Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "No hacer nada")
                        #             iteration+=1
                        #     elif obtain_sequedo2 == componente_a_llegar and componente_a_llegar!=False:
                        #         Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                        #         lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                        #         Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
                        #         # Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2-1)
                        #         iteration+=1

                    elif haylineasiguiente==True  and lista_Yaensamblo.buscar_yaseensamblo(lineaactual)==False:
                        iteration=0
                        while iteration!=correrfilas:
                            Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                            lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                            Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2-1)
                            iteration+=1
                        # Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                        # lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)

                    elif haylineasiguiente==False and lista_Yaensamblo.buscar_yaseensamblo(lineaactual)==False:
                        iteration=0
                        while iteration!=correrfilas:
                            Lista_Compo_Resultados.insertar_componente(idlineaactual, Lista_Linea_Resultados, "ENSAMBLAR-C"+str(int(obtain_sequedo2)-1))
                            lista_Yaensamblo.actualizar_yaseensamblo(lineaactual,True)
                            Lista_Dondequedo.actualizar_dondesequedo(lineaactual, obtain_sequedo2)
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

        # for idi in range(longitud_resultado):
        #     print("☻  ",Lista_Compo_Resultados.cantidad_componente(Lista_Linea_Resultados,idi))
        #     Lista_Compo_Resultados.mostrar_componentes(Lista_Linea_Resultados,idi)
        # Lista_Linea_Resultados.bubblesort()
        loadfile.Lista_Linea_Resultados=Lista_Linea_Resultados
        loadfile.Lista_Compo_Resultados=Lista_Compo_Resultados
        loadfile.Matriz_Resultados.generarHTML_individual()
"""