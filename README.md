# Sistema de Control de Inventario — Ferretería

Trabajo Práctico Integrador de **Programación 1** — Tecnicatura Universitaria en Programación a Distancia (TUPaD), UTN.
1° Cuatrimestre 2026.

## Autor

- **Federico Barranco** — autor del trabajo y de la entrega (individual).
- **Nicolás Tissoni** — colaborador inicial: escribió la primera versión de `cargar_herramientas`, `mostrar_inventario`, `consultar_stock` y `alta_producto`. Dejó la materia en octubre de 2026, y desde entonces terminé el trabajo solo: corregí esas funciones para la consigna vigente y escribí el resto.

## Video y documentación

- 🎥 Video explicativo: *(link pendiente)*
- 📄 Informe en PDF: `Informe TPI - Barranco Federico.pdf`, en la raíz de este repositorio

## Descripción

Una ferretería local necesita digitalizar el control de sus productos para evitar pérdidas de stock. El programa maneja las herramientas a la venta y sus unidades disponibles con un menú que se repite hasta elegir salir:

1. Carga de herramientas con existencias iniciales
2. Visualización de inventario
3. Consulta de stock
4. Reporte de agotados
5. Alta de nuevo producto
6. Actualización de stock (venta / ingreso)
7. Salir

Los datos se guardan en una sola lista de diccionarios, `inventario`, donde cada herramienta tiene las claves `'herramienta'` y `'cantidad'`. Se crea dentro de `main()` y se pasa por parámetro a cada función (no hay variables globales). Los datos no se guardan al cerrar el programa.

## Archivos

| Archivo | Qué tiene |
|---|---|
| `main.py` | `main()`: crea el inventario y repite el menú. **Es el archivo que se ejecuta.** |
| `carga_y_consulta.py` | Opciones 1, 2, 3 y 5, y las funciones auxiliares `validar_nombre` y `buscar_herramienta`. |
| `stock_y_menu.py` | Opciones 4 y 6, y `mostrar_menu`. |

## Cómo ejecutar

Hace falta Python 3 (lo probé con Python 3.14). No usa librerías externas.

```bash
python main.py
```

Ejemplo de uso:

```text
===== FERRETERÍA - CONTROL DE INVENTARIO =====
1. Cargar herramientas con stock inicial
...
7. Salir
Seleccione una opción: 1
Ingrese la cantidad de herramientas: 2
Ingrese el nombre de la herramienta: Martillo
Ingrese el stock de la herramienta: 10
Ingrese el nombre de la herramienta: martillo
Error: martillo ya existe en el inventario
Ingrese el nombre de la herramienta: Pala
Ingrese el stock de la herramienta: 0
Carga terminada
```

## Clonar el repositorio

```bash
git clone https://github.com/fedebarranco/TP_Final-Sistema_de_Control_de_Inventario.git
cd TP_Final-Sistema_de_Control_de_Inventario
python main.py
```
