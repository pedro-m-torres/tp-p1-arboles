#Funcion para mostrar el arbol con una representar grafica.
#En este caso como el formato de cada subarbol se representa [raiz,subarbol_izquierdo,subarbol_derecho]
#Utilizamos la funcion de manera recursiva para encontrar el nodo mas alejado e imprimirlo multiplicando el nivel de espacios.
def imprimir_arbol(lista, nivel=0):
    if lista != []:
        imprimir_arbol(lista[2], nivel + 1)
        print("   " * nivel + str(lista[0]))
        imprimir_arbol(lista[1], nivel + 1)

#Funciones para buscar el valor mas alto y el valor mas bajo.
#Teniendo en cuenta que el arbol binario ordena los valores mas altos del nodo raiz a la derecha y los bajos a la izquierda,
#las funciones evualan recursivamente si el elemento [2] (derecha) y el elemento [1] izquierda esta vacio, en el caso de que asi sea:
#no hay un valor mas alto o bajo a buscar entonces retorna ese nodo [0]

def buscar_mayor(lista):
    if lista != []:
        if lista[2] == []:
            return lista[0]
        else:
            return buscar_mayor(lista[2])
            

def buscar_menor(lista):
    if lista != []:
        if lista[1] == []:
            return lista[0]
        else:
            return buscar_menor(lista[1])

#Funciones para buscar para determinar si el valor buscado se encuentra dentro del arbol.
#En este caso no queremos que la funcion se detenga si hay un elemento vacio por lo que retorna falso para buscar recursivamente hacia la izquierda [1] y la derecha [2]
#Si el nodo es igual al valor del parametro devuelvo True.         

def buscar_valor(lista, valor):
    if lista == []:
        return False
    if lista[0] == valor:
        return True
    return buscar_valor(lista[1], valor) or buscar_valor(lista[2], valor)

#Funcion que tiene como argumento un Booleano para determinar mostrar un mensaje si encontro el valor y otro si no lo encontro.
def mostrar_mensaje(busqueda):
    if busqueda:
        print("Correcto, el valor se encuentra en el arbol.")
    else:
        print("Valor NO encontrado dentro del arbol.")

