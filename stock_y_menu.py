# Reporte de agotados, actualización de stock y texto del menú.
# Autor: Federico Barranco

from carga_y_consulta import validar_nombre, buscar_herramienta


def mostrar_menu():
    """Imprime las 7 opciones del menú principal."""
    print()
    print("===== FERRETERÍA - CONTROL DE INVENTARIO =====")
    print("1. Cargar herramientas con stock inicial")
    print("2. Ver inventario")
    print("3. Consultar stock")
    print("4. Reporte de agotados")
    print("5. Alta de nuevo producto")
    print("6. Actualizar stock (venta / ingreso)")
    print("7. Salir")


def reporte_agotados(inventario):
    """Opción 4: lista solo las herramientas que tienen stock 0."""
    if len(inventario) == 0:
        print("Todavía no hay herramientas cargadas")
    else:
        # primero cuento cuántas hay agotadas para saber qué mensaje mostrar
        cant_agotadas = 0
        for herramienta in inventario:
            if herramienta['cantidad'] == 0:
                cant_agotadas = cant_agotadas + 1

        if cant_agotadas == 0:
            print("Ninguna herramienta tiene stock cero")
        else:
            print("=== Herramientas agotadas ===")
            for herramienta in inventario:
                if herramienta['cantidad'] == 0:
                    print(f"- {herramienta['herramienta']}")


def actualizar_stock(inventario):
    """Opción 6: registra una venta (resta) o un ingreso (suma) de una herramienta.

    Sigue los pasos en orden: inventario vacío, nombre, que exista, tipo de
    movimiento, unidades y stock suficiente. Recién al final cambia el stock,
    así un dato inválido nunca deja el inventario a medias.
    Los ValueError salen de la función y los muestra main().
    """
    # 1. sin herramientas no hay nada que actualizar
    if len(inventario) == 0:
        print("Todavía no hay herramientas cargadas")
        return

    # 2. nombre (si está vacío, validar_nombre lanza ValueError)
    nombre = validar_nombre(input("Nombre de la herramienta: "))

    # 3. tiene que existir en el catálogo
    herramienta = buscar_herramienta(inventario, nombre)
    if herramienta is None:
        print(f"{nombre} no existe en el catálogo")
        return

    # 4. tipo de movimiento: lo comparo como texto, sin int()
    print("1. Venta")
    print("2. Ingreso")
    tipo = input("Tipo de movimiento (1 o 2): ").strip()
    if tipo != "1" and tipo != "2":
        print("Movimiento inválido: tiene que ser 1 (venta) o 2 (ingreso)")
        return

    # 5. unidades: entero mayor que 0
    try:
        unidades = int(input("Unidades: "))
    except ValueError:
        raise ValueError("Las unidades tienen que ser un número entero")
    if unidades <= 0:
        raise ValueError("Las unidades tienen que ser mayores que 0")

    # 6 y 7. en la venta controlo que alcance el stock y recién ahí lo modifico
    if tipo == "1":
        stock_resultante = herramienta['cantidad'] - unidades
        if stock_resultante < 0:
            raise ValueError(f"No hay stock suficiente: quedan {herramienta['cantidad']} unidades")
        herramienta['cantidad'] = stock_resultante
        print(f"Venta registrada. Stock de {herramienta['herramienta']}: {herramienta['cantidad']}")
    else:
        herramienta['cantidad'] = herramienta['cantidad'] + unidades
        print(f"Ingreso registrado. Stock de {herramienta['herramienta']}: {herramienta['cantidad']}")
