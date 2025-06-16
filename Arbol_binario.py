from arbol_add import *
from arbol_search import *
from arbol_order import *
from arbol_print import *

# Menu principal

def main():

    #Lista vacia
    arbol = []

    while True:

        esperar = False

        print("\nMenú:")
        print(" 1) Agregar Puntajes")
        print(" 2) Buscar Puntaje en el árbol")
        print(" 3) Mostrar el puntaje mas alto del árbol")
        print(" 4) Mostrar el puntaje mas bajo del árbol")
        print(" 5) Recorrer el árbol inOrder")
        print(" 6) Recorrer el árbol preOrder")
        print(" 7) Recorrer el árbol postOrder")
        print(" 8) Mostrar grafico del arbol")
        print(" 9) Propiedades del Arbol")
        print("10) Limpiar Arbol ")
        print("0) Salir")

        choice = input("Ingrese su opción (0-9): ")

        if choice == '0':
            break
        elif choice == '1':
            cargar_arbol(arbol)
        elif choice == '2':
            buscado = int(input("Ingrese el valor a buscar: "))
            mostrar_mensaje(buscar_valor(arbol,buscado))
            esperar = True
        elif choice == '3':
            print(f"Valor mas alto: {buscar_mayor(arbol)}")
            esperar = True
        elif choice == '4':
            print(f"Valor mas bajo: {buscar_menor(arbol)}")
            esperar = True
        elif choice == '5':
            Mostrar_InOrden(arbol)
            esperar = True
        elif choice == '6':
            Mostrar_PreOrden(arbol)
            esperar = True
        elif choice == '7':
            Mostrar_PostOrden(arbol)
            esperar = True
        elif choice == '8':
            if len(arbol)>0:
                imprimir_arbol(arbol, nivel=0)
            else:
                print("El árbol está vacío.")
            esperar = True
        elif choice == '9':
            Mostrar_Propiedades(arbol)
            esperar = True
        elif choice == '10':
            confirmar = input("¿Está seguro que desea borrar el árbol? (S/N): ")
            if confirmar.upper() == 'S':
                arbol = []
            print("Árbol borrado con éxito.")
            esperar = True
        else:
            print("Opción inválida. Intente de nuevo.")

        if esperar:
            input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()  
