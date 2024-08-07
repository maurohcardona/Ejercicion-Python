"""
Ejercicio 1: Sistema de Gestión de Inventario
Crea una clase Producto con atributos nombre, precio y cantidad.
Crea una clase Inventario que mantenga una lista de productos y tenga métodos para:
Añadir productos.
Eliminar productos por nombre.
Mostrar todos los productos.
Buscar un producto por nombre.
Añade funcionalidad para actualizar el precio y la cantidad de un producto existente.

"""

class Producto():
    def __init__(self, nombre, precio, cantidad) -> None:
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def info_producto(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Cantidad: {self.cantidad} ")
        
class Inventario():
    def __init__(self) -> None:
        self.inventario = []
        
    def agregar_productos(self, producto):
       for productos in self.inventario:
           if producto.nombre == productos.nombre:
               productos.cantidad += producto.cantidad
               print(f"Se agregaron {producto.cantidad} unidades de {producto.nombre}")
               return
       self.inventario.append(producto)
       print(f"Agregaste  el producto {producto.nombre} al inventario")
       
        
    def eliminar_producto(self, producto):
        for productos in self.inventario:
            if producto.nombre == productos.nombre:
                self.inventario.remove(productos)
                print(f"El producto {producto.nombre} fue eliminado del inventario")
                return
        print(f"El producto {producto.nombre} no se encuentra en el inventario")
                
    def mostrar_productos(self):
        print("Lista de productos")
        if len(self.inventario) > 0:    
            for producto in self.inventario:
                producto.info_producto()
        else:
            print("No hay productos en el inventario aun")
    
    def buscar_producto(self, producto):
        for productos in self.inventario:
            if producto.nombre == producto.nombre:
                producto.info_producto()
                return
        print(f"No se encontro el producto {producto.nombre} en el inventario")

inventario1 = Inventario()
pelota = Producto("Pelota", 100, 2)
jarron = Producto("Jarron", 200, 1)

inventario1.mostrar_productos()
inventario1.agregar_productos(pelota)
inventario1.mostrar_productos()
inventario1.agregar_productos(pelota)
inventario1.buscar_producto(pelota)
inventario1.agregar_productos(jarron)
inventario1.mostrar_productos()
inventario1.eliminar_producto(pelota)
inventario1.mostrar_productos()