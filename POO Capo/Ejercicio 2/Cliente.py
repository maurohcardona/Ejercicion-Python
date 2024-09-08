class Cliente():
    def __init__(self, dni, nombre, apellido) -> None:
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.facturas = []
        

class Articulo():
    codigo = 0
    def __init__(self, denominacion, precio) -> None:
        Articulo.codigo += 1
        self.codigo_articulo = Articulo.codigo
        self.denominacion = denominacion
        self.precio = precio
        
class Factura():
    numero = 0
    def __init__(self, cliente) -> None:
        Factura.numero += 1
        self.numero_factura = Factura.numero
        self.cliente = cliente
        self.lineas = []
        
    def añadir_linea(self, linea):
        self.lineas.append(linea)
        
    def eliminar_linea(self,linea):
        for lin in self.lineas:
            if lin[0] == linea["Articulo"]:
                self.lineas.remove(lin)
            else:
                print("No se encontro el articulo")
                
    def importe_total(self):
        return sum(linea.subtotal() for linea in self.lineas)
    
    def imprimir_factura(self):
        print(f"Factura numero: {self.numero_factura}")
        print(f"Cliente: {self.cliente.nombre} {self.cliente.apellido}")
        print("codigo   Articulo          Cantidad  Subtotal")
        for linea in self.lineas:
            linea.imprimir_linea()
        print(f"Total:   ${self.importe_total()}")
        
     
class Linea():
    def __init__(self, articulo, cantidad) -> None:
        self.articulo = articulo
        self.cantidad = cantidad
        
    def subtotal(self):
        return self.articulo.precio * self.cantidad
    
    def imprimir_linea(self):
        print(f"{self.articulo.codigo_articulo:<8} {self.articulo.denominacion:<18} {self.cantidad:<8} ${self.subtotal():<8}")
        

        