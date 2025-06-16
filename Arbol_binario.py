#Lista vacia
arbol = []
flag = True

#Funcion para crear el arbol con la raiz y dos hijos
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
    

while flag:
    puntaje = int(input("Ingrese el puntaje: "))
    if puntaje == 0:
        flag = False
        break
    crear_arbol(arbol, puntaje)

print(arbol)

#Funcion para mostrar el arbol con una representar visual mas amigable
#En este caso como el formato de cada subarbol se representa [raiz,subarbol_izquierdo,subarbol_derecho]
#Utilizamos la funcion de manera recursiva para encontrar el nodo mas alejado e imprimirlo multiplicando el nivel de espacios.
#[50, [30, [20, [], []], []], [70, [], [80, [], []]]]
def imprimir_arbol(lista, nivel=0):
    if lista != []:
        #Llamamos a la funcion de manera recursiva pero pasandole como argumento la lista del elemento 2 (subarbol_derecho) y aunmentamos en 1 la variable nivel
        imprimir_arbol(lista[2], nivel + 1) #lista[2][0] = 70 | nivel = 1
            ## --> if lista[2] != []: 
            ## -->   imprimir_arbol(lista[2], nivel + 1) #lista[2][0] = 80 | nivel = 2
        print("   " * nivel + str(lista[0]))
            ## -->      print "      80"
            ## -->      print "   70"
            ## -->      print "50"
        imprimir_arbol(lista[1], nivel + 1)
        ## --> if lista[1] != []: 
            ## -->   imprimir_arbol(lista[1], nivel + 1) #lista[1][0] = 30 | nivel = 1
            ## -->      if lista[1] != []: 
            ## -->          imprimir_arbol(lista[1], nivel + 1) #lista[1][0] = 20 | nivel = 2
            ## -->      print "   30"
            ## -->      print "      20"



imprimir_arbol(arbol, nivel=0)


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
            

def buscar_valor(lista, valor):
    if lista == []:
        return False
    if lista[0] == valor:
        return True
    return buscar_valor(lista[1], valor) or buscar_valor(lista[2], valor)

mayor = buscar_mayor(arbol)
menor = buscar_menor(arbol)
busqueda = buscar_valor(arbol,60)

print(f"El valor mas alto del arbol es: {mayor}.")
print(f"El valor mas bajo del arbol es: {menor}.")

if busqueda:
    print("Correcto, el valor se encuentra en el arbol.")
else:
    print("Valor NO encontrado dentro del arbol.")