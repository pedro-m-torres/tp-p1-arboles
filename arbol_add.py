#Funcion para crear el arbol con la raiz y dos hijos
def cargar_arbol(arbol):
    while True:

        puntaje = input("Ingrese el puntaje (0 para salir): ")

        if puntaje.isdigit():
            puntaje = int(puntaje)
        else:
            print("Por favor ingrese númerico!")
            continue
    
        if puntaje == 0:
            break

        crear_arbol(arbol, puntaje)



def crear_arbol(lista, score):
    if lista == []:
        lista += [score,[],[]]
    else:
        ingresar_subarbol(lista,score)



def ingresar_subarbol(nodo,score):
    if(score < nodo[0]):
        if nodo[1] == []:
            nodo[1] = [score, [],[]]
        else:
            ingresar_subarbol(nodo[1],score)

    elif(score > nodo[0]):
        if nodo[2] == []:
            nodo[2] = [score, [],[]]
        else:
            ingresar_subarbol(nodo[2],score)
