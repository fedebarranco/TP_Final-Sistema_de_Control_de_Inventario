# Programa principal: este es el archivo que se ejecuta (python main.py).
# Autor: Federico Barranco

from carga_y_consulta import cargar_herramientas, mostrar_inventario, consultar_stock, alta_producto
from stock_y_menu import mostrar_menu, reporte_agotados, actualizar_stock


def main():
    """Crea el inventario y repite el menú hasta que se elige la opción 7.

    El inventario se crea acá (no es global) y se pasa por parámetro a cada
    función. El except de abajo muestra los errores que llegan hasta acá
    y el while vuelve a mostrar el menú.
    """
    inventario = []
    opcion = 0

    while opcion != 7:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                cargar_herramientas(inventario)
            elif opcion == 2:
                mostrar_inventario(inventario)
            elif opcion == 3:
                consultar_stock(inventario)
            elif opcion == 4:
                reporte_agotados(inventario)
            elif opcion == 5:
                alta_producto(inventario)
            elif opcion == 6:
                actualizar_stock(inventario)
            elif opcion != 7:
                raise ValueError("Opción fuera de rango (1 a 7)")
        except ValueError as e:
            print(f"Error: {e}")

    print("Saliendo del sistema. ¡Hasta luego!")


if __name__ == "__main__":
    main()
