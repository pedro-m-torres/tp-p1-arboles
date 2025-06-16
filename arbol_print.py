#Funcion para mostrar el arbol con una representar grafica.
#En este caso como el formato de cada subarbol se representa [raiz,subarbol_izquierdo,subarbol_derecho]
#Utilizamos la funcion de manera recursiva para encontrar el nodo mas alejado e imprimirlo multiplicando el nivel de espacios.

def imprimir_arbol(lista, nivel=0):
    if lista != []:
        # imprimir_arbol(lista[2], nivel + 1)
        # print("    " * nivel + str(lista[0]) )
        # imprimir_arbol(lista[1], nivel + 1)
        imprimir_arbol(lista[2], nivel + 1)
        print(" " * 4 * nivel + "->", lista[0])
        imprimir_arbol(lista[1], nivel + 1)


def Mostrar_Propiedades(arbol):
    print(f"Altura del árbol: {altura_arbol(arbol)}")
    print(f"Cantidad de nodos: {contar_nodos(arbol)}")
    print(f"Longitud del Árbol: {longitud_arbol(arbol)}")


def altura_arbol(arbol):
    if not arbol:
        return 0
    return 1 + max(altura_arbol(arbol[1]), altura_arbol(arbol[2]))


def contar_nodos(arbol):
    if not arbol:
        return 0
    return 1 + contar_nodos(arbol[1]) + contar_nodos(arbol[2])

    
def longitud_arbol(arbol):
    if not arbol:
        return 0
    return 1 + max(longitud_arbol(arbol[1]), longitud_arbol(arbol[2]))