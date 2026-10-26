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
    while True:
        try:
            cantidad_de_herramientas_ingresadas = int(input("Ingrese la cantidad de herramientas: "))
            
            if cantidad_de_herramientas_ingresadas < 0:
                raise ValueError("La cantidad no puede ser negativa")

            break
        except ValueError as only_num:
            print(f"Error: {only_num}")

    for _ in range(cantidad_de_herramientas_ingresadas):
        while True:
            try:
                nombre_herramienta_ingresada = input("Ingrese el nombre de la herramienta: ")

                if not nombre_herramienta_ingresada.strip():
                    raise ValueError("Ingrese un nombre válido")

                for herramienta in inventario:
                    if herramienta['herramienta'] == nombre_herramienta_ingresada:
                        raise ValueError(f"{herramienta['herramienta']} ya existe en el inventario")

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

    inventario.append({'herramienta': nombre_herramienta_ingresada, 'cantidad': stock_herramienta_ingresada})

def mostrar_inventario(inventario):
    if not inventario:
        print("No hay herramientas cargadas en el inventario")
    else:
        print("=== Inventario Actual ===")
        for herramienta in inventario:
            print(f"Nombre: {herramienta['herramienta']} | Stock: {herramienta['cantidad']}")

def consultar_stock(inventario):
    nombre_de_herramienta_consultado = input("Ingrese el nombre de la herramienta a consultar: ")
    encontrada = False

    for herramienta in inventario:
        if herramienta['herramienta'] == nombre_de_herramienta_consultado:
            print(f"Stock de {herramienta['herramienta']} es {herramienta['cantidad']}")
            encontrada = True

    if not encontrada:
        print(f"{nombre_de_herramienta_consultado} no se encontró")

def alta_producto(inventario):
    nombre_producto_ingresado = input("Ingresar el nombre del producto: ")

    try:
        stock_producto_ingresado = int(input("Ingresar el stock del producto: "))
    except ValueError:
        raise ValueError("Error, ingrese un numero valido.")

    duplicado = False
    for herramienta in inventario:
        if herramienta['herramienta'] == nombre_producto_ingresado:
            duplicado = True

    if not nombre_producto_ingresado:
        raise ValueError("Error ingrese un nombre valido")
    elif duplicado:
        raise ValueError("Error el producto ya existe")
    elif stock_producto_ingresado < 0:
        raise ValueError("Error el stock no puede ser negativo")
    else:
        inventario.append({'herramienta': nombre_producto_ingresado, 'cantidad': stock_producto_ingresado})