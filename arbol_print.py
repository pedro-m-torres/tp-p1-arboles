#Funcion para mostrar el arbol con una representar grafica.
#En este caso como el formato de cada subarbol se representa [raiz,subarbol_izquierdo,subarbol_derecho]
#Utilizamos la funcion de manera recursiva para encontrar el nodo mas alejado e imprimirlo multiplicando el nivel de espacios.

def imprimir_arbol(lista, nivel=0):
    if lista != []:
        imprimir_arbol(lista[2], nivel + 1)
        print(" " * 4 * nivel + "->", lista[0])
        imprimir_arbol(lista[1], nivel + 1)


def Mostrar_Propiedades(arbol):
    print(f"Altura del árbol: {altura_arbol(arbol)}")
    print(f"Peso del árbol: {contar_nodos(arbol)}")
    print(f"Nodo más profundo: {nodo_mas_profundo(arbol)[0]}")



def altura_arbol(arbol):
    if not arbol:
        return 0
    return 1 + max(altura_arbol(arbol[1]), altura_arbol(arbol[2]))


def contar_nodos(arbol):
    if not arbol:
        return 0
    return 1 + contar_nodos(arbol[1]) + contar_nodos(arbol[2])


def nodo_mas_profundo(arbol, nivel=0):
    if not arbol:
        return (None, -1)  # nodo, nivel
    if not arbol[1] and not arbol[2]:
        return (arbol[0], nivel)  # hoja
    # Evaluar subárboles
    nodo_izq, nivel_izq = nodo_mas_profundo(arbol[1], nivel + 1)
    nodo_der, nivel_der = nodo_mas_profundo(arbol[2], nivel + 1)
    if nivel_izq > nivel_der:
        return (nodo_izq, nivel_izq)
    else:
        return (nodo_der, nivel_der)    
