# Funciones de carga y consulta del inventario.
# Las 4 funciones de las opciones (cargar, mostrar, consultar y alta) las escribió
# Nicolás Tissoni; yo (Federico Barranco) las corregí para la consigna nueva
# y agregué las dos funciones auxiliares de acá abajo.


def validar_nombre(nombre):
    """Le saca los espacios del principio y del final al nombre.

    Si queda vacío lanza ValueError. Si no, devuelve el nombre limpio.
    """
    nombre = nombre.strip()
    if nombre == "":
        raise ValueError("El nombre no puede estar vacío")
    return nombre


def buscar_herramienta(inventario, nombre):
    """Busca una herramienta por nombre sin importar mayúsculas.

    Devuelve el diccionario de esa herramienta (el mismo que está en la lista)
    o None si no está en el inventario.
    """
    for herramienta in inventario:
        if herramienta['herramienta'].lower() == nombre.lower():
            return herramienta
    return None


def cargar_herramientas(inventario):
    """Opción 1: carga varias herramientas con su stock inicial.

    Pide cuántas se van a cargar y, por cada una, el nombre y el stock.
    Los errores se atrapan acá adentro para volver a pedir el dato.
    Autor original: Nicolás Tissoni.
    """
    while True:
        try:
            cantidad_de_herramientas_ingresadas = int(input("Ingrese la cantidad de herramientas: "))

            if cantidad_de_herramientas_ingresadas <= 0:
                raise ValueError("La cantidad tiene que ser mayor que 0")

            break
        except ValueError as only_num:
            print(f"Error: {only_num}")

    for _ in range(cantidad_de_herramientas_ingresadas):
        while True:
            try:
                nombre_herramienta_ingresada = validar_nombre(input("Ingrese el nombre de la herramienta: "))

                if buscar_herramienta(inventario, nombre_herramienta_ingresada) is not None:
                    raise ValueError(f"{nombre_herramienta_ingresada} ya existe en el inventario")

                break
            except ValueError as error:
                print(f"Error: {error}")

        while True:
            try:
                stock_herramienta_ingresada = int(input("Ingrese el stock de la herramienta: "))

                if stock_herramienta_ingresada < 0:
                    raise ValueError("El stock no puede ser negativo")

                break
            except ValueError as error:
                print(f"Error: {error}")

        # el append va ADENTRO del for: así se agrega cada herramienta apenas
        # tiene nombre y stock válidos (antes estaba afuera y solo quedaba la última)
        inventario.append({'herramienta': nombre_herramienta_ingresada, 'cantidad': stock_herramienta_ingresada})

    print("Carga terminada")

def mostrar_inventario(inventario):
    """Opción 2: muestra todas las herramientas con su stock.

    Autor: Nicolás Tissoni.
    """
    if not inventario:
        print("No hay herramientas cargadas en el inventario")
    else:
        print("=== Inventario Actual ===")
        for herramienta in inventario:
            print(f"Nombre: {herramienta['herramienta']} | Stock: {herramienta['cantidad']}")

def consultar_stock(inventario):
    """Opción 3: busca una herramienta por nombre y muestra su stock.

    Si el nombre está vacío, validar_nombre lanza ValueError y el error
    sale de la función hasta el except de main().
    Autor original: Nicolás Tissoni.
    """
    if len(inventario) == 0:
        print("Todavía no hay herramientas cargadas")
        return

    nombre_de_herramienta_consultado = validar_nombre(input("Ingrese el nombre de la herramienta a consultar: "))
    herramienta = buscar_herramienta(inventario, nombre_de_herramienta_consultado)

    if herramienta is None:
        print(f"{nombre_de_herramienta_consultado} no se encontró en el catálogo")
    else:
        print(f"Stock de {herramienta['herramienta']} es {herramienta['cantidad']}")

def alta_producto(inventario):
    """Opción 5: agrega una herramienta nueva al final del inventario.

    Primero valida el nombre y recién después pide el stock. Acá los errores
    NO se atrapan para reintentar: salen con raise hasta main(), que muestra
    el motivo y vuelve al menú sin agregar nada.
    Autor original: Nicolás Tissoni.
    """
    nombre_producto_ingresado = validar_nombre(input("Ingresar el nombre del producto: "))

    if buscar_herramienta(inventario, nombre_producto_ingresado) is not None:
        raise ValueError("Error el producto ya existe")

    try:
        stock_producto_ingresado = int(input("Ingresar el stock del producto: "))
    except ValueError:
        raise ValueError("Error, ingrese un numero valido.")

    if stock_producto_ingresado < 0:
        raise ValueError("Error el stock no puede ser negativo")

    inventario.append({'herramienta': nombre_producto_ingresado, 'cantidad': stock_producto_ingresado})
    print(f"{nombre_producto_ingresado} se agregó con stock {stock_producto_ingresado}")