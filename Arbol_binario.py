from arbol_add import *

def main():

    #Lista vacia
    arbol = []

    while True:

        print("\nMenú:")
        print("1) Agregar Puntajes")
        print("2) Buscar Puntaje en el árbol")
        print("3) Mostrar el puntaje mas alto del árbol")
        print("4) Mostrar el puntaje mas bajo del árbol")
        print("5) Recorrer el árbol inOrder")
        print("6) Recorrer el árbol preOrder")
        print("7) Recorrer el árbol postOrder")
        print("8) Mostrar todos los puntajes")
        print("9) Limpiar Puntajes")
        print("0) Salir")

        choice = input("Ingrese su opción (0-9): ")

        if choice == '0':
            break
        elif choice == '1':
            cargar_arbol(arbol)
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        elif choice == '7':
            pass
        elif choice == '8':
            print(arbol)
        elif choice == '9':
            arbol = []
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()  