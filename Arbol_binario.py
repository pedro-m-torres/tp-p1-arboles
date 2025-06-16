from arbol_add import *
from busqueda import *

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
        print("10) Mostrar grafico del arbol")
        print("0) Salir")

        choice = input("Ingrese su opción (0-9): ")

        if choice == '0':
            break
        elif choice == '1':
            cargar_arbol(arbol)
        elif choice == '2':
            buscado = int(input("Ingrese el valor a buscar: "))
            mostrar_mensaje(buscar_valor(arbol,buscado))
        elif choice == '3':
            print(f"Valor mas alto: {buscar_mayor(arbol)}")
        elif choice == '4':
            print(f"Valor mas bajo: {buscar_menor(arbol)}")
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
        elif choice == '10':
            imprimir_arbol(arbol, nivel=0)
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()  
