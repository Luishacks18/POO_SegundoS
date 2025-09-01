import os

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def obtener_id(self):
        return self.id

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.productos = {}
        self.archivo = archivo
        self.cargar_inventario()

    def cargar_inventario(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as file:
                    for line in file:
                        id, nombre, cantidad, precio = line.strip().split(',')
                        self.productos[id] = Producto(id, nombre, int(cantidad), float(precio))
            except (FileNotFoundError, PermissionError) as error:
                print(f"Error al cargar el inventario: {error}")

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos.values():
                    file.write(f"{producto.obtener_id()},{producto.obtener_nombre()},{producto.obtener_cantidad()},{producto.obtener_precio()}\n")
        except (FileNotFoundError, PermissionError) as error:
            print(f"Error al guardar el inventario: {error}")

    def agregar_producto(self, producto):
        if producto.obtener_id() in self.productos:
            print(f"Error: El producto con ID {producto.obtener_id()} ya existe.")
            return
        self.productos[producto.obtener_id()] = producto
        self.guardar_inventario()
        print(f"Producto {producto.obtener_nombre()} agregado al inventario.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            print(f"Producto con ID {id_producto} eliminado del inventario.")
        else:
            print(f"Error: No se encontró ningún producto con ID {id_producto}.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nueva_cantidad is not None:
                producto.actualizar_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.actualizar_precio(nuevo_precio)
            self.guardar_inventario()
            print(f"Producto con ID {id_producto} actualizado.")
        else:
            print(f"Error: No se encontró ningún producto con ID {id_producto}.")

    def buscar_productos(self, nombre_producto):
        resultados = []
        for producto in self.productos.values():
            if nombre_producto.lower() in producto.obtener_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario:")
            for producto in self.productos.values():
                print(producto)

inventario = Inventario()

while True:
    print(" _______________________")
    print("|   Menú de Gestión     |")
    print("|       de Inventario   |")
    print("|_______________________|")
    print("|  1. Agregar Producto  |")
    print("|  2. Eliminar Producto |")
    print("|  3. Actualizar        |")
    print("|  4. Buscar Productos  |")
    print("|  5. Mostrar Inventario|")
    print("|  6. Salir             |")
    print("|_______________________|")

    opcion = input("Ingrese el número de la opción: ")

    if opcion == "1":
        id_producto = input("Ingrese el ID del producto: ")
        nombre_producto = input("Nombre del producto: ")
        cantidad_producto = int(input("Ingrese la cantidad del producto: "))
        precio_producto = float(input("Ingrese el precio del producto: "))
        producto = Producto(id_producto, nombre_producto, cantidad_producto, precio_producto)
        inventario.agregar_producto(producto)

    elif opcion == "2":
        id_producto = input("Ingrese el ID del producto a eliminar: ")
        inventario.eliminar_producto(id_producto)

    elif opcion == "3":
        id_producto = input("Ingrese el ID del producto a actualizar: ")
        nueva_cantidad = input("Ingrese la nueva cantidad: ")
        nuevo_precio = input("Ingrese el nuevo precio: ")
        if nueva_cantidad:
            nueva_cantidad = int(nueva_cantidad)
        else:
            nueva_cantidad = None
        if nuevo_precio:
            nuevo_precio = float(nuevo_precio)
        else:
            nuevo_precio = None
        inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

    elif opcion == "4":
        nombre_producto = input("Ingrese el nombre del producto a buscar: ")
        resultados = inventario.buscar_productos(nombre_producto)
        if not resultados:
            print(f"No se encontraron productos con el nombre '{nombre_producto}'.")
        else:
            print(f"Resultados de la búsqueda de '{nombre_producto}':")
            for producto in resultados:
                print(producto)

    elif opcion == "5":
        inventario.mostrar_inventario()

    elif opcion == "6":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intente de nuevo.")
