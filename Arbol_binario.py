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

print(arbol)

    

    
    




