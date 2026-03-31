# Programa de inventario: solicita nombre, precio y cantidad de un producto,
# valida los datos ingresados, calcula el costo total y muestra los resultados.

# -----------------------------------------------
# Solicitar el nombre del producto
# -----------------------------------------------
nombre = input("Ingrese el nombre del producto: ")

# -----------------------------------------------
# Solicitar y validar el precio del producto
# Se repite la solicitud si el valor ingresado no es un numero valido
# -----------------------------------------------
precio_valido = False
precio = 0.0

while not precio_valido:
    precio_texto = input("Ingrese el precio del producto: ")
    try:
        precio = float(precio_texto)
        precio_valido = True
    except ValueError:
        print("Valor invalido. Por favor ingrese un numero para el precio.")

# -----------------------------------------------
# Solicitar y validar la cantidad del producto
# Se repite la solicitud si el valor ingresado no es un numero entero valido
# -----------------------------------------------
cantidad_valida = False
cantidad = 0

while not cantidad_valida:
    cantidad_texto = input("Ingrese la cantidad del producto: ")
    try:
        cantidad = int(cantidad_texto)
        cantidad_valida = True
    except ValueError:
        print("Valor invalido. Por favor ingrese un numero entero para la cantidad.")

# -----------------------------------------------
# Calcular el costo total multiplicando precio por cantidad
# -----------------------------------------------
costo_total = precio * cantidad

# -----------------------------------------------
# Mostrar los resultados en consola
# -----------------------------------------------
print("Producto:", nombre, "| Precio:", precio, "| Cantidad:", cantidad, "| Total:", costo_total)

# -----------------------------------------------
# Este programa solicita al usuario el nombre, precio y cantidad de un producto.
# Valida que el precio sea un numero decimal y la cantidad un numero entero,
# mostrando un mensaje de error y repitiendo la solicitud si el dato es invalido.
# Luego calcula el costo total (precio * cantidad) y muestra todos los datos en consola.
# -----------------------------------------------