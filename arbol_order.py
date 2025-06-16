# funciones para mostrar el arbol en inOrder, en PreOrder y PostOrder.

def Mostrar_InOrden(arbol):
    if arbol:
        Mostrar_InOrden(arbol[1])
        print(arbol[0], end=" ")
        Mostrar_InOrden(arbol[2])


def Mostrar_PreOrden(arbol):
    if arbol:
       print(arbol[0], end=" ")
       Mostrar_PreOrden(arbol[1])
       Mostrar_PreOrden(arbol[2])

def Mostrar_PostOrden(arbol):
    if arbol:
        Mostrar_PostOrden(arbol[1])
        Mostrar_PostOrden(arbol[2])
        print(arbol[0], end=" ")

