# Programa de inventario con menu interactivo.
# Permite agregar productos, mostrar el inventario y calcular estadisticas.
# Usa listas de diccionarios, condicionales y bucles.

# -----------------------------------------------
# Lista principal donde se almacenan todos los productos
# -----------------------------------------------
inventario = []

# -----------------------------------------------
# Funcion para agregar un producto al inventario
# Solicita nombre, precio y cantidad con validacion de datos
# -----------------------------------------------
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")

    precio_valido = False
    precio = 0.0
    while not precio_valido:
        precio_texto = input("Ingrese el precio del producto: ")
        try:
            precio = float(precio_texto)
            precio_valido = True
        except ValueError:
            print("Valor invalido. Por favor ingrese un numero para el precio.")

    cantidad_valida = False
    cantidad = 0
    while not cantidad_valida:
        cantidad_texto = input("Ingrese la cantidad del producto: ")
        try:
            cantidad = int(cantidad_texto)
            cantidad_valida = True
        except ValueError:
            print("Valor invalido. Por favor ingrese un numero entero para la cantidad.")

    # Crear el diccionario del producto y agregarlo a la lista
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print("Producto agregado correctamente.")

# -----------------------------------------------
# Funcion para mostrar todos los productos del inventario
# Recorre la lista con un bucle for y muestra cada producto
# -----------------------------------------------
def mostrar_inventario():
    if len(inventario) == 0:
        print("El inventario esta vacio.")
    else:
        print("--- Inventario ---")
        for producto in inventario:
            print("Producto:", producto["nombre"], "| Precio:", producto["precio"], "| Cantidad:", producto["cantidad"])

# -----------------------------------------------
# Funcion para calcular estadisticas del inventario
# Calcula el valor total y la cantidad total de productos registrados
# -----------------------------------------------
def calcular_estadisticas():
    if len(inventario) == 0:
        print("El inventario esta vacio. No hay estadisticas que mostrar.")
    else:
        valor_total = 0.0
        cantidad_total = 0

        # Recorrer todos los productos y acumular los valores
        for producto in inventario:
            valor_total = valor_total + (producto["precio"] * producto["cantidad"])
            cantidad_total = cantidad_total + producto["cantidad"]

        print("--- Estadisticas ---")
        print("Valor total del inventario:", valor_total)
        print("Cantidad total de productos registrados:", cantidad_total)

# -----------------------------------------------
# Se muestra el menu una primera vez antes de entrar al bucle
# -----------------------------------------------
print("")
print("--- Menu de Inventario ---")
print("1. Agregar producto")
print("2. Mostrar inventario")
print("3. Calcular estadisticas")
print("4. Salir")
opcion = input("Seleccione una opcion: ")

# -----------------------------------------------
# Bucle principal del menu
# Se ejecuta hasta que el usuario ingrese la opcion 4 para salir
# -----------------------------------------------
while opcion != "4":
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        calcular_estadisticas()
    else:
        print("Opcion invalida. Por favor ingrese un numero entre 1 y 4.")

    # Mostrar el menu nuevamente al final de cada ciclo
    print("")
    print("--- Menu de Inventario ---")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadisticas")
    print("4. Salir")
    opcion = input("Seleccione una opcion: ")

# -----------------------------------------------
# Mensaje de despedida cuando el usuario elige salir
# -----------------------------------------------
print("Saliendo del programa. Hasta luego.")

# -----------------------------------------------
# Este programa implementa un sistema de inventario con menu interactivo.
# Permite al usuario agregar productos (nombre, precio, cantidad), visualizar
# el inventario completo y obtener estadisticas como el valor total y la cantidad
# total de unidades. Los datos se almacenan en una lista de diccionarios y
# el codigo esta organizado en funciones para mayor claridad y orden.
# -----------------------------------------------