#Punto 1

with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,450.0,15\n")
    archivo.write("Regla,200.0,20\n")

#Punto 2
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        datos = linea.split(",")
        nombre = datos[0]
        precio = datos[1]
        cantidad = datos[2]
        print("Producto:", nombre, "| Precio: $", precio, "| Cantidad:", cantidad)

#Punto 3

nombre = input("\nIngrese nombre del producto: ")
precio = input("Ingrese precio: ")
cantidad = input("Ingrese cantidad: ")

with open("productos.txt", "a", encoding="utf-8") as archivo:
    archivo.write(nombre + "," + precio + "," + cantidad + "\n")

#Punto 4

productos = []
with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()
        datos = linea.split(",")
        producto = {
            "nombre": datos[0],
            "precio": float(datos[1]),
            "cantidad": int(datos[2])}
        productos.append(producto)

#Punto 5

buscar = input("\nIngrese el nombre del producto a buscar: ")
encontrado = False
for p in productos:
    if p["nombre"]== buscar:
        print("Nombre:", p["nombre"], "| Precio:", p["precio"], "| Cantidad:", p["cantidad"])
        encontrado = True
if not encontrado:
    print("Producto no encontrado.")

#Punto 6

with open("productos.txt", "w", encoding="utf-8") as archivo:
    for p in productos:
        linea = p["nombre"] + "," + str(p["precio"]) + "," + str(p["cantidad"]) + "\n"
        archivo.write(linea)

print("\nArchivo actualizado correctamente")
